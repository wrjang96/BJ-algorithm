#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;

//priority_queue <int, vector<int>,greater<int> > my_q;
int arr[10000];
priority_queue <int, vector<int>,less<int> > gap;


int main(int argc, char** argv) {
	int N,K;
	cin>>N;
	cin>>K;
	for(int i=0; i<N; i++){
	    cin>> arr[i];		
	} 
	sort(arr,arr+N);
	for(int i=0; i<N-1; i++){
		int gaptemp = arr[i+1]-arr[i];
		gap.push(gaptemp);
		//cout<<gaptemp;
	}
	K = K-1;
	while(K--){
		if(!gap.empty()){
		//cout<<gap.top();
		gap.pop();	
		}
	}
	long long int sum =0;
	while(!gap.empty()){
		sum += gap.top();
		gap.pop();
	}
	cout<<sum;
	return 0;
}
