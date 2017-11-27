
# Advanced Pandas

## Merging Dataframes

```python
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')
print(staff_df.head())
print()
print(student_df.head())

                 Role
Name
Kelly  Director of HR
Sally  Course liasion
James          Grader

            School
Name
James     Business
Mike           Law
Sally  Engineering
```

```python
# UNION 
pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)
        Role            School
Name        
James   Grader          Business
Kelly   Director of HR  NaN
Mike    NaN             Law
Sally   Course liasion  Engineering

# Intersection
        Role            School
Name
James   Grader          Business
Sally   Course liasion  Engineering
```

```python
# set addition 集合加法
# we want the list of all staff
# if they were students, we want to 
# get the student details as well
pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True)
        Role            School
Name
Kelly   Director of HR  NaN
Sally   Course liasion  Engineering
James   Grader          Business

# Right join
pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True)
        Role            School
Name
James   Grader          Business
Mike    NaN             Law
Sally   Course liasion  Engineering
```

 - The merge method has a couple of other interesting parameters. 
    - First, you don't need to use indices to join on, you can use columns as well.

```python
staff_df = staff_df.reset_index()
student_df = student_df.reset_index()
pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')

    Name    Role            School
0   Kelly   Director of HR  NaN
1   Sally   Course liasion  Engineering
2   James   Grader          Business
```

 - What happens when we have conflicts between the DataFrames?

```python
# staff and student has different "Location"
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])
pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')

# Pandas will appends an _x or _y to help differentiate 
    Location_x          Name    Role            Location_y              School
0   State Street        Kelly   Director of HR  NaN                     NaN
1   Washington Avenue   Sally   Course liasion  512 Wilson Crescent     Engineering
2   Washington Avenue   James   Grader          1024 Billiard Avenue    Business
```

 - multi-indexing and multiple columns. 

```python
staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'}])
pd.merge(staff_df, student_df, how='inner', left_on=['First Name','Last Name'], right_on=['First Name','Last Name'])

    First Name  Last Name   Role    School
0   Sally   Brooks  Course liasion  Engineering
```


