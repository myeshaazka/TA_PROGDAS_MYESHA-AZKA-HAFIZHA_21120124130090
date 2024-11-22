#import library
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 

class ConcertTicketBooking:
    def __init__(self, apk):
        self.master = apk
        self.master.title("Pemesanan Tiket Konser")
        
        self.selected_seat = None
        self.selected_category = None
        self.seats = {"VIP": {}, "Festival": {}, "Cat": {}}  # Status kursi berdasarkan kategori
        
        self.create_seats()  # Membuat kursi grid
        self.create_ui()

    def create_seats(self):
        # Membuat grid kursi dan menginisialisasi semua kursi sebagai kosong (False)
        categories = ["VIP", "Festival", "Cat"]
        for category in categories:
            for row in range(5):
                for col in range(5):
                    seat_number = f"{row+1}-{col+1}"
                    self.seats[category][seat_number] = False

    def create_ui(self):
        # Membuat tampilan UI untuk pemilihan kategori kursi dan kursi.
        font_style = ("Arial", 14)
        bg_color = 'lightblue'

        # Frame utama untuk aplikasi
        self.frame_main = tk.Frame(self.master, bg='lightblue')
        self.frame_main.pack(fill="both", expand=True)

        # Menambahkan label judul di jendela utama
        label_title = tk.Label(self.frame_main, text="Pemesanan Tiket Konser", font=("Arial", 20), bg=bg_color)
        label_title.grid(row=0, column=0, columnspan=5, pady=20, sticky="ew")  # Judul berada di tengah secara horizontal

        # Tampilan Pemilihan Kategori Kursi
        self.frame_category = tk.Frame(self.frame_main, bg='lightblue')
        self.frame_category.grid(row=1, column=0, columnspan=5, pady=20)

        # Menambahkan label kategori di tengah
        label_category = tk.Label(self.frame_category, text="Pilih Kategori Kursi", font=("Arial", 16), bg=bg_color)
        label_category.grid(row=0, column=0, columnspan=3, pady=10, sticky="ew")

        # Memuat gambar untuk kategori VIP, Festival, dan Cat
        self.vip_image = self.load_image("vip.jpg")

        # Menambahkan gambar di atas tombol kategori
        label_vip_image = tk.Label(self.frame_category, bg=bg_color)
        label_vip_image.grid(row=1, column=0, padx=10, pady=10)
        button_vip = tk.Button(self.frame_category, text="VIP", width=20, height=2, command=lambda: self.select_category("VIP"))
        button_vip.grid(row=2, column=0, padx=10, pady=10)

        label_festival_image = tk.Label(self.frame_category, image=self.vip_image, bg=bg_color)
        label_festival_image.grid(row=1, column=1, padx=10, pady=10)
        button_festival = tk.Button(self.frame_category, text="Festival", width=20, height=2, command=lambda: self.select_category("Festival"))
        button_festival.grid(row=2, column=1, padx=10, pady=10)

        label_cat_image = tk.Label(self.frame_category, bg=bg_color)
        label_cat_image.grid(row=1, column=2, padx=10, pady=10)
        button_cat = tk.Button(self.frame_category, text="Cat", width=20, height=2, command=lambda: self.select_category("Cat"))
        button_cat.grid(row=2, column=2, padx=10, pady=10)

    def load_image(self, image_path):
        # Memuat gambar menggunakan Pillow dan mengubahnya menjadi format yang sesuai untuk Tkinter
        image = Image.open(image_path)
        image = image.resize((240, 240))  
        return ImageTk.PhotoImage(image)

    def select_category(self, category):
        # pemilihan kategori kursi
        self.selected_category = category
        self.frame_category.grid_forget()  # Sembunyikan frame kategori kursi
        
        # Jika kategori Festival, langsung ke form data diri
        if self.selected_category == "Festival":
            self.show_biodata_form()
        else:
            # Tampilkan frame pemilihan kursi untuk kategori yang dipilih
            self.frame_seat = tk.Frame(self.frame_main, bg='lightblue')
            self.frame_seat.grid(row=2, column=0, columnspan=5, pady=20)

            # Menampilkan judul kategori kursi yang dipilih
            label_category_selected = tk.Label(self.frame_seat, text=f"Kategori Kursi: {self.selected_category}", font=("Arial", 16), bg='lightblue')
            label_category_selected.grid(row=0, column=0, columnspan=5, pady=10, sticky="ew")

            # Menampilkan grid kursi berdasarkan kategori yang dipilih
            self.seat_buttons = []
            for row in range(5):
                row_buttons = []
                for col in range(5):
                    seat_number = f"{row+1}-{col+1}"
                    button = tk.Button(self.frame_seat, text=seat_number, width=16, height=3,
                                       command=lambda sn=seat_number: self.select_seat(sn))
                    button.grid(row=row+1, column=col)
                    row_buttons.append(button)
                self.seat_buttons.append(row_buttons)

            # Tombol untuk melanjutkan ke form data diri
            next_button = tk.Button(self.frame_seat, text="Lanjutkan ke Form Data Diri", font=("Arial", 14), command=self.show_biodata_form)
            next_button.grid(row=6, column=0, columnspan=5, pady=20)

    def show_biodata_form(self):
        # Menampilkan form untuk memasukkan data diri setelah memilih kategori
        # Sembunyikan kursi dan kategori
        if hasattr(self, 'frame_seat'):
            self.frame_seat.grid_forget()

        # Frame untuk form data diri
        self.frame_biodata = tk.Frame(self.frame_main, bg='lightblue')
        self.frame_biodata.grid(row=2, column=0, columnspan=5, pady=20)

        label_nama = tk.Label(self.frame_biodata, text="Masukkan Nama Penerima", font=("Arial", 14), bg='lightblue')
        label_nama.grid(row=0, column=2, pady=10)
        self.entry_nama = tk.Entry(self.frame_biodata)
        self.entry_nama.grid(row=0, column=3)

        label_alamat = tk.Label(self.frame_biodata, text="Masukkan Alamat Email", font=("Arial", 14), bg='lightblue')
        label_alamat.grid(row=1, column=2, pady=5)
        self.entry_alamat = tk.Entry(self.frame_biodata)
        self.entry_alamat.grid(row=1, column=3)

        label_noHP = tk.Label(self.frame_biodata, text="No. HP", font=("Arial", 14), bg='lightblue')
        label_noHP.grid(row=2, column=2, pady=5)
        self.entry_noHP = tk.Entry(self.frame_biodata)
        self.entry_noHP.grid(row=2, column=3)

        # Tombol Submit untuk menyelesaikan pemesanan
        submit_button = tk.Button(self.frame_biodata, text="Pesan Tiket", font=("Arial", 14), command=self.submit_data)
        submit_button.grid(row=3, column=3, columnspan=2, pady=20)

    def select_seat(self, seat_number):
        # pemilihan kursi
        if self.selected_seat:
            # Reset warna kursi yang sebelumnya dipilih
            prev_row, prev_col = map(int, self.selected_seat.split('-'))
            self.seat_buttons[prev_row-1][prev_col-1].config(bg="SystemButtonFace")
        
        self.selected_seat = seat_number
        row, col = map(int, seat_number.split('-'))
        self.seat_buttons[row-1][col-1].config(bg="lightgreen")

    def submit_data(self):
        # Menerima pemesanan dan menampilkan informasi.
        nama = self.entry_nama.get()
        alamat = self.entry_alamat.get()
        noHp = self.entry_noHP.get()
        
        if not nama or not alamat or not noHp:
            messagebox.showwarning("Peringatan", "Silakan lengkapi semua data.")
            return
        
        # Tampilkan pesan sukses
        messagebox.showinfo("Sukses", f"Tiket untuk kursi {self.selected_seat if self.selected_category != 'Festival' else 'Festival'} berhasil dipesan!\n\nNama: {nama}\nAlamat Email: {alamat}\nNo HP: {noHp}")
        
        # Kembali ke halaman awal setelah sukses
        self.frame_biodata.grid_forget()  # Sembunyikan form data diri
        self.create_ui()  

if __name__ == "__main__":
    root = tk.Tk()
    app = ConcertTicketBooking(root)
    root.resizable(False, False)
    root.geometry("600x650")  
    root.mainloop()
