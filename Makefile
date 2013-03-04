objects = peak_1d_n_squared

.PHONY: all
all: $(objects)

# Compilation
$(objects): %: %.c
	gcc -Wall -o $@ $<

# Assembly
.PHONY: %.s
%.s: %.c
	gcc -Wall -S -fverbose-asm -c -o- $<

.PHONY: asm
asm: $(addsuffix .s,$(objects))

# Test
.PHONY: %.cppcheck
%.cppcheck: %.c
	cppcheck $<

.PHONY: cppcheck
cppcheck: $(addsuffix .cppcheck,$(objects))

.PHONY: %.splint
%.splint: %.c
	splint $<

.PHONY: splint
splint: $(addsuffix .splint,$(objects))

.PHONY: %.valgrind
%.valgrind: %
	valgrind ./$<

.PHONY: valgrind
valgrind: $(addsuffix .valgrind,$(objects))

.PHONY: test
test: cppcheck splint valgrind

# Clean up
.PHONY: clean
clean:
	-rm $(objects)
