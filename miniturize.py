#!/usr/bin/env python
import sys
import subprocess
import os

# find all the .nef files
root="/Users/caleb/pine-cone"

def get_files(dir, ext):
    nefs = list()
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(ext):
                nefs.append(file)
    return nefs

def convert(input, output, x, y):
    cmd = ["convert", input, 
           "-geometry", "%dx%d" % (x, y), 
           output
           ]
    print " ".join(cmd)
    sys.stdout.flush()
    subprocess.call(cmd)
    


nefs  = get_files(root, ".nef")
tiffs = get_files(root, ".tiff")

for nef in nefs:
    tiffname = "%s.tiff" % nef
    if (tiffname in tiffs):
        # If not already converted.
        x = 800
        y = 530
        convert(nef, "%dx%d/%s" % (x, y, tiffname), x, y)



