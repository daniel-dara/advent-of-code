#include <stdio.h>

int main() {
	FILE* input = fopen("input.txt", "r");

	int answer = 0;
	char c;

	while (fscanf(input, "%c", &c) != EOF) {
		answer += (c == '(') - (c == ')');
	}

	printf("%d\n", answer);

	fclose(input);

	return 0;
}