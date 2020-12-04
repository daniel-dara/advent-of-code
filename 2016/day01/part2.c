/*
 * This is a lazy solution but one that works since the bounds of the input are known and reasonable for this technique.
 * Instead of immediately adjusting the x and y coordinates to the new location based on the most recent input command,
 * I use a loop to increment an integer at each point in the grid that is crossed. If drawn on a graph, this basically
 * generates a continuously growing snake. Once the "snake" hits it's own tail, it knows to stop since it has reached
 * the first crossing (second visit).
 *
 * Worst case, this solution would take SIZE^2 time if the snake performed a perfect outward-moving spiral. Since the input consists
 * of only a hundred or so commands, I knew it wouldn't cover that much area and would be much less than that (although
 * even a million is doable in a few seconds).
 *
 * For higher coordinate ranges, brute force by comparing new segments against all previous ones and checking for
 * intersection would still work for low values of N (it would run in N^2). For even higher values of N, you could
 * probably use an adapted vertical line scan technique.
 */

#include <stdio.h>
#include <string.h>

#define SIZE 1000

int visited[SIZE][SIZE];

int visit(int x, int y) {
	x += 500;
	y += 500;

	if (x < 0 || y < 0 || x > SIZE || y > SIZE) {
		printf("ERROR: visited size not large enough.\n");
		return 1;
	}

	return ++visited[y][x] > 1;
}

int abs(int i) {
	return i > 0 ? i : -i;
}

int sign(int i) {
	return i < 0 ? -1 : 1;
}

int main() {
	// Example input
	//const char* directions = "R8, R4, R4, R8"

	// Problem input
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

	memset(visited, 0, sizeof(visited));

	while (sscanf(&directions[index], "%c%d, %n", &dir, &count, &charsRead) == 2) {
		index += charsRead;

		curDir = (curDir - (dir == 'L') + (dir == 'R') + 4) % 4;

		int *a;
		int b;

		if (curDir == N || curDir == S) {
			a = &y;
		} else {
			a = &x;
		}

		b = *a;

		int step = (curDir == N || curDir == E) - (curDir == S || curDir == W);

		for (; *a != b + sign(step) * count; *a += step) {
			if (visit(x, y)) {
				printf("distance from first twice: %d\n", abs(x) + abs(y));
				return 0;
			}
		}
	}

	printf("ERROR: No location found twice.\n");
	return 1;
}
