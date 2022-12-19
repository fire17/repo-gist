# Repo-Gist
## This is an ai generated project that helps turn an entire repo into a big gist that chatgpt can consume

### easy install with pip
```
python3 -m pip install repo-gist --upgrade
```

### usage: first cd into your directory, then run 
```
repo-gist .
```

This will generate an {repo}.gist.md file in your repo containing all of itself

*you can add files to .gitignore or .gistignore to exclude files or dir paths (TBD)

### to reupload to pip after edits (internal use only)
```
update setup.py version
python setup.py sdist bdist_wheel
twine upload dist/*
git tag -a 0.1.4 -m "Release 0.1.4"
git push origin --tags
```

:The current dir of the project: # all combined, show me the project folder structure tree with all the files in it
```
├── FollowThrough.md
├── README.md
├── Test
│   ├── B
│   │   └── t.text
│   └── Yo.txt
├── auto-repo-gist.gist.md
├── repoGist.py
└── setup.py
```

:This repo was generated using chatGPT and was tested by a human for correctness (and is actively maintained by it TBD) The seed of this project was this prompt:
```
This is the README.md of the repo
This is an ai generated project that helps turn an entire repo into a big gist that chatgpt can consume

write this program, do it in python, run it on the current directory, the script should print out and save the gist locally. Have it to read all of the files in my current working directory (when running this script), it is already cloned locally, no need for github apis, show me the entire edited script. make sure the output is well formatted, each piece of code should be clearly indicated which path and file it belongs to (as headers, as comments). add a tree dir representation at the end of the gist (in a comment)
```



