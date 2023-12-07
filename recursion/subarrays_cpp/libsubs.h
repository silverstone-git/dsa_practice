# include <vector>
# include <iostream>

void display_recursively(std::vector<int> arr) {
	if(arr.size() < 1) return;
	std::cout << arr[0] << std::endl;
	display_recursively(std::vector<int>(arr.begin() + 1, arr.end()));
}

void showsubs(std::vector<int> arr, std::vector<int> temp, int pos) {
	// recursively goes through every possible subarray of an array
	// make a temp array, take 0th into temp, and recurse with next position
	if(pos == arr.size()) {
		display_recursively(temp);
		return;
	}
	showsubs(arr, temp, pos + 1);
}
