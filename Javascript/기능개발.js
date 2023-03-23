function solution(progresses, speeds) {
    let answer = [];
    const days = progresses.map((progress, index) =>
      Math.ceil((100 - progress) / speeds[index])
    );
    let cnt = 1;
    let maxDay = days[0];
  
    for (let i = 1; i < days.length; i++) {
      if (days[i] <= maxDay) {
        cnt++;
      } else {
        maxDay = days[i];
        answer.push(cnt);
        cnt = 1;
      }
    }
  
    answer.push(cnt);
  
    return answer;
  }