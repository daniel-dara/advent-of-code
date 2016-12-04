/*
 * Relatively trivial solution. O(N) where N is lines of input.
 */

#include <stdio.h>

int main() {
	FILE* input = fopen("input.txt", "r");

	int answer = 0;
	int a, b, c;

	while (fscanf(input, "%d %d %d\n", &a, &b, &c) != EOF) {
		answer += (a + b > c && b + c > a && a + c > b);
	}

	printf("%d\n", answer);

	fclose(input);

	return 0;
}