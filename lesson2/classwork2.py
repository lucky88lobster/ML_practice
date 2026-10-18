import pandas as pd

scores = pd.Series([88, 92, 79], index=["Alice", "Bob", "Cindy"])
print(scores)

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Cindy"],
    "math": [88, 92, 79],
    "english": [91, 85, 95]
})

print(df)

print(df.index)
print(df.columns)
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.describe())

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Cindy"],
    "score": [88, 92, 79]
})

df["passed"] = df["score"] >= 80
print(df)
df["bonus_score"] = df["score"] + 5
print(df)

import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Cindy", "David"],
    "math": [88, 92, 79, 95],
    "english": [91, 85, 95, 87]
})

df["average"] = (df["math"] + df["english"]) / 2
df["passed_math"] = df["math"] >= 80

print(df)
print(df[["name", "average"]])

place = pd.DataFrame({
    "city":["SF", "SJ", "SC"],
    "population":["1", "2", "3"],
    "coastal":["True", "True", "False"]
})

print(place)
print(place["city"])
print(place[["city", "population"]])

studentscores = pd.DataFrame({
    "student": ["Ann", "Ben", "Cara"],
    "score": [76, 91, 84]
})

studentscores["passed"] = studentscores["score"] >= 80
studentscores["score_plus_10"] = studentscores["score"] + 10
print(studentscores)

studentscores.