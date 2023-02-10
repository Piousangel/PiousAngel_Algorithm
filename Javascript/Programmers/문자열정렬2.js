function solution(my_string) {
    let tempArr = [...my_string];
    let arr = [];
    for (ch of tempArr) {
        arr.push(ch.toLowerCase());
    }

    return arr.sort().join("");
}
