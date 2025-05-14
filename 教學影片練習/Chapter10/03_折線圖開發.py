from pyecharts.options import TitleOpts, VisualMapOpts, LabelOpts
"""
演示折線圖開發
"""
import json
# 處理數據
us_f = open("C:/Users/cindy/OneDrive/桌面/Python_practise/教學影片練習/Chapter10/美國.txt","r",encoding="UTF-8")
us_data = us_f.read() # 美國全數據

jp_f = open("C:/Users/cindy/OneDrive/桌面/Python_practise/教學影片練習/Chapter10/日本.txt","r",encoding="UTF-8")
jp_data = jp_f.read() # 日本全數據

kr_f = open("C:/Users/cindy/OneDrive/桌面/Python_practise/教學影片練習/Chapter10/韓國.txt","r",encoding="UTF-8")
kr_data = kr_f.read() # 韓國全數據

# JSON 轉 Python 字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
kr_dict = json.loads(kr_data)


# 獲取 trend key
us_trend_dict = us_dict["United States"]["trend"]
jp_trend_dict = jp_dict["Japan"]["trend"]
kr_trend_dict = kr_dict["South Korea"]["trend"]

# 獲取日期數據，用於X軸，取2021年到(下標 19 結束)
# 美國 x軸
us_x_data = us_trend_dict["updateDate"][:20]

# 日本 x軸
jp_x_data = jp_trend_dict["updateDate"][:20]

# 韓國 x軸
kr_x_data = kr_trend_dict["updateDate"][:20]

# 獲取日期數據，用於Y軸，取2021年到(下標 19 結束)
# 美國 y軸
us_y_data = us_trend_dict["list"][0]["data"][:20]

# 日本 y軸
jp_y_data = jp_trend_dict["list"][0]["data"][:20]

# 韓國 y軸
kr_y_data = kr_trend_dict["list"][0]["data"][:20]

# 生成圖表
from pyecharts.charts import Line
line = Line()
line.add_xaxis(us_x_data) # x軸通用
# 美國
line.add_yaxis("美國確診人數",us_y_data,label_opts=LabelOpts(is_show=False))

# 日本
line.add_yaxis("日本確診人數",jp_y_data,label_opts=LabelOpts(is_show=False))

# 韓國
line.add_yaxis('韓國確診人數', kr_y_data,label_opts=LabelOpts(is_show=False))


line.set_global_opts(
    title_opts=TitleOpts(title="三國疫情折線圖(資料為假)",pos_left="center",pos_bottom="1%"),
    visualmap_opts=VisualMapOpts(is_show=True)
)

line.render("三國疫情折線圖.html")
# 關閉文建
us_f.close()
jp_f.close()
kr_f.close()