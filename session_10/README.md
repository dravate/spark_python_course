
* one

```python 


sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]

print (word_lengths)



```

* Two 
```python 

y = 6
z = lambda x: x*y 

print (z(8))

```

* Three 
```python 

a = range(2, 9)
m = map(lambda: x, y: x **y, a, reversed(a))
n = map(lambda: x, y: x + , a, reversed(a))


```


* Four 
``` python 

d = lambda x: x*5
e = lambda x: x*2

x = d(2)
x = e(x)
x = d(x * x)
print (x) 


```

* Five 
```python 

def writer():
    title = 'Sir'
    name = lambda x: title + '  ' + x
    return name 

who = writer()
who('Arthur')

```



* Six

``` python

CREATE TABLE presidents (
id int primary key NOT NULL,
name char(100) NOT NULL,
age int NOT NULL
);

```
