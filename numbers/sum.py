def mysum(list, num):
    output = 0
    for number in list:
        output += number
    return output + num

print(mysum([10, 20, 30, 40], 50))