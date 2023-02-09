// Add Two Numbers

function ListNode(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
}

var addTwoNumbers = function (l1, l2) {
    let temp = new ListNode();

    let num1 = l1;
    let num2 = l2;

    // 10 이상일때 넘겨줘야해
    let flag = false;
    let nowTemp = temp;

    // console.log(num1.val, num2.val);

    let sum = num1.val + num2.val;

    if (sum >= 10) {
        flag = true;
        sum %= 10;
    }

    nowTemp.val = sum;

    //노드 끝까지 돌릴려고 합니다.
    while (true) {
        if (!num1.next && !num2.next) {
            break;
        }
        // num1 , num2 가 없을수가 있나
        num1 = num1.next || new ListNode();
        num2 = num2.next || new ListNode();

        nowTemp.next = new ListNode();
        nowTemp = nowTemp.next;

        sum = num1.val + num2.val;

        // 아까 flag로 10 이상인지 체크한것
        if (flag) {
            sum += 1;
            flag = false;
        }
        // 계속 확인
        if (sum >= 10) {
            flag = true;
            sum %= 10;
        }

        nowTemp.val = sum;
    }

    // 막 자리
    if (flag) nowTemp.next = new ListNode(1);

    return temp;
};
