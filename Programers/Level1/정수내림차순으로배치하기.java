package Programers.Level1;
import java.util.*;

public class 정수내림차순으로배치하기 {
    
    public long solution(long n) {
        long answer = 0;
        String str = Long.toString(n);
        StringBuilder sb = new StringBuilder();
        Long[] box = new Long[str.length()];
        
        for(int i=0; i < str.length(); i++){
            box[i] = Long.parseLong(str.charAt(i)+"");
        }
        
        Arrays.sort(box, Collections.reverseOrder());
       
        for(long k : box){
            sb.append(k);
        }
        
        str = sb.toString();
        answer = Long.parseLong(str);
        return answer;
    }
}
