# include <iostream>
using namespace std;
int main() {
	int len;
	cout << "enter length : ";
	cin >> len;
	int[] arr[] = new int[len];
	arr[] = {1, 2, 3};
	for(int i = 0; i < len; i ++) {
		cout << arr[i];
	}
}
