money = int(input("Vvodite summu, kotoruy planiruete pologit` pod procenty:"))
per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}

TKB = int((per_cent['TKB']) * (money/100))
SKB = int((per_cent['SKB']) * (money/100))
VTB = int((per_cent['VTB']) * (money/100))
SBER = int((per_cent['SBER']) * (money/100))

deposit = [TKB, SKB, VTB, SBER]
print("Nakoplennye sredstva za god vklada v kagdom iz bankov=",deposit)
print("Maksimalnaya summa,kotoruy vy mogete zarabotat`:", max(deposit))