#  Database 

* One 

```sql 

CREATE TABLE presidents (
   id int PRIMARY key NOT NULL,
   name char(100) NOT NULL,
   age int NOT NULL
);


```

* Two 

```sql 

INSERT INTO presidents (id, name, age) values (1, 'Donalt T', 76);
INSERT INTO presidents (id, name, age) values (1, 'Donalt T', 78);

```

*Three 

```python 
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute(
   '''
   CREATE TABLE stocks (
   date text,
   trans text,
   symbol text,
   qty real,
   price real
);
   '''
);

conn.commit()
conn.close()

```

* Four 

```python 



```
