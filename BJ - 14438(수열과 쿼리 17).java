import java.io.*;
import java.util.*;

public class Main {
	static int N,M;
	static long list[];
	static int  flag,i;
	static long sec;
	static long min_tree[];
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		list = new long[N];
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<N; i++) {
			list[i]= Long.parseLong(st.nextToken());
		}
		
		
		int x = (int) Math.ceil(Math.log(N)/Math.log(2));
		int size = (int)Math.pow(2, x)*2;
		min_tree=new long[size];
		init(1,0,N-1);
		st = new StringTokenizer(br.readLine());
		M = Integer.parseInt(st.nextToken());
		for(int j=0; j<M; j++) {
			st = new StringTokenizer(br.readLine());
			flag = Integer.parseInt(st.nextToken());
			i = Integer.parseInt(st.nextToken());
			sec = Long.parseLong(st.nextToken());
			if(flag == 1) {
				list[(int)i-1] = sec;
				update(1, N, 1, (int)i, sec);
			}
			else {
				System.out.println(min_num(1,0,N-1,i -1,(int)(sec -1)));
			}
			
			
		}
	}
	
	static long min_num(int node, int start, int end, int left, int right) {
		if(left > end || right < start) { 
			return 1000000000;
		} 
		if(left <= start && right >= end) { 
			return min_tree[node];
		}
		int mid = (start+end)/2; 
		return Math.min(min_num(node*2,start,mid,left,right),min_num(node*2+1,mid+1,end,left,right)); 
	}
	
	static long init(int node, int start, int end) {
		if(start==end)
			 return min_tree[node] = list[start];
		
		int mid=(start+end)/2;
		return min_tree[node] = Math.min(init(node*2,start,mid),init(node*2+1,mid+1,end)); 
	}
	
	static long update(int start, int end, int node, int idx, long dif) {
		if (idx < start || idx > end) {
			return min_tree[node];
		}
		min_tree[node] = Math.min(min_tree[node], dif);
		if (start == end) {
			return min_tree[node] = dif;
		}

		int mid = (start + end) / 2;
		return min_tree[node] = Math.min(update(start, mid, node * 2, idx, dif),update(mid + 1, end, node * 2 + 1, idx, dif));
	}
}