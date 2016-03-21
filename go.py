#!/usr/bin/env python
import subprocess
import time
while (1):
    print "Starting loop"
    cmd = ["./sync"]
    subprocess.call(cmd)
    cmd = ["/usr/bin/env", "python", 
           "miniturize.py"]
    subprocess.call(cmd)
    cmd = ["/usr/bin/env", "python", 
           "id.py"]
    subprocess.call(cmd)
    cmd = ["/bin/rm", "b.mp4"]
    subprocess.call(cmd)
    cmd = ["/bin/mv", "a.mp4", "b.mp4"]
    subprocess.call(cmd)
    cmd = ["/usr/bin/env", "python", 
           "encode.py"]
    subprocess.call(cmd)
    time.sleep(1)
