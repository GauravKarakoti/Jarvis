import time

print("Make sure to remove the https:// from the site name\n")

site_block = input("Enter the website you want to block:")

host_path="C:/Windows/System32/drivers/etc/hosts"

print()
print("If you have changed your host path , this might not work\n")

print("You can find your localhost number by opening C:/Windows/System32/drivers/etc/hosts (in notepad format)\n")

redirect = input("Enter your localhost number:")

print("Do You Want To Block This Website\n")

Choice1 = input("Enter Yes or No:")
print()

if Choice1.lower()=="yes":
    print("Blocking started")
        
    with open(host_path,"r+") as host_file:
        content = host_file.read()
        if site_block not in content:
            host_file.write(redirect+" "+site_block+"\n")
        else:
            print("Website is already blocked")

print("Do you want to unblock this site\n")

Choice2 = input("Enter Yes or No:")

if Choice2.lower()=="yes":
    with open(host_path,"r+") as host_file:
        content = host_file.readlines()
        if site_block not in content:
            print("The Website is not blocked")
        else:
            host_file.seek(0)
            for lines in content:
                if site_block not in lines:
                    host_file.write(lines)
            host_file.truncate()
    time.sleep(5)



