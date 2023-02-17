const asteroidCollision = function (asteroids) {
    const stack = [];

    for (asteroid of asteroids) {
        if (asteroid > 0) {
            stack.push(asteroid);
        } else {
            while (
                stack.length > 0 &&
                stack[stack.length - 1] > 0 &&
                stack[stack.length - 1] < Math.abs(asteroid)
            ) {
                stack.pop();
            }
            if (stack[stack.length - 1] === Math.abs(asteroid)) {
                stack.pop();
                continue;
            }
            if (stack.length === 0 || stack[stack.length - 1] < 0) {
                stack.push(asteroid);
            }
        }
    }

    return stack;
};
