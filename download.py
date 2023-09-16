import gdown
import mimetypes

# Prompt the user to enter the Google Drive file ID.
file_id = input("Enter the Google Drive File ID: ")

# Get the file info, including the MIME type.
url = f'https://drive.google.com/uc?id={file_id}'
file_info = gdown.download(url, quiet=False, output=None, proxy=None, speed=None)

# Use mimetypes to determine the file extension.
mime_type, _ = mimetypes.guess_type(url)
if mime_type:
    file_extension = mimetypes.guess_extension(mime_type)
else:
    # Default to a specific extension if the MIME type is not recognized.
    file_extension = '.bin'  # You can change this to your desired default extension.

# Specify the output file name with the correct extension.
output = f'downloaded_file{file_extension}'

# Download the file.
gdown.download(url, output, quiet=False)
