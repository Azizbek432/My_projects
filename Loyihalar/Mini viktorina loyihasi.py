print("Mini Viktorinaga xush kelibsiz!")
print("Har bir savol uchun A,B,C, variantlardan birini belgilang.")
score = 0
print("1.Dunyoning ishlari asarini kim yozgan?")
print("A)Igor Sergeyev")
print("B)O'tkir Hoshimov")    
print("C)Anvar Narzullayev")  
javob1 = input("Javob:").strip().lower()
if javob1 == "b":
    print("To'g'ri!")
    score += 1
else:
    print("Noto'g'ri!To'g'ri javob:B")
print("2.Pythonda input funksiyasi nimani bajaradi?")
print("A)Ingliz tilini o'rgatadi")
print("B)Foydalanuvchidan qiymat oladi")
print("C)Chiroyli yozishni o'rgatadi")
javob2 = input("Javob:").strip().lower()
if javob2 == "b":
    print("To'g'ri!")
    score += 1
else:
    print("Noto'g'ri!To'g'ri javob:B")
print("3.Ingliz tilida Math nima degani?")
print("A)Matematika")
print("B)Kitob")
print("C)Daftar")
javob3 = input("Javob:").strip().lower()
if javob3 == "a":
    print("To'g'ri!Siz bilimdon ekansiz!")
    score += 1
else:
    print("Noto'g'ri!To'g'ri javob: B")
print("4.Shaxmatda ot qanday yuradi?")
print("A)Ikki oyoqlab")
print("B)Tog'ri gorintal bo'ylab")
print("C)L shaklida yuradi")
javob4 = input("Javob:").strip().lower()
if javob4 == "c":
    print("To'g'ri!")
    score += 1
else:
    print("Noto'g'ri!To'g'ri javob: C")
print(f"Tabriklaymiz!Sizning umumiy ballingiz: {score}/4.")
if score == 4:
    print("Ajoyib!Siz haqiqiy dahosiz!")
elif score >= 2:
    print("Yaxshi yana biroz mashq qilsangiz,zo'r bo'ladi.")
else:
    print("Bu safar omadingiz kelmadi.Qayta urinib ko'ring!")