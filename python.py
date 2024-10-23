listem = ['a','b','c','d']
print(type(listem))

word = 'happy'
list_2 = list(word)
print(list_2)

string_1 = 'I quit smoking'

print(list('a b c'))

listem = [1,2,3]
print(len(listem))

yeni = [listem]
print(len(yeni))

a= [[1,2,3],['ali','ayse'],[True,False]]

list_a = [a]
print(len(list_a))

text = "2023's perfect"
print(list(text))

print(list('1234'))
listem = [[1,2,3], 'bir string' , 7.23, True]

print(len(listem))

numbers =[1,4,7]
numbers.append(9)
numbers.append('9')
numbers.append(['a','b','c'])
print(numbers)

empty_list = []
empty_list.append(6666)
print(empty_list) 

numbers = [1,4,7]
numbers.insert(2,9)
print(numbers)

listem = ['a','b','c','d']
listem.insert(3,12)
print(listem)

numbers =[1,2,3,4]
numbers.insert(4,5)
print(numbers)

numbers = [1,4,7,9]
numbers.remove(9)
print(numbers)

listem = ['a','b','c','d']
listem.remove('c')
listem.pop(1)
print(listem)

a = [1,4,7,9,"9",['a','b','c']]
a.pop()
a.clear()
print(a)

numbers = [4,1,9,7]
numbers.sort()
print(numbers)

listem = [2,7,3,0,5]
listem.sort(reverse=True)
print(listem)

list_1 = ['one','four','nine']
list_1.sort()
print(list_1)

print('clarus' + '''way''')

veg = 'Onion'
print("I love {} and {veg}".format("Oneo", veg="Apple"))
