function solution(numbers) {
    const arr = numbers
        .map((v) => String(v))
        .sort((a, b) => {
            return b + a - (a + b);
        });

    return arr[0] === "0" ? "0" : arr.join("");
}
