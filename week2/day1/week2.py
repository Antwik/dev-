
#map 
names = ["sam","john","james"]
map(len, names)
print(list(map(len,names)))

#filter 
def too_old(x): return x > 30
ages = [22, 25, 29, 34, 56, 24, 12]
filter(too_old, ages)
print(list(filter(too_old, ages)))

#ihk 
def acceptance_student(X): 
    
    age = X['age']
    level = X['level']

    return (age>25) and (level>=2)


acceptance_students = [{"age":25,"level":13},{"age":17,"level":3},{"age":100,"level":3}] 

print(list(filter( acceptance_student, acceptance_students)))


#kan
items = [1, 2, 3, 4, 5]
squares = map((lambda x: x ** 2), items)
print(list(map((lambda x: x ** 2), items)))


items = [4, 5, 6, 8, 9]
squares = map((lambda x: x ** 3), items)
print(list(map((lambda x: x ** 3), items)))

kans = [89,87,78]
names = map((lambda y: y + 76), kans)
print(list(map((lambda y: y +76),kans)))

# labs

def is_even(x): 
    return x % 2 == 0
numbers = [1,56,234,87,4,76,24,69,90,135] 
print(list(filter(is_even, numbers)))

 # labs 
def is_odd(x):
    return  x % 2 != 0
numbers = [1,56,234,87,4,76,24,69,90,135]
print(list(filter(is_odd,numbers)))

#labs 

def is_even(x): 
    return not x % 2 == 0
numbers = [1,56,234,87,4,76,24,69,90,135] 
print(list(filter(is_even, numbers)))

#labs
from functools import reduce
total = reduce(lambda item, running_total: item + running_total, [1, 2, 3, 4, 5])
print(total)

#labs 
word = ('hello ' + 'world')
print(word)

#labs
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print(words)
print([len(word) for word in words])

#labs 
numbers1 = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
postnumbs = [numbs for numbs in numbers1 if numbs > 0]
print(postnumbs)

numbers2 = [12, 54, 33, 67, 24, 89, 11, 24, 47]
evennumbs = [numbs for numbs in numbers2 if numbs % 2 == 0]
print(evennumbs)

words = ["hello", "my", "name", "is", "Sam"]
upwords = [(word.upper(),len(word)) for word in words]
print(upwords)