import os
import mimetypes
from convert_to_text import convertToJson

folder_path = 'Hackathon 2024 CVs'


number_of_jsons = 0
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)

        # Extract the file extension
        _, file_extension = os.path.splitext(file)

        # Detect the file's MIME type
        file_type, _ = mimetypes.guess_type(file_path)
        print(f"{number_of_jsons}{file_path}" + str(convertToJson(file_path)))
        number_of_jsons +=1

        # print(f"File: {file_path} | Extension: {file_extension} | Type: {file_type if file_type else 'Unknown'}")


