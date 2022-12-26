function solution(seoul) {
  let answer = "";

  seoul.forEach((item, index) => {
    if (item === "Kim") {
      answer = `김서방은 ${index}에 있다`;
      return false;
    }
  });
  return answer;

  // var idx = seoul.indexOf('Kim');
  // return "김서방은 " + idx + "에 있다";
}
