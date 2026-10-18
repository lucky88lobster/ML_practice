import pandas as pd

df = pd.DataFrame({
    "product": ["pen", "notebook", "eraser", "ruler", "marker"],
    "category": ["A", "B", "A", "B", "A"],
    "price": [1.5, 3.2, 0.8, 2.1, 2.7],
    "stock": [100, 50, 200, 80, 40]
})

print(df[["product", "price"]])
print(["product", "price"])

print(df[["product"]])
print(df["product"])

print((df["category"] == "A") & (df["price"] > 1.0))

print((df[
    (df["category"] == "A") & (df["price"] > 1.0)
]))

print(df.sort_values("stock",ascending = False).reset_index(drop=True))

print(df[df["stock"] < 90][["product"]].reset_index(drop=True))