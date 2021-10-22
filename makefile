CC = gcc

CFLAGS =  -Wall\
          -Iinclude\

SOURCES = src/cAPA102.c

example = cAPA102_example
pov = final
all: $(example) $(pov)

$(example): example/example.c $(SOURCES)
	$(CC) $^ -o $@ $(CFLAGS)


$(pov): example/pov.c $(SOURCES)
	$(CC) $^ -o $@ $(CFLAGS)
clean:
	rm $(example) $(pov)
