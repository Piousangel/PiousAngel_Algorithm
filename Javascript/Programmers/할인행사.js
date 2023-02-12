// 매일 하나 할인 행사
// 할인 제품 하루에 하나씩
// 할인 제품과 수량이 할인 하는 날 10일 연속 일치 -> 회원가입

function solution(want, number, discount) {
    let answer = 0;

    let sum = number.reduce((sum, value) => {
        return (sum += value);
    });

    for (let i = 0; i < discount.length; i++) {
        let tempArr = [];
        let flag = true;

        const map = new Map();

        for (let i = 0; i < want.length; i++) {
            map.set(want[i], number[i]);
        }

        for (let j = i; j < i + sum; j++) {
            if (i + sum - 1 < discount.length) {
                if (!map.has(discount[j])) {
                    break;
                } else {
                    map.set(discount[j], map.get(discount[j]) - 1);
                }
            }
        }

        for (let items of map) {
            if (items[1] !== 0) {
                flag = false;
                break;
            }
        }
        if (flag) {
            answer += 1;
        }
    }

    return answer;
}
