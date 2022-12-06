#siswa.py
from person import Person

class Siswa(Person):
  def __init__(self, nama, alamat,ktp,nim):
    super().__init__(alamat, nama,kp)
    self.nim = nim

  def tampil(self):
    print('nama = ',self.nama,'alamat = ',self.alamat,'nim = ',self.nim,'ktp = ',self.ktp,'')
