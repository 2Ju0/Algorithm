function isRight(s){
    let stack = [];
    
    for(let v of s){
        let top = stack[stack.length - 1];
        
        if(v === ")" && top === "(") stack.pop();
        else if(v === "]" && top === "[") stack.pop();
        else if (v === "}" && top === "{") stack.pop();
        else stack.push(v);
    }
    if(stack.length !== 0) return false;
    
    return true;
}

function solution(s) {
    var answer = 0;
    for(let i = 0; i < s.length; i++){
        let rotated = s.substring(i) + s.substring(0, i);
        if(isRight(rotated)) answer += 1;
    }
    
    return answer;
}