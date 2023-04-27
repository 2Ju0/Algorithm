function solution(s) {
    var answer = '';
    
    const str = s.split(' ');
    answer = `${Math.min(...str)} ${Math.max(...str)}`;
    
    return answer;
}