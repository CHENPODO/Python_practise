"""
- 練習題3：找出最便宜的商品
  跟剛剛那題一樣，只是我們現在找的是「價格最小」的那一個
"""

product_prices = {
    "手機": 25000,
    "筆電": 42000,
    "耳機": 3000,
    "滑鼠": 1200,
    "螢幕": 7800
}
cheapest_produce_price = 9999999999 # 先定為0
cheapest_produce_name = "" # 空字串候傳入

for price in product_prices.keys():
    if product_prices[price] < cheapest_produce_price:
        cheapest_produce_name = price # 取得之key值
        cheapest_produce_price = product_prices[price]
print(f"最便宜的商品是:{cheapest_produce_name},價格是:{cheapest_produce_price}")

