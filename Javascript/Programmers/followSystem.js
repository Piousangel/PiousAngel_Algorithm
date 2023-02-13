class FollowSystem {
    constructor() {
        // to be implemented. do not return anything
        this.followMap = new Map();
        this.result = [null];
    }
    follow(from, to) {
        // to be implemented

        // 자신을 팔로우 하는 멤버가 한명도 없으면, 팔로우하기
        if (!this.followMap.has(to)) {
            this.followMap.set(to, [from]);
            this.result.push(true);
        }
        // 있으면, 그 사람이 나를 팔로우 하고 있는지 확인
        else {
            let followingMember = this.followMap.get(to);
            if (followingMember.includes(from)) {
                this.result.push(false);
            }
            // 없으면 팔로우 목록에 추가
            else {
                followingMember.push(from);
                this.followMap.set(to, followingMember);
                this.result.push(true);
            }
        }
    }
    unfollow(from, to) {
        // 자신을 팔로우 하는 멤버가 한명도 없으면, 언팔중이니 당연히 false;
        if (!this.followMap.has(to)) {
            this.result.push(false);
        }
        // 있으면, 그 사람이 나를 팔로우 하고 있는지 확인
        else {
            let followingMember = this.followMap.get(to);
            if (followingMember.includes(from)) {
                this.result.push(true);
                const newFollowingMember = followingMember.filter(
                    (name) => name != from
                );
                this.followMap.set(to, newFollowingMember);
            }
            // 없으면 팔로우 false
            else {
                this.result.push(false);
            }
        }
    }

    // userID를 팔로우 하고 있는 사람 숫자
    followerCount(userId) {
        let count = 0;
        count = this.followMap.get(userId).length;
        this.result.push(count);
        return count;
    }

    // userID가 팔로잉 하고 있는 사람 숫자
    followingCount(userId) {
        let count = 0;
        for (const [key, value] of this.followMap) {
            if (userId !== key) {
                let list = value;
                for (let name of list) {
                    if (name === userId) {
                        count += 1;
                    }
                }
            }
        }
        this.result.push(count);
        return count;
    }

    isMutualFollowing(user1Id, user2Id) {
        let isMutual = true;

        const user1IdFollowerList = this.followMap.get(user1Id);
        const user2IdFollowerList = this.followMap.get(user2Id);

        if (
            user1IdFollowerList.includes(user2Id) &&
            user2IdFollowerList.includes(user1Id)
        ) {
            isMutual = true;
        } else {
            isMutual = false;
        }

        this.result.push(isMutual);
        return isMutual;
    }
    commonFollowList(user1Id, user2Id) {
        let list = [];

        // const user1IdFollowerList = this.followMap.get(user1Id);
        // const user2IdFollowerList = this.followMap.get(user2Id);
        // console.log("user1IdFollowerList", user1IdFollowerList)
        // console.log("user2IdFollowerList", user2IdFollowerList)
        // list = user1IdFollowerList.filter((follower) =>
        //     user2IdFollowerList.includes(follower)
        // );

        for (const [key, value] of this.followMap) {
            const userFollower = value;
            if (value.includes(user1Id) && value.includes(user2Id)) {
                list.push(key);
                this.result.push(list);
            }
        }
        return list;
    }

    printInfo() {
        console.log(this.followMap);
        console.log(this.result);
    }
}

// const input = [
//     [
//         "FollowSystem",
//         "follow",
//         "follow",
//         "follow",
//         "follow",
//         "unfollow",
//         "isMutualFollowing",
//     ],
//     [
//         [],
//         ["AAA1", "AAA2"],
//         ["AAA1", "AAA2"],
//         ["AAA2", "AAA3"],
//         ["AAA1", "AAA3"],
//         ["AAA3", "AAA1"],
//         ["AAA2", "AAA4"],
//     ],
// ];

const input = [
    [
        "FollowSystem",
        "follow",
        "follow",
        "follow",
        "follow",
        "followerCount",
        "followingCount",
        "isMutualFollowing",
        "commonFollowList",
        "unfollow",
        "followingCount",
        "isMutualFollowing",
    ],
    [
        [],
        ["A", "B"],
        ["A", "C"],
        ["C", "A"],
        ["C", "B"],
        ["A"],
        ["A"],
        ["A", "C"],
        ["A", "C"],
        ["A", "C"],
        ["A"],
        ["A", "C"],
    ],
];

runCode(input[0], input[1]);

function runCode(functionName, targetName) {
    const system = new FollowSystem();
    for (let i = 1; i < functionName.length; i++) {
        switch (functionName[i]) {
            case "follow":
                system.follow(targetName[i][0], targetName[i][1]);
                break;
            case "unfollow":
                system.unfollow(targetName[i][0], targetName[i][1]);
                break;
            case "followerCount":
                system.followerCount(targetName[i][0]);
                break;
            case "followingCount":
                system.followingCount(targetName[i][0]);
                break;
            case "isMutualFollowing":
                system.isMutualFollowing(targetName[i][0], targetName[i][1]);
                break;
            case "commonFollowList":
                system.commonFollowList(targetName[i][0], targetName[i][1]);
                break;
        }
    }

    system.printInfo();
}

