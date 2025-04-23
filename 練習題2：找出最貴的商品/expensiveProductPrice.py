"""
- 練習題2：找出最貴的商品
  你有一個商店的商品價目表（字典）：

"""

product_prices = {
    "手機": 25000,
    "筆電": 42000,
    "耳機": 3000,
    "滑鼠": 1200,
    "螢幕": 7800
}
expensive_produce_price = 0 # 先定為0
expensive_produce_name = "" # 空字串候傳入

for price in product_prices.keys():
    if product_prices[price] > expensive_produce_price:
        expensive_produce_name = price # 取得之key值
        expensive_produce_price = product_prices[price]
print(f"最貴的商品是:{expensive_produce_name},價格是:{expensive_produce_price}")