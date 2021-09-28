#create function close10()
def close10(x, y):
    if (10 - x) > (y - 10):
        return y
    elif (10 - x) == (y - 10):
        return 0
    else:
        return x
