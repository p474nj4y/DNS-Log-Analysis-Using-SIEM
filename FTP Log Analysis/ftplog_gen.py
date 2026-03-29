import random
from datetime import datetime, timedelta

users = ["john", "admin", "root", "sarah", "guest", "anonymous"]
ips = ["192.168.1." + str(i) for i in range(1, 60)] + ["10.0.0." + str(i) for i in range(1, 20)]
files = [
    "/home/john/report.pdf",
    "/uploads/image.png",
    "/var/www/html/index.php",
    "/restricted/data.zip",
    "/root/backdoor.sh",
    "/home/admin/config.cfg",
    "/tmp/malware.exe"
]

commands = ["LOGIN", "GET", "PUT", "DELETE", "LIST"]

start_time = datetime(2026, 3, 29, 8, 0, 0)

def random_time():
    return start_time + timedelta(seconds=random.randint(0, 3600))

def generate_log():
    time = random_time().strftime("%Y-%m-%d %H:%M:%S")
    ip = random.choice(ips)
    user = random.choice(users)

    # Attack patterns
    if random.random() < 0.1:
        # brute force
        return f"{time} SRC_IP={ip} USER={user} COMMAND=LOGIN STATUS=FAILED"

    elif random.random() < 0.05:
        # malware upload
        return f"{time} SRC_IP={ip} USER={user} COMMAND=PUT FILE=/tmp/malware.exe STATUS=SUCCESS"

    elif random.random() < 0.03:
        # privilege abuse
        return f"{time} SRC_IP={ip} USER=admin COMMAND=DELETE FILE=/var/www/html/index.php STATUS=SUCCESS"

    else:
        cmd = random.choice(commands)
        file = random.choice(files)

        if cmd == "LOGIN":
            status = random.choice(["SUCCESS", "FAILED"])
            return f"{time} SRC_IP={ip} USER={user} COMMAND=LOGIN STATUS={status}"
        elif cmd == "LIST":
            return f"{time} SRC_IP={ip} USER={user} COMMAND=LIST PATH=/ STATUS=SUCCESS"
        else:
            return f"{time} SRC_IP={ip} USER={user} COMMAND={cmd} FILE={file} STATUS=SUCCESS"


with open("ftp_log.txt", "w") as f:
    for _ in range(1200):  # 1000+ lines
        f.write(generate_log() + "\n")

print("ftp_log.txt generated with 1200 lines")
