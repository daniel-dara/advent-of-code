/*
 * I redid this solution after doing part2 (the recursive version) so the similarities would be apparent.
 * While a valid solution is to actually generate the decompressed file and take the length of it, doing so
 * is not necessary when you can count the characters as you decompress without actually saving the results.
 * Reading the file linearly, a letter is +1 to the length. A marker (AxB) simply adds A * B to the total, with the
 * trick being that the marker itself doesn't count towards the total and you must continue parsing at 'A'
 * characters further in the input.
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

			total += repeat_count * char_count;
			index += marker_length + char_count - 1; // -1 is due to curIndex already being at the first parend of the sequence to skip
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