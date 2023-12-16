def your_mom(word):
    output = []
    for letter in word:
        if letter in 'aeiou':
            output.append(f'ym{letter}')
        else:
            output.append(letter)
    
    return ''.join(output)

print(your_mom('python'))
