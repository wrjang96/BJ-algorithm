import java.io.*;
import java.util.*;

public class Main {
	static int N,M,K;
	static long list[];
	static int flag, start;
	static long end;
	static long sum_tree[];
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		list = new long[N];
		
		for(int i=0; i<N; i++) {
			list[i]= Long.parseLong(br.readLine());
		}
		
		int x = (int) Math.ceil(Math.log(N)/Math.log(2));
		int size = (int)Math.pow(2, x)*2;
		sum_tree=new long[size];
		
		sum_init(1,0,N-1);
		
		for(int i=0; i<M+K; i++) {
			st = new StringTokenizer(br.readLine());
			flag =Integer.parseInt(st.nextToken());
			start=Integer.parseInt(st.nextToken());
			end=Long.parseLong(st.nextToken());
			if(flag == 2) {
				System.out.println(sum_num(1,0,N-1,start-1,(int)end-1));
			}
			else {
				long dif = end - list[start-1];
				list[start-1] = end;
				update(1, N, 1, start, dif);
			}
		}
	}
	
	static long sum_num(int node, int start, int end, int left, int right) {
		if(left > end || right < start) { 
			return 0;
		} 
		if(left <= start && right >= end) { 
			return sum_tree[node];
		}
		int mid = (start+end)/2; 
		return sum_num(node*2,start,mid,left,right) + sum_num(node*2+1,mid+1,end,left,right); 
	}
	
	static long sum_init(int node, int start, int end) {
		if(start==end)
			 return sum_tree[node] = list[start];
		
		int mid=(start+end)/2;
		return sum_tree[node] = sum_init(node*2,start,mid) + sum_init(node*2+1,mid+1,end); 
	}
	
	static void update(int start, int end, int node, int idx, long dif) {
		if (idx < start || idx > end) {
			return;
		}
		sum_tree[node] += dif;
		if (start == end) {
			return;
		}

		int mid = (start + end) / 2;
		update(start, mid, node * 2, idx, dif);
		update(mid + 1, end, node * 2 + 1, idx, dif);
	}
}