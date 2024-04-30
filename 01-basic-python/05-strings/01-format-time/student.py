def format_time(hours, minutes, seconds):
    list = [hours, minutes, seconds]
    for x in range(len(list)):
        if list[x] < 10:
            list[x] = "0" + str(list[x])
    return f"{list[0]}:{list[1]}:{list[2]}"
