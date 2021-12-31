import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		String [] arr = new String[N];
		for (int i = 0; i < N; i++) {
			arr[i] = br.readLine();
		}

		Arrays.sort(arr, new Comparator<String>() {
			@Override
			public int compare(String first, String second) {
				if(first.length()< second.length()) {
					return -1;
				}
				else if(first.length()>second.length()) {
					return 1;
				}
				else {
					if(add(first) == add(second)) {
						return first.compareTo(second);
					}
					else {
						return Integer.compare(add(first),add(second));
					}
				}
			}
		});
		for (String i : arr) {
			System.out.println(i);
		}

	}
	public static int add(String s) {
		int sum = 0;
		for(int i =0; i <s.length(); i ++) {
			if (s.charAt(i)>='0' &&s.charAt(i)<='9') {
				sum +=s.charAt(i)-'0';
			}
		}
		return sum;
	}

}

class sort implements Comparable<sort> {
	String str;
	
	@Override
	public int compareTo(sort o) {
		if (str.length() < o.str.length()) {
			return 1;
		} else if (str.length() > o.str.length()) {
			return -1;
		} else {
			int sum1 = 0;
			int sum2 = 0;

			for (int i = 0; i < str.length(); i++) {
				if ((byte) str.charAt(i) >= (byte) '0' && (byte) str.charAt(i) <= (byte) '9') {
					sum1 += str.charAt(i)-'0';
				}
				if ((byte) o.str.charAt(i) >= (byte) '0' && (byte) o.str.charAt(i) <= (byte) '9') {
					sum2 += o.str.charAt(i)-'0';
				}
			}
			
			if (sum1 < sum2) {
				return 1;
			} else if (sum1 > sum2) {
				return -1;
			} else {
				for (int i = 0; i < str.length(); i++) {
					if (str.charAt(i) < o.str.charAt(i)) {
						return 1;
					} else if (str.charAt(i) > o.str.charAt(i)) {
						return -1;
					}
				}
			}

		}
		return 0;
	}

}