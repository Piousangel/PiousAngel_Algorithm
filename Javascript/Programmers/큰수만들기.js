function solution(number, k) {
    const stack = [];

    for (val of number) {
        while (0 < k && stack[stack.length - 1] < val) {
            stack.pop();
            k -= 1;
        }
        stack.push(val);
    }
    stack.splice(stack.length - k, k);
    return stack.join("");
}
