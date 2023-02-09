function solution(before, after) {
    let answer = 0;

    const bArr = [...before];
    const aArr = [...after];
    let cnt = 0;

    const map1 = new Map();
    const map2 = new Map();

    for (b of bArr) {
        if (map1.has(b)) {
            map1.set(b, map1.get(b) + 1);
        } else map1.set(b, 1);
    }

    for (a of aArr) {
        if (map2.has(a)) {
            map2.set(a, map2.get(a) + 1);
        } else map2.set(a, 1);
    }

    let sortedMap1 = new Map([...map1].sort());
    let sortedMap2 = new Map([...map2].sort());

    if (sortedMap1 == sortedMap2) return 1;
    else return 0;
}
