// 무조건 5번 고정시키기

function dfs(arr, minerals, idx, total) {
    let temp = 0;
    for (let i = 0; i < arr.length; i++) {
        temp += arr[i];
    }

    if (temp === 0 || idx === minerals.length) {
        console.log(total);
        answer = Math.min(answer, total);
        return;
    }

    if (arr[0] !== 0) {
        const nowArr = [arr[0] - 1, arr[1], arr[2]];
        dfs(nowArr, minerals, idx + 1, total + 1);
    }
    if (arr[1] !== 0) {
        const nowArr = [arr[0], arr[1] - 1, arr[2]];
        minerals[idx] === "diamond"
            ? dfs(nowArr, minerals, idx + 1, total + 5)
            : dfs(nowArr, minerals, idx + 1, total + 1);
    }
    if (arr[2] !== 0) {
        const nowArr = [arr[0], arr[1], arr[2] - 1];
        if (minerals[idx] === "diamond") {
            dfs(nowArr, minerals, idx + 1, total + 25);
        } else if (minerals[idx] === "iron") {
            dfs(nowArr, minerals, idx + 1, total + 5);
        } else {
            dfs(nowArr, minerals, idx + 1, total + 1);
        }
    }
}

let answer = 100000;
function solution(picks, minerals) {
    const newArr = picks.map((value) => value * 5);
    dfs(newArr, minerals, 0, 0);
    return answer;
}
