// 3 2 1 0 1 2 3
// RT CF JM AN

function solution(survey, choices) {
    let answer = "";
    const arr = ["R", "T", "C", "F", "J", "M", "A", "N"];
    const map = new Map();

    for (let i = 0; i < 8; i++) {
        map.set(arr[i], 0);
    }

    for (let i = 0; i < choices.length; i++) {
        let score = Math.abs(4 - choices[i]);

        let alphabet = "";
        if (choices[i] < 4) {
            alphabet = survey[i][0];
        } else if (choices[i] > 4) {
            alphabet = survey[i][1];
        }
        if (alphabet !== "") {
            map.set(alphabet, map.get(alphabet) + score);
        }
    }

    if (map.get("R") >= map.get("T")) {
        answer += "R";
    } else {
        answer += "T";
    }
    if (map.get("C") >= map.get("F")) {
        answer += "C";
    } else {
        answer += "F";
    }
    if (map.get("J") >= map.get("M")) {
        answer += "J";
    } else {
        answer += "M";
    }
    if (map.get("A") >= map.get("N")) {
        answer += "A";
    } else {
        answer += "N";
    }

    return answer;
}
