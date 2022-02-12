"""
ハングマンゲーム
"""
def hangman():
    import random
    # 答えの単語をリストからランダムに選ぶ
    word_list = ["apple", "study", "world", "demon", "ahead", "enter", "share"]
    rand = random.randint(0, len(word_list))
    word = word_list[rand]

    wrong = 0
    stages = [
    "",
    "______    ",
    "|         ",
    "|    |    ",
    "|    o    ",
    "|   /|\   ",
    "|   / \   ",
    "|         "
    ]
    rletters = list(word)
    board =["_"] * len(word)
    win = False

    print("Welcome to Hangman!")

    while wrong < len(stages)-1:
        print("\n")
        msg = ("let's guess a word.")
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose. answer is {}.".format(word))

hangman()
