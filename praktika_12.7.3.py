per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
m= int(input("Vvedite summu vklada:"))#m=money

deposit_tkb = per_cent['TKB'] 
print(int(deposit_tkb*m/100))

deposit_skb = per_cent["SKB"] 
print(int(deposit_skb*m/100))

deposit_vtb = per_cent['VTB'] 
print(int(deposit_vtb*m/100))

deposit_sber = per_cent['SBER'] 
print(int(deposit_sber*m/100))


deposit_new = [int(deposit_tkb*m/100), int(deposit_skb*m/100), int(deposit_vtb*m/100),int(deposit_sber*m/100)]
print(deposit_new)
print("Maksimal`naya summa, kotoruy vy mogete zarabotat`:",max(deposit_new),"v banke:", 'SKB'  )