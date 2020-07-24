Databases


Databases are programs that store and maintain data.


Types of Databases:

- Relational databases

- File systems

- Non-relational databases 

- Heirarchal databases


Relational Databases store data in the form of Tables, and then maintains the relationship
among the tables.


Relationships between tables are important, since we can relate and join different tables based
on similar columns.

When there is a relationship between two tables, it's called a RDMS - Relational Database Management System.


SQL - Structured Query Language

- Perform Create, Read, Update, and Delete operations on tables


Databases allow many people to access and edit data at the same time.


Aggregation

- takes several rows and summarizes them into a single row


Common Aggregation Functions in SQL 


COUNT

- the number of rows

AVG

- the average

MAX

- the max

MIN 

- the min 

SUM 

- the sum 


SELECT Queries

- Fetch data out of the database

SELECT <column> FROM <table> WHERE <condition>

The result will be a table with one column (<column>), and the rows which meet the condition.

We can rename the column using 'AS'.

SELECT <column> AS <new-column> FROM <table> WHERE <condition> 

We can also select multiple columns

SELECT <column-1> AS <new-column-1>, <column-2> AS <new-column-2>, FROM <table> WHERE <condition> 


Related Tables and JOIN 

- When two tables have common data with the same meaning (eg. common Item IDs), they can be joined

Example

Table 1 - categories

id  name    type

1   Apple   Fruit
2   Orange  Fruit
3   Bread   Grain

Table 2 - location

left-isle  right-isle    most-popular

1           2            2
1           3            1
2           3            2

We could join these two tables to get a new table, such as:

left-isle  right-isle    most-popular

Apple      Orange        Orange
Apple      Bread         Apple
Orange     Bread         Orange


Example 2 - Say we had another table 

Table 3 - health-impact

type    base-price    causes-diabetes

Grain   5              Yes
Fruit   7              No

We could join the 'categories' table with the 'health-impact' table to get:

id  name    type    causes-diabetes

1   Apple   Fruit   No
2   Orange  Fruit   Yes
3   Bread   Grain   No

Using the following join query:

SELECT
    categories.name
    categories.type
    health-impact.causes-diabetes

    FROM categories JOIN health-impact
        ON categories.type =
            health-impact.type;

We can also apply WHERE clauses to these new tables. For example, if we only want the types that cause diabetes,
we could use:

SELECT
    categories.name
    categories.type
    health-impact.causes-diabetes

    FROM categories JOIN health-impact
        ON categories.type =
            health-impact.type
        WHERE causes-diabetes = 'YES'

Unique Identifiers called Primary Keys are given to rows in databases to distinguish entries.


Minimal and Non-Minimal Candidate Keys

A superkey is a set of attributes within a table whose values can be used to uniquely
identify a tuple. A candidate key is a minimal set of attributes necessary to identify
a tuple; this is also called a minimal superkey. Given an employee schema consisting
of the attributes employeeID, name, job, and departmentID, where no value in the
employeeID attribute is ever repeated, we could use the employeeID in combination
with any or all other attributes of this table to uniquely identify a tuple in the
table. Examples of superkeys in this schema would be:

{employeeID, Name}, {employeeID, Name, job}, and {employeeID, Name, job, departmentID}
 
The last example is known as trivial superkey, because it uses all attributes of this
table to identify the tuple.

In a real database we do not need values for all of those attributes to identify a
tuple. We only need, per our example, the set {employeeID}.

This is a minimal superkey—that is, a minimal set of attributes that
can be used to identify a single tuple. employeeID is a candidate key.