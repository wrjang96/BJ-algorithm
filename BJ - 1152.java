import java.util.Scanner;

public class BJ1152 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String a = sc.nextLine();
		String [] arr = a.split(" "); 

		// + 입력 안들어올 경우 에러처리 안함
		// 처리 안하면 ArrayIndexOutOfBounds 에러 뜸 
		if(arr.length > 0) {
			if(arr[0].equals("")) {
				System.out.println((arr.length - 1));
			}
			else {
				System.out.println((arr.length));
			}
		}
		else {
			System.out.println("0");	
		}
	}
}
