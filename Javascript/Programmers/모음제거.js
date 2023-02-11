function solution(my_string) {
    const arr = ["a", "e", "i", "o", "u"];
    let str = "";

    for (ch of my_string) {
        if (!arr.includes(ch)) {
            str += ch;
        }
    }
    return str;
}
