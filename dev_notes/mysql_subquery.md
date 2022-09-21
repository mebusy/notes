...menustart

- [Mysql SubQuery](#a101a8d7738f063d1d49004a43b7a86f)
    - [Scalar Subquery](#27a7afaf078ad5a7de12c2991e900e31)
    - [Multiple row Subquery](#d10dd98dd93c479b1064b7ef27c80ad0)
        - [multiple rows and multiple columns](#6cee8944a69e5a841ff3c73052c30c3b)
        - [multiple rows , but single columns](#ca1a624f1891364dc5965442aff0564a)
    - [Correlated Subquery](#02e03046079cab57176425349a6f3032)
    - [With Clause](#68eadeedf129085779b3676895d18c57)
    - [Use sub-query in `SELECT` clause](#81e8ded1361f12f673dc6ec8222a0048)
    - [Use sub-query in `HAVING` clause](#bf0acc0d777390e702fa05c6915669a1)

...menuend


<h2 id="a101a8d7738f063d1d49004a43b7a86f"></h2>


# Mysql SubQuery


- Different Types of Subqueries
    - Scalar Subquery
    - Multiple row Subquery
    - Correlated Subquery
- SubQuery can be used in SELECT command
    - SELECT 
    - FROM
    - WHERE
    - HAVING
- also in other COMMANDs
    - INSERT
    - UPDATE
    - DELETE


<h2 id="27a7afaf078ad5a7de12c2991e900e31"></h2>


## Scalar Subquery

- always return just **1 row and 1 column**
- example: subquery in **where**
    - find the employees whose salary is more than the average salary earned by all employees
    ```sql
    select * -- outer query / main query
    from employee
    where salary > ( select avg(salary) from employee ) ;  -- subquery / inner query
    ```
- subquery in **join** condition
    ```sql
    select *
    from employee e
    join ( select avg(salary) from employee ) avg_sal
        on e.salary > avg_sal.sal ;
    ```

<h2 id="d10dd98dd93c479b1064b7ef27c80ad0"></h2>


## Multiple row Subquery

- will return multiple rows, or multiple columns

<h2 id="6cee8944a69e5a841ff3c73052c30c3b"></h2>


### multiple rows and multiple columns

- Question: find the employees(full row) who earn the highest salary in each department
    ```sql
    select * 
    from employee
    where (dept_name, salary) in (  select dept_name, max(salary)
                                    from employee
                                    group by dept_name ) ;
    ```
- tips: 
    - multiple column comparsion `(dept_name, salary) in`
    - use `=` if the right hand side returns a single row `(dept_name, salary) in` 


<h2 id="ca1a624f1891364dc5965442aff0564a"></h2>


### multiple rows , but single columns

- Question: find department who do not have any employees
    ```sql
    select *
    from department
    where dept_name not in ( select distinct dept_name from employee )
    ```


<h2 id="02e03046079cab57176425349a6f3032"></h2>


## Correlated Subquery

- a subquery which is related to the outer query
    - so far, the subqueries we saw do not depend on any other query , and it will execute the subquery just once. 
    - but when it comes to a correlated subquery it's going to be slightly different.
    - for every single record that is processed from the outer query, the correlated subquery will be executed.
- Question: find the employees in each department who earn more than the average salary in that department
    - *you can actually solve it by using `groupby`, but here we're going to use correlated subquery.*
    ```sql
    select *
    from employee e1
    from salary > ( select avg(salary) 
                    from employee e2
                    where e2.dept_name = e1.dept_name  )
    ```
    - note: this subquery will be executes *n* times,  where n = #rows in employee table

- Question: find department who do not have any employees
    ```sql
    select *
    from department d
    where not exists ( select 1 from employee e where e.dept_name = d.dept_name ) ;
    ```

<h2 id="68eadeedf129085779b3676895d18c57"></h2>


## With Clause

```sql
with sales as ( select store_name, sum(price) as total_sales
            from sales
            group by store_name)
select * 
from sales
where ....
```



<h2 id="81e8ded1361f12f673dc6ec8222a0048"></h2>


## Use sub-query in `SELECT` clause

```sql
select id, IFNULL( (select avatar_frame from pvp_avatarframe_hsw where pvp_avatarframe_hsw.uuid = pvp_hsw.uuid ) , avatar_frame ) as avatarframe from pvp_hsw where uuid = ?
```


```sql
select COALESCE( sum(orderAmount), 0 )  from payment_vivosdk   
where 
    uuid="test-User-0" and 
    paidtime >= ( select COALESCE( AVG(startTime), -1) from tbl_rechargeAcc where activity_kind = 2 and endTime > 969393337  ) and 
    paidtime <= ( select COALESCE( AVG(deadline),  -1) from tbl_rechargeAcc where activity_kind = 2 and endTime > 969393337  ) 
```


```sql
select *,
    (case when salary > (select avg(salary) from employee)
        then 'Higher than average'
        else null
     end ) as remarks
from employee ;

-- emp_id | emp_name | dept_name | salary | remarks
```

You can always find alternative ways to remove the subquery in select clause, e.g. JOIN clause


<h2 id="bf0acc0d777390e702fa05c6915669a1"></h2>


## Use sub-query in `HAVING` clause

```sql
select store_name, sum(quantity)
from sales
group by store_name
having sum(quantity) > ( select avg(quantity) from sales ) ;
```



