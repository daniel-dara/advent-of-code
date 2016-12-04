/*
 * Straightforward state machine.
 */

#include <stdio.h>

#define SIZE 3

int main() {
	FILE* input = fopen("day2.in", "r");

	char c;

	char numpad[SIZE][SIZE] = {
		{'1', '2', '3'},
		{'4', '5', '6'},
		{'7', '8', '9'}
	};

	int col = 1;
	int row = 1;

	char num[5] = {0};
	int index = 0;

	while (fscanf(input, "%c", &c) != EOF) {
		if (c == 'U' && col > 0) {
			col--;
		} else if (c == 'D' && col < SIZE - 1) {
			col++;
		} else if (c == 'L' && row > 0) {
			row--;
		} else if (c == 'R' && row < SIZE - 1) {
			row++;
		} else if (c == '\n') {
			num[index++] = numpad[col][row];
		}
	}

	num[index++] = numpad[col][row];

	printf("%s\n", num);

	return 0;
}