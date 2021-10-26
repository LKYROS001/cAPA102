CC = gcc

CFLAGS =  -Wall\
          -Iinclude\

SOURCES = src/cAPA102.c

example = cAPA102_example
pov = final
test = tester
vid = video

all: $(example) $(pov) $(test) $(vid)

$(example): example/example.c $(SOURCES)
	$(CC) $^ -o $@ $(CFLAGS)


$(pov): example/pov.c $(SOURCES)
	$(CC) $^ -o $@ $(CFLAGS)
	
$(test): example/test.c $(SOURCES)
	$(CC) $^ -o $@ $(CFLAGS)
	
$(vid): example/vid.c $(SOURCES)
	$(CC) $^ -o $@ $(CFLAGS)
	
clean:
	rm $(example) $(pov) $(test) $(vid)
