[](...menustart)

- [Advanced Pandas](#adf4334b9c5df6b20ed4f5f5e20bb7a0)
    - [Merging Dataframes](#ee2aad0e21ce73c25e8bcddcd01d1426)
    - [Pandas Idioms](#4c7fe48a07b6ad92d0c079eccc80142d)
        - [apply function](#6255c3e0f88024e53b86048db1711cc1)
    - [Group by](#be87d8c3de2675bbc53f9442af9d8feb)
        - [aggregate](#39adbeb6bc21a3133e5fdcf1ec05d1a0)
    - [Scales](#34da875e03f8175113bd901cb46c2945)
    - [Pivot Tables](#2df968ba4419f25ab2e5bbeaee9eacc3)
    - [Date Functionality](#124cf81690d7ad3c6cb1a8e2572c30b7)
        - [Timestamp](#a3d5de3eac8bb00ae86fd1a1005f1500)
        - [Period](#1901606ea069a83dc7beea17881ef95a)
        - [DatetimeIndex](#31c3ed93084fde1e4cfb189455db3ae0)
        - [PeriodIndex](#3e4d11c471477ea15990deaf351ecbe2)
        - [Converting to Datetime](#e5e5d211bc65027dfbc69a0ab7b42824)
        - [Timedeltas](#345b4ea198c499ed502b17952e076b36)
        - [Working with Dates in a Dataframe](#ee353674a132153d42025f4ba3237d30)

[](...menuend)


<h2 id="adf4334b9c5df6b20ed4f5f5e20bb7a0"></h2>

# Advanced Pandas

<h2 id="ee2aad0e21ce73c25e8bcddcd01d1426"></h2>

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
pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True)

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

--- 

<h2 id="4c7fe48a07b6ad92d0c079eccc80142d"></h2>

## Pandas Idioms

- Chain Inexing :
    - `df.loc["Washtenaw"]["Total Population"]` 
    - Generally bad, pandas could return a copy of a view depending upon numpy
- Code smell
    - if you see a `][` , you should think carefully about what you are doing 
- Method chaining
    - Method chaining though, little bit different. 
    - The general idea behind method chaining is that every method on an object returns a reference to that object. 
    - The beauty of this is that you can condense many different operations on a DataFrame, for instance, into one line or at least one statement of code.

```python
# Pandorable code
(df.where(df['SUMLEV']==50)
    .dropna()
    .set_index(['STNAME','CTYNAME'])
    .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}))

# NOT Pandorable
df = df[df['SUMLEV']==50]
df.set_index(['STNAME','CTYNAME'], inplace=True)
df.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})
```

<h2 id="6255c3e0f88024e53b86048db1711cc1"></h2>

### apply function

- apply something to all rows

```python
import numpy as np
def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    return pd.Series({'min': np.min(data), 'max': np.max(data)})

# use lambda
rows = ['POPESTIMATE2010',
        'POPESTIMATE2011',
        'POPESTIMATE2012',
        'POPESTIMATE2013',
        'POPESTIMATE2014',
        'POPESTIMATE2015']
df.apply(lambda x: np.max(x[rows]), axis=1)

```

<h2 id="be87d8c3de2675bbc53f9442af9d8feb"></h2>

## Group by

- takes some column name or names and splits the dataframe up into chunks based on those names, it returns a dataframe group by object. 
    - 非常适合需要对部分数据进行统计的情形

```python
for group, frame in df.groupby('STNAME'):
    print( group  )

Alabama
Alaska
Arizona
Arkansas
California
Colorado
...

 SUMLEV  REGION  DIVISION  STATE  COUNTY   STNAME            CTYNAME  \
1       50       3         6      1       1  Alabama     Autauga County
2       50       3         6      1       3  Alabama     Baldwin County
3       50       3         6      1       5  Alabama     Barbour County
4       50       3         6      1       7  Alabama        Bibb County
5       50       3         6      1       9  Alabama      Blount County
6       50       3         6      1      11  Alabama     Bullock County
...
```


- Now, 99% of the time, you'll use group by on one or more columns. 
    - But you can actually provide a function to group by as well and use that to segment your data. 
    - eg. you may want to handle 1/3 data each time

```python
df = df.set_index('STNAME')

def fun(item):
    if item[0]<'M':
        return 0
    if item[0]<'Q':
        return 1
    return 2

for group, frame in df.groupby(fun):
    print('There are ' + str(len(frame)) + ' records in group ' + str(group) + ' for processing.')
```


<h2 id="39adbeb6bc21a3133e5fdcf1ec05d1a0"></h2>

### aggregate

- A common work flow with group by that you split your data, you apply some function, then you combine the results. 
    - This is called split apply combine pattern. 
    - And we've seen the splitting method, but what about apply? 
        - the groupby object also has a method called `agg` which is short for aggregate. 
        - This method applies a function to the column or columns of data in the group, and returns the results. 

```python
df = pd.read_csv('census.csv')
df = df[df['SUMLEV']==50]

df.groupby('STNAME').agg({'CENSUS2010POP': np.average})

    CENSUS2010POP
STNAME
Alabama 71339.343284
Alaska  24490.724138
Arizona 426134.466667
Arkansas    38878.906667
California  642309.586207
...
```

- while much of the documentation and examples will talk about a single groupby object, there's really two different objects. 
    - The data frame groupby and the series groupby. 
    - And these objects behave a little bit differently with aggregate. 

```python
print(type(df.groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']))
print(type(df.groupby(level=0)['POPESTIMATE2010']))

<class 'pandas.core.groupby.DataFrameGroupBy'>
<class 'pandas.core.groupby.SeriesGroupBy'>

(df.set_index('STNAME').groupby(level=0)['CENSUS2010POP']
    .agg({'avg': np.average, 'sum': np.sum}))
        avg             sum
STNAME      
Alabama 71339.343284    4779736
Alaska  24490.724138    710231
...


(df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']
    .agg({'avg': np.average, 'sum': np.sum}))

            avg                              sum
        POPESTIMATE2010 POPESTIMATE2011 POPESTIMATE2010 POPESTIMATE2011
STNAME              
Alabama 71420.313433    71658.328358    4785161 4801108
Alaska  24621.413793    24921.379310    714021  722720
Arizona 427213.866667   431248.800000   6408208 6468732

```

<h2 id="34da875e03f8175113bd901cb46c2945"></h2>

## Scales

- Q: try casting this series to categorical with the oridering Low < Medium < High

```python
s = pd.Series(['Low', 'Low', 'High', 'Medium', 'Low', 'High', 'Low'])
s.astype('category', categories=['Low', 'Medium', 'High'], ordered=True)
0   Low
1   Low
2   High
3   Medium
4   Low
5   High
6   Low
dtype: category
Categories (3, object) : [Low < Medium < High ]
```

- `pd.cut` can bin your data into bins

```python
s = pd.Series([168, 180, 174, 190, 170, 185, 179, 181, 175, 169, 182, 177, 180, 171])
pd.cut(s, 3)
0     (167.978, 175.333]
1     (175.333, 182.667]
2     (167.978, 175.333]
3         (182.667, 190]
4     (167.978, 175.333]
5         (182.667, 190]
6     (175.333, 182.667]
7     (175.333, 182.667]
8     (167.978, 175.333]
9     (167.978, 175.333]
10    (175.333, 182.667]
11    (175.333, 182.667]
12    (175.333, 182.667]
13    (167.978, 175.333]
dtype: category
Categories (3, object): [(167.978, 175.333] < (175.333, 182.667] < (182.667, 190]]


# You can also add labels for the sizes [Small < Medium < Large].
pd.cut(s, 3, labels=['Small', 'Medium', 'Large'])
0      Small
1     Medium
2      Small
3      Large
4      Small
5      Large
6     Medium
7     Medium
8      Small
9      Small
10    Medium
11    Medium
12    Medium
13     Small
dtype: category
Categories (3, object): [Small < Medium < Large]
```

<h2 id="2df968ba4419f25ab2e5bbeaee9eacc3"></h2>

## Pivot Tables

- A pivot table is a way of summarizing data in a data frame for a particular purpose. 
    - It makes heavy use of the aggregation function. 
- A pivot table is itself a data frame, where the rows represent one variable that you're interested in, the columns another, and the cell's some aggregate value. 
- A pivot table also tends to includes marginal values as well, which are the sums for each column and row.

```python
#http://open.canada.ca/data/en/dataset/98f1a129-f628-4ce4-b24d-6f16bf24dd64
df = pd.read_csv('cars.csv')
df.head()
    YEAR    Make    Model   Size    (kW)    Unnamed: 5  TYPE    CITY (kWh/100 km)   HWY (kWh/100 km)    COMB (kWh/100 km)   CITY (Le/100 km)    HWY (Le/100 km) COMB (Le/100 km)    (g/km)  RATING  (km)    TIME (h)
0   2012    MITSUBISHI  i-MiEV  SUBCOMPACT  49  A1  B   16.9    21.4    18.7    1.9 2.4 2.1 0   n/a 100 7
1   2012    NISSAN  LEAF    MID-SIZE    80  A1  B   19.3    23.0    21.1    2.2 2.6 2.4 0   n/a 117 7
2   2013    FORD    FOCUS ELECTRIC  COMPACT 107 A1  B   19.0    21.1    20.0    2.1 2.4 2.2 0   n/a 122 4
```


- A pivot table allows us to pivot out one of these columns into a new column headers and compare it against another column as row indices. 
    - For instance, let's say we wanted to compare the makes of electric vehicles versus the years and that we wanted to do this comparison in terms of battery capacity. 

```python
df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=np.mean)
Make    BMW CHEVROLET   FORD    KIA MITSUBISHI  NISSAN  SMART   TESLA
YEAR                                
2012    NaN NaN NaN NaN 49.0    80.0    NaN NaN
2013    NaN NaN 107.0   NaN 49.0    80.0    35.0    280.000000
2014    NaN 104.0   107.0   NaN 49.0    80.0    35.0    268.333333
2015    125.0   104.0   107.0   81.0    49.0    80.0    35.0    320.666667
2016    125.0   104.0   107.0   81.0    49.0    80.0    35.0    409.700000

df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=[np.mean,np.min], margins=True)
Make    BMW CHEVROLET   FORD    KIA MITSUBISHI  NISSAN  SMART   TESLA   All BMW CHEVROLET   FORD    KIA MITSUBISHI  NISSAN  SMART   TESLA   All
YEAR
2012    NaN NaN NaN NaN 49.0    80.0    NaN NaN 64.500000   NaN NaN NaN NaN 49.0    80.0    NaN NaN 49.0
2013    NaN NaN 107.0   NaN 49.0    80.0    35.0    280.000000  158.444444  NaN NaN 107.0   NaN 49.0    80.0    35.0    270.0   35.0
2014    NaN 104.0   107.0   NaN 49.0    80.0    35.0    268.333333  135.000000  NaN 104.0   107.0   NaN 49.0    80.0    35.0    225.0   35.0
2015    125.0   104.0   107.0   81.0    49.0    80.0    35.0    320.666667  181.428571  125.0   104.0   107.0   81.0    49.0    80.0    35.0    280.0   35.0
2016    125.0   104.0   107.0   81.0    49.0    80.0    35.0    409.700000  252.263158  125.0   104.0   107.0   81.0    49.0    80.0    35.0    283.0   35.0
All 125.0   104.0   107.0   81.0    49.0    80.0    35.0    345.478261  190.622642  125.0   104.0   107.0   81.0    49.0    80.0    35.0    225.0   35.0
```

<h2 id="124cf81690d7ad3c6cb1a8e2572c30b7"></h2>

## Date Functionality

- Pandas has four main time related classes. 
    - Timestamp, DatetimeIndex, Period, and PeriodIndex.

<h2 id="a3d5de3eac8bb00ae86fd1a1005f1500"></h2>

### Timestamp

- Timestamp represents a single timestamp and associates values with points in time. 
    - Timestamp is interchangeable with Python's datetime in most cases. 

```python
pd.Timestamp('9/1/2016 10:05AM')
Timestamp('2016-09-01 10:05:00')
```

<h2 id="1901606ea069a83dc7beea17881ef95a"></h2>

### Period

- Period represents a single time span, such as a specific day or month. 


```python
pd.Period('1/2016')
Period('2016-01', 'M')

pd.Period('3/5/2016')
Period('2016-03-05', 'D')
```

<h2 id="31c3ed93084fde1e4cfb189455db3ae0"></h2>

### DatetimeIndex

- The index of a timestamp is DatetimeIndex.

```python
t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
2016-09-01    a
2016-09-02    b
2016-09-03    c
dtype: object

type(t1.index)
pandas.tseries.index.DatetimeIndex
```

<h2 id="3e4d11c471477ea15990deaf351ecbe2"></h2>

### PeriodIndex

```python
t2 = pd.Series(list('def'), [pd.Period('2016-09'), pd.Period('2016-10'), pd.Period('2016-11')])
2016-09    d
2016-10    e
2016-11    f
Freq: M, dtype: object

type(t2.index)
pandas.tseries.period.PeriodIndex
```

<h2 id="e5e5d211bc65027dfbc69a0ab7b42824"></h2>

### Converting to Datetime

```python
d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=d1, columns=list('ab'))

                a   b
2 June 2013     16  46
Aug 29, 2014    14  66
2015-06-26      59  99
7/12/16         27  17
```

- Looking at the index we can see that it’s pretty messy and the dates are all in different formats. 
- Using pandas `to_datetime`, pandas will try to convert these to Datetime and put them in a standard format. 

```python
ts3.index = pd.to_datetime(ts3.index)
            a   b
2013-06-02  16  46
2014-08-29  14  66
2015-06-26  59  99
2016-07-12  27  17
```

- `to_datetime` also has options to change the date parse order
    - For example, we can pass in the argument `dayfirst = True` to parse the date in European date format. 

```python
pd.to_datetime('4.7.12', dayfirst=True)
Timestamp('2012-07-04 00:00:00')
```

<h2 id="345b4ea198c499ed502b17952e076b36"></h2>

### Timedeltas

- Timedeltas are differences in times

```python
pd.Timestamp('9/3/2016')-pd.Timestamp('9/1/2016')
Timedelta('2 days 00:00:00')

pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H')
Timestamp('2016-09-14 11:10:00')
```

<h2 id="ee353674a132153d42025f4ba3237d30"></h2>

### Working with Dates in a Dataframe

- `data_range`

```python
# Suppose we want to look at nine measurements, taken bi-weekly, every Sunday, starting in October 2016.
dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
DatetimeIndex(['2016-10-02', '2016-10-16', '2016-10-30', '2016-11-13',
               '2016-11-27', '2016-12-11', '2016-12-25', '2017-01-08',
               '2017-01-22'],
              dtype='datetime64[ns]', freq='2W-SUN')

```

- Now, let's create a DataFrame using these dates, and some random data

```python
df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5, 10, 9).cumsum(),
                  'Count 2': 120 + np.random.randint(-5, 10, 9)}, index=dates)
          Count 1 Count 2
2016-10-02  104 125
2016-10-16  109 122
2016-10-30  111 127
2016-11-13  117 126
2016-11-27  114 126
2016-12-11  109 121
2016-12-25  105 126
2017-01-08  105 125
2017-01-22  101 123
```

- we can check what day of the week a specific date is

```python
df.index.weekday_name
array(['Sunday', 'Sunday', 'Sunday', 'Sunday', 'Sunday', 'Sunday',
       'Sunday', 'Sunday', 'Sunday'], dtype=object)
```

- We can use *diff* to find the difference between each date's value. 

```python
df.diff()
        Count 1 Count 2
2016-10-02  NaN NaN
2016-10-16  5.0 -3.0
2016-10-30  2.0 5.0
2016-11-13  6.0 -1.0
2016-11-27  -3.0    0.0
2016-12-11  -5.0    -5.0
2016-12-25  -4.0    5.0
2017-01-08  0.0 -1.0
2017-01-22  -4.0    -2.0
```

- Suppose we wanted to know what the mean count is for each month in our DataFrame. 
    - We can do this using `resample`. 

```python
df.resample('M').mean()
            Count 1 Count 2
2016-10-31  108.0   124.666667
2016-11-30  115.5   126.000000
2016-12-31  107.0   123.500000
2017-01-31  103.0   124.000000
```

- We can use partial string indexing to find values from a particular year, or from a particular month, or we can even slice on a range of dates. 
    - For example, here we only want the values from December 2016 onwards. 

```python
df['2017']
        Count 1 Count 2
2017-01-08  105 125
2017-01-22  101 123

df['2016-12']
    Count 1 Count 2
2016-12-11  109 121
2016-12-25  105 126

df['2016-12':]
        Count 1 Count 2
2016-12-11  109 121
2016-12-25  105 126
2017-01-08  105 125
2017-01-22  101 123
```

- Another cool thing we can do is change the frequency of our dates in our DataFrame using `asfreq`

```python
df.asfreq('W', method='ffill')
        Count 1 Count 2
2016-10-02  95  119
2016-10-09  95  119
2016-10-16  101 122
2016-10-23  101 122
2016-10-30  104 128
2016-11-06  104 128
...
```

- Importing matplotlib.pyplot, and using the iPython magic %mapplotlib inline, will allow you to visualize the time series in the notebook. 

```python
import matplotlib.pyplot as plt
%matplotlib inline

df.plot()
```


