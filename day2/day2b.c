/*
 * Hardly different from first problem. Just can't rely on absolute dimensional bounds anymore so must use padding instead.
 */

#include <stdio.h>

#define SIZE 5

int main() {
	FILE* input = fopen("input.txt", "r");

	char c;

	char numpad[SIZE][SIZE] = {
		{0, 0, '1', 0, 0},
		{0, '2', '3', '4', 0},
		{'5', '6', '7', '8', '9'},
		{0, 'A', 'B', 'C', 0},
		{0, 0, 'D', 0, 0}
	};

	int col = 2;
	int row = 0;

	char num[5] = {0};
	int index = 0;

	while (fscanf(input, "%c", &c) != EOF) {
		if (c == 'U' && col > 0 && numpad[row][col - 1] != 0) {
			col--;
		} else if (c == 'D' && col < SIZE - 1 && numpad[row][col + 1] != 0) {
			col++;
		} else if (c == 'L' && row > 0 && numpad[row - 1][col] != 0) {
			row--;
		} else if (c == 'R' && row < SIZE - 1 && numpad[row + 1][col] != 0) {
			row++;
		} else if (c == '\n') {
			num[index++] = numpad[col][row];
		}
	}

	num[index++] = numpad[col][row];

	printf("%s\n", num);

	fclose(input);

	return 0;
}