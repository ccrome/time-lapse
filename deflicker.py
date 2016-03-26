#!/usr/local/bin/python
from gi.repository import Vips
import os.path
from vipsCC import *
import utils
import json
#from pylab import *
#import numpy as np

indir  = "800x530"
outdir = "800x530.out"
ids = utils.get_files(indir, ".tiff")

im = Vips.Image.new_from_file(ids[0][0])
target_avg = im.avg()

for full_fn, dir, fn  in ids:
    im = Vips.Image.new_from_file(full_fn)
    avg = im.avg()
    r = target_avg/avg
    print r
    im_out = im.linear([r, r, r], [0, 0, 0]).cast(im.format)
    out_fn = os.path.join(outdir, fn)
    new_avg =im_out.avg()
    print out_fn
    im_out.write_to_file(out_fn)
#
##
#
#all_data = {}
#for fn, dir, b in ids:
#    try:
#        x = json.load(open(fn))
#    except ValueError as e:
#        print "Erorr reading %s " % (fn), e
#        exit()
#    all_data[fn] = x
#
#
#means = list()
#for fn in sort(all_data.keys()):
#    means.append(all_data[fn]["mean"])
#
#
#start_date =  11 + 21.0/60
#num = len(means)
#end_date = start_date + num * 2.0/60
#t = linspace(start_date, end_date, num)
#plot(t, means)
#show()

