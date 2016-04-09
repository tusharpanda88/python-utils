import os
import glob

def main():
    list_pdf = glob.glob("*.pdf")
    print "pdf files in directory:",list_pdf

main()
