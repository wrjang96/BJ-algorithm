#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
int N;
priority_queue<pair<int,int>,vector<pair<int,int> >,greater<pair<int,int> > > pq;
int main(){	
	cin>>N;
	for(int i =0; i<N; i++){
		int start, end;
		cin>>start>>end;
		pq.push({end, start});
	}
	int cnt =0;
	while(!pq.empty()){
		int end = pq.top().first;
		int start = pq.top().second;
		pq.pop(); cnt++;
		if(pq.empty()) break;
		while(end > pq.top().second){
			pq.pop();
			if(pq.empty()) break;
		}
	}
	cout<<cnt<<'\n';
	
}

