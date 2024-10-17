import pandas as pd
import numpy as np

## Series

data = pd.Series([1, 2, 3])

data = pd.Series([1, 2, 3, 4],
                 index=["a", "b", "c", "d"])

population_dict = {"California": 38332521,
                   "Texas": 26448193,
                   "New York": 19651127,
                   "Florida": 19552860}
population = pd.Series(population_dict)

### Attributes of Series

population.values
population.index

### Access

data = pd.Series(["a", "b", "c"], index=[1, 3, 5])

data.loc[1]
"""
'a'
"""
data.loc[1:3]
"""
1 a
3 b
"""

data.iloc[1]
"""
'b'
"""
data.iloc[1:3]
"""
3 b
5 c
"""

## DataFrame

area_dict = {"California": 423967,
             "Texas": 695662,
             "New York": 141297,
             "Florida": 170312,
             "Illinois": 149995}
area = pd.Series(area_dict)
states = pd.DataFrame({"population": population,
                       "area": area})

data = [{"a": i, "b": 2 * i} for i in range(3)]
pd.DataFrame(data)

### Attributes of DataFrame

states.values
states.index
states.columns

### Transpose (Swap rows and columns)

states.T
"""
            California     Florida  Illinois    New York       Texas
population  38332521.0  19552860.0       NaN  19651127.0  26448193.0
area          423967.0    170312.0  149995.0    141297.0    695662.0
"""

### Access

states["area"] # Returns one column
"""
California 423967
Texas      695662
New York   141297
Florida    170312
"""

states.loc["California", "area"]
states.loc[:"New York", :"population"]

states.iloc[1, 1]

## Multiple index

index = [("California", 2000),
         ("California", 2010),
         ("New York", 2000),
         ("New York", 2010),
         ("Texas", 2000),
         ("Texas", 2010)]
index = pd.MultiIndex.from_tuples(index)

pop = [33871648, 37253956,
       18976457, 19378102,
       20851820, 25145561]
pop = pd.Series(pop, index=index)

### Level names

pop.index.names = ["state", "year"]

### Stack, Unstack

pop_df = pop.unstack()
"""
year            2000      2010
state
California  33871648  37253956
New York    18976457  19378102
Texas       20851820  25145561
"""

pop_df.stack()
"""
state       year
California  2000    33871648
            2010    37253956
New York    2000    18976457
            2010    19378102
Texas       2000    20851820
            2010    25145561
"""

### Multiple index for columns

hindex = pd.MultiIndex.from_product([[2013, 1014], [1, 2]], names=["year", "visit"])
hcolumns = pd.MultiIndex.from_product([["Bob", "Guido", "Sue"], ["HR", "Temp"]], names=["subject", "type"])
hdata = np.round(np.random.randn(4, 6), 1)
hdata[:, ::2] *= 10
hdata += 37
health_data = pd.DataFrame(hdata, index=hindex, columns=hcolumns)

health_data.loc[:, "Guido"]
"""
type          HR  Temp
year visit
2013 1      43.0  37.4
     2      26.0  37.5
1014 1      46.0  37.0
     2      35.0  37.4
"""

health_data.loc[(2013, 1), ("Guido", "HR")]
"""
43.0
"""

idx = pd.IndexSlice
health_data.loc[idx[:, 1], idx[:, "HR"]]
"""
subject      Bob Guido   Sue
type          HR    HR    HR
year visit
2013 1      22.0  43.0  37.0
1014 1      34.0  46.0  40.0
"""

### Set and reset index

pop_flat = pop.reset_index(name="population")
"""
        state  year  population
0  California  2000    33871648
1  California  2010    37253956
2    New York  2000    18976457
3    New York  2010    19378102
4       Texas  2000    20851820
5       Texas  2010    25145561
"""

pop_flat.set_index(["state", "year"])
"""
                 population
state      year
California 2000    33871648
           2010    37253956
New York   2000    18976457
           2010    19378102
Texas      2000    20851820
           2010    25145561
"""

if __name__ == "__main__":
    print(pd.__version__)
