function solution(s1, s2) {
    let answer = 0;
    for (ch of s1) {
        if (s2.includes(ch)) answer += 1;
    }
    return answer;
}
