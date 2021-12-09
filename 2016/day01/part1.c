/*
 * This is a simple linear time solution that tracks the current position and heading as it reads each command from
 * input. Some clever boolean conversions keep the meat of the solution to just 3 lines. Modulo arithmetic is used to
 * determine the heading (NSEW) and the appropriate coordinate is then adjusted (+/- depending on heading) by count.
 * Since we are dealing with taxicab geometry, not euclidean distance, the shortest path to the destination is just the
 * x and y differences summed.
 */

#include <stdio.h>

int abs(int i) {
	return i > 0 ? i : -i;
}

int main() {
	// Example input.
	//const char* directions = "R2, L3";
	//const char* directions = "R2, R2, R2";
	//const char* directions = "R5, L5, R5, R3";

	// Problem input.
	const char* directions = "L2, L5, L5, R5, L2, L4, R1, R1, L4, R2, R1, L1, L4, R1, L4, L4, R5, R3, R1, L1, R1, L5, L1, R5, L4, R2, L5, L3, L3, R3, L3, R4, R4, L2, L5, R1, R2, L2, L1, R3, R4, L193, R3, L5, R45, L1, R4, R79, L5, L5, R5, R1, L4, R3, R3, L4, R185, L5, L3, L1, R5, L2, R1, R3, R2, L3, L4, L2, R2, L3, L2, L2, L3, L5, R3, R4, L5, R1, R2, L2, R4, R3, L4, L3, L1, R3, R2, R1, R1, L3, R4, L5, R2, R1, R3, L3, L2, L2, R2, R1, R2, R3, L3, L3, R4, L4, R4, R4, R4, L3, L1, L2, R5, R2, R2, R2, L4, L3, L4, R4, L5, L4, R2, L4, L4, R4, R1, R5, L2, L4, L5, L3, L2, L4, L4, R3, L3, L4, R1, L2, R3, L2, R1, R2, R5, L4, L2, L1, L3, R2, R3, L2, L1, L5, L2, L1, R4";

	// input helpers
	char dir;
	int count;
	int charsRead;
	int index = 0;

	// directional constants
	const int N = 0, E = 1, S = 2, W = 3;

	// current position
	int curDir = 0;
	int x = 0;
	int y = 0;

	while (sscanf(&directions[index], "%c%d, %n", &dir, &count, &charsRead) == 2) {
		index += charsRead;

		curDir = (curDir - (dir == 'L') + (dir == 'R') + 4) % 4;

		x += count * ((curDir == E) - (curDir == W));
		y += count * ((curDir == N) - (curDir == S));
	}

	printf("distance from start: %d\n", abs(x) + abs(y));
	return 0;
}

