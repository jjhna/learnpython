'''

Python = SQL Equivalents

(Note that joins are covered under the python merge() and pandas dataframes

### 1. **Set Creation**
- **Python**: `set()` creates an empty set; `set(iterable)` creates a set from an iterable.
- **SQL**: You don’t explicitly create an empty set in SQL. Instead, SQL operates on tables and rows, which are conceptually sets of data.

### 2. **Adding Elements**
- **Python**: `add(elem)` adds an element to the set.
- **SQL**: Inserting a row into a table is equivalent to adding an element to a set.
  - **SQL**: `INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...)`

### 3. **Removing Elements**
- **Python**: `remove(elem)` removes an element from the set, raises `KeyError` if not found; `discard(elem)` removes an element if it exists, but does nothing if it doesn’t.
- **SQL**: To remove data, you can use the `DELETE` statement.
  - **SQL**: `DELETE FROM table_name WHERE condition;`
  - There’s no direct equivalent to `discard()` in SQL, but a `DELETE` without a match simply does nothing.

### 4. **Union**
- **Python**: `union(*others)` combines two or more sets, removing duplicates.
- **SQL**: The equivalent operation in SQL is the `UNION` or `UNION ALL` operator.
  - **SQL**: `SELECT * FROM table1 UNION SELECT * FROM table2;`
  - `UNION` removes duplicates, while `UNION ALL` keeps duplicates.

### 5. **Intersection**
- **Python**: `intersection(*others)` returns the common elements between sets.
- **SQL**: The equivalent in SQL is using `INTERSECT`.
  - **SQL**: `SELECT * FROM table1 INTERSECT SELECT * FROM table2;`
  - This gives the common rows between the two result sets.

### 6. **Difference**
- **Python**: `difference(*others)` returns elements present in the first set but not in others.
- **SQL**: The equivalent in SQL is using a `LEFT JOIN` or `EXCEPT`.
  - **SQL**: `SELECT * FROM table1 EXCEPT SELECT * FROM table2;`
  - This returns rows that are in `table1` but not in `table2`.

### 7. **Symmetric Difference**
- **Python**: `symmetric_difference(other)` returns elements that are in either set, but not in both.
- **SQL**: There’s no direct SQL function for symmetric difference, but you can combine `EXCEPT` and `UNION`.
  - **SQL**:
    ```sql
    (SELECT * FROM table1 EXCEPT SELECT * FROM table2)
    UNION
    (SELECT * FROM table2 EXCEPT SELECT * FROM table1);
    ```

### 8. **Subset and Superset**
- **Python**: `issubset(other)` checks if one set is a subset of another; `issuperset(other)` checks if one set is a superset of another.
- **SQL**: This concept is typically handled with `NOT EXISTS` or `EXISTS` combined with a `SELECT` query.
  - **SQL (Subset)**: `SELECT * FROM table1 WHERE NOT EXISTS (SELECT * FROM table2 WHERE table2.column = table1.column);`
  - **SQL (Superset)**: You can check if all rows from one table exist in another with a query like this:
    ```sql
    SELECT * FROM table1 WHERE NOT EXISTS (
      SELECT * FROM table2 WHERE table2.column = table1.column
    );
    ```

### 9. **Disjoint Sets**
- **Python**: `isdisjoint(other)` checks if two sets have no elements in common.
- **SQL**: This can be done with the `NOT EXISTS` operator to check if there's no intersection between two sets.
  - **SQL**:
    ```sql
    SELECT * FROM table1 WHERE NOT EXISTS (
      SELECT * FROM table2 WHERE table2.column = table1.column
    );
    ```
  - If no results are returned, the sets are disjoint.

### 10. **Copying a Set**
- **Python**: `copy()` creates a shallow copy of the set.
- **SQL**: In SQL, copying data can be done with `INSERT INTO` and a `SELECT` query.
  - **SQL**: `INSERT INTO table2 (column1, column2) SELECT column1, column2 FROM table1;`

### 11. **Set Size**
- **Python**: `len(set)` returns the number of elements in a set.
- **SQL**: The equivalent in SQL is using the `COUNT()` function.
  - **SQL**: `SELECT COUNT(*) FROM table_name;`

### 12. **Checking Membership**
- **Python**: `in` checks if an element is in the set.
- **SQL**: `IN` is used to check membership in a list or subquery.
  - **SQL**: `SELECT * FROM table_name WHERE column_name IN (value1, value2, value3);`

### Example SQL Queries with Set Operations:

#### **Union**
```sql
SELECT * FROM table1
UNION
SELECT * FROM table2;
```

#### **Intersection**
```sql
SELECT * FROM table1
INTERSECT
SELECT * FROM table2;
```

#### **Difference**
```sql
SELECT * FROM table1
EXCEPT
SELECT * FROM table2;
```

#### **Symmetric Difference**
```sql
(SELECT * FROM table1 EXCEPT SELECT * FROM table2)
UNION
(SELECT * FROM table2 EXCEPT SELECT * FROM table1);
```

#### **Checking if Subset**
```sql
SELECT * FROM table1 WHERE NOT EXISTS (
  SELECT * FROM table2 WHERE table2.column = table1.column
);
```

These SQL operations correspond to the basic set operations available in Python. SQL is essentially designed to work with sets of data, and many of the same principles apply!

'''



a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
# a != b
# so answer should be: Jake, Eric
print(a.difference(b))

c = ["Jake", "John", "Eric"]
d = ["John", "Jill"]

C = set(c)
D = set(d)

print(C.difference(D))