#include <iostream>
#include <queue>
#include <algorithm>
using namespace std; 
queue<pair<long long int, long long int> > my_q;
int main(){
	int A,B;
	cin>>A>>B;
	my_q.push({A,1});
	long long int result =-1;
	while(!my_q.empty()){
		long long int x = my_q.front().first;
		long long int cnt = my_q.front().second;
		my_q.pop();
		if(x==B){
			result = cnt;
			break;
		}
		long long int x2 = x*2;
		long long int x101 =x*10+1;
		if(x2<=B){
		    my_q.push({x2,cnt+1});		
		} 
		if(x101<=B){
			my_q.push({x101,cnt+1});
		}
	}
	cout<<result;
}

/*
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std; 

queue<pair<long long int,long long int> > my_q;
int main(int argc, char** argv) {
	int A,B;
	cin>>A>>B;
	my_q.push({A,1});
	
	long long int result = -1;
	while(!my_q.empty()){
		long long int x = my_q.front().first;
		long long int cnt = my_q.front().second;
		my_q.pop();
		if(x==B){
			result = cnt;
			break;
		}
		long long int x2 = x*2;
		long long int x101 = x*10 + 1;
		if(x2<=B){
			my_q.push({x2,cnt+1});
		}
		if(x101<=B){
			my_q.push({x101,cnt+1});
		}
	}
	cout<<result;
	return 0;
}
*/
