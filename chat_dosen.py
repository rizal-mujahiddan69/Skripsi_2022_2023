import configparser as confp

class chat_dos:
    def __init__(self):
        conf = confp.ConfigParser()
        conf.read('data_chat_dosen.conf')

        nama_asli = conf['mahasiswa']['NAMA']
        # nama_asli = input("Tuliskan Nama Lengkap:\n")
        # nama_asli = nama_asli if nama_asli!="" else "Rizal Mujahiddan"

        nim = conf['mahasiswa']['NIM']
        # nim       = input("\nTuliskan NIM Anda:\n")
        # nim       = nim if nim!="" else "G64190069"

        jurusan = conf['mahasiswa']['JURUSAN']
        # jurusan   = input("\nTuliskan jurusan anda:\n")
        # jurusan   = jurusan if jurusan!="" else "Ilmu Komputer"

        pembukaan = "Assalamualaikum wr.wb. Kenalkan Nama saya {} ({}) Jurusan {}. ".format(nama_asli,nim,jurusan)

        nama_dosen = conf['dosen']['NAMA']
        # nama_dosen = input("\nMasukkan nama_dosen:\n")
        # nama_dosen = nama_dosen if nama_dosen!="" else "Wulandari"

        jk_dosen = conf['dosen']['JK']
        # jk_dosen   = input("\njenis kelamin(L/P):\n").lower()
        # jk_dosen   = jk_dosen if jk_dosen!="" else "p"

        maaf = "Maaf apabila mengganggu waktu {} {}. ".format("Ibu" if jk_dosen[0]=="p" else "Bapak",nama_dosen)
        keperluan = input("\nTuliskan Keperluan Anda:\n")
        penutup = ". Terima kasih atas perhatiannya."

        tulisan_wa = pembukaan + maaf + keperluan + penutup
        return ("\n\n\n\n"+tulisan_wa)