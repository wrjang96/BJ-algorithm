/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Main
{
	public static void main(String[] args) {
	    Scanner in = new Scanner(System.in);
		int N = in.nextInt();
		int[] arr = new int[N];
		for(int i=0 ; i<N ; i++){
			arr[i] = in.nextInt();
		} 
		Arrays.sort(arr);
		System.out.print(arr[0] + " " + arr[N - 1]);
		in.close();
	}
}