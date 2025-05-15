# 引入
import folium
from folium import FeatureGroup

# 建立礁溪鄉地圖
jiaoxi_map = folium.Map(
    location=[24.8261,121.7728], # 礁溪鄉中心點
    tiles="openstreetmap",
    zoom_start=16
)

# 建立圖層群組（FeatureGroups）
"""
1. 交通 traffic 2. 教育 school 3. 溫泉 spa 4. 自然 nature
"""
group_traffic = FeatureGroup("交通").add_to(jiaoxi_map)
group_school = FeatureGroup("教育").add_to(jiaoxi_map)
group_spa = FeatureGroup("溫泉").add_to(jiaoxi_map)
group_nature = FeatureGroup("自然").add_to(jiaoxi_map)

# 景點資訊
locations = {
     "礁溪火車站": {
        "coords": [24.827020, 121.774690],
        "icon": ("train", "blue", "fa"),  # (icon name, color, prefix)
        "group_map":group_traffic
    },
    "湯圍溝公園": {
        "coords": [24.829552, 121.773001],
        "icon": ("spa", "green", "fa"),
        "group_map":group_spa
    },
    "礁溪溫泉公園": {
        "coords": [24.827657, 121.772424],
        "icon": ("hot-tub", "red", "fa"),
        "group_map":group_spa
    },
    "礁溪國小": {
        "coords": [24.821977, 121.768499],
        "icon": ("graduation-cap", "orange", "fa"),
        "group_map": group_school
    },
    "五峰旗瀑布": {
        "coords": [24.834333303714846, 121.74706869325325],
        "icon": ("tint", "cadetblue", "fa"),
        "group_map":group_nature
    },
}

# 加入每個景點的 marker
for name,data in locations.items():
    latlng = data["coords"]
    icon_name, color, prefix = data["icon"]
    group = data["group_map"]
    folium.Marker(
        location=latlng,
        tooltip=name,
        icon=folium.Icon(icon=icon_name,prefix=prefix,color=color)
       ).add_to(group)

# 散步路線順序
trail_order = [
    "礁溪火車站",
    "湯圍溝公園",
    "礁溪溫泉公園",
    "礁溪國小",
    "五峰旗瀑布"
]
# 產生座標列表
trail_coordinates = [locations["name"]["coords"] for name in trail_order]

folium.PolyLine(
    trail_coordinates,
    tooltip="散步路線",
    color="#fa0",
    weight=6,
).add_to(jiaoxi_map)

# 加入圖層控制開關
folium.LayerControl().add_to(jiaoxi_map)

# 儲存地圖
jiaoxi_map.save("C:/Users/cindy/OneDrive/桌面/Python_practise/教學影片練習/Chapter11/jiaoxi_map.html")
