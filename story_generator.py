import random
from colorama import Fore, Style, init

init(autoreset=True)

# --- Şablon Veri Setleri ---

karakterler = ["Gizemli Bilim Adamı", "Cesur Kedi", "Uzaylı Komutan", "Robot Tamirci"]
eylemler = [
    "bir zaman kapsülü keşfetti",
    "gökyüzünde uçan balıkları gördü",
    "kayıp bir hazinenin peşine düştü",
    "bir sihirli formül buldu"
]
mekanlar = [
    "terk edilmiş bir kütüphanede",
    "Mars'ın en yüksek dağında",
    "okyanusun dibindeki kristal şehirde",
    "büyük bir ormanın derinliklerinde"
]
sonuclar = [
    "ve dünyayı kurtardı.",
    "ancak sadece bir fincan çay bulabildi.",
    "ve büyük bir parti verdi.",
    "ve öğrendi ki, macera her şeyden önemliydi."
]

# --- Kullanıcıdan Girdi Alma ---
print(Fore.CYAN + "=== Otomatik Hikaye Anlatıcısına Hoş Geldiniz! ===")
print("Hikayenin temelini oluşturalım.\n")

ana_karakter = input(Fore.YELLOW + "Hikayenin ana karakterinin adını/rolünü girin (örn: Genç Kaşif): ")
ana_mekan = input(Fore.YELLOW + "Hikayenin geçeceği ana mekanı girin (örn: Eski Şato): ")

# Boş bırakılırsa rastgele seçim yap
if not ana_karakter.strip():
    ana_karakter = random.choice(karakterler)
    print(Fore.MAGENTA + f"(Boş bırakıldı — karakter olarak '{ana_karakter}' seçildi.)")

if not ana_mekan.strip():
    ana_mekan = random.choice(mekanlar)
    print(Fore.MAGENTA + f"(Boş bırakıldı — mekan olarak '{ana_mekan}' seçildi.)")

# --- Hikaye Oluşturma ---
secilen_eylem = random.choice(eylemler)
secilen_sonuc = random.choice(sonuclar)

hikaye_sablonu = (
    f"\nBir zamanlar, {ana_mekan} isimli yerde yaşayan {ana_karakter} vardı.\n"
    f"Bir gün, {ana_karakter} uyandığında {secilen_eylem} ve bu onun hayatını değiştirdi.\n"
    f"Bu inanılmaz olay onu uzun bir yolculuğa çıkardı, {secilen_sonuc}"
)

print(Fore.GREEN + "\n--- İşte Senin Hikayen ---")
print(Style.BRIGHT + hikaye_sablonu)
print(Fore.GREEN + "---------------------------\n")
