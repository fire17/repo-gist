import os
import sys

def main():
    # Get the path to the repository from the command-line argument
    repo_path = sys.argv[1]

    # Initialize an empty string to hold the concatenated contents
    concatenated_contents = ""

    # Get the list of files in the repository
    files = os.listdir(repo_path)

    # Iterate through the files
    for file in files:
        # Add a header with the file path and filename
        concatenated_contents += f"\n\n# File: {os.path.abspath(file)}\n"

        # Open the file and read its contents
        with open(file, "r") as f:
            contents = f.read()
        # Append the contents to the concatenated string
        concatenated_contents += contents

    # Add a tree representation of the directory as a comment
    tree_representation = os.popen(f'tree {repo_path} /f').read()
    concatenated_contents += f"\n\n# Directory tree:\n{tree_representation}"

    # Print the concatenated contents
    print(concatenated_contents)

if __name__ == "__main__":
    main()
