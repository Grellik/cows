from random import randint

auto_num = str(randint(1, 9)) + str(randint(1, 9)) + \
    str(randint(1, 9)) + str(randint(1, 9))
print("How many tries do you want?")
lives = int(input())


def game(auto_num, lives):
    tries = 0
    user_num = 0
    while tries != lives and user_num != auto_num:
        an = list(auto_num)
        cor = 0
        mispl = 0
        user_num = str(input())
        un = list(user_num)
        i = 0
        while i < 4:
            if i < len(un):
                if un[i] == an[i]:
                    cor += 1
                    un.remove(un[i])
                    an.remove(an[i])
                    i -= 1
            i += 1
        i = 0
        while i < 4:
            if i < len(un):
                if un[i] in an:
                    mispl += 1
                    an.remove(un[i])
                    del un[i]
                    i -= 1
            i += 1
        tries += 1
        print(cor, "correct ", mispl, "misplaced")
    if tries == lives:
        print("You lost, the number was", auto_num)
    else:
        print("You won in", tries, "tries")


game(auto_num, lives)
