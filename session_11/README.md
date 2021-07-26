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


import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute("INSERT INTO stocks VALUES('2021-07-26', 'BUY', 'GOOG', 100, 35.50)")

conn.commit()
conn.close()


```

* Five 

```python 
import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
symbol = 'GOOG'
c.execute("SELECT * from stocks where symbol='%s'" % symbol)
print(c.fetchone())

```

* Six

```python 

purchases = [
             ('2020-07-26', 'BUY', 'IBM', 1000, 45.00),
             ('2020-07-26', 'BUY', 'MSFT', 1000, 45.00),
             ('2020-07-26', 'BUY', 'GOOG', 1000, 45.00),
             ('2020-07-26', 'SELL', 'IBM', 500, 65.00),
           ]

purchases

c.executemany(
        'INSERT into stocks values(?, ?, ?, ? , ?)', purchases
        )

for row in c.execute("SELECT * from stocks ORDER BY PRICE"):
    print (row)


```

* Seven 

```sql 

create table project (
    name        text primary key,
    description text,
    deadline    date
);

create table task (
    id           integer primary key autoincrement not null,
    priority     integer default 1,
    details      text,
    status       text,
    deadline     date,
    completed_on date,
    project      text not null references project(name)
);


```

* Eight 

```sql 

create table project (
    name        text primary key,
    description text,
    deadline    date
);

create table task (
    id           integer primary key autoincrement not null,
    priority     integer default 1,
    details      text,
    status       text,
    deadline     date,
    completed_on date,
    project      text not null references project(name)
);

```

