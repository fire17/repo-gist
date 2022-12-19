from setuptools import setup

setup(
    name="repo-gist",
    version="0.1.1",
    py_modules=["repoGist"],
    install_requires=[],
    author="Tami",
    author_email="fire17@gmail.com",
    description="Create a gist from the contents of a repository, easy share with ChatGPT",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/fire17/auto-repo-gist",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "repo-gist = repoGist:main"
        ]
    }
)
