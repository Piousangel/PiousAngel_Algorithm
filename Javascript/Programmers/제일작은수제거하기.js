function solution(arr) {
  if (arr.length === 1) return [-1];
  const minNum = Math.min.apply(null, arr);
  const answer = arr.filter((x) => x !== minNum);
  return answer;
}
