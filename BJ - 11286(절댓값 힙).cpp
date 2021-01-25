#include <iostream>
#include <queue>
using namespace std;

int main() {
	priority_queue<int> my_q;
	priority_queue<int, vector<int>, greater<int> > my_pq;
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int N;
	cin >> N;
	int command;
	while (N--) {
		cin >> command;
		if (command == 0) {
			if (my_q.empty() && my_pq.empty()) {
				cout << 0 << '\n';
			}
			else if (!my_q.empty() && my_pq.empty()) {
				cout << my_q.top() << '\n';
				my_q.pop();
			}
			else if (my_q.empty() && !my_pq.empty()) {
				cout << my_pq.top() << '\n';
				my_pq.pop();
			}
			else {
				if (my_q.top() * -1 > my_pq.top()) {
					cout << my_pq.top() << '\n';
					my_pq.pop();
				}
				else if (my_q.top() * -1 == my_pq.top()) {
					cout << my_q.top() << '\n';
					my_q.pop();
				}
				else {
					cout << my_q.top() << '\n';
					my_q.pop();
				}
			}
		}
		else if (command > 0) {
			my_pq.push(command);
		}
		else {
			my_q.push(command);
		}
	}
	return 0;
}
