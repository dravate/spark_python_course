
* One 

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

*two

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

* Three

```python

f = None

for i in range(5):
    with open ('data.txt', 'w') as f:
        if i> 2:
            break;
print (f.closed)



```

