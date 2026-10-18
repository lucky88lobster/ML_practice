import pandas as pd

df = pd.DataFrame({
    "name": ["Ann", "Ben", "Cara", "Dan"],
    "student_id": [1, 2, 3, None],
})

df["student_id"] = df["student_id"].fillna(df["student_id"].mean())

print(df)


df = pd.DataFrame({
    "store": ["north", "south", "north", "south", "north"],
    "sales": [120, 150, 90, 130, 110]
})

total = df.groupby("store")["sales"].sum()
print(total)
average = df.groupby("store")["sales"].mean()
print(average)
max = df.groupby("store")["sales"].max()
print(max)

all = df.groupby("store")["sales"].agg(["sum", "mean", "max"])
print(all)
#the total sales by store
#the average sales by store
#the maximum sales by store

df = pd.DataFrame({
    "student_id": ["1", "2", "3", "5"],
    "name": ["Sam", "Josh", "John", "Felix"],
})

pf = pd.DataFrame({
    "student_id": ["1", "2", "3", "4"],
    "science_score": [60, 99, 100, 7]
})

hi = df.merge(pf, on = "student_id", how = "outer")

print(hi)


