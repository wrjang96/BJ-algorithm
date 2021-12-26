import java.io.*;
import java.util.*;

public class Main {
	static int N,Q;
	static long list[];
	static long X,Y,A,B;
	static long sum_tree[];
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		Q = Integer.parseInt(st.nextToken());
		
		list = new long[N];
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<N; i++) {
			list[i]= Integer.parseInt(st.nextToken());
		}
		
		int x = (int) Math.ceil(Math.log(N)/Math.log(2));
		int size = (int)Math.pow(2, x)*2;
		sum_tree=new long[size];
		
		sum_init(1,0,N-1);
		
		for(int i=0; i<Q; i++) {
			st = new StringTokenizer(br.readLine());
			X = Long.parseLong(st.nextToken());
			Y = Long.parseLong(st.nextToken());
			A = Long.parseLong(st.nextToken());
			B = Long.parseLong(st.nextToken());
			System.out.println(sum_num(1,0,N-1,Math.min((int)X-1, (int)Y-1),Math.max((int)X-1, (int)Y-1)));
			long dif = B - list[(int)A-1];
			list[(int)A-1] = B;
			update(1, N, 1, (int)A, dif);
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