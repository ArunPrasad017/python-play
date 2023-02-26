def average(salary):
    cnt, sum_of_elements = 0, 0
    salary.sort()
    for i in range(1, len(salary) - 1):
        sum_of_elements += salary[i]
        cnt += 1
    return (sum_of_elements / cnt) if cnt > 0 else 0


salary = [4000, 3000, 1000, 2000]
print(average(salary))