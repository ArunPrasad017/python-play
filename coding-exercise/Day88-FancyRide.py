def fancyRide(l, fares):
    max_val = 0
    lst = ["UberX", "UberXL", "UberPlus", "UberBlack", "UberSUV"]
    for i, fare in enumerate(fares):
        if l * fare <= 20:
            max_val = i
    return lst[max_val]


l = 30
fares = [0.3, 0.5, 0.7, 1, 1.3]
print(fancyRide(l, fares))
