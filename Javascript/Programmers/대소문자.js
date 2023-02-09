function solution(my_string) {
    let answer = "";
    for (ch of my_string) {
        if (ch.toLowerCase() === ch) answer += ch.toUpperCase();
        else answer += ch.toLowerCase();
    }
    return answer;
}
