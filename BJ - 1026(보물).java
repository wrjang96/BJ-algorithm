import java.lang.*;
import java.io.*;
import java.util.*;
import java.util.Arrays;
import java.util.Scanner;

class Main {
	public static void main(String[] args) throws Exception { 
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] A = new int[n];
        int[] B = new int[n];
 
        for (int i = 0; i < n; i++) {
            A[i] = sc.nextInt();
        }
        for (int i = 0; i < n; i++) {
            B[i] = sc.nextInt();
 
        }
        Arrays.sort(A);
        Arrays.sort(B);
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += A[i] * B[n - 1 - i];
        }
        System.out.println(sum);
 
    }
}
