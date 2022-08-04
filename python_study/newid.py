import re
id='"...!@BaT#*..y.abcdefghijklm.'

def solution(new_id) :
    step1=new_id.lower()
    step2=re.sub('[^a-z0-9\-_\.]', '', step1) # ^ - not
    step3=re.sub('[\.]{2,}', '.', step2) #{2}-2회 , {2,}-2회이상
    step4=re.sub('^[\.]|[\.]$', '', step3) # ^[a] - a로 시작, [a]$ - a로 끝

    if step4 :
        step5=step4
    else :
        step5='a'
    
    if len(step5)>=16 :
        step6=step5[:15]
        step6=re.sub('[\.]$', '', step6)
    else :
        step6=step5

    while True :
        if len(step6)>=3 :
            step7=step6
            break;
        else :
            step6=step6+step6[-1]

    return step7
            

print(solution(id))
   
