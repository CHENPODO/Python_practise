# 設計一個手機類，內部含有:
# - 私有成員變量: __5g_enable,類型bool,True表示開啟5g,False為關閉5g
# - 私有成員方法:__check_5g(),會判斷私有成員__is_5g_enable的值
#     - 若為true,打印輸出:5g已開啟
#     - 若為False,打印輸出:5G關閉,使用4G網路

# - 公開成員方法:call_by_5g(),調用他會執行
#     - 調用私有成員方法: __check_5g(),判斷5g網路狀態
#     - 打印輸出:正在通話中

# 運行結果 -> 5G關閉,使用4G網路
#            正在通話中
class Phone:
    # 設計一個私有成員變量 __5g_enable
    __5g_enable = False # 5g狀態close


    # 私有成員方法:__check_5g()
    def __check_5g(self):
        if self.__5g_enable:
            print("5g已開啟")
        else:
            print("5G關閉,使用4G網路")


    # 公開成員方法:call_by_5g
    def call_by_5g(self):
        self.__check_5g()
        print("正在通話中")

phone = Phone()
phone.call_by_5g()