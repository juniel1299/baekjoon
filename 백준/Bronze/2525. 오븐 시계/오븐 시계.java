import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
        
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        
        int d = (60*a) + b + c;
         a = d/60;
         b = d%60;
        
        if(a>23){
            a=a-24;
        } System.out.println(a+" "+b);
    }
}

        