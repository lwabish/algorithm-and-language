# add:append,insert
# del:del pop() pop(i) remove(v)
# modify:list[i]=
# get:list[i]
persons = ['abc', 'def', 'qqq']

print('Come and join me with dinner'+persons[1])

persons[2] = 'eee'

persons.insert(0, 'abdsafsdf')
persons.insert(int(len(persons) / 2), 'mid')
persons.append('last')
print(persons)

# list.sort() 原地升序
# sorted() 复制排序
# list.reverse() 原地掉头
# reversed() 复制掉头

# 切片复制[::]
# 倒序[::-1]
