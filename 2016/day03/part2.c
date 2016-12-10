/*
 * Relatively trivial solution. O(N) where N is lines of input.
 */

#include <stdio.h>

int isTriangle(int t[]) {
	return (t[0] + t[1] > t[2] && t[1] + t[2] > t[0] && t[0] + t[2] > t[1]);
}

int main() {
	FILE* input = fopen("input.txt", "r");

	int answer = 0;
	int t1[3];
	int t2[3];
	int t3[3];

	while (fscanf(input, "%d %d %d", &t1[0], &t2[0], &t3[0]) != EOF) {
		fscanf(input, "%d %d %d", &t1[1], &t2[1], &t3[1]);
		fscanf(input, "%d %d %d", &t1[2], &t2[2], &t3[2]);

		answer += isTriangle(t1) + isTriangle(t2) + isTriangle(t3);
	}

	printf("%d\n", answer);

	fclose(input);

	return 0;
}