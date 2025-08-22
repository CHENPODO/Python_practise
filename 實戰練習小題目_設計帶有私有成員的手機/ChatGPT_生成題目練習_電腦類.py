# 練習題目
# 題目 1: 電腦類
# 設計一個電腦類 Computer
class Computer:
    # 私有成員變量: __power_on，型別 bool，True 表示開機，False 表示關機。
    # __power_on = True # 電腦開機狀態
    def __init__(self,__power_on = False):
        self.__power_on = __power_on # 初始化可決定是否開機
    # 私有成員方法: __check_power()
    def __check_power(self):
        # 若開機 (True) → 輸出: "電腦已開機"
        if self.__power_on:
            print("電腦已開機")
        # 若關機 (False) → 輸出: "電腦未開機，請先開機"
        else:
            print("電腦未開機，請先開機")

    # 公開成員方法: use()
    # 會先調用 __check_power()
    # 然後輸出: "正在使用電腦"
    def use(self):
        self.__check_power()
        print("正在使用電腦")

# PC1
pc1 = Computer(False)
pc1.use()

# PC2
pc2 = Computer(True)
pc2.use()