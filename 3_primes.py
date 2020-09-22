# Question :
# Write a function which, taking in a positive integer n as input, returns an array of all primes lower than n.
# sample expected output:

# getPrimes(5); ⇒ array(2, 3)
# getPrimes(10); ⇒ array(2, 3, 5, 7)

# Answer :

import array as arr

def getPrimes(n):
    res = arr.array('i')
    for x in range(2, n):
        cek = True
        for y in range(2, x):
            if (x % y == 0): cek = False

        if (cek == True): res.append(x)

    print(res)

def main():
    n = int(input("Masukkan nilai n = "))
    getPrimes(n)

if __name__ == '__main__':
    main()

