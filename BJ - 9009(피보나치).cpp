#include <iostream>
#include <queue>
#include <vector>
using namespace std;

priority_queue<int,vector<int>,greater<int> > my_q;// 작은 것 부터 
long long int fibo[50] = {0,};
int count [50];


int main(int argc, char** argv) {
	fibo[0]=0;
	fibo[1] =1;
	//46인가 까지 들어가짐 
	for(int i = 2; i<50; i++){
		fibo[i] = fibo[i-1]+fibo[i-2];
	}	
	int N;
	cin>>N;
	while(N--){
		long long int temp;
		cin>>temp;
		while(temp){
			for(int i =49; i>=1; i--){
				if(fibo[i]<=temp){
					temp -=fibo[i];
					my_q.push(fibo[i]);;
				}
			}
		}
		while(!my_q.empty()){
			cout<<my_q.top()<<' ';
			my_q.pop();
		}
		cout<<'\n';		
	}
	return 0;
}
