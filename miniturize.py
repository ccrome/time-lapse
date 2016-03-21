#!/usr/bin/env python
import Queue as queue
import threading
import sys
import subprocess
import os
import time
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
    
def worker(job, q):
    nef, x, y, tiffname = job
    convert(nef, "%dx%d/%s" % (x, y, tiffname), x, y)
    q.put("Done")

nefs  = get_files(root, ".nef")
tiffs = get_files(root, ".tiff")

jobs = []
for nef in nefs:
    tiffname = "%s.tiff" % nef
    if (tiffname not in tiffs):
        # If not already converted.
        x = 800
        y = 530
        jobs.append((nef, x, y, tiffname))

nthreads = 2
threads = list( )

q = queue.Queue()
running = 0

while (len(jobs)):
    job = jobs.pop()
    t = threading.Thread(target = worker, args=(job, q))
    #t.daemon = True
    t.start()
    running = running + 1
    if (running == nthreads):
        running = running - 1
        # Running as many parallel threads as needed.
        q.get() # wait for one to finish
