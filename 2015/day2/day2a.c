#include <stdio.h>

int min(int a, int b) {
	return a < b ? a : b;
}

int main() {
	FILE* input = fopen("input.txt", "r");

	int answer = 0;
	int l, w, h;

	while (fscanf(input, "%dx%dx%d", &l, &w, &h) != EOF) {
		answer += 2*l*w + 2*w*h + 2*h*l + min(min(l*w, w*h), l*h);
	}

	printf("%d\n", answer);

	fclose(input);

	return 0;
}