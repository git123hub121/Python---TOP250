import pandas as pd
from pyecharts.charts import Bar, Line, Grid
from pyecharts import options as opts
from pyecharts.globals import ThemeType
import os
#柱状图
df = pd.read_csv("D:\Python\douban_HTML\douban250_2.csv",
                 header=0, names=["title", "info", "score", "people"])
# place_message = df.groupby(['score'])
# place_count = place_message['score'].agg(['count'])#分组计数
# place_count.reset_index(inplace=True)
#分组计数,并构建count列
place_count = df.groupby(['score'])['score'].agg(['count'])
# print(place_count)#这里还是df形式，不是列表
#重置place_count的索引
place_count.reset_index(inplace=True)
#按照索引排序---这里还是DataFrame形式，并以score进行默认排序-升序
place_com = place_count.sort_index()
dom = place_com.sort_values('score', ascending=True)
# print(dom)
# print(type(dom))#DataFrame形式 也是一个可按照索引的遍历对象
#构建x,y轴的数据源
data_x = list(dom['score'])  # data_x = dom['score']
print(data_x)
data_y = list(dom['count'])  # data_y = dom['count']
print(data_y)
#如果不转换为列表格式，数据无法被读取
#折线图的x轴数据需要时字符串，要不然默认会把它当做数值读取
data_xstr = []
for i in data_x:
    i = str(i)
    data_xstr.append(i)
#生产柱形图.折线图
bar = (
    Bar(

    )
    .add_xaxis(data_x)
    .add_yaxis("评分计数", data_y)
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="柱形"
        ),
        legend_opts=opts.LegendOpts(

        ),
        yaxis_opts=opts.AxisOpts(

        ),
        toolbox_opts=opts.ToolboxOpts(

        ),
    )
    # .render("score.html")
)
line = (
    Line()
    .add_xaxis(data_xstr)
    .add_yaxis("评分计数", data_y)
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="折线",
            pos_top="60%"
        ),
        legend_opts=opts.LegendOpts(

        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
        ),
        toolbox_opts=opts.ToolboxOpts(

        ),
    )
    # .render("score.html")
)
grid = (
    Grid()
    .add(bar, grid_opts=opts.GridOpts(pos_bottom="60%"))
    .add(line, grid_opts=opts.GridOpts(pos_top="60%"))
    .render("score.html")
)


# import datetime
# day = datetime.datetime.now().weekday()
# print(day)
#0,1,2,3,4,5,6
