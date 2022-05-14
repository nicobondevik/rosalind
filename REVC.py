#!bin/bash/env python
from sys import argv

def main():
    with open(argv[1]) as infile:
        compl = {"A": "T", "T": "A", "G": "C", "C": "G"}
        seq = list()
        for line in infile:
            seq.extend([compl[nt] for nt in line.strip()])
        seq.reverse()
    
    with open("out", "w") as outfile:
        outfile.write("".join(seq))

if __name__ == "__main__":
    main()