import random
import datetime
import string

sub_alf = 10 #対象文字数
def_alf = 2 #欠損文字数
n = 2 #挑戦回数
alp_lst = random.sample(string.ascii_uppercase, sub_alf)


def shutudai(alp_lst):
    print("対象文字：")
    for c in alp_lst:
        print(c, end=" ")
    print()

    abs_chars = random.sample(alp_lst, def_alf)
    print("欠損文字（デバッグ用）：")
    for c in abs_chars:
        print(c, end=" ")
    print()

    print("表示文字：")
    for c in alp_lst:
        if c not in abs_chars:
            print(c, end=" ")
    print()

    return abs_chars


def kaitou(abs_chars):
    num = int(input("欠損文字はいくつあるでしょうか？"))
    if num != def_alf:
        print("不正解です")
    else:
        print("正解です。それでは、具体的に欠損文字を1つずつ入力してください")
        for i in range(num):
            ans = input(f"{i+1}つ目の文字を入力してください")
            if ans not in abs_chars:
                print("不正解です")
                return False
            else:
                abs_chars.remove(ans)
        print("全部正解です")
        return True


if __name__ == "__main__":
    for _ in range(n):
        abs_chars = shutudai(alp_lst)
        ret = kaitou(abs_chars)
        if ret:
            break
        else:
            print("-"*20)
