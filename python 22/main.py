a = int(input("შეიყვანეთ პირველი კათეტის სიგრძე: "))
b = int(input("შეიყვანეთ მეორე კათეტის სიგრძე: "))
c = (a**2 + b**2) ** 0.5
s =(a * b) / 2
print("ჰიპოტენუზის სიგრძე არის:", c)
print("ფართობი:", s)

wami_raodenoba = int(input("შეიყვანეთ წამების რაოდენობა:"))
saati = wami_raodenoba // 3600
nashti = wami_raodenoba % 3600
wuti = nashti // 60
wami = nashti % 60
print(saati, "საათი", wuti, "წუთი", wami, "წამი",)

