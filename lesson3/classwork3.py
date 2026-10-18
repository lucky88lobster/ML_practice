import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Cindy", "David", "Eva"],
    "grade": [10, 10, 11, 11, 10],
    "math": [88, 92, 79, 95, 84],
    "club": ["robotics", "music", "robotics", "sports", "music"]
})

print(df["math"])

print(df[["name", "math"]])

print(df.iloc[0])
print(df.iloc[0:3])
print(df.iloc[2, 3])

print(df[df["math"] >= 90])

print(df[(df["grade"] == 10) & (df["club"] == "music")])

print(df[(df["math"] >= 90) & (df["club"] == "music")])

print(df.sort_values("math"))

print(df.sort_values("math", ascending=False))

print(df.sort_values(["grade", "math"], ascending=[True, False]))

print(df.sort_values(["grade", "math"], ascending=[True, False]).reset_index(drop=True))

import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Cindy", "David", "Eva"],
    "grade": [10, 10, 11, 11, 10],
    "math": [88, 92, 79, 95, 84],
    "club": ["robotics", "music", "robotics", "sports", "robotics"]
})

answer = df[
    (df["club"] == "robotics") & (df["math"] >= 80)
][["name", "club", "math"]].sort_values("math", ascending=False)

print(answer)

answer = df[
    (df["club"] == "robotics") & (df["math"] >= 80)
].sort_values("math", ascending=False)

print(answer)

