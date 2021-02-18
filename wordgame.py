import random
WORDS = ("python", "jumble", "easy", "difficult", "answer", "continue", "phone", "position", "game")
# 開始遊戲
print(
    """
    welcome to wordgame
    please spell the right word
    """)

iscontinue = "y"
while iscontinue=="y" or iscontinue=="Y":
    word = random.choice(WORDS)
    correct = word
    jumble = ""
    while word:
        # 根據word長度產生word的隨機位置
        position = random.randrange(len(word))
        # 根據position位置的字母組合到亂數後單字
        jumble += word[position]
        # 透過切片，將position位置的字母從原單字中刪除
        word = word[:position] + word[(position+1):]
    print("亂數後的單字: ", jumble)
    guess = input("please answer the word: ")
    while guess !=correct and guess!="":
        print("wrong")
        guess = input("answer again")
    if guess == correct:
        print("Congratulations")
    iscontinue = input("play again? (Y/N): ")

