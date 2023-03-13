// > 오른쪽, < 왼쪽
// 아무 블록에서 출발 가능
// 도로를 빠져나오는 것이 목표
// 도로를 빠져나올 수 있는 출발점의 개수 구하기
//

function solution(p) {
    const arr = [...p];
    let answer = 0;
    // let target = arr.length;

    for (let i = 0; i < arr.length; i++) {
        let flag = false;
        let curPos = i;
        let idx = arr.length;
        while (idx > 0) {
            if (arr[curPos] === "<") {
                curPos -= 1;
            } else {
                curPos += 1;
            }
            if (curPos < 0 || curPos > arr.length - 1) {
                flag = true;
                break;
            }
            idx -= 1;
        }
        if (flag) {
            answer += 1;
            arr.splice(i, 1);
            i -= 1;
        }
    }

    return answer;
}
