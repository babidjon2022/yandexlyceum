import string
import random

upperletters = tuple(string.ascii_uppercase.replace('I', '').replace('O', ''))
lowerletters = tuple(string.ascii_lowercase.replace('l', '').replace('o', ''))
digits = tuple(string.digits.replace('0', '').replace('1', ''))


def generate_password(m):
    uposs = list(upperletters)
    lposs = list(lowerletters)
    dposs = list(digits)
    allposs = uposs + lposs + dposs
    uindex, lindex, dindex = random.sample(range(m), k=3)
    password = ['' for _ in range(m)]
    password[uindex] = random.choice(upperletters)
    uposs.remove(password[uindex])
    allposs.remove(password[uindex])
    password[lindex] = random.choice(lowerletters)
    lposs.remove(password[lindex])
    allposs.remove(password[lindex])
    password[dindex] = random.choice(digits)
    dposs.remove(password[dindex])
    allposs.remove(password[dindex])
    for i in range(m):
        if i in {uindex, lindex, dindex}:
            continue
        password[i] = random.choice(allposs)
        allposs.remove(password[i])
    return ''.join(password)


def main(n, m):
    passwordslist = list()
    k = 0
    while True:
        password = generate_password(m)
        if password in passwordslist:
            continue
        passwordslist.append(password)
        k += 1
        if k == n:
            break
    return passwordslist
