# def i():
#     for a in [1,2,3,4,5]:
#         yield a
# aboba = i()
# print(next(aboba))
# print(next(aboba))
# print(next(aboba))
# print(next(aboba))
# print(next(aboba))

def recursia(i):
    if i == 20:
        return
    print(i)
    recursia(i-1)
recursia(36)