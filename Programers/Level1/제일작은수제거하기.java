package Programers.Level1;
import java.util.*;

public class 제일작은수제거하기 {
    public int[] solution(int[] arr) {
        
        if(arr.length == 1) return new int[] {-1};
        ArrayList<Integer> list = new ArrayList<>();
        int[] answer = new int[arr.length-1];
        
        int min = 10001;
        for(int tmp : arr){
            if(min > tmp) min = tmp;
            list.add(tmp);
        }

        list.remove(Integer.valueOf(min));
        for(int i=0; i < list.size(); i++){
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}
