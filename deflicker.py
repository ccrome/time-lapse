import utils
import json
from pylab import *
import numpy as np

ids = utils.get_files("800x530", ".id")
all_data = {}
for fn, dir, b in ids:
    try:
        x = json.load(open(fn))
    except ValueError as e:
        print "Erorr reading %s " % (fn), e
        exit()
    all_data[fn] = x


means = list()
for fn in sort(all_data.keys()):
    means.append(all_data[fn]["mean"])


start_date =  11 + 21.0/60
num = len(means)
end_date = start_date + num * 2.0/60
t = linspace(start_date, end_date, num)
plot(t, means)
show()

