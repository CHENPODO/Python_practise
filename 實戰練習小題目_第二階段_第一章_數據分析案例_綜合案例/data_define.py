"""
數據定義的類
Record 建立構造方法
"""
# Record 紀錄數據機本訊息
class Record:
    def __init__(self,date,order_id,money,province):
        # 從參數中拿到內容，並把內容複製給我們的成員變量
        self.date = date            # 訂單日期
        self.order_id = order_id    # 訂單ID
        self.money = money          # 訂單金額
        self.province = province    # 訂單地區

    def __str__(self):  # 將地址值轉字串
        return f"{self.date},{self.order_id},{self.money},{self.province}"