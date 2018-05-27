import os
 
while(1):
    mod = int(input("1) Update and Sync\n2) Install Package\n3) Exit\n==> "))
    if mod == 1:
        os.system("sudo pacman -Syu")
        print("---------------------")
        print("Update and Sync OK.")
        print("---------------------")
    elif mod == 2:
        package_name = input("Input package name: ")
        os.system("sudo pacman -S " + package_name)
        print("---------------------")
        print("Package Install OK.")
        print("---------------------")
    elif mod == 3:
        exit(1)
    else:
        print("Try again!")
