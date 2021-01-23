#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;
priority_queue<int, vector<int>, greater<int> > pq;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	int N;
	cin>>N;
	if(N==1){
		cout<<0;
		return 0;
	}
	while(N--){
		int temp;
		cin>>temp;
		pq.push(temp);
	}
	int result=0;
	while(1){
		int first = pq.top();
		pq.pop();
		int sec = pq.top();
		pq.pop();
		if(pq.empty()==true) {
			result += first;
		result += sec;
		break;
		}	
		
		result += first;
		result += sec;
		pq.push(first+sec);
	}
	cout<<result;
}
