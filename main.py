# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

   # buổi 1. input
# name = input("nhập tên của bạn:")
# old = input("nhập tuổi của bạn:")
# print("thông tin của bạn là:",name,old,"tuổi")

#   # buổi 2. ép kiểu 
# age = "23"
# price = "10.5"
# sum = int(age) + float(price)
# print("tổng tuổi và tiền là : " + str(sum))


    # buổi 3. if/else, so sánh, bool()
# username = input("nhập username:")
# if bool(username):
#     print("bạn đã nhập username là :", username)
# else:
#     print("bạn chưa nhập username ")
   
# age = input("enter yor age: ")
# if(int(age) > 18):
#     print("you allowed drive")
# else:
#     print("you not allowed drive")

# score = float(input("enter your score: "))
# if(score >=8):
#     print("you are excellent")
# elif(score >=6.5):
#     print("you are good")
# else:
#     print("you are not good, neet to improve")

role = input("enter your role: ")
if(role == "admin"):
    print("you can access this module")
else:
    print("you can not access this module")