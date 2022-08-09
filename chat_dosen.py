import configparser as confp

class chat_dos:
    def __init__(self,nama_data):
        self.conf = confp.ConfigParser()
        self.conf.read(nama_data)
    
    def tulis(self):
        self.nama_asli = self.conf['mahasiswa']['NAMA']
        # nama_asli = input("Tuliskan Nama Lengkap:\n")
        # nama_asli = nama_asli if nama_asli!="" else "Rizal Mujahiddan"

        self.nim = self.conf['mahasiswa']['NIM']
        # self.nim       = input("\nTuliskan NIM Anda:\n")
        # self.nim       = self.nim if self.nim!="" else "G64190069"

        self.jurusan = self.conf['mahasiswa']['JURUSAN']
        # self.jurusan   = input("\nTuliskan self.jurusan anda:\n")
        # self.jurusan   = self.jurusan if self.jurusan!="" else "Ilmu Komputer"

        self.pembukaan = "Assalamualaikum wr.wb. Kenalkan Nama saya {} ({}) Jurusan {}. ".format(self.nama_asli,self.nim,self.jurusan)

        self.nama_dosen = self.conf['dosen']['NAMA']
        # self.nama_dosen = input("\nMasukkan self.nama_dosen:\n")
        # self.nama_dosen = self.nama_dosen if self.nama_dosen!="" else "Wulandari"

        self.jk_dosen = self.conf['dosen']['JK']
        # self.jk_dosen   = input("\njenis kelamin(L/P):\n").lower()
        # self.jk_dosen   = self.jk_dosen if self.jk_dosen!="" else "p"

        self.nama_dosen = "Ibu" if self.jk_dosen[0]=="p" else "Pak" + self.nama_dosen

        self.maaf = "Maaf apabila mengganggu waktu {}. ".format(self.nama_dosen)
        self.keperluan = input("\nTuliskan Keperluan Anda:\n")
        self.penutup = ". Terima kasih atas perhatiannya. Waalaikumussalam wr.wb"

        tulisan_wa = self.pembukaan + self.maaf + self.keperluan + self.penutup
        return ("\n\n\n\n"+tulisan_wa)

cek_chat = chat_dos('data_chat_dosen.conf').tulis()
print(cek_chat)