import java.lang.*;
import java.io.*;
import java.util.*;


public class Main {
	public static void main(String[] args) throws Exception { 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		int N = Integer.parseInt(br.readLine());
		int [] arr = new int[N];
		int [] numbers = new int[8001];
		int sum = 0;
		int max = -4001;
		int min = 4001;
		int maxcnt = 0 ;
		for(int i = 0; i <N; i ++) {
			arr[i] = Integer.parseInt(br.readLine());
			if (max < arr[i]) {
				max = arr[i];
			}
			if(arr[i] < min) {
				min = arr[i];
			}
			sum += arr[i];
			numbers[arr[i] + 4000] +=1;
			if(maxcnt < numbers[arr[i] + 4000]) {
				maxcnt = numbers[arr[i] + 4000];
			}
		}
		bw.write((int)Math.round((double)sum/N)+ "\n");
		Arrays.sort(arr);
		bw.write(arr[N/2]+ "\n");
		List<Integer> list =new ArrayList<>();
		for(int i = 0; i <8001; i++) {
			if(numbers[i] == maxcnt) {
				list.add(i - 4000);
			}
		}
		if(list.size() > 1) {
			Collections.sort(list);
			bw.write(list.get(1)+ "\n");
		}
		else {
			bw.write(list.get(0)+ "\n");
		}
		bw.write(max-min + "\n");
		bw.flush();
		bw.close();
		br.close();
 
    }
}
