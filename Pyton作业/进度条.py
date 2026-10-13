# 进度条
import time

print("Download ...")

# total 一共20小段
total = 20
for n in range(total + 1):
    # n 代表现在完成了几段，从0，1，2 ... 20
    ok = "=" * n
    no = " " * (total - n)
    jin_du_tiao = "[" + ok + no + "]"
    baifenbi = int(n / total * 100)

    print(f"\r{jin_du_tiao} {baifenbi}%", end="")
    time.sleep(0.2)
print()