/*
 * Because none of the decoy rooms were actually decoys (out of all rooms real or not, only one had "northpole" in it),
 * a majority of the previous solution was left out to simplify this one. Besides the parsing (which is same as last
 * solution), the only thing to it was decryption of the room name. This is done with some simple modulo
 * arithmetic.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CHECKSUM_SIZE 5

int main() {
	FILE* input = fopen("input.txt", "r");

	char c;
	char room_name[100] = {0};
	int index = 0;

	while (fscanf(input, "%c", &c) != EOF) {
		if (c >= 'a' && c <= 'z') {
			room_name[index++] = c;
		} else if (c != '-') {
			// parse sector_id (first digit is already in c)
			int sector_id;
			fscanf(input, "%d[[^]]*]\n", &sector_id);
			sector_id += 100 * (c - '0');

			// decrypt the room name
			for (int i = 0; i < index; i++) {
				if (room_name[i] != ' ') {
					room_name[i] = ((sector_id + room_name[i] - 'a') % 26) + 'a';
				}
			}

			if (strstr(room_name, "northpole") != NULL) {
				printf("room name: %s\nsector id: %d\n", room_name, sector_id);
				fclose(input);
				return 0;
			}

			memset(room_name, 0, sizeof(room_name));
			index = 0;
		} else {
			room_name[index++] = ' ';
		}
	}

	printf("ERROR: Room \"northpole\" not found.\n");
	fclose(input);

	return 1;
}