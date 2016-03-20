#!/usr/bin/env python
# create .id files of each miniature .tiff file, for later use in deflicker, white balance, etc.
import sys
import subprocess
import os
from utils import get_files

# find all the .nef files
root="/Users/caleb/pine-cone"

def identify(input_fn, id_output):
    fields = [
        ["base", "base filename, no suffixes (as %t)"],
        ["channels", "??? channels in use - colorspace ???"],
        ["colorspace", "Colorspace of Image Data (excluding transparency)"],
        ["copyright", "ImageMagick Copyright String"],
        ["depth", "depth of image for write (as input unless changed)"],
        #["deskew:angle", "The deskew angle in degrees of rotation"],
        ["directory", "directory part of filename (as %d)"],
        #["distortion", "how well an image resembles a reference image (-compare)"],
        ["entropy", "CALCULATED: entropy of the image"],
        ["extension", "extension part of filename (as %e)"],
        ["gamma", "value of image gamma"],
        ["group", "window group"],
        ["height", "original height of image (when it was read in)"],
        ["kurtosis", "CALCULATED: kurtosis statistic of image"],
        #["label", "label meta-data property"],
        ["magick", "coder used to read image (not the file suffix)"],
        ["max", "CALCULATED: maximum value statistic of image"],
        ["mean", "CALCULATED: average value statistic of image"],
        ["min", "CALCULATED: minimum value statistic of image"],
        #["name", "The original name of the image"],
        ["opaque", "CALCULATED: is image fully-opaque?"],
        ["orientation", "image orientation"],
        ["page", "Virtual canvas (page) geometry"],
        #["profile:icc", "ICC profile info"],
        #["profile:icm", "ICM profile info"],
        #["profiles", "list of any embedded profiles"],
        ["resolution.x", "X density (resolution) without units"],
        ["resolution.y", "Y density (resolution) without units"],
        ["scene", "original scene number of image in input file"],
        ["size", "original size of image (when it was read in)"],
        ["skewness", "CALCULATED: skewness statistic of image"],
        ["standard-deviation", "CALCULATED: standard deviation statistic of image"],
        ["type", "CALCULATED: image type"],
        ["unique", "unique temporary filename"],
        ["units", "image resolution units"],
        ["version", "Version Information of this running ImageMagick"],
        ["width", "original width of image (when it was read in)"],
        ["zero", "zero (unique filename for delegate use)"],
        ]
    format = "{\n" + ",\n".join(["    \"%s\" : \"%%[%s]\"" % (x[0], x[0]) for x in fields]) + "\n}\n"
    cmd = ["identify",
           "-format", format,
           input_fn]
    print "outputting to  %s" % id_output
    sys.stdout.flush()
    f = open(id_output, "w")
    process = subprocess.Popen(cmd, stdout = f)
    out, err = process.communicate()
    f.close()
    exit()

tiffs  = get_files(root, ".tiff")
ids = get_files(root, ".tiff.id")

for tiff, dir, fn in tiffs:
    idname = "%s.id" % tiff 
    if (idname not in ids):
        identify(tiff, idname)
