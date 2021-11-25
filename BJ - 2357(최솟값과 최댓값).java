import java.io.*;
import java.util.*;

public class Main {
	static int N,M;
	static int list[];
	static int start,end;
	static long min_tree[];
	static long max_tree[];
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N=Integer.parseInt(st.nextToken());
		M=Integer.parseInt(st.nextToken());
		
		list = new int[N];
		
		for(int i=0; i<N; i++) {
			list[i]=Integer.parseInt(br.readLine());
		}
		
		int x = (int) Math.ceil(Math.log(N)/Math.log(2));
		int size = (int)Math.pow(2, x)*2;
		min_tree=new long[size];
		max_tree=new long[size];
		
		min_init(1,0,N-1);
		max_init(1,0,N-1);
		
		for(int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			
			start=Integer.parseInt(st.nextToken());
			end=Integer.parseInt(st.nextToken());
			
			System.out.print(min_num(1,0,N-1,start-1,end-1));
			System.out.print(" ");
			System.out.println(max_num(1,0,N-1,start-1,end-1));
		}
	}
	
	static long min_num(int node, int start, int end, int left, int right) {
		if(left > end || right < start) { 
			return Integer.MAX_VALUE;
		} 
		if(left <= start && right >= end) { 
			return min_tree[node];
		}
		int mid = (start+end)/2; 
		return Math.min(min_num(node*2,start,mid,left,right), min_num(node*2+1,mid+1,end,left,right)); 
	}
	static long max_num(int node, int start, int end, int left, int right) {
		if(left > end || right < start) { 
			return Integer.MIN_VALUE;
		} 
		if(left <= start && right >= end) { 
			return max_tree[node];
		}
		int mid = (start+end)/2; 
		return Math.max(max_num(node*2,start,mid,left,right), max_num(node*2+1,mid+1,end,left,right)); 
	}
	static long min_init(int node, int start, int end) {
		if(start==end)
			 return min_tree[node] = list[start];
		
		int mid=(start+end)/2;
		return min_tree[node]=Math.min(min_init(node*2,start,mid), min_init(node*2+1,mid+1,end)); 
	}
	static long max_init(int node, int start, int end) {
		if(start==end)
			 return max_tree[node] = list[start];
		
		int mid=(start+end)/2;
		return max_tree[node]=Math.max(max_init(node*2,start,mid), max_init(node*2+1,mid+1,end)); 
	}
}