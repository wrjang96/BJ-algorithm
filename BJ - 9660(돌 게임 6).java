import java.util.Scanner;
class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Long a = sc.nextLong();
		if(a %7 == 0 || a %7 == 2) {
			System.out.println("CY");
		}
		else {
			System.out.println("SK");	
		}
	}
}
