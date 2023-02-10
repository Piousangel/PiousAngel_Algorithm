// 문자열 a로 시작
// 3번 규칙을 0번이상 반복
// 2개 행동 중 하나 선택
// x개 만큼 문자열 양옆에 b 추가
// aba -> a가 2개니까 bbababb
// 혹은 맨앞 혹은 맨 뒤에 a를 추가
// 해당 문자열이 나올 수 있는지 불가능한지
// 완탐 돌리면 될려나

function dfs(str, target) {
    if (str.length === target.length) {
        if (str === target) {
            arr.push(str);
            return;
        }
    }
    if (str.length > target.length) {
        return;
    }

    let aCount = str.split("a").length - 1;
    let tempStr = "";
    for (let i = 0; i < aCount; i++) {
        tempStr += "b";
    }

    dfs(str + "a", target);
    dfs("a" + str, target);
    dfs(tempStr + str + tempStr, target);
}

let answer = [];
let arr = [];
function solution(a) {
    let startStr = "a";
    for (let i = 0; i < a.length; i++) {
        arr = [];
        dfs(startStr, a[i]);
        if (arr.includes(a[i])) {
            answer.push(true);
        } else {
            answer.push(false);
        }
    }

    return answer;
}
