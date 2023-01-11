function solution(my_string) {
    var answer = '';
    answer = reverseString(my_string);
    return answer;
}
function reverseString(str) {
  if (str === "")
    return "";
  else
    return reverseString(str.substr(1)) + str.charAt(0);
}
