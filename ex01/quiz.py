import random #randamモジュールを呼び出し
import datetime #datetimeモジュールを呼び出し


def shutudai(qa_lst): #ランダムに選んだ問題を出題し、回答をmainに渡す
    qa = random.choice(qa_lst) #qa_lstから問題文をランダムに選ぶ
    print("問題：" +qa["q"]) #問題文を出力
    return qa["a"] #問題の回答を返す


def kaitou(ans_lst): #回答と正解をチェックし、結果を出力する
    st = datetime.datetime.now() #回答初めの時間を記録
    ans = input("答えるんだ：") #入力を受け付ける
    ed = datetime.datetime.now() #回答終わりの時間を記録
    if ans in ans_lst: #正解の単語が含まれていれば
        print("正解！！！！！") #正解文を出力
    else: #そうでなければ
        print("出直してこい") #不正解文を出力
    
    print(f"回答時間：{(ed-st).seconds}秒") #回答時間を出力


if __name__ == "__main__": #コマンドラインから実行された時のみ動く
    qa_lst = [
            {"q":"サザエの旦那の名前は？", "a":["マスオ", "ますお"]}, #問題1の問題文と回答
            {"q":"カツオの妹の名前は？", "a":["ワカメ", "わかめ"]}, #問題2の問題文と回答
            {"q":"タラオはカツオから見てどんな関係？", "a":["甥", "おい", "甥っ子", "おいっこ"]}] #問題3の問題文と回答
    
    ans_lst = shutudai(qa_lst) #shutudai関数の呼び出し、回答の収納
    kaitou(ans_lst) #kaitou関数の呼び出し