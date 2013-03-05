#include <stdio.h>
#include <stdlib.h>
#include <sysexits.h>
#include <time.h>

int search(int values[], int count, int index, int step) {
	printf ("Index %d\n", index);
	int next_step = (step + 1) / 2;
	if (index != 0 && values[index - 1] > values[index]) {
		return search(values, count, index - next_step, next_step);
	} else if (index != count -1 && values[index + 1] > values[index]) {
		return search(values, count, index + next_step, next_step);
	} else {
		return index;
	}
}

int main (void) {
	int result;
	unsigned seed = (unsigned)time(NULL);
	int count = 4;
	int limit = 4;
	int values[count];
	int index;

	printf ("Seed: %u\n", seed);
	srand(seed);
	printf ("Input:\n");
	for (index = 0; index < count; index++) {
		values[index] = rand() % limit;
		printf ("%8d: %d\n", index, values[index]);
	}

	result = search(values, count, count / 2, count / 2);

	if (result != -1) {
		printf ("Peak found at index %d: %d\n", result, values[result]);
	} else {
		printf ("No peak found\n");
	}

	return EX_OK;
}
