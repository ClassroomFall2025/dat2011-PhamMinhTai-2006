from SinhVien import *
class QuanLySinhVien:
    def __init__ (self):
        self.danh_sach_sinh_vien=[]
        self.menu = {
    0: "Thoát ứng dụng",
    1: "Nhập danh sách sinh viên",
    2: "Xuất thông tin danh sách sinh viên",
    3: "Xuất danh sách sinh viên có học lực giỏi",
    4: "Sắp xếp danh sách sinh viên theo điểm"
}
    def them_sinh_vien(self):
        self.danh_sach_sinh_vien.append(self.tao_sv_moi())
        
    def xuat_danh_sach(self):
        print("Danh sách sinh viên")
        for i ,sinhvien in enumerate(self.danh_sach_sinh_vien, start=1):
            print(f"sinh viên thứ: {i}",end=",")
            sinhvien.xuat_tt()

    def xuat_sv_gioi(self):
        print("danh sách sinh viên giỏi")
        SVgioi=[]
        for sinh_vien in self.danh_sach_sinh_vien:
            if sinh_vien.get_hoc_luc() == "Giỏi":
                SVgioi.append(sinh_vien)
        for i ,sinhvien in enumerate(SVgioi, start=1):
            print(f"sinh viên thứ: {i}",end=",")
            sinhvien.xuat_tt()

    def SXSV_theo_diem(self):
        self.danh_sach_sinh_vien.sort(key=lambda sinh_vien: sinh_vien.get_diem(),reverse=True)
        for i ,sinhvien in enumerate(self.danh_sach_sinh_vien, start=1):
            print(f"sinh viên thứ: {i}",end=",")
            sinhvien.xuat_tt()

    def xuat_menu(self):
        print("\n===============================")
        print("   CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
        print("===============================")
        for key, value in self.menu.items():
            print(f"{key}. {value}")
        print("===============================")
            
    def tao_sv_moi(self):
        print("\n--- Nhập thông tin sinh viên mới ---")
        ten = input("Họ và Tên: ").strip()
        nganh = input("Nhập ngành học: ").strip().lower()
        diem=float(input("Nhập vào điểm"))
        sinh_vien_moi = SinhVienPoly(ten, nganh)
        sinh_vien_moi.set_diem(diem)
        return sinh_vien_moi
