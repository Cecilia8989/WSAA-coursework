# Web Service and Application
# assignement 4
# Author: Cecilia Pastore 


# import the needed library
from github import Github
from config import configK as cfg

# Function to retrieve content of a file from a GitHub repository
def get_content_file(repo, filename):
    # Get file information
    file_info = repo.get_contents(filename)
    # Decode content from bytes to string
    content = file_info.decoded_content.decode("utf-8")
    return content
   
# Function to create a new file or update existing file in a GitHub repository
def create_or_get_file(repo, filename, file_content):
    try:
        # Check if the file exists
        repo.get_contents(filename)
        print(f"The file '{filename}' exist in the repository '{github_repository}'")
        print(f"Changing the content based on the variable 'file_content'.")
    except Exception as e:
        # File doesn't exist, create it
        print(f"The file '{filename}' does not exist in the repository.")
        print(f"Creating the file: file name {filename}")
        repo.create_file(filename, "Initial commit", file_content)
    else:
        # File exists, update its content to the define one in the variable "file_content"
        file_info = repo.get_contents(filename)
        repo.update_file(file_info.path, "Update txt file", file_content, file_info.sha)

# Function to update content of an existing file in a GitHub repository
def update_file_content(repo, filename, name_to_replace, new_name):
    # get file info and content from the file
    file_info = repo.get_contents(filename)
    content = file_info.decoded_content.decode("utf-8")
    # Replace specified text in the content
    new_content = content.replace(name_to_replace, new_name)
    # Update file with new content
    repo.update_file(file_info.path, "Update txt file", new_content, file_info.sha)

# Function to delete a file from a GitHub repository if requested by the user
def delete_file_if_requested(repo, filename):
    # Ask the user if he wants delete the file 
    delete_input = input(f"Do you want to delete the file '{filename}'? (yes/no): ").lower()
    # if user answer yes delete the file 
    if delete_input == "yes" or delete_input == "y":
            # Get file information
            file_info = repo.get_contents(filename)
            # Delete the file
            repo.delete_file(file_info.path, "Delete file", file_info.sha)
            print(f"The file '{filename}' has been deleted.")
    else:
        print(f"The file is in the repository '{github_repository}'")
            

# Define the API key to be used
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
content = get_content_file(repo, filename)
print(f"Original content of the file: {content}")

# Update file content
update_file_content(repo, filename, name_to_replace, new_name)

# Display new file content
content = get_content_file(repo, filename)
print(f"New content of the file: {content}")

# Prompt user for file deletion
delete_file_if_requested(repo, filename)