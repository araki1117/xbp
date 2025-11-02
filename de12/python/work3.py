for i in range(1,4): #コロンが入っていることに注意
    print(i,"人目") #タブでずらしていることに注意！

    name=input ("名前を教えて下さい")

    waist=float(input("腹囲は？"))
    age=int(input("年齢は？"))
    bmi=20
    



    if waist>85 and age>40:
        print(name,"さん、内臓脂肪蓄積注意です")
    elif waist==85 and age==40:
        print(name,"さん、どっちでもないつまらない体です")
    else:
        print(name,"さん、腹囲は問題ありません")

    # 出力結果
    # 0 人目
    # 1 人目
    # 2 人目
