// The key to this solution is to use a double-linked list so that insertion/removal is O(1).

#include <iostream>
#include <list>

#define SIZE 3014387

int main() {
	std::list<int> elves;

	for (int i = 1; i <= SIZE; i++) {
		elves.push_back(i);
	}

	std::list<int>::iterator elf = elves.begin();

	while (elves.size() > 1) {
		// Skip an elf
		elf++;

		// Wrap around
		if (elf == elves.end()) {
			elf = elves.begin();
		}

		// Remove an elf
		elf = elves.erase(elf);

		// Wrap around
		if (elf == elves.end()) {
			elf = elves.begin();
		}
	}

	// last man standing
	std::cout << *elves.begin() << std::endl;

	return 0;
}