class Node:
    def __init__(self, judul, penyanyi):
        self.judul = judul
        self.penyanyi = penyanyi
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def tambah_lagu(self, judul, penyanyi):
        new_node = Node(judul, penyanyi)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            self.current = self.head
        else:
            last = self.head.prev
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node

    def hapus_lagu(self, judul):
        if not self.head: return
        curr = self.head
        while True:
            if curr.judul.lower() == judul.lower():
                if curr == self.head and curr.next == self.head:
                    self.head = None
                    self.current = None
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    if curr == self.head: self.head = curr.next
                    if curr == self.current: self.current = curr.next
                return
            curr = curr.next
            if curr == self.head: break

    def tampilkan_playlist(self):
        if not self.head:
            print("\nPlaylist Kosong.")
            return
        
        # Format Playlist:
        print("\nPlaylist:")
        curr = self.head
        no = 1
        while True:
            print(f"{no}. {curr.judul} - {curr.penyanyi}")
            curr = curr.next
            no += 1
            if curr == self.head: break
        
        # Format Now Playing & Next Lagu
        if self.current:
            print("\nNow Playing:")
            print(f"{self.current.judul} - {self.current.penyanyi}")
            
            print("\nNext Lagu:")
            print(f"{self.current.next.judul} - {self.current.next.penyanyi}")

    def next_lagu(self):
        if self.current:
            self.current = self.current.next

    def prev_lagu(self):
        if self.current:
            self.current = self.current.prev

    def cari_lagu(self, judul):
        curr = self.head
        if not curr: return
        while True:
            if curr.judul.lower() == judul.lower():
                print(f"\nData ditemukan: {curr.judul} - {curr.penyanyi}")
                return
            curr = curr.next
            if curr == self.head: break
        print("\nLagu tidak ditemukan.")

def menu_playlist():
    pl = CircularDoublyLinkedList()
    
    # Inisialisasi data awal sesuai gambar agar langsung muncul saat di-run
    pl.tambah_lagu("Hati-Hati di Jalan", "Tulus")
    pl.tambah_lagu("Monokrom", "Tulus")
    pl.tambah_lagu("Sial", "Mahalini")

    while True:
        print("\n===== MENU PLAYLIST =====")
        print("1. Tambah Lagu")
        print("2. Hapus Lagu")
        print("3. Tampilkan Playlist")
        print("4. Next Lagu")
        print("5. Prev Lagu")
        print("6. Cari Lagu")
        print("7. Keluar")
        
        pilihan = input("Pilihan: ")
        
        if pilihan == '1':
            j = input("Masukkan Judul Lagu: ")
            p = input("Masukkan Nama Penyanyi: ")
            pl.tambah_lagu(j, p)
        elif pilihan == '2':
            j = input("Masukkan Judul Lagu yang akan dihapus: ")
            pl.hapus_lagu(j)
        elif pilihan == '3':
            pl.tampilkan_playlist()
        elif pilihan == '4':
            pl.next_lagu()
            pl.tampilkan_playlist() # Langsung tampilkan output seperti di kertas
        elif pilihan == '5':
            pl.prev_lagu()
            pl.tampilkan_playlist()
        elif pilihan == '6':
            j = input("Cari Judul Lagu: ")
            pl.cari_lagu(j)
        elif pilihan == '7':
            print("Keluar dari program...")
            break

if __name__ == "__main__":
    menu_playlist()