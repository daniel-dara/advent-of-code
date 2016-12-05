/*
 * A straightforward solution but rather tricky to parse in C. Calculation of the expected checksum
 * is done by incrementing elements in the alphabet array to track letter occurences. When the room name is completely
 * parsed/counted, the alphabet is iterated over from a to z. The expected checksum starts off as blank with each
 * letter occurence being 0. For each letter, the entire checksum is iterated over and if the current letter's occurence
 * is higher than one in the checksum, the new letter is inserted in it's place and everything else shifted back.
 * This ensures ties are handled alphabetically.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CHECKSUM_SIZE 5

void insert(char* array, char val, int i) {
	int j;

	for (j = CHECKSUM_SIZE - 1; j > i; j--) {
		array[j] = array[j - 1];
	}

	array[j] = val;
}

int main() {
	FILE* input = fopen("input.txt", "r");

	int total = 0;
	char c;
	int alphabet[26] = {0};

	while (fscanf(input, "%c", &c) != EOF) {
		if (c >= 'a' && c <= 'z') {
			alphabet[c - 'a']++;
		} else if (c != '-') {
			// parse sector_id (first digit is already in c)
			int sector_id;
			fscanf(input, "%d[", &sector_id);
			sector_id += 100 * (c - '0');

			// calculate expected checksum
			int i, j;
			char expected_checksum[CHECKSUM_SIZE + 1] = {0};
			char checksum_counts[CHECKSUM_SIZE] = {0};

			for (i = 0; i < 26; i++) {
				for (j = 0; j < CHECKSUM_SIZE; j++) {
					if (alphabet[i] > checksum_counts[j]) {
						insert(expected_checksum, i + 'a', j);
						insert(checksum_counts, alphabet[i], j);
						break;
					}
				}
			}

			// parse actual checksum
			char actual_checksum[CHECKSUM_SIZE + 1] = {0};
			fscanf(input, "%[^]]]\n", actual_checksum);

			if (!strcmp(actual_checksum, expected_checksum)) {
				total += sector_id;
			}

			memset(alphabet, 0, sizeof(alphabet));
		}
	}

	printf("%d\n", total);

	fclose(input);

	return 0;
}