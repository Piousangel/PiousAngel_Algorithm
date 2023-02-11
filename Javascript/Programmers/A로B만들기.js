function solution(before, after) {
    let sortedBefore = [...before].sort().join("");
    let sortedAfter = [...after].sort().join("");
    const answer = sortedBefore === sortedAfter ? 1 : 0;
    return answer;
}
