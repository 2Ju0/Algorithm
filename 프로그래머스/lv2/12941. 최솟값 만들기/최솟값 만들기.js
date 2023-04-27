function solution(A,B){
    var answer = 0;
    A.sort((next, prev) => next - prev);
    B.sort((next, prev) => prev - next);
    
    for(let i = 0; i < A.length; i++){
        answer += A[i] * B[i];
    }
    
    return answer;
}