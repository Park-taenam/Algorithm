import sys

text = sys.stdin.readline().strip().upper()

# 풀이 1 - 딕셔너리
'''딕셔너리로 풀면 value 값으로 key를 찾아야되서 번거로움'''
cnt = {}

for s in text:
    if s in cnt.keys():
        cnt[s] += 1
    else:
        cnt[s] = 1

if list(cnt.values()).count(max(list(cnt.values()))) > 1:
    print("?")
else:
    result = [k for k, v in cnt.items() if v == max(list(cnt.values()))]
    print(result[0])

# 풀이 2 - 리스트
word_list = list(set(text))
count_list = []

for i in word_list:
    count_list.append(text.count(i))

if count_list.count(max(count_list))>=2:
    print("?")
else:
    print(word_list[count_list.index(max(count_list))])