
# 1- Girilen 2 sayıdan hangisi büyüktür?
print("1. Sorunun Çözümü: ")
a = int(input("a: "))
b = int(input("b: "))

result = (a > b)
print(f"a: {a} b: {b} den büyüktür: {result}")

print("-"*50)

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
print("2. Sorunun Çözümü: ")

vize1 = float(input("1. vize: "))
vize2 = float(input("2. vize: "))
final = float(input("final: "))

ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)

print(f"not ortalamanız : {ortalama} ve dersten geçme durumunuz: {ortalama>=50}")

print("-"*50)

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
print("3. Sorunun Çözümü: ")

sayi = int(input("sayı: "))
tekcift = (sayi % 2 == 0)

# """ verilen sayı bilgisinin mod 2 sini aldığımızda eğer sonuç sıfıra eşitse sayıya çift diyebiliriz. Yani sayıyı sürekli 2 ye bölüp sonunda da kalan sıfır oluyorsa sayıya çift diyebiliriz. """

print(f"girilen sayının çift olma durumu: {tekcift}")

print("-"*50)

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.
print("4. Sorunun Çözümü: ")

sayi = int(input("sayı: "))
pozitifmi = (sayi > 0)

print(f"girilen sayının pozitif olma durumu: {pozitifmi}")

print("-"*50)

# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
# (email:email@sadikturan.com parola:abc123)
print("5. Sorunun Çözümü: ")

email = "email@sadikturan.com"
password = "abc123"

girilenEmail = input("email: ")
girilenPassword = input("parola: ")

isEmail = (email == girilenEmail.strip())
isPassword = (password == girilenPassword.strip())

# strip() metodu ile girilen değerlerin başlangıcında veya sonunda bırakılan boşluklar silinir.

print(f"Email bilgisi doğru mu: {isEmail} ve Parola doğru mu: {isPassword}")
