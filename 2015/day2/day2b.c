#include <stdio.h>

int min(int a, int b) {
	return a < b ? a : b;
}

int main() {
	FILE* input = fopen("input.txt", "r");

	int answer = 0;
	int l, w, h;

	while (fscanf(input, "%dx%dx%d", &l, &w, &h) != EOF) {
		answer += l*w*h + 2 * min(min(l+w, w+h), l+h);
	}

	printf("%d\n", answer);

	fclose(input);

	return 0;
}