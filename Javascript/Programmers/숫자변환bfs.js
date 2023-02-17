function solution(x, y, n) {
    const set = new Set();

    q = [];
    q.push([x, 0]);

    while (q.length > 0) {
        const [num, cnt] = q.shift();

        if (num === y) {
            return cnt;
        }

        if (num * 3 <= y && !set.has(num * 3)) {
            set.add(num * 3);
            q.push([num * 3, cnt + 1]);
        }
        if (num * 2 <= y && !set.has(num * 2)) {
            set.add(num * 2);
            q.push([num * 2, cnt + 1]);
        }
        if (num + n <= y && !set.has(num + n)) {
            set.add(num + n);
            q.push([num + n, cnt + 1]);
        }
    }
    return -1;
}
