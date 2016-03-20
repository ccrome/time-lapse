import subprocess
import utils

fps = 25
resolution = "hd720"

cmd = ["ffmpeg", 
       "-pattern_type", "glob", "-i", '800x530/TestTimelapse*.nef.tiff',
       "-r", "%s" % fps,
       "-s", resolution,
       "-vcodec", "libx264",
       "a.mp4"]
subprocess.call(cmd)
