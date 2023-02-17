function ListNode(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
let addTwoNumbers = function (l1, l2) {
    const nodeList = new ListNode();

    let num1 = l1;
    let num2 = l2;

    let curNode = nodeList;
    let flag = false;

    let total = num1.val + num2.val;

    if (total > 9) {
        flag = true;
        total %= 10;
    }

    curNode.val = total;

    while (num1.next || num2.next) {
        num1 = num1.next || new ListNode();
        num2 = num2.next || new ListNode();
        curNode.next = new ListNode();
        curNode = curNode.next;
        total = num1.val + num2.val;

        if (flag) {
            total += 1;
            flag = false;
        }

        if (total > 9) {
            flag = true;
            total %= 10;
        }

        curNode.val = total;
    }
    if (flag) {
        curNode.next = new ListNode(1);
    }

    return nodeList;
};
