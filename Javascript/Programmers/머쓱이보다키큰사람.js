function solution(array, height) {
    const a = array.filter((n) => n > height);
    return a.length;
}
