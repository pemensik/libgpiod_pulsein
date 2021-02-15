CC=gcc
CFLAGS=-I. -Wall -O3
LIBS=-lgpiod -pthread
DEPS=libgpiod_pulsein.h
OBJ=libgpiod_pulsein.o circular_buffer.o

%.o: %.c $(DEPS)
		$(CC) -c $(CFLAGS) -o $@ $<

libgpiod_pulsein: $(OBJ)
		$(CC) -o $@ $^ $(LDFLAGS) $(CFLAGS) $(LIBS)
