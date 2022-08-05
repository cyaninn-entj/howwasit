a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
b="right"

def solution(numbers, hand):
    last_right=[4,1] # *
    last_left=[4,3] # #
    nc=[[4,2],[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]]
    answer=''

    for i in numbers :
        if i in [1,4,7] :
            last_left=nc[i]
            answer=answer+'L'
        elif i in [3,6,9] :
            last_right=nc[i]
            answer=answer+'R'
        else :
            next_num=[nc[i][0], nc[i][1]]
            ld=abs(next_num[0]-last_left[0])+abs(next_num[1]-last_left[1])
            rd=abs(next_num[0]-last_right[0])+abs(next_num[1]-last_right[1])
            if ld>rd :
                last_right=next_num
                answer=answer+'R'
            elif ld<rd :
                last_left=next_num
                answer=answer+'L'
            else :
                if hand=='right' :
                    last_right=next_num
                    answer=answer+'R'
                else :
                    last_left=next_num
                    answer=answer+'L'

    return answer

print(solution(a,b))
