import base64

def base64_coz(veri):
    try:
        # Veriyi byte tipine çeviren kod.
        cozulmus_byte = base64.b64decode(veri)
        # Metni utf-8 formatında stringe dönüştüren kod.
        return cozulmus_byte.decode('utf-8')
    except Exception as e:
        return f"Hata: Geçersiz Base64 formatı! ({e})"

# Base64 girilecek yer.
girdi = input("Çözmek istediğin Base64 metnini yapıştır: ")
sonuc = base64_coz(girdi)

print("-" * 20)
print(f"Sonuç: {sonuc}")
