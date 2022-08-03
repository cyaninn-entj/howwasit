import re

ex_text='123%^#asd f456...-_    |*\lkj'

#문자클래스 축약표현
# \d - 숫자를 찾음
print(re.findall("\d", ex_text))
#output
#['1', '2', '3', '4', '5', '6']

# \D - 숫자가 아닌 것을 찾음
print(re.findall("\D", ex_text))
#output
#['%', '^', '#', 'a', 's', 'd', ' ', 'f', '.', '.', '.', '-', '_', 
# ' ', ' ', ' ', ' ', '|', '*', '\\', 'l', 'k', 'j']

# \s - whitespace 문자인 것을 찾음 (스페이스,탭,개행)
print(re.findall("\s", ex_text))
#output
#[' ', ' ', ' ', ' ', ' ']

# \S - whitespace 문자가 아닌 것을 찾음
print(re.findall("\S", ex_text))
#output
# ['1', '2', '3', '%', '^', '#', 'a', 's', 'd', 'f', 
# '4', '5', '6', '.', '.', '.', '-', '_', '|', '*', '\\', 'l', 'k', 'j']

# \w - 문자+숫자인 것을 찾음(특수문자 제외, _포함)
print(re.findall("\w", ex_text))
#output
#['1', '2', '3', 'a', 's', 'd', 'f', '4', '5', '6', '_', 'l', 'k', 'j']

# \W - 문자+숫자가 아닌 것을 찾음
print(re.findall("\W", ex_text))
#output
#['%', '^', '#', ' ', '.', '.', '.', '-', ' ', ' ', ' ', ' ', '|', '*', '\\']



#주요 함수

# re.search(pattern, string, flags=0)
# string을 스캔해서 정규식 pattern이 일치하는 첫번째 위치를 찾고 객체를 반환
# 일치하는 결과가 없으면 None으로 반환
re_search1=re.search('456', ex_text)
re_search2=re.search('b', ex_text)
print(re_search1)
if re_search1 : 
    print('1')
if re_search2 :
    print('2_true')
else :
    print('2_false')
#output
#<re.Match object; span=(0, 3), match='123'>
#1
#2_false

# re.match(pattern, string, flags=0)
# string이 시작 부분에서 0개 이상의 문자가 pattern과 일치하면 일치 객체를 반환
re_match1=re.match('456', ex_text)
re_match2=re.match('12', ex_text)
print(re_match2)
if re_match1 : 
    print('1_true')
else :
    print('1_false')
if re_match2 :
    print('2_true')
else :
    print('2_false')
#output
#<re.Match object; span=(0, 2), match='12'>
#1_false
#2_true

# re.findall(pattern, string, flags=0)
# string에서 겹치지 않는 pattern의 모든 일치를 문자열 리스트로 반환
re_findall1=re.findall('[a-z]', ex_text)
re_findall2=re.findall('[\W]', ex_text)
print(re_findall1)
print(re_findall2)
#output
#['a', 's', 'd', 'f', 'l', 'k', 'j']
#['%', '^', '#', ' ', '.', '.', '.', '-', ' ', ' ', ' ', ' ', '|', '*', '\\']

# re.sub(pattern, repl, string, count=0, flags=0)
# string에서 겹치지 않는 pattern의 가장 왼쪽 일치를 repl로 치환하여 얻은 문자열을 반환
re_sub=re.sub('[a-z\s]', '', ex_text)
print(re_sub)
#output
#123%^#456...-_|*\
