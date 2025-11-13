yosh = input("Yoshingizni kiriting:")
if yosh.isdigit():
    yosh = int(yosh)
    if yosh < 7:
        print("Siz 7 yoshdan kichiksiz.")
    elif yosh < 18: 
        print("Siz 7 yoshdan katta,lekin 18 yoshdan kichik ekansiz.")
    elif yosh < 65:
        print("Siz 18 yoshdan katta, lekin 65 yoshdan kichik ekansiz.")
    else:
        print("Siz 65 yoshdan kattasiz.")
else:
    print("Xatolik!Iltimos to'g'ri yoshni kiriting.")