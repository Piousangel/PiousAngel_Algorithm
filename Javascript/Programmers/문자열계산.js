function solution(my_string) {
    let answer = 0;
    let cal = '+';
    const string_list = my_string.split(' ');
    for(str of string_list){
        if(str === ' ') continue;
        if(str === '+'){
            cal = '+';
        }
        else if(str === '-'){
            cal = '-';
        }
        else{
            if(cal === '+'){
                answer += Number(str);
            }
            else{
                answer -= Number(str);
            }
        }
    }
    
    return answer;
}