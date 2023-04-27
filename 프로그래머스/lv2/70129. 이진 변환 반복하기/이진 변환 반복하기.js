function toBinary(num) {
    let answer = [];
    
    while(true){
        answer.unshift(num % 2);
        if (parseInt(num / 2) === 0) break;
        num = parseInt(num / 2);
    }

    return answer.join('');
}

function solution(s) {
    let numOfChange = 0;
    let numOfZero = 0;
    
    while(s !== '1'){
        let tmp = s.replace(/0/g, '');
        let len = tmp.length;
        
        numOfChange += 1;
        numOfZero += s.length - s.replace(/0/g, '').length;
        
        s = toBinary(len);
    }
    
    return [numOfChange, numOfZero];
}