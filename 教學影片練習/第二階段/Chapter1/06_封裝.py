# 定義一個類，內涵私有成員便亮和私有成員方法
# 兩個底線開頭為 私有成員

# 在類中提供內部使用的屬性和方法，而不對外開放(類對象無法使用)

class Phone:
    # 定義 私有成員 __current_voltage
    __current_voltage = 1

    # 定義 私有方法
    def __keep_single_core(self):
        print("讓CPU用單核模式運行")

    # 透過創建設定一個新的公開的變量，使得可以去訪問私有的成員類對象
    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5G is Running!!!")
        else:
            self.__keep_single_core()
            print("電量不足開啟5G")
phone = Phone()
phone.call_by_5g()

