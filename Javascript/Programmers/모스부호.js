function solution(letter) {
    let answer = "";

    morse = {
        ".-": "a",
        "-...": "b",
        "-.-.": "c",
        "-..": "d",
        ".": "e",
        "..-.": "f",
        "--.": "g",
        "....": "h",
        "..": "i",
        ".---": "j",
        "-.-": "k",
        ".-..": "l",
        "--": "m",
        "-.": "n",
        "---": "o",
        ".--.": "p",
        "--.-": "q",
        ".-.": "r",
        "...": "s",
        "-": "t",
        "..-": "u",
        "...-": "v",
        ".--": "w",
        "-..-": "x",
        "-.--": "y",
        "--..": "z",
    };

    const map = new Map();
    const str = JSON.stringify(morse);
    const list = str.slice(1, str.length - 1).split(",");

    for (temp of list) {
        const [key, value] = temp.split(":");
        const chageKey = key.slice(1, key.length - 1);
        const chageValue = value.slice(1, value.length - 1);
        map.set(chageKey, chageValue);
    }

    const letter_list = letter.split(" ");

    for (mos of letter_list) {
        answer += map.get(String(mos));
    }

    return answer;
}
