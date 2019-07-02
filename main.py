print("[*] Welcome to Zabbix tool")
print("[-] Select the number of function to use or key 'q' to leave")
print(" [1] Add New Host")
print(" [2] Disable an Existing Host")
print(" [3] List All Existing Hosts")
print(" [4] Screenshot", end="\n\n")
target = ""
known = [str(i+1) for i in range(4)]
fileList = {
    "1": "add_host.py",
    "2": "disable_host.py",
    "3": "list_host.py",
    "4": "screenshot_host.py",
}

while target != "q":
    target = input("> ")
    if target not in known:
        print("[*] Not a valid function number. Please try again.")
    else:
        filename = fileList[target]
        print(filename)
