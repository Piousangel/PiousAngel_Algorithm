function solution(reqs) {
    let answer = [];

    // 정보와 돈 정보 저장 map
    let accountInfoMap = new Map();

    for (info of reqs) {
        const info_list = info.split(" ");

        //create
        if (info_list[0] === "CREATE") {
            //없으면
            if (!accountInfoMap.has(info_list[1])) {
                accountInfoMap.set(info_list[1], info_list[2]);
                answer.push(200);
                // 있으면 403
            } else {
                answer.push(403);
            }
        } //deposit
        else if (info_list[0] === "DEPOSIT") {
            //없으면 404
            if (!accountInfoMap.has(info_list[1])) {
                answer.push(404);
            } else {
                accountInfoMap.set(
                    info_list[1],
                    accountInfoMap.get(info_list[1]) + info_list[2]
                );
                answer.push(200);
            }
        } // withdraw
        else {
            //출금 계좌가 없으면 404
            if (!accountInfoMap.has(info_list[1])) {
                answer.push(404);
            }
            //있으면 기존 돈과 비교해서 충분하면 출금 or 모자라면 출금 안하고 403
            else {
                if (accountInfoMap.get(info_list[1]) >= info_list[2]) {
                    accountInfoMap.set(
                        info_list[1],
                        accountInfoMap.get(info_list[1]) - info_list[2]
                    );
                    answer.push(200);
                } else {
                    answer.push(403);
                }
            }
        }
    }

    return answer;
}
