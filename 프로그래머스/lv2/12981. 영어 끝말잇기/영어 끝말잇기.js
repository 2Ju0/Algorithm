function solution(n, words) {
    let stack = [];
    
    for(let i = 0; i < words.length; i++){
        let numOfPlay = Math.ceil((i + 1) / n);
        let numOfPerson = ((i + 1) % n === 0 ? n : (i + 1) % n);
        
        if(stack.includes(words[i])){
            return [numOfPerson, numOfPlay];
        }
        if(stack.length && (stack[stack.length - 1].slice(-1) !== words[i].slice(0, 1))){
            return [numOfPerson, numOfPlay];
        }
        stack.push(words[i]);
    }
    return [0, 0];
}