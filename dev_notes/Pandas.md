...menustart

 - [Pandas](#251d2bbfe9a3b95e5691ceb30dc6784a)
 - [Basic Data Processing with Pandas](#2beb23af04774d7f04142fdc60c1e388)
     - [The Series Data Structure](#b2d7146a323c3e1734532ceb0f3b8b85)
     - [Querying a Series](#8397ade4c8ed93da5a52c39691b7879e)
     - [The DataFrame Data Structure](#831bfe24989afb7977d21427c1cfa747)

...menuend


<h2 id="251d2bbfe9a3b95e5691ceb30dc6784a"></h2>

# Pandas 

<h2 id="2beb23af04774d7f04142fdc60c1e388"></h2>

# Basic Data Processing with Pandas

<h2 id="b2d7146a323c3e1734532ceb0f3b8b85"></h2>

## The Series Data Structure

 - You think of it a cross between a list and a dictionary. 
    - The items are all stored in an order and there's labels with which you can retrieve 
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/pandas_series.png)

```python
import pandas as pd
pd.Series?
```

```python
animals = ['Tiger', 'Bear', 'Moose']
pd.Series(animals)
0    Tiger
1     Bear
2    Moose
dtype: object

numbers = [1, 2, 3]
pd.Series(numbers)
0    1
1    2
2    3
dtype: int64
```

 - Underneath panda stores series values in a typed array using the Numpy library. 
    - This offers significant speed-up when processing data versus traditional python lists. 
 - There's some other typing details that exist for performance that are important to know. 
    - The most important is how Numpy and thus pandas handle missing data.
    - In Python, we have the none type to indicate a lack of data. 
    - But what do we do if we want to have a typed list like we do in the series object? 

```python
animals = ['Tiger', 'Bear', None]
pd.Series(animals)
0    Tiger
1     Bear
2     None
dtype: object

numbers = [1, 2, None]
pd.Series(numbers)
0    1.0
1    2.0
2    NaN
dtype: float64
```

 - `NaN` is not `None` , and you can directly compare with `NaN`, use `np.isnan` instead

```python
import numpy as np
np.nan == None
False

np.nan == np.nan
False

np.isnan(np.nan)
True
```

 - Create from Dictionary

```python
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
s
Archery           Bhutan
Golf            Scotland
Sumo               Japan
Taekwondo    South Korea
dtype: object

s.index
Index(['Archery', 'Golf', 'Sumo', 'Taekwondo'], dtype='object')
```

 - You could also separate your index creation from the data by passing in the index as a list explicitly to the series

```python
s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
s
India      Tiger
America     Bear
Canada     Moose
dtype: object
```

 - So what happens if your list of values in the index object are not aligned with the keys in your dictionary for creating the series? 

```python
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey'])
s
Golf      Scotland
Sumo         Japan
Hockey         NaN   # missing value
dtype: object
```

<h2 id="8397ade4c8ed93da5a52c39691b7879e"></h2>

## Querying a Series

 - A panda.Series can be queried, either by the index position or the index label. 
    - To query by numeric location, starting at zero, use the `iloc` attribute.
    - To query by the index label, you can use the `loc` attribute.

```python
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
s
Archery           Bhutan
Golf            Scotland
Sumo               Japan
Taekwondo    South Korea
dtype: object

s.iloc[3]
'South Korea'

s.loc['Golf']
'Scotland'

s[3]  # same as iLoc
'South Korea'

s['Golf']  # same as Loc
'Scotland'
```

 - So what happens if your index is a list of integers? 
    - This is a bit complicated, and Pandas can't determine automatically whether you're intending to query by index position or index label. 
    - So you need to be careful when using the indexing operator on the series itself. 
    - And the safer option is to be more explicit and use the `iloc` `or` loc attributes directly. 

```python
sports = {99: 'Bhutan',
          100: 'Scotland',
          101: 'Japan',
          102: 'South Korea'}
s = pd.Series(sports)
s
99          Bhutan
100       Scotland
101          Japan
102    South Korea
dtype: object

s[0] # This won't call s.iloc[0] but generates an error
```

 - working with series
    - Pandas and the underlying NumPy libraries support a method of computation called vectorization. 

```python
s = pd.Series([100.00, 120.00, 101.00, 3.00])
total = np.sum(s)
total
324.0
```

```python
s = pd.Series(np.random.randint(0,1000,10000))
s.head()
0    350
1    862
2     86
3    604
4    310
dtype: int64

s+=2 #adds two to each item in s using broadcasting
s.head()
0    352
1    864
2     88
3    606
4    312
dtype: int64
```

 - iterate series , slow than broadcasting 

```python
for label, value in s.iteritems():
    s.set_value(label, value+2)
s.head()
```

 - If the value you pass in as the index doesn't exist, then a new entry is added. And keep in mind, indices can have mixed types. While it's important to be aware of the typing going on underneath, Pandas will automatically change the underlying NumPy types as appropriate. 

```python
s = pd.Series([1, 2, 3])
s.loc['Animal'] = 'Bears'
s
0             1
1             2
2             3
Animal    Bears
dtype: object
```

 - Up until now I've shown only examples of a series where the index values were unique. 
    - I want to end this lecture by showing an example where index values are not unique, and this makes data frames different, conceptually, that a relational database might be. 

```python
original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England'], 
                                   index=['Cricket',
                                          'Cricket',
                                          'Cricket',
                                          'Cricket'])
all_countries = original_sports.append(cricket_loving_countries)

original_sports
Archery           Bhutan
Golf            Scotland
Sumo               Japan
Taekwondo    South Korea
dtype: object

cricket_loving_countries
Cricket    Australia
Cricket     Barbados
Cricket     Pakistan
Cricket      England
dtype: object

all_countries
Archery           Bhutan
Golf            Scotland
Sumo               Japan
Taekwondo    South Korea
Cricket        Australia
Cricket         Barbados
Cricket         Pakistan
Cricket          England
dtype: object

Cricket    Australia
Cricket     Barbados
Cricket     Pakistan
Cricket      England
dtype: object
```

 - There are a couple of important considerations when using append. 
    - First, Pandas is going to take your series and try to **infer** the best data types to use. 
        - In this example, everything is a string, so there's no problems here. 
    - Second, the append method **doesn't** actually change the underlying series.
        - It instead returns a new series which is made up of the two appended together. 
 - This is actually a significant issue for new Pandas users who are used to objects being changed in place. 
    - So watch out for it, not just with append but with other Pandas functions as well.  

---

<h2 id="831bfe24989afb7977d21427c1cfa747"></h2>

## The DataFrame Data Structure

 - The DataFrame is conceptually a two-dimensional series object
    - where there's an index and multiple columns of content, with each column having a label. 
    - In fact, the distinction between a column and a row is really only a conceptual distinction. 
    - And you can think of the DataFrame itself as simply a two-axes labeled array. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/pandas_dataframe.png)

```python
import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
df.head()

            Cost    Item Purchased  Name
Store 1     22.5    Dog Food        Chris
Store 1     2.5     Kitty Litter    Kevyn
Store 2     5.0     Bird Seed       Vinod

df.loc['Store 2']
Cost                      5
Item Purchased    Bird Seed
Name                  Vinod
Name: Store 2, dtype: object

type(df.loc['Store 2'])
pandas.core.series.Series

df.loc['Store 1']
            Cost    Item Purchased  Name
Store 1     22.5    Dog Food        Chris
Store 1     2.5     Kitty Litter    Kevyn

df.loc['Store 1', 'Cost']
Store 1    22.5
Store 1     2.5
Name: Cost, dtype: float64
```

 - What if we just wanted to do column selection and just get a list of all of the costs? 
 - There is a couple of options.
 - First, you can get a transpose of the DataFrame, using the capital T attribute, which swaps all of the columns and rows. 
    - This works, but it's pretty ugly. 

```python
df.T
                Store 1     Store 1         Store 2
Cost            22.5        2.5             5
Item Purchased  Dog Food    Kitty Litter    Bird Seed
Name            Chris       Kevyn           Vinod

df.T.loc['Cost']
Store 1         22.5
Store 1         2.5
Store 2         5
Name: Cost, dtype: object
```

 - Since iloc and loc are used for row selection, the Panda's developers reserved indexing operator directly on the DataFrame for column selection.
    - In a Panda's DataFrame, columns always have a name. 
    - So this selection is always label based, not as confusing as it was when using the square bracket operator on the series objects. 
    - For those familiar with relational databases, this operator is analogous to column projection. 
 - Finally, since the result of using the indexing operators, the DataFrame or series, you can chain operations together.
    - But chaining can come with some costs and is best avoided if you can use another approach. 
    - In particular, chaining tends to cause Pandas to return a copy of the DataFrame instead of a view on the DataFrame.

```python
df['Cost']
Store 1    22.5
Store 1     2.5
Store 2     5.0
Name: Cost, dtype: float64

df.loc['Store 1']['Cost']
Store 1    22.5
Store 1     2.5
Name: Cost, dtype: float64

df.loc[:,['Name', 'Cost']]
        Name    Cost
Store 1 Chris   22.5
Store 1 Kevyn   2.5
Store 2 Vinod   5.0
```

 - let's talk about dropping data. 
    - It's easy to delete data in series and DataFrames, and we can use the drop function to do so
    - The drop function doesn't change the DataFrame by default. And instead, returns to you a copy of the DataFrame with the given rows removed. 

```python
df.drop('Store 1') # won't change df
        Cost    Item Purchased  Name
Store   2 5.0   Bird Seed       Vinod

df
        Cost    Item Purchased  Name
Store 1 22.5    Dog Food        Chris
Store 1 2.5     Kitty Litter    Kevyn
Store 2 5.0     Bird Seed       Vinod
```

 - Let's make a copy with the copy method and do a drop on it instead. 
    - This is a very typical pattern in Pandas, where in place changes to a DataFrame are only done if need be, usually on changes involving indices. 
   
```python
copy_df = df.copy()
copy_df = copy_df.drop('Store 1')
copy_df
            Cost    Item Purchased  Name
Store   2   5.0     Bird Seed       Vinod
```

 - Drop has two interesting optional parameters. 
    - The first is called in place, and if it's set to true, the DataFrame will be updated in place, instead of a copy being returned. 
    - The second parameter is the axes, which should be dropped. By default, this value is 0, indicating the row axes. But you could change it to 1 if you want to drop a column. 

 - There is a second way to drop a column, however. And that's directly through the use of the indexing operator, using the del keyword. 

```python
del copy_df['Name']
copy_df
            Cost    Item Purchased
Store 2     5.0     Bird Seed
```

 - Finally, adding a new column to the DataFrame is as easy as assigning it to some value.

```python
df['Location'] = None
df
            Cost    Item Purchased  Name    Location
Store 1     22.5    Dog Food        Chris   None
Store 1     2.5     Kitty Litter    Kevyn   None
Store 2     5.0     Bird Seed       Vinod   None
```

---
















