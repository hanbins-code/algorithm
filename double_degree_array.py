# -*- coding: utf-8 -*-
"""double degree array.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VCehJVmb_MNmT0MhlIGbRAhAPxp1LizR
"""

'''
제목 ; 인접 리스트를 이용한 Double Degree Array 프로그램
프로그램 기능 : n 개의 요소가 있고, 그 요소들은 랜덤으로 서로 연결 되어있거나 연결 되어 있지 않는다고 생각해보자.
                그럼 거미줄 같은 그림이 상상될 것이다. 이 때 한 요소에 연결 되어 있는 모든 다른 요소에 연결 되어 있는 수를 구하는 기능이다.
                ex) 1의 요소에는 3의 요소가 연결되어 있다고 가정하자. 3의 요소는 다시 2와 1의 요소와 서로 연결되어 있다. 
                    따라서 입력값이 1 (요소의 이름)이라면, 출력값은 2 (요소 3의 연결된 수)이다.
최종 수정 날짜 : 2021.02.02
만든이 : 김한빈
'''

def Clear_data_list(a): # ex) "1 2 3 4\n" ==>> "[1, 2, 3, 4]"
    return [list(map(int, (data.replace("\n", '')).split(" "))) for data in a]

def Flatten(data): # ex) [[1, 2], [2, 3], [3, 4, 5]] ==> [1, 2, 2, 3, 3, 4, 5]
    output = []
    for item in data:
        if type(item) == list:
            output += Flatten(item)
        else:
            output += [item]
    return output

def Get_linklist(num, data):
    answer_list = []
    for a in clear_list:
        if num == a[0]:
            answer_list.append(a[1])
        elif num == a[1]:
            answer_list.append(a[0])
    return answer_list

def Get_answerlist(link, num_list):
    sum = 0
    for b in link:
        sum = sum + num_list[b-1]
    return sum

f = open('/content/sample_data/rosalind_ddeg.txt', 'r') # 파일을 열어 필요한 정보들을 저장
summary = f.readline().replace('\n', "").split(' ')
data = f.readlines()
f.close()

clear_list = Clear_data_list(data) # 데이터 정제
flatten_list = Flatten(clear_list) # 데이터 리스트 평탄화
num_list = [] # 연결된 횟수를 저장할 리스트

for a in range(1, int(summary[0]) + 1): # 1 부터 5까지 (a의 범위), 참조할 리스트에서 연결된 값을 검색하여 다른 리스트에 저장
  num_list.append(flatten_list.count(a))


link_list = []

for i in range(1, int(summary[0]) + 1): # 검사 대상은 요소값들의 범위와 같음
  link_list.append(Get_linklist(i, clear_list))


answer_list = []

for a in link_list:
    answer_list.append(Get_answerlist(a, num_list))

g = open('/content/sample_data/answer.txt', 'w') # 파일을 열어 필요한 정보들을 저장
for t in answer_list:
    g.write(str(t))
    g.write(" ")

g.close()