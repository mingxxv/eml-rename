import os

from email import message_from_file

# Path to folder where .eml files are stored.
path = "./eml_files"

def rename_files(path):
    # Iterate through all files in the folder and rename them as "sender's email address - subject.eml"
    for filename in os.listdir(path):
        with open(os.path.join(path, filename)) as f:
            msg = message_from_file(f)
            subject = msg["subject"]
            sender = msg["from"]
            new_filename = sender + " - " + subject + ".eml"
            os.rename(os.path.join(path, filename), os.path.join(path, new_filename))