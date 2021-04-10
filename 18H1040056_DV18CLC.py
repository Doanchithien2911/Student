import math
import random
class Person:
    def __init__(self,n):
        self.so_sinh_vien=n
        self.age=[]
        self.name=[]
        self.gender=[]
    def ho_ten(self):
        for i in range(0,self.so_sinh_vien):
            hoten=str(input("nhap ho va ten sinh vien thu {} : ".format(i)))
            self.name.append(hoten)
        return self.name
    def tuoi(self):
        for i in range(0,self.so_sinh_vien):
            tuoisv=int(random.randrange(17,26))
            self.age.append(tuoisv)
        return self.age
    def gioi_tinh(self):
        for i in range(0,self.so_sinh_vien):
            sex=str(input("gioi tinh sinh vien thu {} : ".format(i)))
            self.gender.append(sex)
        return self.gender    
class StudentList(Person):
    def __init__(self,n):
        super().__init__(n)
        self.id=[]
        self.cl=[]
        self.grade=[]
        self.danhsach={}
    def nhap_id(self):
        for i in range(0,self.so_sinh_vien):
            idcard=int(input("nhap so id cho sinh vien thu {} : ".format(i)))
            self.id.append(idcard)
        return self.id
    def lop_hoc(self):
        for i in range(0,self.so_sinh_vien):
            tenlop=str(input("nhap ten lop cho sinh vien thu {} : ".format(i)))
            self.cl.append(tenlop)
        return self.cl
    def diem_so(self):
        for i in range(0,self.so_sinh_vien):
            diem=int(input("nhao so diem cua sinh vien thu {} : ".format(i)))
            if diem < 0 or diem > 10:
                exit()
            self.grade.append(diem)
        return self.grade
    def danh_sach(self):
        for i in range(0,self.so_sinh_vien):
            a={"ho ten sinh vien {} ".format(i) :self.name[i] }
            self.danhsach.update(a)
            b={"tuoi sinh vien {} ".format(i) : self.age[i]}
            self.danhsach.update(b)
            c={"gioi tinh sinh vien {} ".format(i) : self.gender[i]}
            self.danhsach.update(c)
            d={"ma id cua sinh vien {} ".format(i) : self.id[i]}
            self.danhsach.update(d)
            e={"lop ho cua sinh vien {} ".format(i):self.cl[i]}
            self.danhsach.update(e)
            f={"diem cua sinh vien {} ".format(i):self.grade[i]}
            self.danhsach.update(f)
        return self.danhsach
class Kiemtra(StudentList):
    def __init__(self,n):
        super().__init__(n)
    def max_grade(self):
        maxi=max(self.grade)
        for i in range(0,self.so_sinh_vien):
            if self.grade[i] == maxi:
                vitri = i
        return  print(self.name[vitri],self.age[vitri],"tuoi", self.gender[vitri],"ma id" ,self.id[vitri],"lop",self.cl[vitri],"diem cao nhat",self.grade[vitri])
class Sophuc:            
    def __init__(self,thuc,ao):
        self.real=thuc
        self.image=ao
    def module_sophuc(self):
        z=math.sqrt((self.real)**2+(self.image)**2)
        return z
test=Kiemtra(3)
test.ho_ten()
test.tuoi()
test.gioi_tinh()
test.nhap_id()
test.lop_hoc()
test.diem_so()
print(test.danh_sach())
test.max_grade()