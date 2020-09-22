# Question :
# In the language of your choice, write a function which, taking a positive integer n as input, finds all sets of numbers that sum up to n.
# For example, n=4, we have: 
# 4
# 3,1
# 2,2
# 2,1,1
# 1,1,1,1

# Note that 2,1,1 is same as 1,2,1 or 1,1,2 .

# Answer :

def setNilai(x, n):
    loop = 0
    for i in range(0, n):
        loop += 1
        seperator = ","
        if (loop == n):
            seperator = ""

        print(x[i], end=seperator)


def main():
    n = int(input("Masukkan nilai n = "))
    x = [0] * n
    y = 0
    x[y] = n

    while True:
        y_tmp = y+1

        setNilai(x, y_tmp)
        print()

        tmp = 0
        while x[y] == 1 and y >= 0:
            tmp += x[y]
            y -= 1

        tmp += 1
        x[y] -= 1

        if (y < 0): return

        while tmp > x[y]:
            x[y+1] = x[y]
            tmp -= x[y]
            y += 1

        x[y+1] = tmp
        y += 1

if __name__ == '__main__':
    main()

