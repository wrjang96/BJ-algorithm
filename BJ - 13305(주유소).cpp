#include <iostream>
#include <algorithm>

using namespace std;

long long d[100000];
long long dist[100000];
long long price[100000];
 
	
int main(int argc, char** argv) {
	int N;
	cin>>N;
	for(int i =0; i<N-1; i++){
		cin>>dist[i];
	}
	for(int i =0; i<N; i++){
		cin>>price[i];
	}
	long long int minp = price[0];
	d[0] = minp*dist[0];
	long long int sum = d[0];
	
	for(int i =1; i<N-1; i++){
		minp = min(minp,price[i]);
		d[i] = minp*dist[i];
		sum +=d[i];
	}
	cout<<sum<<'\n';
	/*
	for(int i =0; i<N-1; i++){
		cout<<d[i]<<'\n';
	}
	*/
	return 0;
}
