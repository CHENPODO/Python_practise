# 1. 設計一個鬧鐘類
class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000,1000)

# 2. 構建2個類對象並工作
clock_1 = Clock()
clock_2 = Clock()

clock_1.id = '1001'
clock_1.price = 490
print(f"鬧鐘編號1: {clock_1.id}，價格: {clock_1.price}")
clock_1.ring()
clock_2.id = "1002"
clock_2.price = 490
print(f"鬧鐘編號2: {clock_2.id}，價格: {clock_2.price}")
clock_2.ring()