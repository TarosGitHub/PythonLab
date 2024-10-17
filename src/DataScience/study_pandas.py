import pandas as pd

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

if __name__ == "__main__":
    print(pd.__version__)
