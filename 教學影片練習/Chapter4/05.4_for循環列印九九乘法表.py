for i in range(1, 10):           # 外層：控制行數（從第1行到第9行）
    for j in range(1, i+1):       # 內層：控制每一行要印幾個乘法
        if j <= i:               # 只印上三角形部分（j 不會超過 i）
            print(f"{j} * {i} = {j * i}\t", end='')  # \t 是對齊用
    print()                      # 每列印完一行換行
