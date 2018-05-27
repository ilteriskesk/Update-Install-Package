import os

mod = int(input("1) Update\n2) Upgrade\n3) Install Package\n4) Exit\n==> "))

while(1):
    if mod == 1:
        os.system("sudo apt update -y")
        print("------------")
        print("Update OK.")
        print("------------")
    elif mod == 2:
        os.system("sudo apt upgrade -y")
        print("------------")
        print("Upgrade OK.")
        print("------------")
    elif mod == 3:
        package_name = input("Input Package Name: ")
        os.system("sudo apt install " + package_name)
        print("--------------------")
        print("Package Install OK.")
        print("--------------------")
    elif mod == 4:
        exit(1)
    else:
        print("Try again!")
