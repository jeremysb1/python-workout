def mmysum(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output

print(mmysum(10, 20, 30, 40))