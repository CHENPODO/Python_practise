"""
文件相關類定義
"""
import json

from simplejson import JSONEncoder

from data_define import Record # 導包

# 先定義一個抽象類用來做頂層設計，確定有哪些功能需樣實現
# 文件讀取器
class FileReader:
    def read_data(self) -> list[Record]: # 返回值的註解
        # 得到每一條數據都轉換為Record 對象，將它們都封裝到 list內返回即可
        pass

class TextFileReader(FileReader):
    def __init__(self,path):
        self.path = path # 定義成員變量，紀錄文件的路徑

        # 複寫(實現抽象方法)
    def read_data(self) -> list[Record]:
        f = open(self.path,"r",encoding="UTF-8")

        record_list : list[Record] = [] # 變量:註解 = 值
        # 透過讀取 並用for迴圈跑每一行
        for line in f.readlines():
            line = line.strip() # 可去除讀取時讀取到的 \n ，並在附值給 line 變量
            data_list = line.strip(",") # 透過切割 -> . (逗號) 獲取附值到列表之中
            record = Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
            record_list.append(record)

            print(line)
        f.close()
        return record_list
# JSON
class JsonReader(FileReader):

    def __init__(self,path):
        self.path = path # 定義成員變量，紀錄文件的路徑

    # 實現抽象方法 read_data
    def read_data(self) -> list[Record]:
        record_list: list[Record] = []  # 變量:註解 = 值
        f = open(self.path, "r", encoding="UTF-8")

        # 透過讀取 並用for迴圈跑每一行
        for line in f.readlines():
            dict_data = json.loads(line)
            record = Record(dict_data["date"], dict_data["order_id"], dict_data["money"], dict_data["province"])
            record_list.append(record)
            print(line)
        f.close()

        return record_list

# 運行時可以跑內容，但導包進來時，這裡面內容不會執行
if __name__ == '__main__':
    text_file_reader = TextFileReader("C:/Users/cindy/OneDrive/桌面/Python_practise/實戰練習小題目_第二階段_第一章_數據分析案例_綜合案例/2011年1月銷售數據.txt")
    json_file_reader = JsonReader("C:/Users/cindy/OneDrive/桌面/Python_practise/實戰練習小題目_第二階段_第一章_數據分析案例_綜合案例/2011年2月銷售數據JSON.txt")
    list1 = text_file_reader.read_data() # 返回list
    list2 = json_file_reader.read_data() # 返回list

    for l in list1:
        print(l)

    for l in list2:
        print(l)