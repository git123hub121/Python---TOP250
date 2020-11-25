import pandas as pd
from pyecharts.charts import Bar,Page
#导入设置系列配置和全局配置，下面会说到用法
from pyecharts import options as opts
from pyecharts.globals import ThemeType
import os
# 读取文件
df = pd.read_csv('D:\Python\douban_HTML\douban250.csv', header=0, names=["title", "year", "score", "people"])
# 计数排序
place_message = df.groupby(['score'])
place_com = place_message['score'].agg(['count'])
place_com.reset_index(inplace=True)
place_com_last = place_com.sort_index()
dom3 = place_com_last.sort_values('score', ascending=True)
# 生成柱状图
v1 = list(dom3['score'])
# print(v1)
attr = list(dom3['count'])

place_message = df.groupby(['year'])
place_com = place_message['year'].agg(['count'])
place_com.reset_index(inplace=True)
place_com_last = place_com.sort_index()
dom1 = place_com_last.sort_values('year', ascending=True)
# 生成柱状图
v11 = list(dom1['year'])
# print(v1)
attr1 = list(dom1['count'])
page = Page(layout=Page.DraggablePageLayout)
bar = (
    Bar(
        init_opts=opts.InitOpts(theme=ThemeType.CHALK)  # 设置主题 不知道如何添加宽高
    )
    .add_xaxis(v1)
    .add_yaxis("2019年豆瓣电影TOP250上映评分统计",attr)
        
    .set_global_opts(
        title_opts=opts.TitleOpts(title="豆瓣电影上映评分分布",
                                  subtitle="",
                                 ),
        #图例设置
        legend_opts=opts.LegendOpts(
            pos_left='center',    # 图例放置的位置，分上下左右，可用左右中表示，也可用百分比表示
            pos_top='top',
            orient='vertical',   # horizontal、vertical #图例放置的方式 横着放or竖着放
            textstyle_opts=opts.TextStyleOpts(
                font_size=16,
                color='skyblue',
                font_family='Times New Roman',
            ),
        ),
        yaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(
                font_size=20,
                font_family='Times New Roman',
                color='skyblue',
            ),
        ),
        #显示工具栏
        toolbox_opts=opts.ToolboxOpts(is_show=True),
)
)
bar1 = (
    Bar(
        init_opts=opts.InitOpts(theme=ThemeType.MACARONS)  # 设置主题 不知道如何添加宽高
    )
    .add_xaxis(v11)
    .add_yaxis("2019年豆瓣电影TOP250上映年份统计",attr1)
        #.set_colors(["orange"])  # 柱子的颜色
    .set_global_opts(
        title_opts=opts.TitleOpts(title="豆瓣电影上映年份分布",
                                  subtitle="",
                                             ),
                                
        #图例设置
        legend_opts=opts.LegendOpts(
            pos_left='center',    # 图例放置的位置，分上下左右，可用左右中表示，也可用百分比表示
            pos_top='top',
            orient='vertical',   # horizontal、vertical #图例放置的方式 横着放or竖着放
            textstyle_opts=opts.TextStyleOpts(
                font_size=16,
                color='skyblue',
                font_family='Times New Roman',
            ),
        ),
        yaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(
                font_size=20,
                font_family='Times New Roman',
                color='skyblue',
            ),
        ),
        #显示工具栏
        toolbox_opts=opts.ToolboxOpts(is_show=True),
    )
)
page.add(bar, bar1)
page.render("test.html")
os.system("test.html")

