class Mahasiswa:
    '''Dasar kelas Mahasiswa'''
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, program_studi, alamat, tgl_lahir):
        self.nama = nama
        self.nim = nim
        self.program_studi = program_studi
        self.alamat = alamat
        self.tgl_lahir = tgl_lahir
        Mahasiswa.jumlah_mahasiswa += 1

    def jumlah(self):
        print("Total Mahasiswa: ", Mahasiswa.jumlah_mahasiswa)

    def tampilkan_mahasiswa(self):
        print("Nama          : ", self.nama)
        print("NIM           : ", self.nim)
        print("Program Studi : ", self.program_studi)
        print("Alamat        : ", self.alamat)
        print("Tanggal Lahir : ", self.tgl_lahir)

mahasiswa1 = Mahasiswa("Vania Atalie Pratista", "M0119092", "Matematika", "Purbalingga", "24 Desember 2000")
mahasiswa2 = Mahasiswa("Nabila Shafia Indira", "M0119012", "Matematika", "Banjarnegara", "05 Januari 2002")
mahasiswa3 = Mahasiswa("Rizki Eka Oktavia", "M0119074", "Matematika", "Tegal", "05 Oktober 2001")
mahasiswa4 = Mahasiswa("Yessy Dwi Ramadhani", "M0119096", "Matematika", "Solo", "12 Mei 2001")
mahasiswa5 = Mahasiswa("Siti Roqhilu Yumaroh", "M0119082", "Matematika", "Tanjung Pinang", "22 Maret 2001")

mahasiswa1.tampilkan_mahasiswa()
mahasiswa2.tampilkan_mahasiswa()
mahasiswa3.tampilkan_mahasiswa()
mahasiswa4.tampilkan_mahasiswa()
mahasiswa5.tampilkan_mahasiswa()
print("Total Mahasiswa: ", Mahasiswa.jumlah_mahasiswa)
