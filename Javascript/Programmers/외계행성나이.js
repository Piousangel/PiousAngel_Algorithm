function solution(age) {
    let answer = "";
    const alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"];
    const tempArr = [...String(age)];
    for (num of tempArr) {
        answer += alphabet[Number(num)];
    }
    return answer;
}
