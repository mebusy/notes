
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

## Multiple row Subquery

- will return multiple rows, or multiple columns

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


### multiple rows , but single columns

- Question: find department who do not have any employees
    ```sql
    select *
    from department
    where dept_name not in ( select distinct dept_name from employee )
    ```


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

## With Clause

```sql
with sales as ( select store_name, sum(price) as total_sales
            from sales
            group by store_name)
select * 
from sales
where ....
```



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


## Use sub-query in `HAVING` clause

```sql
select store_name, sum(quantity)
from sales
group by store_name
having sum(quantity) > ( select avg(quantity) from sales ) ;
```



