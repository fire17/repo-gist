:After the intial prompt, and all of the promts to give me the file contents, these were used to help me turn this into a product:


call this script repoGist.py
make a package out of this , that i can easily share on pypi, show me all the necessary files i need in a folder tree structure view, and all of the files' contents 

make it so that after i install this package, ill be able to run it with the command:
repogist .

after running the script im getting 
IsADirectoryError: [Errno 21] Is a directory: '.git'
make sure that the script runs over nested directories properly, also skip any files or dirs that are usually found in gitignore

give me the updated code, also make sure that at the end , after the printing, the output is saved to a local file named the same as the repo name but ends with .gist.txt

change the script so that it fetches the repo_name from pwd , also make it so that it produces an md instead of text. each file should be clearly seperated in it's own code block (using ```) make  sure to change all instances of ``` in the original file's text to ''' to not break out of the code block

: gptchat is stuggeling to finish it's full response
instead of one big main method, make in several, reusable functions

give me all of the function names in repoGist

give me the contents of the following functions:
read_file
get_tree_representation
create_gist
write_gist
and main

give it a main function so i can still run it using repogist .
show me only the contents of main

(base) ➜  auto-repo-gist git:(main) ✗ python3 repoGist.py .
Traceback (most recent call last):
  File "repoGist.py", line 32, in read_file
    return f.read()
  File "/home/magic/anaconda3/lib/python3.7/codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x9f in position 13: invalid start byte

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "repoGist.py", line 84, in <module>
    main()
  File "repoGist.py", line 79, in main
    gist = create_gist(repo_name, files, tree_representation)
  File "repoGist.py", line 57, in create_gist
    contents = read_file(file_path).replace("*", "\\*").replace("_", "\\_")
  File "repoGist.py", line 36, in read_file
    contents = f.read().decode("utf-8")
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x9f in position 13: invalid start byte


include printing traceback exception, for debugging, and also the file that was currently checked when the execption was made, also suggest a fix, the previous iteration (the one that saves gist.txt intead of gist.md) was working properly, make sure it works similarly, but with the correct walk of dirs, the md formatting and all other things i requested

i think the problem is with the .replace("*", "\\*").replace("_", "\\_")
it should be .replace("```", "'''")
it is the other way arround , should eliminate all instanses of "```"
use .replace("```", "***")

the get files function is not skipping propely, instead of skipping the files .gitignore and .git , make sure to ignore all of the files listed inside the .gitignore file, and also ignore all the files in the .git directory. show me the changes
make sure this won't fail incase .gitignore is not found or accessible for any reason

make sure that you also skip the file that is named the {repo_name}.gist.md because it's an output from the previous run (which should not be included) in the gist


You are about to consume a gist containing all of the files and data in a repo
The problem with the code is that it includes files in the .git directory of the repo
i think the problem is in the line
if root.startswith(".git"):
it's probably not starting like that , maybe its ./.git or full path with ./git/ in it... figure out a better way to do this properly

{gist}

how do i upload this to pypi?
echo '''[distutils]
index-servers =
  pypi

[pypi]
repository: https://upload.pypi.org/legacy/
username: YOUR_USERNAME
password: YOUR_PASSWORD
''' > ~/.pypirc 
python setup.py sdist
python setup.py sdist upload
