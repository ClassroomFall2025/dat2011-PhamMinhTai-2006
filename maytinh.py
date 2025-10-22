import random
import datetime

class BaiLamThem:
    def __init__(self):
        self.file_ghichu = "ghichu.txt"

    # 1. Tính toán cơ bản
    def tinh_toan(self):
        print("\n--- TÍNH TOÁN CƠ BẢN ---")
        try:
            a = float(input("Nhập số thứ nhất: "))
            b = float(input("Nhập số thứ hai: "))
            print("1. Cộng\n2. Trừ\n3. Nhân\n4. Chia")
            choice = input("Chọn phép tính (1-4): ")

            if choice == "1":
                print(f"Kết quả: {a} + {b} = {a + b}")
            elif choice == "2":
                print(f"Kết quả: {a} - {b} = {a - b}")
            elif choice == "3":
                print(f"Kết quả: {a} * {b} = {a * b}")
            elif choice == "4":
                if b != 0:
                    print(f"Kết quả: {a} / {b} = {a / b}")
                else:
                    print("Không thể chia cho 0!")
            else:
                print("Lựa chọn không hợp lệ!")
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")

    # 2. Xem thời gian hiện tại
    def xem_thoi_gian(self):
        now = datetime.datetime.now()
        print("\n--- THỜI GIAN HIỆN TẠI ---")
        print("Bây giờ là:", now.strftime("%H:%M:%S - %d/%m/%Y"))

    # 3. Ghi chú
    def ghi_chu(self):
        print("\n--- GHI CHÚ ---")
        note = input("Nhập ghi chú của bạn: ")
        with open(self.file_ghichu, "a", encoding="utf-8") as f:
            f.write(note + "\n")
        print("Đã lưu ghi chú vào file ghichu.txt")

    # 4. Đọc ghi chú
    def doc_ghi_chu(self):
        print("\n--- ĐỌC GHI CHÚ ---")
        try:
            with open(self.file_ghichu, "r", encoding="utf-8") as f:
                data = f.read()
                if data.strip():
                    print(data)
                else:
                    print("Chưa có ghi chú nào.")
        except FileNotFoundError:
            print("Chưa có file ghi chú. Hãy tạo ghi chú trước!")

    # 5. Random số may mắn
    def random_so(self):
        a=int(input("Nhập số bắt đầu:"))
        b=int(input("Nhập số kết thúc:"))
        print("======== RAMDOM SỐ NGẪU NHIÊN NHE =========")
        so=random.randint(a,b)
        print(f"Con Số may mắn hôm nay là:{so}")
        

    # Menu chính
    def menu(self):
        while True:
            print("\n========= MÁY TÍNH MINI =========")
            print("1. Tính toán")
            print("2. Xem thời gian hiện tại")
            print("3. Ghi chú")
            print("4. Đọc ghi chú")
            print("5. Random số may mắn")
            print("6. Thoát")
            chon = input("Chọn chức năng (1-6): ")

            if chon == "1":
                self.tinh_toan()
            elif chon == "2":
                self.xem_thoi_gian()
            elif chon == "3":
                self.ghi_chu()
            elif chon == "4":
                self.doc_ghi_chu()
            elif chon == "5":
                self.random_so()
            elif chon == "6":
                print("Tạm biệt!")
                break
            else:
                print("Lựa chọn không hợp lệ, vui lòng thử lại!")
