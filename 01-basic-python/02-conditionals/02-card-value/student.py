def card_value(string):
    if string in ["Jack", "Queen", "King", "Ace"]:
        if string == "Jack":
            return 11
        elif string == "Queen":
            return 12
        elif string == "King":
            return 13
        else:
            return 1
    else:
        return int(string)
