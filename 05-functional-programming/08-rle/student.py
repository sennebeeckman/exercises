def rle_encode(data):
    data = iter(data)

    try:
        last_item = next(data)
        count = 1
        for element in data:
            if element == last_item:
                count += 1
            else:
                yield (last_item, count)
                last_item = element
                count = 1
        yield (last_item, count)
    except StopIteration:
        pass


def rle_decode(data):
    for item, count in data:
        for _ in range(count):
            yield item
