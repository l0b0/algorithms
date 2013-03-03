#include <stdio.h>
#include <stdlib.h>
#include <sysexits.h>
#include <time.h>

int main (void) {
	int result = -1;
	unsigned seed = (unsigned)time(NULL);
	int count = 10;
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

	for (index = 0; index < count; index++) {
		if (((index == 0) || (values[index] >= values[index - 1])) && ((index == count - 1) || (values[index] >= values[index + 1]))) {
			result = index;
			break;
		}
	}

	if (result != -1) {
		printf ("Peak found at index %d: %d\n", result, values[result]);
	} else {
		printf ("No peak found\n");
	}

	return EX_OK;
}
