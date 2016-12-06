/*
 * Exact same as part1 but min instead.
 */

#define WORD_SIZE 8

#include <stdio.h>
#include <string.h>

char minCharOccurence(int alpha[26]) {
	char min = 'z';

	for (int i = 0; i < 26; i++) {
		if (alpha[i] < alpha[min - 'a']) {
			min = i + 'a';
		}
	}

	return min;
}

int main() {
	FILE* input = fopen("input.txt", "r");

	char word[WORD_SIZE];
	int common[WORD_SIZE][26];

	memset(common, 0, sizeof(common));

	while (fscanf(input, "%s", word) != EOF) {
		for (int i = 0; i < WORD_SIZE; i++) {
			common[i][word[i] - 'a']++;
		}
	}

	char final_word[WORD_SIZE + 1] = {0};

	for (int i = 0; i < WORD_SIZE; i++) {
		final_word[i] = minCharOccurence(common[i]); 
	}

	printf("%s\n", final_word);

	fclose(input);

	return 0;
}