# # 1. List 
# user = ["An", "Bình", "Chiến","Dũng"]
# print ("Danh sách user :", user)
# print(user[0]) # in ra phần tử đầu tiên của list
# print(user[-1]) # in ra phần tử cuối cùng của list

# user.append("Hùng") # thêm phần tử vào cuối list
# print("Danh sách sau khi thêm là : ", user)

# user.remove("Chiến") # xóa phần tử trong list
# print("Danh sách sau khi xóa là : ", user)

# user.pop(0) # xóa phần tử đầu tiên trong list
# print("Danh sách sau khi xóa phần tử đầu tiên là:", user)

# user.pop() # xóa phần tử cuối cùng trong list
# print("Danh sách sau khi xóa phần tử cuối cùng là : ", user)

# # 2. Đếm số phần tử 
# print("Số phần tử trong list là : ", len(user))

# # 3. Kiểm tra có tồn tại phần tử trong list hay không
# phone =["iphone","samsum","oppo","nokia"]
# print("nokia"in phone) # True
# print("xiaomi"in phone) #False

# print("Kiểm tra loại điện thoại nhập vào có trong list không:")
# yourphone = input("Nhập loại điện thoại của bạn : ").lower() # đổi chuỗi nhập vào thành chữ thường
# print(" Điện thoại của bạn có trong list không :", yourphone in phone)

# # 4. Sửa phần tử trong list 
# food =["cơm","phở","bún","bánh mì"] 
# print("Danh sách ban đầu là : ", food)
# food[0]="bún chả" # sửa phần tử đầu tiên trong list
# print("Danh sách sau khi sửa là : ", food)

# #5. Duyệt list ( rất quan trọng)
# trees =["xoài","bưởi","cam","quýt"]
# for tree in trees:
#     print("Danh sách cây ban đầu là:",tree) # Mỗi lần lặp sẽ in ra 1 phần tử trong list

# for index, tree in enumerate(trees): # enumerate() sẽ trả về cả index và phần tử trong list
#     print("Danh sách cây ban đầu là:",str(index)+"-"+ tree)


#---------------Mini project-------------------
# employees = []
# while True:
#     print("\n===== MENU =====")
#     print("1. Thêm nhân viên")
#     print("2. Hiển thị danh sách")
#     print("3. Xóa nhân viên")
#     print("4. Thoát")

#     choice = input("Chọn: ")

#     # TODO:
#     # - Nếu chọn 1: nhập tên và thêm vào list
#     # - Nếu chọn 2: in danh sách nhân viên
#     # - Nếu chọn 3: nhập tên và xóa nếu tồn tại
#     # - Nếu chọn 4: kết thúc chương trình


print("\n========DANH SÁCH NHÂN VIÊN ===========")
print("1. Thêm nhân viên ")
print("2. Liệt kê danh sách nhân viên")
print("3. Xóa nhân viên")
print("4. Thoát")
print("\n Hãy chọn option bạn muốn thực hiện:")

employees =["quỳnh","huyền"]
yourchoice = input("Nhập số từ 1 đến 4:")
if int(yourchoice)==1:
    name = input("Nhập tên bạn muốn thêm :")
    employees.append(name)
    print("Danh sách nhân viên hiện tại là:", employees)
elif int(yourchoice)==2:
    print("Danh sách nhân viên hiện tại là:", employees)
elif int(yourchoice)==3:
    name1 = input("Nhập tên bạn muốn xóa:").lower()
    if name1 in employees:
        employees.remove(name1)
        print("Đã xóa nhân viên: ", name1)
        print("Danh sách nhân viên sau khi xóa:", employees)
    else :
        print("Nhân viên không tồn tại trong danh sách.")
elif int(yourchoice)==4:
    print("Thoát chương trình")
else:
    print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")
