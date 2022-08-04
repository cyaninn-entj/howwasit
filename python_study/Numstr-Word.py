import re

a='one4seveneight'
b='1zerotwozero3'

def solution(s):
    en_list=['zero', 'one', 'two', 'three', 'four', 'five',
    'six', 'seven', 'eight', 'nine']

    for i in range(0,10) :
        s=re.sub(en_list[i], str(i), s)

    if type(s)==str :
        result=int(s)

    return result

print(solution(b))
