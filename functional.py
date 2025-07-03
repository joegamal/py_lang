def inputFunction(fun, val):
    fun(val)


inputFunction(print, "functional programming")


def returnFunction():
    return 4, 5, 6



[_, num, _] = returnFunction()

print(num)

