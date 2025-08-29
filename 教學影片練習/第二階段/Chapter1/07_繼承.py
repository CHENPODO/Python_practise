class Phone:
    IMEI = None
    producer = "PD"

    def call_by_4g(self):
        print("4G通話")


# 單繼承
class Phone_2025(Phone):
    face_id = 123123
    def call_by_5g(self):
        print("5G通話")


phone = Phone_2025()
phone.call_by_4g()
phone.call_by_5g()
print(phone.face_id)

# 多繼承
class NFC_Reader:
    nfc_type = "第五代"
    producer = "PDOL"
    def read_card(self):
        print("NFC 讀卡")
    def write_card(self):
        print("NFC 寫卡")

class RemoteControl:
    rc_type = "紅外遙控"

    def control(self):
        print("紅外線開啟了")

class MyPhone(Phone,NFC_Reader,RemoteControl):
    pass # 補全語法用
# 多繼承下，父類成員名一致的場景

phone = MyPhone()
phone.read_card()
phone.write_card()
phone.control()
print(phone.producer) # 按照左邊先印