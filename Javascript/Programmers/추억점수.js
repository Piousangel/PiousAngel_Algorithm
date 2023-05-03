function solution(name, yearning, photo) {
    const answer = [];
    const map = new Map();

    for (let i = 0; i < name.length; i++) {
        map.set(name[i], yearning[i]);
    }

    for (let i = 0; i < photo.length; i++) {
        let temp = 0;
        for (let j = 0; j < photo[i].length; j++) {
            if (!map.get(photo[i][j])) {
                continue;
            }
            temp += map.get(photo[i][j]);
        }
        answer.push(temp);
        temp = 0;
    }

    return answer;
}
