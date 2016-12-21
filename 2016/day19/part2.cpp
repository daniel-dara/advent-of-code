// The key to this solution is to use a double-linked list so that insertion/removal is O(1).

#include <iostream>
#include <list>

#define SIZE 3014387

int main() {
	int middle = 1; // elf whose turn it is
	std::list<int> left; // elves to the left of middle
	std::list<int> right; // elves to the right of middle

	// Initialize left and right.
	int i;
	for (i = 2; i <= SIZE / 2 + 1; i++) {
		left.push_front(i);
	}

	for (; i <= SIZE; i++) {
		right.push_front(i);
	}

	while (right.size() > 0) {
		// Remove front elf since either left = right or left + 1 = right, either way, he goes!
		left.pop_front();

		// Now the middle elf gets moved to the right
		right.push_front(middle);

		// We move elves even if the lists are equal since we still have to pop one from the left for the middle.
		while (left.size() <= right.size()) {
			// The last elf|elves on the right circles all the way back to start on the left again.
			left.push_front(*--right.end()); right.pop_back();
		}

		// The last elf on the left becomes the new middle.
		middle = *--left.end(); left.pop_back();
	}

	std::cout << middle << std::endl;

	return 0;
}