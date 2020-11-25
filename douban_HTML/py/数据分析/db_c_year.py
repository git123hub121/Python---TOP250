import pandas as pd
from pyecharts.charts import Line
#导入设置系列配置和全局配置，下面会说到用法
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# 读取文件
df = pd.read_csv('D:\Python\douban_HTML\douban250_2.csv', header=0, names=["title", "info", "score", "people"])
(dom1, dom2, dom6, dom7) = ([], [], [], [])
# 清洗数据,获取电影年份及国家,增加年份列及国家列
for i in df['info']:
    country = i.split('/')[1].split(' ')[0].strip()
    #print(country)
    if country in ['中国大陆', '台湾', '香港']:
        dom1.append('中国')
    else:
        dom1.append('外国')
    dom2.append(i.split('/')[0].replace('(中国大陆)', '').strip())
df['country'] = dom1
df['year'] = dom2
# 对中国电影计数排序
df_last = df.loc[df['country'] == '中国']
place_message = df_last.groupby(['year'])
print(place_message)
place_com = place_message['year'].agg(['count'])
print(place_com)
place_com.reset_index(inplace=True)
place_com_last = place_com.sort_index()
dom3 = place_com_last.sort_values('year', ascending=True)
# 对外国电影计数排序
df_last_1 = df.loc[df['country'] == '外国']
place_message = df_last_1.groupby(['year'])
place_com = place_message['year'].agg(['count'])
# print(place_com)
place_com.reset_index(inplace=True)
place_com_last = place_com.sort_index()
dom4 = place_com_last.sort_values('year', ascending=True)
# 对所有电影计数排序,获取完整年份时间
place_message = df.groupby(['year'])
place_com = place_message['year'].agg(['count'])
# print(place_com)
place_com.reset_index(inplace=True)
place_com_last = place_com.sort_index()
dom5 = place_com_last.sort_values('year', ascending=True)
# 横坐标
attr = ["{}".format(i) for i in dom5['year']]
print(attr)
# 中国电影纵坐标
for j in attr:
    for x, y in zip(dom3['year'], dom3['count']):
        if x == j:
            aaa = int(y)
            break
        else:
            aaa = int('0')
            continue
    dom6.append(aaa)
# 外国电影纵坐标
for j in attr:
    for x, y in zip(dom4['year'], dom4['count']):
        if x == j:
            aaa = int(y)
            break
        else:
            aaa = int('0')
            continue
    dom7.append(aaa)
# print(dom6)
# print(dom7)

#希望前面自己能够独立写出来
line = (
    Line(
        init_opts=opts.InitOpts(theme=ThemeType.DARK)  # 设置主题 不知道如何添加宽高
    )
    .add_xaxis(attr)
    .add_yaxis("中国",dom6)
    .add_yaxis("外国",dom7)
        #.set_colors(["orange"])  # 柱子的颜色
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="豆瓣电影TOP250-中外电影上映年份分布",
                                  subtitle="",
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
                # color='skyblue',
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
            # name='Proportion(%)',
            # name_location='middle',
            # name_gap=30,
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
            axislabel_opts=opts.LabelOpts(
                font_size=20,
                font_family='Times New Roman',
                color='skyblue',

            ),
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


#line.render('豆瓣电影TOP250中外上映年份分布.html')

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