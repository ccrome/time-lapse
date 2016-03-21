## Synopsis

This will be a collection of scripts that I use for processing a time lapse.  Likely not interesting to anybody but me.

## Code Example

rsync -av /Volumes/pictures/*.nef ~/pine-cone # syncrhonize the files from the teathered machine
miniturize.py -- given a bunch of .nef (raw) files, convert them to small versions of themselves.
id.py -- create json .id files of the miniturized files
deflicker.py
encode.py -- encode the files into an mp4.
