
NEFS=$(wildcard nefs/*.nef)
PPMS_=$(patsubst %.nef,%.ppm,$(NEFS))
PPMS=$(patsubst nefs/%,ppms/%,$(PPMS_))
SHRINKS_=$(patsubst ppms/%,shrinks/%,$(PPMS))
SHRINKS=$(patsubst %.ppm,%.jpg, $(SHRINKS_))

.PRECIOUS: ppms/%.ppm shrinks/%.jpg
shrinks/%.jpg: ppms/%.ppm
	vips resize $< $@ .2
ppms/%.ppm: nefs/%.nef
	ufraw-batch --out-path=ppms --out-depth=8 $<

encode: $(SHRINKS)
	ffmpeg -pattern_type glob -i 'shrinks/TestTimelapse*.jpg' -r 25 -s hd1080 -vcodec libx264 -pix_fmt yuv420p a.mp4
sync:
	mkdir -p shrinks ppms
	rsync -av --size-only ~/pine-cone/pictures/*.nef ~/pine-cone/nefs # syncrhonize the files from the teathered machine
