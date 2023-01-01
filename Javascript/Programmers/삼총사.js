function solution(number) {
    let result = 0;

    const comb = (current, start) => {
        if (current.length === 3) {
            result += current.reduce((acc, cur) => acc + cur, 0) === 0 ? 1 : 0;
            return;
        }
        
        for (let i = start; i < number.length; i++) {
            comb([...current, number[i]], i + 1);
        }
    }
    comb([], 0);
    return result;
}