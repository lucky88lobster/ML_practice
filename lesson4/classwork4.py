import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Cindy", "David"],
    "math": [88, None, 79, 95],
    "english": [91, 85, None, 87]
})

print(df)

print(df.isna())
print(df.isna().sum())

#df["math"] = df["math"].fillna(df["math"].mean())
#df["english"] = df["english"].fillna(df["math"].max())
#print(df)

clean_df = df.dropna()
print(clean_df)

df["average"] = (df["math"] + df["english"]) / 2
df["passed"] = df["average"] >= 80
print(df)

import pandas as pd

df = pd.DataFrame({
    "team": ["red", "blue", "red", "blue", "red"],
    "points": [8, 11, 10, 7, 90]
})

print(df.groupby("team")["points"].mean())
print(df["points"].mean())

summary = df.groupby("team")["points"].agg(["count", "mean", "max"])
print(summary)

import pandas as pd

df = pd.DataFrame({
    "student": ["Ann", "Ben", "Cara", "Dan", "Ella"],
    "grade": [10, 10, 11, 11, 10],
    "club": ["music", "robotics", "music", "robotics", "music"],
    "score": [82, 94, 88, 91, 79]
})

print(df.groupby("grade")["score"].mean())
print(df.groupby("club")["score"].agg(["count", "mean", "max"]))

students = pd.DataFrame({
    "student_id": [1, 2, 3],
    "name": ["Ann", "Ben", "Cara"]
})

scores = pd.DataFrame({
    "student_id": [1, 2, 3],
    "math": [82, 94, 88]
})

merged = students.merge(scores, on="student_id")
print(merged)

students = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "name": ["Ann", "Ben", "Cara", "Dan"]
})

scores = pd.DataFrame({
    "student_id": [1, 2, 3],
    "math": [82, 94, 88]
})

merged = students.merge(scores, on="student_id")
print(merged)

