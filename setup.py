from setuptools import setup

setup(
    name="repo-gist",
    version="0.1.0",
    py_modules=["repoGist"],
    install_requires=[],
    author="Your Name",
    author_email="your@email.com",
    description="A script to create a gist from the contents of a repository",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/repo-gist",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "repogist = repoGist:main"
        ]
    }
)
