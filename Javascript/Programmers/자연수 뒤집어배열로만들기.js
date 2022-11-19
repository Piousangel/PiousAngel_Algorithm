function solution(n) {
  let answer = n.toString().split("").reverse();
  const a = answer.map((x) => Number(x));
  return a;
}
