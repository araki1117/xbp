import time
while True: 

    print("========== 確率減少ゲーム ==========")
    print("\n")
    name=input ("名前を教えて下さい")

    print(name, "さん、ようこそ確率減少ゲームへ")
    time.sleep(2)
    print("\n\n")

    number=int(input("1から10で好きな数字を選んでね"))
    time.sleep(2)
    print("\n\n")


    if 1 <= number <= 10:

        print("あなたの選んだ数字は", number,"ですね！")

    else:
        print(name,"さん、その数字は選べないよ！")
        time.sleep(2)
        break
        print("\n\n")
    if number==5:
        print("残念！逆にすごいね、、、")
        break
        
    else:
        print("おめでとう10/9の確率を当てたよ！、まあさすがにね")

        time.sleep(2)
        print("\n\n")

        print("次ははずれが２つになるよ!")
        time.sleep(2)
        print("\n\n")

        number=int(input("1から10で好きな数字を選んでね"))
        print()

    if 1 <= number <= 10:
        print("あなたの選んだ数字は", number,"ですね！")
        print("\n\n")
        time.sleep(2)
    else:
        print(name,"さん、その数字は選べないよ！")
        break
    if number in[2,5]:
        print("残念！どんまい！")
        break

    if number not in [2,5]:
       print("おめでとう！次に進もう")
       print("\n\n")
       time.sleep(2)

       number=int(input("1から10で好きな数字を選んでね"))
       print()

    if 1 <= number <= 10:
        print("あなたの選んだ数字は", number,"ですね！")
        print("\n\n")
        time.sleep(2)
    else:
        print(name,"さん、その数字は選べないよ！")
        time.sleep(2)
        break

    if number in[3,7,9]:
        print("残念！どんまい！")
        break

    if number not in[3,7,9]:
       print("おめでとう！ナイスだ！")
       print("\n\n")
       time.sleep(2)

       number=int(input("1から10で好きな数字を選んでね"))
       print()

    if 1 <= number <= 10:
        print("あなたの選んだ数字は", number,"ですね！")
        print("\n\n")
        time.sleep(2)
    else:
        print(name,"さん、その数字は選べないよ！")
        time.sleep(2)
        break

    if number in[3,5,9,10]:
        print("残念！切り替えよう")
        break

    if number not in[3,5,9,10]:
       print("おめでとう！いい調子！")
       time.sleep(2)
       print("\n\n")

       number=int(input("1から10で好きな数字を選んでね"))
       print()
       time.sleep(2)

    if 1 <= number <= 10:
        print("あなたの選んだ数字は", number,"ですね！")
        print("\n\n")
        time.sleep(2)
    else:
        print(name,"さん、その数字は選べないよ！")
        time.sleep(2)
        break

    if number in[2,3,5,7,8]:
        print("残念！あと1問で半分だったね")
        break

    if number not in[2,3,5,7,8]:
       print("おめでとう！えぐい、半分じゃん")
       time.sleep(2)
       print("\n\n")


       number=int(input("1から10で好きな数字を選んでね"))
       print()
       time.sleep(2)

    if 1 <= number <= 10:
        print("あなたの選んだ数字は", number,"ですね！")
        time.sleep(2)
        print("\n\n")
    else:
        print(name,"さん、その数字は選べないよ！")
        time.sleep(2)
        break

    if number in[1,4,6,7,9,10]:
        print("残念！また挑戦してね")
        break

    if number not in[1,4,6,7,9,10]:
        print("おめでとう！このままの調子で！")
        time.sleep(2)
        print("\n\n")

        number=int(input("1から10で好きな数字を選んでね"))
        print("\n")
        time.sleep(2)

    if 1 <= number <= 10:
        print("あなたの選んだ数字は", number,"ですね！")
        print("\n\n")
        time.sleep(2)
    else:
        print(name,"さん、その数字は選べないよ！")
        time.sleep(2)
        break

    if number in[2,3,5,6,8,9,10]:
        print("残念！あと少しだったね")
        break

    if number not in[2,3,5,6,8,9,10]:
       print("おめでとう！あと2問だ！")
       print("\n\n")
       time.sleep(2)

       number=int(input("1から10で好きな数字を選んでね"))
       print()
       time.sleep(2)

    if 1 <= number <= 10:
        print("あなたの選んだ数字は", number,"ですね！")
        print("\n\n")
        time.sleep(2)
    else:
        print(name,"さん、その数字は選べないよ！")
        time.sleep(2)
        break

    if number in[1,2,3,4,5,6,7,8]:
        print("残念！惜しい！、あと1問だったのに！")
        break

    if number not in[1,2,3,4,5,6,7,8]:
       print("おめでとう！次で最後だ！")
       time.sleep(2)
       print("\n\n")

       number=int(input("1から10で好きな数字を選んでね"))
       print()
       time.sleep(2)

    if 1 <= number <= 10:
        print("あなたの選んだ数字は", number,"ですね！")
        print("\n\n")
        time.sleep(2)
    else:
      print(name,"さん、その数字は選べないよ！")
      time.sleep(2)
      break

    if number in[1,2,3,4,6,7,8,9,10]:
        print("・・・・・・・・・・・")
        time.sleep(2)
        print("残念！めちゃくちゃ惜しかった！")
        break

    else:
        print("・・・・・・・・・・・")
        time.sleep(2)
        print("すごい！おめでとう！今すぐ宝くじ買った方がいいよ！！！")
        print("\n\n")
        time.sleep(2)
        print("遊んでくれてありがとう！")
        break


       











