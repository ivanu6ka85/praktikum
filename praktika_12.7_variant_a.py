per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
money= int(input("Vvedite summu vklada:"))

deposit_tkb = per_cent['TKB'] 
print(int(deposit_tkb*money/100))

deposit_skb = per_cent["SKB"] 
print(int(deposit_skb*money/100))

deposit_vtb = per_cent['VTB'] 
print(int(deposit_vtb*money/100))

deposit_sber = per_cent['SBER'] 
print(int(deposit_sber*money/100))


deposit_i = [int(deposit_tkb*money/100), int(deposit_skb*money/100), int(deposit_vtb*money/100),int(deposit_sber*money/100)]
print(deposit_i)
print("Maksimal`naya summa, kotoruy vy mogete zarabotat`:",max(deposit_i),"v banke:", 'SKB'  )