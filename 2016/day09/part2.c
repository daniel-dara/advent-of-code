/*
 * As stated by the problem, the decompressed output is too large to hold in memory, but technically, since markers within
 * markers must be counted, there would be no other way to solve the problem if it weren't for one special characteristic
 * of the input. Markers will only appear inside of other markers as a whole marker, this makes it possible to simply do
 * a linear count like before, with some recursion to consume inner markers. If this characteristic weren't true,
 * you could decompress to separate markers which when concatenated, created a third marker that you would only know
 * through actually storing the output.
 */

#include <stdio.h>

#define MAX_INPUT_SIZE 20000

typedef unsigned long long ull;

char file[MAX_INPUT_SIZE];

// Returns the length of the decompressed string from index to maxIndex in file.
ull decompress(int index, int maxIndex) {
	ull total = 0;

	while (index < maxIndex) {
		if (file[index] == '(') {
			int char_count, repeat_count, marker_length;
			sscanf(&file[index], "(%dx%d)%n", &char_count, &repeat_count, &marker_length);

			index += marker_length;
			total += repeat_count * decompress(index, index + char_count);
			index += char_count - 1; // -1 is due to curIndex already being at the first parend of the sequence to skip
		} else {
			total++;
		}

		index++;
	}

	return total;
}

int main() {
	FILE* input = fopen("input.txt", "r");
	int fileLength;

	while (fscanf(input, "%s%n ", file, &fileLength) != EOF) {
		printf("%lld\n", decompress(0, fileLength));
	}

	fclose(input);

	return 0;
}