# coding: utf-8
# 需要安装最新的pyecharts才可以运行.
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Boxplot
from pyecharts.globals import ThemeType

df = pd.read_csv('douban250_2.csv', header=0, names=["title", "info", "score", "people"])
(dom1, dom2) = ([], [])
# 清洗数据,获取电影年份及国家,增加年份列及国家列
for i in df['info']:
    country = i.split('/')[1].split(' ')[0].strip()
    if country in ['中国大陆', '台湾', '香港']:
        dom1.append('中国')
    else:
        dom1.append('外国')
    dom2.append(i.split('/')[0].replace('(中国大陆)', '').strip())
df['country'] = dom1
df['year'] = dom2
# 获取特定数据
df1 = df.loc[df['country'] == '中国']
df2 = df.loc[df['country'] == '外国']
x_axis = ['中国', '外国']
y_axis = [list(df1['score']), list(df2['score'])]
#最终数据一定要变成列表
# print(y_axis)
boxplot = Boxplot()
        # init_opts=opts.InitOpts(theme=ThemeType.DARK,width=800, height=400,)  # 设置主题 不知道如何添加宽高
boxplot = (
    boxplot.add_xaxis(x_axis)
    .add_yaxis(series_name="评分", y_axis=boxplot.prepare_data(y_axis))
        #.set_colors(["orange"])  # 柱子的颜色
    .set_global_opts(
        title_opts=opts.TitleOpts(title="豆瓣电影TOP250-中外电影评分情况",
                                  subtitle="",pos_top=18,
                                #   title_textstyle_opts=opts.TextStyleOpts(color='red',
                                #                                               font_size=12,
                                #                                               font_family='Times New Roman',
                                #                                               font_weight='bold',),
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
#         xaxis_opts=opts.AxisOpts(
#             name='Type',
#             name_location='middle',
#             name_gap=20,
# #                 x轴名称的格式配置
#             name_textstyle_opts=opts.TextStyleOpts(
#                 font_family= 'Times New Roman',
#                 font_size=14,
#             ),
# #                 坐标轴刻度配置项
#             axistick_opts=opts.AxisTickOpts(
# #                     is_show=False,  # 是否显示
#                 is_inside=True,  # 刻度线是否在内侧
#             ),
# #                 坐标轴线的配置
#             axisline_opts=opts.AxisLineOpts(
#                 linestyle_opts=opts.LineStyleOpts(
#                     width=1,
#                     color='black',
#                 )
#             ),
# #                 坐标轴标签的配置
#             axislabel_opts=opts.LabelOpts(
#                 font_size=12,
#                 font_family='Times New Roman',
#             ),
#         ),
        yaxis_opts=opts.AxisOpts(
            max_=10,
            min_=8,
            type_="value",
            name="评分",
            # name='Proportion(%)',
            # name_location='middle',
            name_gap=5,
            # name_textstyle_opts=opts.TextStyleOpts(
            #     font_family= 'Times New Roman',
            #     font_size=16,
            #     color='skyblue',
            #     font_weight='bolder',
            # ),
#             axistick_opts=opts.AxisTickOpts(
# #                     is_show=False,  # 是否显示
#                 is_inside=True,  # 刻度线是否在内侧
#             ),
            # axislabel_opts=opts.LabelOpts(
            #     font_size=20,
            #     font_family='Times New Roman',
            #     color='skyblue',
            # ),
        ),
        #显示工具栏
        toolbox_opts=opts.ToolboxOpts(is_show=True),
    )
    # .set_series_opts(
    #     label_opts=opts.LabelOpts(
    #         position="Top",
    #         font_size=12,
    #         font_family='Times New Roman',
    #     )
    # )
)

boxplot.render('豆瓣电影TOP250中外评分情况.html')

thm = '''
 |  CHALK = 'chalk' #粉笔风
 |  
 |  DARK = 'dark'  #暗黑风
 |  
 |  ESSOS = 'essos' #厄索斯大陆
 |  
 |  INFOGRAPHIC = 'infographic' #信息图
 |  
 |  LIGHT = 'light' #明亮风格
 |  
 |  MACARONS = 'macarons' #马卡龙
 |  
 |  PURPLE_PASSION = 'purple-passion' #紫色激情
 |  
 |  ROMA = 'roma' #石榴
 |  
 |  ROMANTIC = 'romantic' #浪漫风
 |  
 |  SHINE = 'shine' #闪耀风
 |  
 |  VINTAGE = 'vintage' #复古风
 |  
 |  WALDEN = 'walden' #瓦尔登湖
 |  
 |  WESTEROS = 'westeros' #维斯特洛大陆
 |  
 |  WHITE = 'white' #洁白风
 |  
 |  WONDERLAND = 'wonderland' #仙境
 '''