def fizzbuzz():
    item = 0
    while True:
        item += 1
        if item%3 + item%5 == 0:
            yield "fizzbuzz"
        elif item%3 == 0:
            yield "fizz"
        elif item%5 == 0:
            yield "buzz"
        else:
            yield str(item)
