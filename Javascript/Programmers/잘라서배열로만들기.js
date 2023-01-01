function solution(my_str, n) {
    let answer = [];
    let cnt = 0;
    let temp = "";
    for(let i = 0 ; i < my_str.length ; i ++) {
        cnt ++;
        temp += my_str[i];
        if (cnt % n === 0) {
            answer.push(temp)
            temp = "";
        } 
    }
    if (temp !== ""){
        answer.push(temp);
    }
    
    return answer;
}
