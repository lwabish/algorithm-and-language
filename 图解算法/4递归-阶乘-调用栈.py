def product_to_1(x):
    if x == 1:
        return 1
    else:
        return x*product_to_1(x-1)


print(product_to_1(3))
