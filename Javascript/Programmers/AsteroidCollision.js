/**
 * @param {number[]} asteroids
 * @return {number[]}
 */

// 두 행성? 만나면 작은거 파괴
// 같으면 둘다 파괴
// 절대값이 크긴가요?
// 근데 같은 부호끼리는 안만나네요
// 먼가 스택에 넣고 처리하면 될거같은데

var asteroidCollision = function (asteroids) {
    let stack = [];

    // true 일때를 stack에 양수가 들어있다 생각할게요
    let buho = true;

    for (let i = 0; i < asteroids.length; i++) {
        let val = asteroids[i];
        // 스택 비어있으면 하나 넣자
        if (stack.length === 0) {
            if (val > 0) buho = true;
            else buho = false;

            stack.push(asteroids[i]);
        }

        // 아니면 부호 같은지 비교?
        // 부호 다르면 계속 가면서 빼야지
        else {
            if ((buho && val > 0) || (!buho && val < 0)) stack.push(val);
            else {
                // 절대값 비교하면서 stack을 빼던 안넣던 해야함
                while (true) {
                    if (Math.abs(stack[stack.length - 1]) <= Math.abs(val)) {
                        stack.pop();
                    } else break;
                }
            }
        }
    }

    return stack;
};
