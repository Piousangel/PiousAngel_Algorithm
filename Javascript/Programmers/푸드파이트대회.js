function solution(food) {
    let answer = "";
    let temp = "";

    for (let i = 1; i < food.length; i++) {
        for (let j = 0; j < parseInt(food[i] / 2); j++) {
            temp += String(i);
        }
    }

    answer = temp + "0" + temp.split("").reverse().join("");
    return answer;
}
