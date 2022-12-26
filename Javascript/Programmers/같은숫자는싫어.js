function solution(arr) {
  let answer = [arr[0]];
  arr.filter((element, index) => {
    if (index !== 0) if (element !== arr[index - 1]) answer.push(element);
  });
  return answer;
}
