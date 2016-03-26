
NEFS=$(wildcard nefs/*.nef)
PPMS_=$(patsubst %.nef,%.ppm,$(NEFS))
PPMS=$(patsubst nefs/%,ppms/%,$(PPMS_))
SHRINKS_=$(patsubst ppms/%,shrinks/%,$(PPMS))
SHRINKS=$(patsubst %.ppm,%.jpg, $(SHRINKS_))

.PRECIOUS: ppms/%.ppm shrinks/%.jpg
shrinks/%.jpg: ppms/%.ppm
	vips resize $< $@ .7
ppms/%.ppm: nefs/%.nef
	ufraw-batch --out-path=ppms --out-depth=8 $<

encode: $(SHRINKS)
	touch a.mp4
	#ffmpeg -pattern_type glob -i 'shrinks/TestTimelapse*.jpg' -r 30 -s hd1080 -vcodec libx264 -pix_fmt yuv420p a.mp4
	#ffmpeg -pattern_type glob -i 'shrinks/TestTimelapse005*.jpg'  -r 25 -s hd1080 -vcodec libx264 -pix_fmt yuv420p a.mp4
	#ffmpeg -pattern_type glob -i '/Users/caleb/pine-cone/shrinks/TestTimelapse*.jpg' -r 25 -vf scale=-1:2160 a.mp4
	cp -f a.mp4 b.mp4
	rm -f a.mp4
	ffmpeg -pattern_type glob -i 'shrinks/TestTimelapse*.jpg'  -r 25 -s 4k  a.mp4
	scp a.mp4 192.168.1.12:
	scp a.mp4 se.dyndns-ip.com:
sync:
	mkdir -p shrinks ppms
	rsync -av --size-only ~/pine-cone/pictures/ ~/pine-cone/nefs # syncrhonize the files from the teathered machine

shrinks: $(SHRINKS)

.PHONY: sync shrinks encode
all:


