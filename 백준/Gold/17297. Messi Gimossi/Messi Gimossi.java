import java.util.*;
import java.io.*;

public class Main {
	static int N = 42; //문제에서 주어진 M의 범위((2**30)-1)를 초과하지 않는 가장 큰 수
	static int[] resultLength = new int[N]; 
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int M = Integer.parseInt(br.readLine());
		resultLength[1] = 5;
		resultLength[2] = 13;
		for (int i = 3; i < N; i++) {
			resultLength[i] = resultLength[i-1] + 1 + resultLength[i-2];
		}
		
		System.out.println(recursion(M,N));
	}
	
	public static String recursion(int X, int depth) {
    	
		if(depth <= 2) {
			return baseCondition(X);
		}
		
        // depth-1번째에서 X를 찾는것과 동일
		if(X <= resultLength[depth-1]) return recursion(X,depth-1);
        
        // 띄어쓰기 자리에 걸리면 
		if(X == resultLength[depth-1] +1) return "Messi Messi Gimossi";
        
        // X가 depth-2번째 문자열에 포함 할 때 
		if(resultLength[depth-1]+1 < X && X < resultLength[depth]) return recursion(X-(resultLength[depth-1]+1),depth-2);
        
        // X가 depth번째 문자열의 길이와 동일 할 때
		if(X == resultLength[depth]) return "i";
		
		return "";
	}
	
	public static String baseCondition(int X) {
		if(X == 1) return "M";
		if(X == 2) return "e";
		if(X == 3 || X == 4 || X == 11 || X == 12) return "s";
		if(X == 5 || X == 8 || X == 13) return "i";
		if(X == 6) return "Messi Messi Gimossi";
		if(X == 7) return "G";
		if(X == 9) return "m";
		if(X == 10) return "o";
		return "";
	}
	
}	