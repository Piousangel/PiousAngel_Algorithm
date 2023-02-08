function solution(id_pw, db) {
    let answer = "";
    let flag = false;

    for (arr of db) {
        const id = arr[0];
        const pw = arr[1];

        if (id === id_pw[0]) {
            flag = true;
            if (pw === id_pw[1]) {
                answer = "login";
                break;
            } else {
                answer = "wrong pw";
                break;
            }
        }
    }
    if (!flag) return "fail";

    return answer;
}
