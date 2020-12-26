product = [
    ("produt1", 10),
    ("product3", 15),
    ("product4", 25),
    ("product6", 20),
]
#lambda parameter:expression
product.sort(key=lambda x: x[1])
print(product)
