function solution(skill, skill_trees) {
    var answer = 0;
    
    for(let skill_tree of skill_trees){
        let stack = [...skill];
        let isPossible = true;
        
        for(let v of skill_tree){
            if(stack.includes(v)){
                if(stack[0] === v) stack.shift();
                else{
                    isPossible = false;
                    break;
                }
            }
        }
        if(isPossible) answer++;
    }
    return answer;
}