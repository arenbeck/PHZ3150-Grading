from canvasapi import Canvas
import zipfile, os, shutil, importlib.util

# Instructions on how to get token: https://canvas.instructure.com/doc/api/file.oauth.html#manual-token-generation
API_TOKEN = os.getenv("CANVAS_API_TOKEN") # Each user (grader/Professor) needs to get their own api token
COURSE_ID = '1472271' # Can be found in the URL

# Canvas API URL
API_URL = "https://webcourses.ucf.edu"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_TOKEN)
course = canvas.get_course(COURSE_ID) # Get's course
users = course.get_users(enrollment_type=['student'])


def get_submission_from_user(submissions, user):
    for submission in submissions:
        if submission.user_id == user.id:
            return submission
    return None

def get_user_from_id(id):
    for u in users:
        if u.id == id:
            return u
    return None

def get_user_from_name(name):
    for u in users:
        if u.name == name:
            return u
    return None


def extract_zip_file(file_path, output_dir):
    """
    Extracts a zip file to the specified directory and moves into a folder
    starting with 'hw' if present, ignoring hidden files.
    """
    if zipfile.is_zipfile(file_path):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
        print(f"Extracted ZIP file: {file_path} to {output_dir}")
        os.remove(file_path)  # Remove the original zip file after extraction

        # Look for a folder starting with 'hw'
        for root, dirs, files in os.walk(output_dir):
            for dir_name in dirs:
                dir_name = dir_name.lower()
                if dir_name.startswith('hw'):
                    hw_dir = os.path.join(root, dir_name)
                    move_files_to_root(hw_dir, output_dir)
                    break  # Stop after handling the first matching folder
    else:
        print(f"{file_path} is not a ZIP file")


def move_files_to_root(source_dir, target_dir):
    """
    Moves all non-hidden files and subdirectories from source_dir to target_dir,
    then removes source_dir, including any hidden files or subdirectories.
    """
    for item in os.listdir(source_dir):
        src_path = os.path.join(source_dir, item)
        dst_path = os.path.join(target_dir, item)

        # Skip moving if destination already exists (prevents duplicates)
        if not item.startswith('.') and not os.path.exists(dst_path):
            shutil.move(src_path, dst_path)

    # Remove empty source directory if it exists
    cleanup_directory(source_dir)


def cleanup_directory(directory):
    """
    Recursively removes all files and hidden files before deleting the directory.
    """
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    try:
        os.rmdir(directory)
    except OSError:
        print(f"Could not remove directory: {directory}, may already be empty")

# Gets all the submitted files from an assignment and puts them in a folder "submission_dir"
# Each file will be added to a folder with the students canvas ID as the name of the folder
def get_files_from_assignment(assignment_id, submissions_dir):
    """
    Fetches files from an assignment and handles ZIP extraction.
    If submissions_dir already exists, deletes and recreates it.
    """
    # Remove existing directory and create a fresh empty one
    if os.path.exists(submissions_dir):
        shutil.rmtree(submissions_dir)
    os.makedirs(submissions_dir)

    assignment = course.get_assignment(assignment_id)
    submissions = assignment.get_submissions()  # Gets submissions
    for submission in submissions:
        if submission.grade is not None and submission.grade_matches_current_submission:
            continue
        attachments = submission.attachments
        if not attachments:
            continue
        output_dir = f'{submissions_dir}/{submission.user_id}'
        os.makedirs(output_dir, exist_ok=True)

        for attachment in attachments:
            file_path = attachment.filename
            attachment.download(file_path)
            dst = os.path.join(output_dir, file_path)
            shutil.move(file_path, dst)

            # Extract ZIP files if detected
            extract_zip_file(dst, output_dir)

# Get's all the submissions from an assignment
def getSubmissions(assignment_id):
    assignment = course.get_assignment(assignment_id)
    submissions = assignment.get_submissions() # Get's submissions
    return submissions

# Grades all the students that did not submit
def grade_not_submitted(submissions):
    not_submitted = [s for s in submissions if len(s.attachments) == 0]
    for s in not_submitted:
        if s.score != None: continue
        s.edit(submission = {'posted_grade' : str(0)}, comment={'text_comment': 'No submission.'})


# Can be used to make manually grading with the rubric faster
def ask_questions_from_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    grade = 0
    for line in lines:
        grade += float(input(line.strip() + ' '))

    comment = input('Comment? ')
    if comment != '':
        comment += '\n'

    return grade, comment

# Prints all the homework assignments and their IDs (for reference)
if __name__ == '__main__':
    assignments = course.get_assignments()
    for a in assignments:
        print(a)


# # Old function to get the zip codes, might need to be fixed
# def old_get_files_from_assignment(assignment_id, submissions_dir):
#     if os.path.exists(submissions_dir):
#         shutil.rmtree(submissions_dir)
#     else:
#         os.makedirs(submissions_dir)
#
#     assignment = course.get_assignment(assignment_id)
#     submissions = assignment.get_submissions() # Get's submissions
#     for submission in submissions:
#         attachments = submission.attachments
#         for attachment in attachments:
#             if not any(a.filename.endswith('.zip') for a in attachments):
#                 output_dir = submissions_dir + '/' + str(submission.user_id)
#                 if not os.path.isdir(output_dir):
#                     os.makedirs(output_dir)
#                 filePath = attachment.filename
#                 attachment.download(filePath)
#                 dst = os.path.join(output_dir, filePath)
#                 shutil.move(filePath, dst)
#                 continue
#             if not attachment.filename.endswith('.zip'): continue
#             zipFilePath = attachment.filename
#             attachment.download(zipFilePath)
#             output_dir = str(submission.user_id)
#             unzipContent(submissions_dir, zipFilePath, output_dir)
#             os.remove(zipFilePath)
#
# # Unzips a file (might need to be fixed)
# def unzipContent(submissions_dir, zipFilePath, output_dir):
#     temp_dir = 'temp_extract'
#     if os.path.exists(temp_dir):
#         shutil.rmtree(temp_dir)
#     else:
#         os.makedirs(temp_dir)
#
#     with zipfile.ZipFile(zipFilePath, 'r') as zip_ref:
#         # Extract all contents to a temporary directory
#         zip_ref.extractall(temp_dir)
#
#     # Check if the extracted content is a folder
#     extracted_items = os.listdir(temp_dir)
#     new_folder = os.path.join(submissions_dir, output_dir)
#     os.makedirs(new_folder)
#     files = list_files_with_relative_path(temp_dir)
#
#     for file in files:
#         file_name = file.split('/')[-1]
#         dst = os.path.join(new_folder, file_name)
#         shutil.move(file, dst)
#
#     # Remove the temporary extract folder
#     shutil.rmtree(temp_dir)
#
#
# # Old helper function for unzip
# def list_files_with_relative_path(folder_path):
#     parent = os.getcwd()
#     file_list = []
#     for root, dirs, files in os.walk(folder_path):
#         directories = root.split('/')
#         if any(directory.startswith('.') for directory in directories): continue
#         for file in files:
#             if file.startswith('.'): continue
#             relative_path = os.path.relpath(os.path.join(root, file), parent)
#             if '__MACOSX' in relative_path: continue
#             file_list.append(relative_path)
#
#     return file_list
