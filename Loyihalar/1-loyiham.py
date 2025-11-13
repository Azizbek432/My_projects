import random
son = random.randint(1,100)

taxmin = int(input("1 dan 100 gacha son o'yladim.Topib ko'ringchi?"))

if taxmin == son:
    print("Barakalla! To'g'ri topdingiz.")
else:
    print(f"Afsus , men {son} sonini o'ylagandim.")
