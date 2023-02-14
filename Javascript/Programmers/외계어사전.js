function solution(spell, dic) {
    let flag = 2;

    for (word of dic) {
        let temp_list = [...spell];

        for (ch of word) {
            if (spell.includes(ch)) {
                temp_list = temp_list.filter((v) => v !== ch);
            }
        }

        if (temp_list.length === 0) {
            flag = 1;
            break;
        }
    }

    return flag;
}
