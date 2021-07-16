
* One 

```python

lst = ["easy", "simple", "cheap", "free"]
print (lst[-1])


lst = [3, 5, 7]

lst.append(42)
print (lst)

lst = lst.append(42)

print (lst)

cities = ["Pune", "Mumbai", "Nagpur", "Nashik"]

c1 = cities.pop(0)
print (c1)
print (cities)


```

* Two 

```python 

L = [1, 10, 20, 5, 15, 9, 19]

L.reverse()
print (L)

L.sort()
print (L)

new_L = sorted(L)
print(new_L)
print (L)


```

*Three

```python


names1 = ["amir", "shahruk", "chales", "deo"]
names2 = names1
names3 = names1[:]

names2[0] = 'Alice'
names3[1] = 'Bob'

sum = 0

for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
       sum +=10

print (sum)


```


* Four

```python

confusion = {}
confusion[1] = 1
confusion['1'] = 2
confusion[1] +=1

sum = 0
for k in confusion:
    sum += confusion[k]

print (sum)


```

*Five

```python 

confusion = {}
confusion[1] = 1
confusion['1'] = 2
confusion[1.0] = 4
confusion[1] +=1

sum = 0
for k in confusion:
    sum += confusion[k]

print (sum)



```
