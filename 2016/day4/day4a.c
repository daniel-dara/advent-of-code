/*
 * Comments
 */

#include <stdio.h>

int main() {
	FILE* input = fopen("input.txt", "r");

	int answer = 0;
	int foo;

	while (fscanf(input, "%d", &foo) != EOF) {
		
	}

	printf("%d\n", answer);

	fclose(input);

	return 0;
}