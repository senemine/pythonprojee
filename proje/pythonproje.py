class Library:
 
    def __init__(self):
        self.dosya = open("books.txt", "a+")
        
    def __del__(self):
        self.dosya.close()
        
    def kitap_listele(self):
        self.dosya.seek(0)
        kitap_satir = self.dosya.read().splitlines()
        
        if not kitap_satir:
            print("Kitap listesi boş!\n")
        else:
            print("Kayıtlı Kitapların Listesi\n")
            for satir in kitap_satir:
                kitap_satir = satir.split(',')
                print(f"Kitap adı: {kitap_satir[0]} , Yazarı: {kitap_satir[1]}\n")
    
    def kitap_ekle(self):
        kitap_adi = input("Kitap Adı:")
        yazar = input("Yazar Adı:")
        yayin_yili = input("Yayın Yılı:")
        sayfa_sayisi = input("Sayfa Sayısı:")
        
        kitap_bilgisi = f"{kitap_adi}, {yazar}, {yayin_yili}, {sayfa_sayisi}\n"
        self.dosya.write(kitap_bilgisi)
        print(f"{kitap_adi} kitabı listeye eklendi.\n")
        
    def kitap_sil(self):
        ad_ile_silme = input("Silmek istediğiniz Kitabın adını giriniz: ")
        self.dosya.seek(0)
        kitap_baslik = self.dosya.read().splitlines()
        kitap_bulundu = False

        with open("books.txt", "w") as dosya:
            for satir in kitap_baslik:
                kitap_adı = satir.split(',')[0]
                if kitap_adı.strip() == ad_ile_silme.strip():
                    print(f"{ad_ile_silme} kitabı silindi.\n")
                    kitap_bulundu = True
                else:
                    dosya.write(satir + '\n')  
                    if kitap_bulundu:
                        break  

            if not kitap_bulundu:
                print(f"{ad_ile_silme} kitabı bulunamadı.\n")

lib = Library()
while True:
    print("Kütüphane Yönetim Sistemi")
    print("------Menü İşlemleri-----")
    print("1- Kitapları Listele")
    print("2- Kitap Ekle")
    print("3- Kitap Sil")
    print("4- Çıkış")
      
    menu_secim = input("Yapmak İstediğiniz İşlemin Numarasını Giriniz: ")
    if menu_secim == "1":
        lib.kitap_listele()
    elif menu_secim == "2":
        print("Yeni Kitap Ekleme\n")
        lib.kitap_ekle()
    elif menu_secim == "3":
        print("Kitap Silme\n")
        lib.kitap_sil()
    elif menu_secim == "4":
        print("Sistem Kapatıldı.\n")
        break
    else:
        print("Lütfen Geçerli Bir İşlem Numarası Giriniz!\n")
