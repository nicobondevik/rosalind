#!bin/bash/env python
from sys import argv

def main():
    count = {"A": 0, "C": 0, "G": 0, "T": 0}
    with open(argv[1]) as infile:
        for line in infile:
            for nt in line.strip():
                count[nt] += 1
    
    with open("out", "w") as outfile:
        for nt in count:
            outfile.write(f"{count[nt]} ")

if __name__ == "__main__":
    main()