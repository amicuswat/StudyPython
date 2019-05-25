import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1"
websites_list = ["www.facebook.com", "facebook.com"]

i = 0
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours")
        with open(hosts_temp, "r+") as file:
            content = file.read()
            for website in websites_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    else:
        with open(hosts_temp, "r+") as file:
            content = file.readlines()
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
        print("Free time")
    time.sleep(5)
