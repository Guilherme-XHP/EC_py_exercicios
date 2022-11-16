list = [1,2,3,4,5]

end = 5

while end > 1:

    troc = False

    x = 0

    while x < (end - 1):
        if list[x] < list[x+1]:

            troc = True

            temp = list[x]

            list[x] = list[x+1]

            list[x+1] = temp

        x += 1

    if not troc:

        break

    end -= 1

for e in list:

    print(e)