# PostgreSQL

# SQL
## DDL (Data Definition Language)
* Create
* Alter
* Drop

## DML (Data Manipulation Language)
* Insert
* Updata
* Delete
* Select

### Insert
The PostgreSQL INSERT statement allows you to insert a new row into a table.

Here’s the basic syntax of the INSERT statement:

```sql INSERT INTO table1(column1, column2, …)
VALUES (value1, value2, …);```

In this syntax:

First, specify the name of the table (table1) that you want to insert data after the INSERT INTO keywords and a list of comma-separated columns (colum1, column2, ....).
Second, supply a list of comma-separated values in parentheses (value1, value2, ...) after the VALUES keyword. The column and value lists must be in the same order.

### Update
The PostgreSQL UPDATE statement allows you to update data in one or more columns of one or more rows in a table.

Here’s the basic syntax of the UPDATE statement:

```sql
UPDATE table_name
SET column1 = value1,
    column2 = value2,
    ...
WHERE condition;
In this syntax:
```

First, specify the name of the table that you want to update data after the UPDATE keyword.
Second, specify columns and their new values after SET keyword. The columns that do not appear in the SET clause retain their original values.
Third, determine which rows to update in the condition of the WHERE clause.

### Delete
The PostgreSQL DELETE statement allows you to delete one or more rows from a table.

The following shows the basic syntax of the DELETE statement:

```sql
DELETE FROM table_name
WHERE condition;
```

In this syntax:

First, specify the name (table_name) of the table from which you want to delete data after the DELETE FROM keywords.
Second, specify a condition in the WHERE clause to determine which rows to delete.
The WHERE clause is optional. If you omit the WHERE clause, the DELETE statement will delete all rows in the table.

The DELETE statement returns the number of rows deleted. It returns zero if the DELETE statement did not delete any row.
