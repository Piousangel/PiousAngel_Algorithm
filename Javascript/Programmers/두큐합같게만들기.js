// 하나의 큐에서 빼서 다른 큐에 집어넣기
// 이것이 1번이라 간주
// fifo로 진행
// re

let answer = 1000000;

function dfs(q1, q2, idx) {
    if (q1.length === 0 || q2.length === 0) {
        return;
    }

    const q1Total = q1.reduce((a, b) => {
        return a + b;
    });

    const q2Total = q2.reduce((a, b) => {
        return a + b;
    });

    if (q1Total === q2Total) {
        console.log(q1, q2);
        answer = Math.min(answer, idx);
        return;
    }

    const newQ1 = [...q1];
    const newQ2 = [...q2];
    const newQ3 = [...q1];
    const newQ4 = [...q2];

    newQ1.unshift(newQ2.pop());
    newQ4.unshift(newQ3.pop());

    dfs(newQ1, newQ2, idx + 1);
    dfs(newQ4, newQ3, idx + 1);
}

function solution(queue1, queue2) {
    dfs(queue1, queue2, 0);
    if (answer === 1000000) return -1;
    return answer;
}
