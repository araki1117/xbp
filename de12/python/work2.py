a=15
if a > 10:
    print("10より大きい")

name=input ("名前を教えて下さい")

waist=float(input("腹囲は？"))
age=int(input("年齢は？"))
bmi=20
print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

if waist>85 and age>40:
    print(name,"さん、内臓脂肪蓄積注意です")
elif waist==85 and age==40:
    print(name,"さん、どっちでもないつまらない体です")
else:
    print(name,"さん、腹囲は問題ありません")


