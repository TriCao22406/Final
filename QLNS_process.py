class Nhanvien_TTca_nhan():  # class này cần def them hàm get image của nhân sự để hiển thị lên trang cá nhân nhâ
   def __init__(self,manv,tennv,ngaysinh,gt,sdt,email,diachi,hocvan,):
      self.manv = manv
      self.tennv = tennv
      self.ngaysinh = ngaysinh
      self.gt = gt
      self.sdt = sdt
      self.email = email
      self.diachi = diachi
      self.hocvan = hocvan
      # class này có cần def getimage vào đề show infor tren trang cá nhân không nhỉ
class  thongtinluong(Nhanvien_TTca_nhan):
   def __init__(self,manv,tennv,ngaysinh,gt,sdt,email,diachi,hocvan,bophan,vitri,noilamviec,Bacluong,Donvitiente,Phucap,BHYT,BHXH,Trocap,Luongthang13):
      super().__init__(manv,tennv,ngaysinh,gt,sdt,email,diachi,hocvan)
      self.bophan= bophan
      self.vitri = vitri
      self.noilamviec= noilamviec
      self.bacluong= Bacluong
      self.phucap= Phucap
      self.BHYT = BHYT
      self.BHXH = BHXH
      self.trocap= Trocap
      self.tiente= Donvitiente
      self.luongthang13 = Luongthang13

