	import java.util.*;
	import java.io.*;
	
	public class Main {
		static int N,Q,start,end,ans;
		static int arr[],sum_arr[];
		public static void main(String[] args) throws IOException{
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
			StringTokenizer st;
			N= Integer.parseInt(br.readLine());
			arr = new int [N];
			sum_arr = new int [N];
			st = new StringTokenizer(br.readLine());
			for(int i =0; i <N; i ++) {
				arr[i] = Integer.parseInt(st.nextToken());
			}
			for(int i =1; i <N; i ++) {
				if(arr[i] < arr[i-1]) {
					sum_arr[i] +=1;
				}
				sum_arr[i] += sum_arr[i-1]; 
			}
			Q= Integer.parseInt(br.readLine());
			for(int i =0; i <Q; i ++) {
				st = new StringTokenizer(br.readLine());
				start = Integer.parseInt(st.nextToken());
				end = Integer.parseInt(st.nextToken());
				bw.write(sum_arr[end-1] - sum_arr[start-1] + "\n");
			}
		bw.flush();
		br.close();
		bw.close();
	}
	}