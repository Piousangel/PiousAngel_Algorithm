function solution(polynomial) {
    let answer = "";
    let x = 0;
    let num = 0;
    const cal_list = polynomial.split(" + ");

    for (temp of cal_list) {
        if (temp.includes("x")) {
            if (temp.length === 1) x += 1;
            else x += Number(temp.slice(0, temp.length - 1));
        } else {
            num += Number(temp);
        }
    }

    if (x === 0) {
        answer = String(num);
    } else {
        if (num === 0) {
            if (x === 1) {
                answer = "x";
            } else answer = String(x) + "x";
        } else {
            if (x === 1) {
                answer = "x + " + String(num);
            } else answer = String(x) + "x + " + String(num);
        }
    }

    return answer;
}
