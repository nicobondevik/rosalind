#!bin/bash/env python
from sys import argv

def main():
    with open(argv[1]) as infile:
        seq = list()
        for line in infile:
            seq.extend(["U" if nt=="T" else nt for nt in line.strip()])
    
    with open("out", "w") as outfile:
        outfile.write("".join(seq))

if __name__ == "__main__":
    main()