def hitung_biaya_pengiriman(berat, jarak, jenis_pengiriman, status_member): 
    # Biaya dasar pengiriman
    total_biaya = 10000 
    
    # Tambahan biaya jika berat lebih dari 5 kg
    if berat > 5:
        total_biaya += 5000

    # Tambahan biaya jika jarak lebih dari 10 km
    if jarak > 10:
        total_biaya += 8000
    
    # Tambahan biaya jika memilih pengiriman express
    if jenis_pengiriman == "express":
        total_biaya += 20000
    
    # Diskon 10% untuk member
    if status_member:
        diskon = total_biaya * 10/100
        total_biaya -= diskon
    
    return total_biaya

# Mengambil input dari user
berat = float(input("Masukkan berat barang dalam kg: "))
jarak = float(input("Masukkan jarak dalam km: "))
jenis_pengiriman = input("Pilih jenis pengiriman (express/normal): ").lower()
status_member = input("Apakah Anda member (ya/tidak): ").lower()

# Menghitung total biaya pengiriman
biaya = hitung_biaya_pengiriman(berat, jarak, jenis_pengiriman, status_member == "ya")

# Menampilkan total biaya pengiriman
print(f"Total biaya pengiriman: Rp{biaya}")
