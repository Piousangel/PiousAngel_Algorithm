package Programers;
import java.io.IOException;

public class 정수제곱근판별 {
    
    public long solution(long n) {
        long answer = 0;
        long a = (long)Math.sqrt(n);
        
        if(a*a == n) answer = (a+1) * (a+1);
        else answer = -1;
        
        return answer;
    }

}
