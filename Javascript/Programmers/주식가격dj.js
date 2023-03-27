function solution(n) {
    let answer = [];

    for (let i = 0; i < n.length; i++) {
        let stack = n[i];
        let j = i + 1;
        let temp = 0;

        while (j < n.length + 1) {
            if (stack <= n[j]) {
                temp += 1;
                j += 1;
                continue;
            } else if (temp == 0 && stack > n[j]) {
                temp = 1;
                answer.push(temp);
                temp = 0;
                break;
            } else if (temp == 0 && j == n.length) {
                console.log(j);
                answer.push(temp);
                break;
            }
            answer.push(temp);
            temp = 0;
            break;
        }
    }
    return answer;
}
