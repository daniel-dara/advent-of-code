/*
 * Keep alphabet counts for each column of the word and at the end, grab the max char from each column's alphabet.
 */

#define WORD_SIZE 8

#include <stdio.h>
#include <string.h>

char maxCharOccurence(int alpha[26]) {
	char max = 'a';

	for (int i = 0; i < 26; i++) {
		if (alpha[i] > alpha[max - 'a']) {
			max = i + 'a';
		}
	}

	return max;
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
		final_word[i] = maxCharOccurence(common[i]); 
	}

	printf("%s\n", final_word);

	fclose(input);

	return 0;
}