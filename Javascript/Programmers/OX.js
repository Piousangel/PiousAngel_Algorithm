function solution(quiz) {
    let answer = [];

    for (q of quiz) {
        const sol = q.split(" = ");
        const leftQ = sol[0].split(" ");
        let temp = 0;
        if (leftQ[1] === "+") {
            temp = Number(leftQ[0]) + Number(leftQ[2]);
        } else temp = Number(leftQ[0]) - Number(leftQ[2]);

        if (Number(sol[1]) === temp) answer.push("O");
        else answer.push("X");
    }

    return answer;
}
