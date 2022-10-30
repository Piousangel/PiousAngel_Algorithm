function solution(n) {
  let answer = 0;
  const arr = n.toString().split("");
  arr.forEach((element) => {
    answer += Number(element);
  });
  return answer;
}
