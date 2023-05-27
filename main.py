import random
def guess(a):
    r_no = random.randint(1, a)
    gss = 0
    while gss != r_no:
        gss = int(input(f'guess the number between 1 & {a}: '))
        if gss < r_no:
            print('Too low, try again ')
        elif gss > r_no:
            print('Too high, try again ')
    print(f'Congratulation! {gss} is the correct guess')

a = int(input('Ente the range: '))
guess(a)