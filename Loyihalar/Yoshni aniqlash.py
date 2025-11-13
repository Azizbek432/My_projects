from datetime import datetime

try:
    kun = int(input("Tug'ilgan kuningizni kiriting (1-31 gcha):"))
except ValueError:
    print("Xatolik yuz berdi.")
oy = int(input("Tug'ilgan oyingizni kiriting: (1-12):"))
yil = int(input("Tug'ilgan yilingizni kiriting:(masalan:2010)"))

tugilgan_sana = datetime(yil,oy,kun) 
bugun= datetime.now ()

if tugilgan_sana > bugun:
    print("Kelajakdagi sana kiritildi.Iltimos,to'g'ri sanani kiriting.")
else:
    farq = bugun - tugilgan_sana
kunlar = farq.days
yosh_yil = kunlar //365
yosh_kun = kunlar % 365
yosh_oy = yosh_kun % 30
print(f"Siz {yosh_yil} yil,{yosh_oy} oy va {yosh_kun} kundan beri yashayapsiz.Xudoga shukur qiling!!")
if yosh_yil >= 18:
    print("Siz voyaga yetgansiz.")
else:
    qolgan = 18 - yosh_yil
print(f"Siz hali voyaga yetmagansiz.Voyaga yetishingizga {qolgan} yil qoldi.")
