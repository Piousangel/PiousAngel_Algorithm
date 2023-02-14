// class WeightedRandomCollection {}

// 데이터를 가중치의 오름차순으로 정렬
// 랜덤 기준값 설정 => 정렬된 데이터를 순회하며 각 가중치를 누적하다 기준값 이상이 되면 종료

const WeightedRandomCollection = function () {
    // To be implemented, do not return anything
    this.collectionMap = new Map();
    this.result = [null];
};
/**
 * @param {number} userId
 * @return {boolean}
 */
WeightedRandomCollection.prototype.add = function (userId) {
    // To be implemented

    // 기존 컬렉션에 해당 userId가 존재하지 않으면 추가
    if (!this.collectionMap.has(userId)) {
        this.collectionMap.set(userId, 1);
        this.result.push(true);
    } else {
        let newValue = this.collectionMap.get(userId) + 1;
        this.collectionMap.set(userId, newValue);
        this.result.push(false);
    }
};
/**
 * @param {number} val
 * @return {boolean}
 */
WeightedRandomCollection.prototype.delete = function (userId) {
    // To be implemented

    // 해당 유저가 존재한 적이 없으면 false
    if (!this.collectionMap.has(userId)) {
        this.result.push(false);
    } else {
        const oldValue = this.collectionMap.get(userId);
        // 다 삭제했으면 false
        if (oldValue < 1) {
            this.result.push(false);
        } // 삭제할 것이 남았으면 제거 후 true;
        else {
            const newValue = this.collectionMap.get(userId) - 1;
            this.collectionMap.set(userId, newValue);
            this.result.push(true);
        }
    }
};
/**
 * @return {number}
 */
WeightedRandomCollection.prototype.pickRandom = function () {
    // To be implemented
    let target = 0;
    // 가중치 합
    let totalWeight = 0;
    for (const [key, value] of this.collectionMap) {
        totalWeight += value;
    }
    
    const percentMap = new Map();

    // 가중치를 백분율로 치환
    for (const [key, value] of this.collectionMap) {
        percentMap.set(key, value / totalWeight);
    }

    // 오름차순 정렬
    let sortedPercentMap = new Map([...percentMap].sort((a, b) => a[1] - b[1]));

    const pivot = Math.random();

    let cumulativeSum = 0;
    // 누적해가면서 pivot보다 커지면 리턴
    for (const [key, value] of this.collectionMap) {
        cumulativeSum += value;

        if (pivot <= cumulativeSum) {
            target = key;
            break;
        }
    }

    this.result.push(target);
};

WeightedRandomCollection.prototype.printInfo = function () {
    console.log(this.collectionMap);
    console.log(this.result);
};

const input = [
    [
        "WeightedRandomCollection",
        "add",
        "add",
        "add",
        "add",
        "add",
        "add",
        "delete",
        "delete",
        "delete",
        "delete",
        "pickRandom",
        "pickRandom",
        "pickRandom",
        "pickRandom",
        "pickRandom",
        "pickRandom",
        "pickRandom",
        "pickRandom",
        "pickRandom",
        "pickRandom",
    ],
    [
        [],
        [1],
        [1],
        [2],
        [1],
        [2],
        [2],
        [1],
        [2],
        [2],
        [2],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    ],
];

// const input = [
//     [
//         "WeightedRandomCollection",
//         "add",
//         "add",
//         "add",
//         "add",
//         "add",
//         "delete",
//         "delete",
//         "delete",
//         "add",
//         "delete",
//         "pickRandom",
//         "pickRandom",
//         "pickRandom",
//         "pickRandom",
//         "pickRandom",
//         "pickRandom",
//         "pickRandom",
//         "pickRandom",
//         "pickRandom",
//         "pickRandom",
//     ],
//     [
//         [],
//         [1],
//         [1],
//         [2],
//         [2],
//         [2],
//         [1],
//         [1],
//         [2],
//         [1],
//         [2],
//         [],
//         [],
//         [],
//         [],
//         [],
//         [],
//         [],
//         [],
//         [],
//         [],
//     ],
// ];

runCode(input[0], input[1]);

function runCode(functionName, targetName) {
    const obj = new WeightedRandomCollection();

    for (let i = 1; i < functionName.length; i++) {
        switch (functionName[i]) {
            case "add":
                obj.add(targetName[i][0]);
                break;
            case "delete":
                obj.delete(targetName[i][0]);
                break;
            case "pickRandom":
                obj.pickRandom();
                break;
        }
    }

    obj.printInfo();
}
