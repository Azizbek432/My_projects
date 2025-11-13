import string

parol = input("Parolingizni kiriting:")

ball = 0

if len(parol) >= 8:
    ball += 1

if any(harf.isupper() for harf in parol):
    ball += 1

if any(harf.islower() for harf in parol):
    ball += 1

if any(son.isdigit() for son in parol):
    ball += 1

if any(belgi in string.punctuation for belgi in parol):
    ball += 1

if ball <= 2:
    baho = "Juda zaif parol!"
elif ball == 3:
    baho = "Zaif parol!"
elif ball ==4:
    baho = "Yaxshi parol!"
else:
    baho = "Juda kuchli parol!"
print(f"Sizning parolingiz kuchi:{baho}")