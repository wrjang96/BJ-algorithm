	import java.util.*;
	import java.io.*;
	
	public class Main {
		static int N,M;
		static int[] arr, permutation;
		static boolean [] visited;
		static LinkedHashSet<String> ans;
		public static void main(String[] args) throws IOException{
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
			StringTokenizer st;
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			arr = new int[N];
			permutation = new int[M];
			visited = new boolean[N];
			ans = new LinkedHashSet<>();
			st = new StringTokenizer(br.readLine());
			for(int i =0; i <N; i ++) {
				arr[i] = Integer.parseInt(st.nextToken());
			}
			Arrays.sort(arr);
			permutations(0);
			ans.forEach(System.out::println);
				
			}
		static void permutations(int cnt) {
			if (cnt == M) {
	            StringBuilder sb = new StringBuilder();
	            for (int p : permutation)
	                sb.append(p).append(' ');
	            ans.add(sb.toString());
	            return;
	        }

	        for (int i = 0; i < N; i++) {
	            if (visited[i])
	                continue;
	            visited[i] = true;
	            permutation[cnt] = arr[i];
	            permutations(cnt + 1);
	            visited[i] = false;
	        }
		}
	}
	