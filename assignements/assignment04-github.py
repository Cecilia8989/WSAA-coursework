from github import Github
from config import configK as cfg

def create_or_get_file(repo, filename, file_content):
    try:
        # Check if the file exists
        repo.get_contents(filename)
    except Exception as e:
        # File doesn't exist, create it
        print(f"The file '{filename}' does not exist in the repository.")
        print(f"Creating the file: file name {filename}")
        repo.create_file(filename, "Initial commit", file_content)
    else:
        #reinstate initial commit
        file_info = repo.get_contents(filename)
        repo.update_file(file_info.path, "Update txt file", file_content, file_info.sha)
         


def update_file_content(repo, filename, name_to_replace, new_name):
    file_info = repo.get_contents(filename)
    content = file_info.decoded_content.decode("utf-8")
    new_content = content.replace(name_to_replace, new_name)
    repo.update_file(file_info.path, "Update txt file", new_content, file_info.sha)


def delete_file_if_requested(repo, filename):
    delete_input = input(f"Do you want to delete the file '{filename}'? (yes/no): ").lower()
    if delete_input == "yes" or delete_input == "y":
        try:
            file_info = repo.get_contents(filename)
            repo.delete_file(file_info.path, "Delete file", file_info.sha)
            print(f"The file '{filename}' has been deleted.")
        except Exception as e:
            print(f"Failed to delete the file '{filename}'.")
    else:
        print("Deletion aborted.")

# Define the apikey to be used
apikey = cfg["githubkey"]
# Define the owner of the GitHub repository 
github_owner = "Cecilia8989"
# Define the name of the repository 
github_repository = "Messy_wsa"
# Define file name 
filename = "assignement_week5.txt"
# Define file content 
file_content = "Hi, My name is Andrew. By Andrew"
# Define name to replace 
name_to_replace = "Andrew"
# Define New Name 
new_name = "Cecilia"

# Initialize GitHub instance with your API key
g = Github(apikey)
repo = g.get_repo(f"{github_owner}/{github_repository}")

# Create or get the file
create_or_get_file(repo, filename, file_content)

# Display old file content
file_info = repo.get_contents(filename)
content = file_info.decoded_content.decode("utf-8")
print(f"Original content of the file: {content}")

# Update file content
update_file_content(repo, filename, name_to_replace, new_name)

# Display file content
file_info = repo.get_contents(filename)
content = file_info.decoded_content.decode("utf-8")
print(f"New content of the file: {content}")

# Prompt user for file deletion
delete_file_if_requested(repo, filename)
