function solution(k, tangerine) {
    var answer = 0;
    let size = [];
    let map = new Map();
    
    for(let v of tangerine){
        if(map.get(v)) map.set(v, map.get(v) + 1);
        else map.set(v, 1);
    }
    for(let [k, v] of map) size.push(v);
    
    size.sort((a, b) => b - a);

    console.log(size);
    for(let v of size){
        if((k - v == 0) || (k - v < 0)) return answer + 1;
        else if(k - v > 0){
            k -= v;
            answer += 1;
        }
    }
    
    return answer;
}