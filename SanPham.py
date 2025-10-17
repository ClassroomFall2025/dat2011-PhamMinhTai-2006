class SP:
    def __init__(self,ten_san_pham,gia_ban,giam_gia):
        self.__ten_san_pham=ten_san_pham
        self.__gia_ban=gia_ban
        self.__giam_gia= giam_gia
    def get_ten(self):
        return self.__ten_san_pham
    
    def set_ten(self,ten_san_pham):
        self.__ten_san_pham=ten_san_pham

    def get_gia(self):
        return self.__gia_ban
    def set_gia(self,gia_ban):
        if gia_ban >= 0:
            self.__gia_ban=gia_ban
        else:
            print("giá bán không hợp lệ")

    def get_giam_gia(self):
        return self.__giam_gia
    def set_giam_gia(self,giam_gia):
        if 0 <= giam_gia <= self.__gia_ban:
            self.__giam_gia=giam_gia
        else:
            print("giảm giá không hợp lệ")
            
    def Thue_NK(self):
        return self.__gia_ban*0.1
    
    def nhap_thong_tin(self):
        self.__ten_san_pham=input("nhập tên sản phẩm")
        self.__gia_ban=float(input("nhập giá bán"))
        self.__giam_gia=float(input("nhập giảm giá"))

    def xuat(self):
        print(f"Tên sản phẩm: {self.__ten_san_pham}, giá bán: {self.__gia_ban}, giảm giá: {self.__giam_gia}, thuế nhập khẩu: {self.Thue_NK()}")
    def __str__ (self):
        return f"Tên sản phẩm: {self.__ten_san_pham}, giá bán: {self.__gia_ban}, giảm giá: {self.__giam_gia}, thuế nhập khẩu: {self.Thue_NK()}"    
    
