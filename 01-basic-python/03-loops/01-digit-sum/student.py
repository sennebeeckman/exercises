def digit_sum(n):
    sum = 0
    for cijfer in str(n):
        sum += int(cijfer)
    return sum

def last_digit(n):
    return n%10

def remove_last_digit(n):
    return n//10

        

