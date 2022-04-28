values_list = [7,75,45,23,15,54,105]
divisible_values = list(filter(lambda i : i%15 == 0,values_list))
print(divisible_values)