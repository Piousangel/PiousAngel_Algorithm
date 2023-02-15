// 잘린 조각들의 크기와 올려진 토핑 개수 상관없이
// 각 조각에 동일한 가짓수의 토핑이 올라가면 공평하게 나눠진것이라고 생각
// 토핑 - 1,2,3,4 총 4가지
// 배열 2개로 나눠 동일한 가지수 몇개인지 구하기
// re

function chkTopping(mid, arr, set) {
    for (num of arr) {
        set.add(num);
    }
    return set.size;
}
function solution(topping) {
    let answer = 0;

    let left = 0;
    let right = topping.length - 1;
    let mid = Math.floor((left + right) / 2);

    while (left <= right) {
        const leftSet = new Set();
        const rightSet = new Set();

        const leftArr = topping.slice(0, mid + 1);
        const rightArr = topping.slice(mid + 1, topping.length);

        const leftCnt = chkTopping(mid, leftArr, leftSet);
        const rightCnt = chkTopping(mid, rightArr, rightSet);

        if (leftCnt === rightCnt) {
            answer += 1;
        }
        if (leftCnt > rightCnt) {
            right = mid - 1;
            mid = Math.floor((left + right) / 2);
        } else {
            left = mid + 1;
            mid = Math.floor((left + right) / 2);
        }

        break;
    }

    return answer;
}
