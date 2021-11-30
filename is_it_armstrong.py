while True:
    num = int(input("Sayı Gir"))
    num2 = str(num)
    lenght = len(num2)
    toplam = 0
    for i in num2:
        force = int(i) ** lenght
        toplam += force

    if toplam == num:
        print("{}' sayısı Bir ARMSTRONG sayısıdır.".format(num))
    else:
        print("{}'sayısı birr armstrong sayısı değildir.".format(num))


    



