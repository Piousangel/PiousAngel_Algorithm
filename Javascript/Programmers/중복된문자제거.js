function solution(my_string) {
    let answer = "";
    let arr = [];

    for (ch of my_string) {
        if (arr.includes(ch)) continue;
        else {
            arr.push(ch);
            answer += ch;
        }
    }
    return answer;
}
