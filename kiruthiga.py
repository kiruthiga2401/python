# f=open(r"C:\Users\keerthy\Desktop\task\filehandling\keerthyfile",'x')
# f=open(r"C:\Users\keerthy\Desktop\task\filehandling\keerthyfile")
# # print(f.read())
# with open (r"C:\Users\keerthy\Desktop\task\filehandling\keerthyfile")as f:
#     print(f.read())
# with open(r"C:\Users\keerthy\Desktop\task\filehandling\keerthyfile","w")as f:
#     f.write("today i am in python class")
# f=open(r"C:\Users\keerthy\Desktop\task\filehandling\keerthyfile")
# print(f.readline())
# f.close()


# a=3

# try:
#     print(a)
# except:
#     print("error")
# # s=3
# try:
#     print(s)
# except:
#     print("error")
# else:
# #     print("crt") 
# # x=3
# try:
#     print(x)
# except:
#     print("wrong")
# finally:
#     print("eror")

# try:
#     f=open(r'C:\Users\keerthy\Desktop\task\filehandling\keerthyfile',"w")
#     f.write("hihihihihih")
# except:
#     print("wrong")
# finally:
#     print("ghjk")



mytup=('tomato','onion','potato')
for i in mytup:
    print(i)

lst=[1,3,4,6,5,7,9]
mylst=iter(lst)
print(next(mylst))
print(next(mylst))
print(next(mylst))
print(next(mylst))
print(next(mylst))
print(next(mylst))

class numbers:
    def __iter__(self):
        self.a=0
        return self
    def __next__(self):
        x=self.a
        self.a+=3
        return x
mynum=numbers()
myiter=iter(mynum)

print(next(myiter))
print(next(myiter))
print(next(myiter))


# class mynum:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         if self.a<=10:
#             x=self.a
#             self.a+=2
#             return x
        
#         else:
#             raise StopIteration
# mycs=mynum()
# myit=iter(mycs)
# for x in myit:
#     print(x)        