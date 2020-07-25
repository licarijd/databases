Database Management System Theory 


Indexing 

Indexes are used to speed-up query process in SQL Server, resulting in high performance.
They are similar to textbook indexes. In textbooks, if you need to go to a particular chapter,
you go to the index, find the page number of the chapter and go directly to that page. Without indexes,
the process of finding your desired chapter would have been very slow.

The same applies to indexes in databases. Without indexes, a DBMS has to go through all the records in the
table in order to retrieve the desired results. This process is called table-scanning and is extremely slow.
On the other hand, if you create indexes, the database goes to that index first and then retrieves the
corresponding table records directly.

There are two types of Indexes in SQL Server:

1) Clustered Index

2) Non-Clustered Index


Clustered Indexes 

Clustered indexes sort and store the data rows in the table or view based on their key values.
These are the columns included in the index definition. There can be only one clustered index per table,
because the data rows themselves can be stored in only one order.  

The only time the data rows in a table are stored in sorted order is when the table contains a
clustered index. When a table has a clustered index, the table is called a clustered table.
If a table has no clustered index, its data rows are stored in an unordered structure called a heap.


Non-Clustered Indexes 

A nonclustered index is a data structure that improves the speed of data retrieval from tables.
Unlike a clustered index, a nonclustered index sorts and stores data separately from the data rows
in the table. It is a copy of selected columns of data from a table with the links to the associated table.

Similar to a clustered index, a nonclustered index uses the B-tree structure to organize its data.

A table may have one or more nonclustered indexes and each non-clustered index may include one or more
columns of the table.

** For more information on Indexes, see https://docs.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described?view=sql-server-ver15
and https://www.sqlservertutorial.net/sql-server-indexes/sql-server-create-index/

B- Trees 

In computer science, a B-tree is a self-balancing tree data structure that maintains sorted data
and allows searches, sequential access, insertions, and deletions in logarithmic time.
The B-tree generalizes the binary search tree, allowing for nodes with more than two children.
Unlike other self-balancing binary search trees, the B-tree is well suited for storage systems
that read and write relatively large blocks of data, such as discs. It is commonly used in
databases and file systems.

B+ Trees and Indexing 

A B+ tree is an m-ary tree with a variable but often large number of children per node.
A B+ tree consists of a root, internal nodes and leaves. The root may be either a leaf or a node with two or
more children.

A B+ tree can be viewed as a B-tree in which each node contains only keys (not key–value pairs),
and to which an additional level is added at the bottom with linked leaves.

The primary value of a B+ tree is in storing data for efficient retrieval in a block-oriented
storage context — in particular, filesystems. This is primarily because unlike binary search trees,
B+ trees have very high fanout (number of pointers to child nodes in a node,
typically on the order of 100 or more), which reduces the number of I/O operations required to find
an element in the tree.

Thus, B+ Tree Indexes are the most common index type.

The ReiserFS, NSS, XFS, JFS, ReFS, and BFS filesystems all use this type of tree for metadata indexing;
BFS also uses B+ trees for storing directories. NTFS uses B+ trees for directory and security-related
metadata indexing. EXT4 uses extent trees (a modified B+ tree data structure) for file extent indexing.


Decomposition

Decomposition in Database Management Systems removes redundancy, anomalies and inconsistencies
from a database by dividing the table into multiple tables.


Lossless Decomposition

Decomposition is lossless if it is feasible to reconstruct relation R from decomposed tables using Joins.
This is the preferred choice. The information will not lose from the relation when decomposed.
The join would result in the same original relation.


ACID 

ACID (atomicity, consistency, isolation, durability) is a set of properties of database transactions intended
to guarantee validity even in the event of errors, power failures, etc.


Atomicity 

An atomic transaction is an indivisible and irreducible series of database operations such that either all
occur, or nothing occurs. A guarantee of atomicity prevents updates to the database occurring only
partially, which can cause greater problems than rejecting the whole series outright. As a consequence,
the transaction cannot be observed to be in progress by another database client. At one moment in time,
it has not yet happened, and at the next it has already occurred in whole (or nothing happened if the
transaction was cancelled in progress).

Atomicity as a concept is also discussed in the Concurrency repo.


Consistency 

Consistency in database systems refers to the requirement that any given database transaction must
change affected data only in allowed ways. Any data written to the database must be valid according
to all defined rules, including constraints, cascades, triggers, and any combination thereof.
This does not guarantee correctness of the transaction in all ways the application programmer
might have wanted (that is the responsibility of application-level code) but merely that any programming
errors cannot result in the violation of any defined database constraints.


Isolation 

In a database system where more than one transaction are being executed simultaneously and
in parallel, the property of isolation states that all the transactions will be carried out
and executed as if it is the only transaction in the system. No transaction will affect the existence
of any other transaction.


Durability 

In database systems, durability is the ACID property which guarantees that transactions that have committed
will survive permanently. For example, if a flight booking reports that a seat has successfully been booked,
then the seat will remain booked even if the system crashes.

Durability can be achieved by flushing the transaction's log records to non-volatile storage before acknowledging
commitment.


Serial and Serializable Schedules 

When multiple transactions are being executed by the operating system in a multiprogramming environment,
there are possibilities that instructions of one transactions are interleaved with some other transaction.


Schedule

A chronological execution sequence of a transaction is called a schedule. A schedule can have many transactions
in it, each comprising of a number of instructions/tasks.


Serial Schedule 

In a Serial Schedule, transactions are aligned in such a way that one transaction is executed first.
When the first transaction completes its cycle, then the next transaction is executed. Transactions
are ordered one after the other. This type of schedule is called a serial schedule, as transactions are
executed in a serial manner.

A schedule is called serializable whenever executing the transactions sequentially, in some order,
could have left the database in the same state as the actual schedule.


Serial Schedule Example 

T1:                     T2:

R(A) // Read A
A:= A + 100 // Write A 
R(B)
B:= B + 100

                        R(A)
                        A:= A x 2
                        R(B)
                        B:= B x 2


If there is interleaving of operations between transactions, then a schedule is not serial:

T1:                     T2:

R(A) // Read A
A:= A + 100 // Write A 

                        R(A)
                        A:= A x 2

R(B)
B:= B + 100

                        R(B)
                        B:= B x 2


However, the above schedule is serializable (the schedule is equivalent to the same 
serial execution of transaction, in the first example).
                    

In a multi-transaction environment, serial schedules are considered as a benchmark. The execution sequence of an
instruction in a transaction cannot be changed, but two transactions can have their instructions executed in a
random fashion. This execution does no harm if two transactions are mutually independent and working on different
segments of data; but in case these two transactions are working on the same data, then the results may vary.
This ever-varying result may bring the database to an inconsistent state.

To resolve this problem, we allow parallel execution of a transaction schedule, if its transactions are
either serializable or have some equivalence relation among them.


Result Equivalence

If two schedules produce the same result after execution, they are said to be result equivalent.
They may yield the same result for some value and different results for another set of values.
That's why this equivalence is not generally considered significant.


View Equivalence

Two schedules would be view equivalent if the transactions in both the schedules perform similar
actions in a similar manner.

For example, if S1 and S2 are schedules, and T is a transaction:

- if T reads the initial data in S1, then it also reads the initial data in S2

- if T reads the value written by J in S1, then it also reads the value written by J in S2

- if T performs the final write on the data value in S1, then it also performs the final write
on the data value in S2


Conflict Equivalence

Two schedules would be conflicting if they have the following properties:

- both belong to separate transactions

- both accesses the same data item

- at least one of them is "write" operation

Two schedules having multiple transactions with conflicting operations are said to
be conflict equivalent if and only if:

- both the schedules contain the same set of Transactions

- the order of conflicting pairs of operations is maintained in both the schedules


View equivalent schedules are view serializable and conflict equivalent schedules are
conflict serializable. All conflict serializable schedules are view serializable too.
Every conflict serializable schedule is serializable.


Example - Conflict Serializable 

R1(A); W1(A); R2(A); W2(A); R1(B); W1(B); R2(B); W2(B)

- can we transform this non-serial schedule into a serial schedule by swapping non-conflicting 
actions? Yes!

R1(A); W1(A); R1(B); W1(B); R2(A); W2(A); R2(B); W2(B)

- out above achieves the same order of conflicting operations 


Example 2 - Conflict Serializable 

R2(A); R1(B); W2(A); R3(A); W1(B); W3(A); R2(B); W2(B)

We can first let T1 modify B, then let T2 run.

Then we can let T2 modify A, and let T3 run.

State T1 ---  B  ---> State T2 ---  A  ---> State T3


Example - Non-Conflict Serializable 

R2(A); R1(B); W2(A); R3(A); W1(B); W3(A); R2(B); W2(B)

-> In this case, the output of T1 is dependent on T2 and vice versa

___________
|         |
|         |
v         v
T1 - B -> T2 - A -> T3


Strict Schedules 

A scheudle S is strict if a value written by Ti is not read or overwritten by a following transaction Tj 
until Ti aborts or commits (supports Atomicity).


Example of a Strict Schedule:

W1(A); W1(B); commit1; W2(A); R2(B); commit2;

Strict Schedules are recoverable, and avoid cascading aborts.

The Scheduler is the module that schedules the transaction's actions and ensures serializability, 
using locks and timestamps.


Lock Based Concurrency Model 

Database Management Systems aim to only allow recoverable and serializable schedules 

- this ensures that committed transactions are not un-done while aborting other transactions

- locking protocols are used (locks control concurrent access to a data object)


Locking Scheduler 

- each element has a lock 

- transaction must first acquire the lock before reading/writing that element 

- if the lock is taken by another transaction, wait 

- the transaction must release the lock 


Locking Scheduler Example 

** Notation:

Li(A) = transaction Ti acquires lock for element A 

Ui(A) = transaction Ti releases lock for element A 


T1                  T2 

L1(A)
R1(A) W1(A)
U1(A) L1(B)

                    L2(A)
                    R2(A) W2(A)
                    U2(A)
                    L2(B)  DENIED // The scheduler has enforced conflict serializability, we need to U1(B) first 

R1(B) W1(B)
U1(B)

                    GRANTED:
                    R2(B), W2(B)
                    U2(B)


Types of Locks 

Shared Locks - for reading 

Exclusive Locks - for writing (and reading)


Strict 2-Phase Locking 

There are 2 rules for strict 2-phase locking:

1) Each action must obtain a shared lock on an object before reading, and an exclusive lock 
before writing.

2) All locks held by a transaction are released when the transaction is complete.

** This is only allowed for serializable graphs!


** A schedule is not serializable if one transaction reads another's dirty data (uncommitted data)

** for a schedule to be serializable, the outcome must be equal to each transaction running serially in 
the same order 


Normalization and Normal Forms 

The process of converting a schema to normal form is called normalization.


1st Normal Form (1NF)

- no multi values in an attribute, eg.

course(name, instructor, [student, email])


2nd Normal Form (2NF)

- needs to be a subset of 1NF 

- and, the primary key of the table should compose of exactly 1 column 

Counter Example:

Movies(title, year, star, studio, sudioAddress, salary)

Counter Example:

Student name	Course code
Rahul           CS152
Rajat	        CS101
Rahul	        CS154
Raman	        CS101

Neither column is unique; we don't have a primary key of 1 column.

To put this into 2NF, we can break it into 2 tables:

Student name	Enrolment number
Rahul	        1
Rajat	        2
Raman	        3

Course code	    Enrolment number
CS101	        2
CS101	        3
CS152	        1
CS154	        1


3rd Normal Form (3NF)

- needs to be a subset of 2NF 

- there should not be any functional dependency

Column A is said to be functionally dependent on column B if changing the value of A may require a
change in the value of B. As an example, consider the following table:

Course code	        Course venue	        Instructor's name	            Department
MA214	            Lecture Hall 18	        Prof. George	                CS Department
ME112	            Auditorium building	    Prof. John	                    Electronics Department

Here, the department column is dependent on the professor name column.
This is because if in a particular row, we change the name of the professor,
we will also have to change the department value. 

This is not desirable since someone who is updating the database may remember to change
the name of the professor, but may forget updating the department value. This can cause
inconsistency in the database.

Third normal form avoids this by breaking this into separate tables:

Course code	        Course venue	        Instructor's ID
MA214	            Lecture Hall 18	        1
ME112	            Auditorium building	    2

Instructor's ID	    Instructor's Name	    Department
1	                Prof. Ronald	        Mathematics Department
2	                Prof. John	            Electronics Department


Boyce-Codd Normal Form (BCNF)

Boyce-Codd Normal form is a stronger generalization of third normal form. A table is in Boyce-Codd Normal
form if and only if at least one of the following conditions are met for each functional dependency A → B:

- A is a superkey 

- it is a trivial functional dependency 

Example:

Course code	        Course venue	        Instructor Name	        Instructor’s phone number
CS101	            Lecture Hall 20	        Prof. George	        +1 6514821924
CS152	            Lecture Hall 21	        Prof. Atkins	        +1 6519272918
CS154	            CS Auditorium	        Prof. George	        +1 6514821924

Here, the first column (course code) is unique across various rows. So, it is a superkey. Consider
the combination of columns (course code, professor name). It is also unique across various rows.
So, it is also a superkey. A superkey is basically a set of columns such that the value of that set
of columns is unique across various rows. That is, no 2 rows have the same set of values for those columns.
Some of the superkeys for the table above are:

Course code
Course code, professor name
Course code, professor mobile number

A superkey whose size (number of columns) is the smallest is called as a candidate key. For instance, the first superkey above has just 1 column. The second one and the last one have 2 columns. So, the first superkey (Course code) is a candidate key.

Boyce-Codd Normal Form says that if there is a functional dependency A → B, then either A is a superkey or
it is a trivial functional dependency. A trivial functional dependency means that all columns of B are
contained in the columns of A. For instance, (course code, professor name) → (course code) is a trivial
functional dependency because when we know the value of course code and professor name, we do know the
value of course code and so, the dependency becomes trivial.


** More on Normalization: https://hackr.io/blog/dbms-normalization