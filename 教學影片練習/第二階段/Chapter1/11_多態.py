# 指的是:多種狀態，即完成某行為時，使用不同對象會得到不同狀態

class Animal:
    # 這是一個空的方法，它只是告訴大家：
    # 所有「動物」都必須要有 speak() 這個功能
    def speak(self):
        pass

class cat(Animal):
    # Cat 繼承了 Animal，並重新定義了自己的 speak()
    def speak(self):
        print("喵喵喵")

class dog(Animal):
    # Dog 也繼承了 Animal，並重新定義了自己的 speak()
    def speak(self):
        print("汪汪汪")

def speak_noise(animal:Animal):
    """製造噪音，需要傳入Animal對象"""
    animal.speak()

# 演示多態，使用2個子類對象來調用函數
dog = dog()
cat = cat()
speak_noise(cat) # 喵喵喵
speak_noise(dog) # 汪汪汪

# 演示抽象類
class AC:
    def cool_wind(self):
        """製冷"""
        pass
    def hot_wind(self):
        """製熱"""
        pass
    def swing_l_r(self):
        """左右擺頭"""
        pass

class Midea_AC(AC):
    def cool_wind(self):
        """製冷"""
        print("美的空調製冷")

    def hot_wind(self):
        """製熱"""
        print("美的空調製熱")


    def swing_l_r(self):
        """左右擺頭"""
        print("美的空調左右擺頭")

class gree_AC(AC):
    def cool_wind(self):
        """製冷"""
        print("格立空調製冷")

    def hot_wind(self):
        """製熱"""
        print("格立空調製熱")


    def swing_l_r(self):
        """左右擺頭"""
        print("格立空調左右擺頭")

def make_cool(ac:AC):
    ac.cool_wind()

# 構建類對象
midea_ac = Midea_AC()
gree_ac = gree_AC()

make_cool(midea_ac)
make_cool(gree_ac)