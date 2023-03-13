const solution = (keymap, targets) => {
    let answer = [];
    let object = {};
    const set = [...new Set(targets.join(''))];

    set.map((v) => {
      
      keymap.map((value) => {
        if (!value.includes(v)) return;
    
        const index = value.indexOf(v);
    
        if (!object.hasOwnProperty(v)) return (object[v] = index);
        if (object.hasOwnProperty(v))
          return (object[v] = object[v] > index ? index : object[v]);
      });
    });

    targets.map((v, i) => {
      for (let a = 0; a < v.length; a++) {
        if (!object.hasOwnProperty(v[a])) return (answer[i] = -1);
        if (object.hasOwnProperty(v[a]) && !answer[i]) answer[i] = 0;
        answer[i] += object[v[a]] + 1;
      }
    });
    return answer;
  };