def int_to_rome(x):
    numbers = [1,4,5,9,10,40,50,90,100]
    roman = ["I","IV","V","IX","X","XL","L","XC","C"]
    i=8
    roman_numeral=""
    while x != 0:
        if numbers[i] <=x:
            roman_numeral += roman[i]
            x = x-numbers[i]
        else:
            i -= 1
    return roman_numeral 
print(int_to_rome(49))
