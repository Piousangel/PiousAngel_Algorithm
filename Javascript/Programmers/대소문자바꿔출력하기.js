let input = [];

rl.on("line", function (line) {
    input = [line];
}).on("close", function () {
    str = input[0];
    let answer = "";
    for (char of str) {
        if (char.toUpperCase() === char) answer += char.toLowerCase();
        else answer += char.toUpperCase();
    }
    console.log(answer);
});
