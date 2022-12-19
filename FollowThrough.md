:After the intial prompt, and all of the promts to give me the file contents, these were used to help me turn this into a product:


call this script repoGist.py
make a package out of this , that i can easily share on pypi, show me all the necessary files i need in a folder tree structure view, and all of the files' contents 

make it so that after i install this package, ill be able to run it with the command:
repogist .

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
