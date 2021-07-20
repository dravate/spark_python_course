* One 
```python

f = open('simple_data.txt', 'w')
f.write("Hello to writing data into the file")
f.write("Line 2")
f.write("Line 3")
f.write("Line 4")
f.close()


```
* two 

```python 

f = open('simple_data.txt', 'r') 
print (f.read()) 
f.close()



```

* three


```python

f = None

for i in range(5):
    with open ('data.txt', 'w') as f:
        if i> 2:
            break;
print (f.closed)



```


* four 
```python 

for i in range(5):
    with open ("data.txt", "w"):
        f.write("Number: ", i)

with open("data.txt", "w") as fr:
    print (fr.read()) 


```

* five

```python 

def foo():
	try:
		return 1
	finally: 
		return 2

print (foo())


```


* six 
```python 


def func(a, b=5, c=10):
	print (
		"a is ", a,
		"b is ", b,
		"c is ", c)

func(3, 7)
func(25, c = 24)
func(c=50, a = 100)
 
```
