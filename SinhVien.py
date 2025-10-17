
class SinhVienPoly:
    def __init__(self, ten_sinh_vien, nganh_hoc):
        self.ten_sinh_vien = ten_sinh_vien
        self.nganh_hoc = nganh_hoc
    def set_diem(self,diem:float) -> None:
        """Hàm này để set điểm cho sinh vien"""
        if 0 <= diem <= 10:
            self.diem = diem
        else:
            raise ValueError("Điểm phải nằm trong khoảng từ 0 đến 10!")

    def nhap_tt(self):
        self.ten_sinh_vien=input("Họ và tên")
        self.nganh_hoc=input("Ngành Học:")
        
        
    def get_diem(self):
        return self.diem
    
    def get_hoc_luc(self):
        if 10> self.get_diem() >= 9:
            return "xuất sắc"
        elif self.get_diem() >= 8:
            return "Giỏi"
        elif self.get_diem() >= 7:
            return "Khá"
        elif self.get_diem() >= 5:
            return "trung bình"
        elif self.get_diem() < 5:
            return "Rớt Môn"
        
    def xuat_tt(self):
        print(f"Họ và tên: {self.ten_sinh_vien}, Ngành học: {self.nganh_hoc}, Điểm trung bình: {self.get_diem():.2f}, Học Lực: {self.get_hoc_luc()}")  
    def __str__(self):
        return f"Họ và tên: {self.ten_sinh_vien}, Ngành học: {self.nganh_hoc},Điểm trung bình: {self.get_diem():.2f}, Học Lực: {self.get_hoc_luc()}"


class SinhVienIT(SinhVienPoly):
    def __init__(self, ten_sinh_vien, nganh_hoc, java, html, css):
        super().__init__(ten_sinh_vien, nganh_hoc)
        self.java = java
        self.html = html
        self.css = css 
    
    def nhap_tt(self):
        super().nhap_tt()
        self.java=int(input("điểm java:"))
        self.html=int(input("điểm html:"))
        self.css=int(input("điểm css:"))

    def get_diem(self):
        return (self.java*2 + self.html + self.css)/4 
    

class SinhVienBiz(SinhVienPoly):
    def __init__(self, ten_sinh_vien, nganh_hoc, marketing, sales):
        super().__init__(ten_sinh_vien, nganh_hoc)
        self.marketing = marketing
        self.sales = sales

    def nhap_tt(self):
        super().nhap_tt()
        self.marketing = float(input("Nhập điểm Marketing: "))
        self.sales = float(input("Nhập điểm Sales: "))

    def get_diem(self):
        return (self.marketing + self.sales)/2