"""
演示 pyecharts 的基礎入門
"""

# 導入
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, VisualMapOpts, ToolboxOpts

# 創建一個折線圖對象
line = Line()

# 給折線圖對象添加 x 軸的數據
line.add_xaxis(["美國","法國","日本"])
# 給折線圖對象添加 y 軸的數據

line.add_yaxis("GDP",[30,20,10])
# 設置全局配置項
line.set_global_opts(
    title_opts=TitleOpts(title="GDP 圖表生成",pos_left="center",pos_bottom='1%'),
    legend_opts=LegendOpts(is_show=True), # 顯示圖表中的 GDP 開關，但默認就是True
    visualmap_opts=VisualMapOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True)
)
# 透過 .render 生成圖表
line.render()