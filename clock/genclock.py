import subprocess
for hour in range(0, 12):
    for minute in range(0, 60):
        print "%02d:%02d" % (hour, minute)
        rot_min = 360.0 / 60 * minute
        rot_hour = 360.0 / 12 * hour + ( (360.0 / 12) * 1/60*minute)
        cmd = ["composite", 
               "-rotate", "%f" % rot_min, "clock_minute.png",
               "clock_face.png",
               "out.png"]
        subprocess.call(cmd)
        cmd = ["composite", 
               "-rotate", "%f" % rot_hour, "clock_hour.png",
               "out.png",
               "clock-%02d:%02d.png" % (hour, minute)]
        subprocess.call(cmd)


