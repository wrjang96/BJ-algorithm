	import java.util.*;
	import java.io.*;
	
	public class Main {
		static int x1,x2,y1,y2,cx,cy,r,ans;
		static double t1,t2;
		public static void main(String[] args) throws IOException{
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
			int testcase = Integer.parseInt(br.readLine());
			for(int i =0; i <testcase; i ++) {
				StringTokenizer st;
				st = new StringTokenizer(br.readLine());
				x1 = Integer.parseInt(st.nextToken());
				y1 = Integer.parseInt(st.nextToken());
				x2 = Integer.parseInt(st.nextToken());
				y2 = Integer.parseInt(st.nextToken());
				ans = 0;
				int N = Integer.parseInt(br.readLine());
				for (int j =0; j <N; j ++) {
				st = new StringTokenizer(br.readLine());
				cx = Integer.parseInt(st.nextToken());
				cy = Integer.parseInt(st.nextToken());
				r = Integer.parseInt(st.nextToken());
				t1 = Math.sqrt(Math.pow((double)x1-(double)cx,2) + Math.pow((double)y1-(double)cy,2)) - r;
				t2 = Math.sqrt(Math.pow((double)x2-(double)cx,2) + Math.pow((double)y2-(double)cy,2)) - r;
				if (t1 * t2 < 0) {
					ans +=1;
				}
				}
				bw.write(ans + "\n");
			}
			bw.flush();
			br.close();
			bw.close();
		}
	}