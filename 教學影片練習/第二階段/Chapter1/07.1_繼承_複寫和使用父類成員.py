# 複寫 -> 子類繼承父類的成員屬性和成員方法後，如果對其 "不滿意"，那就可以複寫
# 及:在子類中重新定義同名的屬性或方法即可

class Phone:
    IMEI = None            # 序列號
    producer = "IT_CAST_A"   # 廠商

    def call_by_5g(self):
        print("使用5G網路通話")

# 定義子類，複寫父類成員
class MyPhone(Phone):
    producer = "IT_CAST_B" # 父寫父類的成員複寫

    def call_by_5g(self):
        print("開啟單核模式，確保通話時省電")
        # print("使用5G網路通話")
        # 通過父類名調用

        # 方法一
        # print(f"父類的廠商是:{Phone.producer}")
        # Phone.call_by_5g(self) # 調用父類成員方法

        # 方法二
        print(f"父類的廠商是:{super().producer}") # 可以直接call 父類對象
        super().call_by_5g() # 不需要傳入 self
        print("開啟單核模式，確保性能")

phone = MyPhone()
phone.call_by_5g()
# 結果為(繼承父類) ->
# 開啟單核模式，確保通話時省電
# 使用5G網路通話
# 開啟單核模式，確保性能
# 在子類中，調用父類成員
print(phone.producer) # 複寫行為 -> IT_CAST_B (子類父寫)

# 在子類中，調用父類成員