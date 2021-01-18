#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
priority_queue<int,vector<int>,less<int> >my_q;// 1 이상인 수, 큰것부터 나오게 
priority_queue<int,vector<int>,greater<int> >my_q2;// 0이하인 수 , 작은 것 부터 나오게  

int main() {
	long long int sum =0;//sum의 숫자 가 크니 자료형도 크게  
	int N; cin>>N;
	while(N--){
	int input;
	cin>>input;
	if(input>0){
	my_q.push(input);	
	}
	else{
	my_q2.push(input);		
	}
	}
	while(!my_q.empty()){
		int temp = my_q.top(); my_q.pop();
		if(my_q.empty()){
				sum +=temp;// 하나만 있으면 더하고 
				break;
		}
		int temp2= my_q.top();
		my_q.pop();
		if(temp2 ==1){
		sum +=(temp+temp2);	// 다만 곱할때 1일 경우, 더하는 것이 더 낫다. 2+1 =3, 2*1 =2
		}
		else{
			sum +=(temp*temp2);// 두개 다 있으면 더한다. 
		}
	}
	// 음수 부분도 위와 같다. 
	while(!my_q2.empty()){
		int tmp = my_q2.top();my_q2.pop(); 
		if(my_q2.empty()){
				sum +=tmp;
				break;
		}
		int tmp2= my_q2.top();
		my_q2.pop();
		sum +=(tmp*tmp2);
	}
	cout<<sum<<'\n';
	return 0;
}
