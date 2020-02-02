CC := g++

CFLAGS := -std=c++17 -Wall -Werror

main.out: num.o main.o
	$(CC) $(CFLAGS) $^ -o $@

main.o: main.cpp
	$(CC) $(CFLAGS) -c $<

num.o: num.cpp num.h
	$(CC) $(CFLAGS) -c $<

clean:
	rm *.o *.out

