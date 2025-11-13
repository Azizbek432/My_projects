import random

rekord = None

def bahola(farq):
    if farq == 0:
        return "To‘g‘ri topdingiz! 🎉"
    elif farq <= 1:
        return "Qaynoq! 🔥"
    elif farq <= 3:
        return "Iliq 😊"
    elif farq <= 5:
        return "Yomg‘irli ob-havo 🌧️"
    elif farq <= 10:
        return "Sovuq ❄️"
    else:
        return "Izg‘irin! 🥶"

def oyin_boshlash():
    global rekord
    davom_et = True

    while davom_et:
        ism = input("Ismingizni kiriting: ").capitalize()
        print(f"\nXush kelibsiz, {ism}! Men 1 dan 100 gacha son o‘yladim.")
        sirli_son = random.randint(1,100)
        urinishlar = 0

        while True:
            try:
                taxmin = int(input("Taxminingizni kiriting: "))
                urinishlar += 1
                farq = abs(taxmin - sirli_son)
                print(bahola(farq))

                if taxmin == sirli_son:
                    print(f"Siz {urinishlar} urinishda topdingiz!")
                    if rekord is None or urinishlar < rekord:
                        rekord = urinishlar
                        print("Yangi rekord! 🏆")
                    else:
                        print(f"Rekord: {rekord} urinish.")
                    break
            except ValueError:
                print("Iltimos, faqat butun son kiriting.")

        yana = input("Yana oynaysizmi? (ha/yo'q): ").lower()
        if yana != "ha":
            davom_et = False
            print("O'yin tugadi. Xayr! 👋")

oyin_boshlash()