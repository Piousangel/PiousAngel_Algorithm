let answer = null;
function solution(elements) {
    answer = new Set(elements);

    for (let i = 2; i <= elements.length; i++) {
        conbination(elements, i);
    }
    return answer.size;
}

function conbination(arr, num) {
    for (let i = 0; i < arr.length; i++) {
        let sum = 0;
        for (let j = 0; j < num; j++) {
            sum += arr[(i + j) % arr.length];
        }
        answer.add(sum);
    }
}
