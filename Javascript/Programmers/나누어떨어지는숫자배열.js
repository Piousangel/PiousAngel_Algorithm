function solution(arr, divisor) {
  const answer = arr
    .filter((x) => x % divisor == 0)
    .sort((a, b) => {
      return a - b;
    });
  if (answer.length === 0) return [-1];
  else return answer;
}
