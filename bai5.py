
# Bài 5 : for, range(),while , break, continue 
# print("\nLiệt kê số từ 0-10:")
# for i in range(11): # range(11) sẽ tạo ra 1 dãy số từ 0 đến 10
#     print(i)

# print("\nLiệt kê các số từ 30-36:")
# for i in range(30,37): #range(start,stop)
#     print(i)

# print("\nLiệt kê số chẵn từ 2 đến 20: ")
# for i in range(2,21,2): #range(start,stop,step)
#     print(i)

# print("\nSắp xếp giảm dần từ 10 đến 1:")
# for i in range(10,0,-1):
#     print(i)

# fruits =["cam","quýt", "mít", "dừa", "dưa"]
# print("Danh sách các loại quả là:")
# for fruit in fruits:
#     print(fruit)

# for i in range(len(fruits)):
#     print(i,fruits[i])

# While sẽ lặp đến khi điều kiện sai.
# i = 0
# while i <= 5:
#     print(i)
#     i+=1

password ="123456"
your_password =""
while your_password != password:
    your_password= input("nhập mật khẩu:")
    if your_password == password:
        print ("Mật khẩu đúng")

# for i in range(10):
#     if i == 5:
#         break # thoát khỏi vòng lặp khi i = 5
#     print(i)

# i=0
# while i < 10:
#     i+=3
#     if(i==3)or(i==6):
#         continue  # bỏ qua các giá trị i = 3 và i = 6
#     print(i)

for i in range(3):
    for j in range(2):
        print(i, j)