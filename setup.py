from setuptools import setup, find_packages
# from EXATools import Version

with open("README.md", "r", encoding = "utf-8") as RD:
    README = RD.read()

setup(
    name = "EXATools", 
    version = "0.0.0", 
    description = "暗星Atom制造的一些Python小工具", 
    long_description_content_type = "text/markdown",
    long_description = README, 
    license = "MIT", 
    author = "EXAtom", 
    author_email = "3522542971@qq.com", 
    url = "https://github.com/lihansen12345/EXATools", 
    packages = find_packages(), 
    install_requires = ["pyperclip", "pygame", "requests", "pillow"], 
    classifiers = [ 
        "Programming Language :: Python", 
        "Programming Language :: Python :: 3" ,
        "Operating System :: OS Independent", 
        "License :: OSI Approved :: MIT License",
    ]
)