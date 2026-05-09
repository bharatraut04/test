import sys
print("Arguments:", sys.argv)

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--name", type = str , help = "your name ")
parser.add_argument("--age", type = int , help = "your age ")
args = parser.parse_args()
print(f"hello {args.name}, your are {args.age} years old!")


import argparse
parser = argparse.ArgumentParser(description="count words in a file")
parser.add_argument("file", type = str , help = "File Path")
args = parser.parse_args()
with open(args.file, "r") as f:
    text = f.read()
    words = text.split()
print(f"Word Count : {len(words)}")



import argparse
parser = argparse.ArgumentParser()

#add command line arguments 
parser.add_argument("url",help = "Url of the file to download")
parser.add_argument("output",help = "by which name do you want to save your file")

# Parse the arguments
args = parser.parse_args()

# use the arguments in your code
print(args.arg1)
print(args.arg2)

