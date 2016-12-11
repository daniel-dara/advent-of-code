#include <stdio.h>

int main() {
	FILE* input = fopen("input.txt", "r");

	int answer;
	int floor = 0;
	int position = 0;
	char c;

	while (fscanf(input, "%c", &c) != EOF) {
		floor += (c == '(') - (c == ')');

		position++;

		if (floor == -1) {
			answer = position;
			break;
		}
	}

	printf("%d\n", answer);

	fclose(input);

	return 0;
}