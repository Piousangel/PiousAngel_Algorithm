function solution(numbers, direction) {
    switch (direction) {
        case "right":
            const lastItem = numbers.pop();
            numbers.unshift(lastItem);
            break;

        case "left":
            const firstItem = numbers.shift();
            numbers.push(firstItem);
            break;
    }
    return numbers;
}
