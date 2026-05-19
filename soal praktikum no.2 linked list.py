class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_akhir(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def traversal(self):
        curr = self.head
        res = []
        while curr:
            res.append(str(curr.data))
            curr = curr.next
        # Menggunakan simbol panah ( -> ) sesuai gambar
        print(" -> ".join(res))

    def searching(self, key):
        print(f"\nCari data {key}:")
        curr = self.head
        while curr:
            if curr.data == key:
                print("Data ditemukan")
                return True
            curr = curr.next
        print("Data tidak ditemukan")
        return False

    def delete_node(self, key):
        print(f"\nHapus data {key}:")
        curr = self.head
        
        # Jika data yang dihapus ada di head
        if curr and curr.data == key:
            self.head = curr.next
            return
        
        # Mencari data yang akan dihapus
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        
        # Jika data ditemukan, sambungkan pointer
        if curr:
            prev.next = curr.next

# Menjalankan simulasi agar output persis seperti di gambar
def main():
    ll = LinkedList()
    
    # 1. Insert data
    print("Insert: 10, 20, 30, 40")
    for val in [10, 20, 30, 40]:
        ll.insert_akhir(val)
    
    # 2. Hasil Linked List
    print("\nHasil Linked List:")
    ll.traversal()
    
    # 3. Cari data
    ll.searching(30)
    
    # 4. Hapus data dan tampilkan hasil akhir
    ll.delete_node(20)
    ll.traversal()

if __name__ == "__main__":
    main()