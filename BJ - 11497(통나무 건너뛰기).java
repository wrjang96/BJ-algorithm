	import java.util.*;
	import java.io.*;
	
	public class Main {
		static int testcase,N,answer;
		static int arr[];
		public static void main(String[] args) throws IOException{
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
			StringTokenizer st;
			testcase= Integer.parseInt(br.readLine());
			
			for(int i =0; i <testcase; i ++) {
				N = Integer.parseInt(br.readLine());
				arr = new int [N];
				st = new StringTokenizer(br.readLine());
				for(int j =0; j <N; j ++) {
					arr[j] = Integer.parseInt(st.nextToken());
				}
				Arrays.sort(arr);
				answer = Math.abs(arr[0] - arr[1]);
				answer = Math.max(answer, Math.abs(arr[N-1] - arr[N-2]));
				for(int tmp =0; tmp <N-2; tmp ++) {
					answer = Math.max(Math.abs(arr[tmp + 2] - arr[tmp]), answer);
				}
				bw.write(answer + "\n");
				
			}
		bw.flush();
		br.close();
		bw.close();
	}
	}