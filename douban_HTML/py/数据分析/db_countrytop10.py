import pandas as pd
from pyecharts.charts import Bar
#导入设置系列配置和全局配置，下面会说到用法
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# 读取文件
df = pd.read_csv('douban250_2.csv', header=0, names=["title", "info", "score", "people"])
dom1 = []
# 生成电影国家列表
for i in df['info']:
    country = i.split('/')[1].split(' ')[0].strip()
    print(country)
    dom1.append(country)
df['country'] = dom1
# 计数排序
place_message = df.groupby(['country'])
place_com = place_message['country'].agg(['count'])
print(place_com)
place_com.reset_index(inplace=True)
place_com_last = place_com.sort_index()
dom2 = place_com_last.sort_values('count', ascending=False)[0:10]
print(dom2)
# 生成柱状图
attr = list(dom2['country'])
v1 = list(dom2['count'])
attr.reverse()
v1.reverse()
print(attr)
print(v1)
bar = (
    Bar(
        init_opts=opts.InitOpts(theme=ThemeType.WONDERLAND,)  # 设置主题 不知道如何添加宽高 写到里面去即可width='900px',height='600px'
    )
    .add_xaxis(attr)
    .add_yaxis("count",v1)
    .reversal_axis()
    .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        #.set_colors(["orange"])  # 柱子的颜色
    .set_global_opts(
        title_opts=opts.TitleOpts(title="豆瓣电影TOP250-国家-地区电影数TOP10",
                                  subtitle="",pos_left="center",
                                #   title_textstyle_opts=opts.TextStyleOpts(color='red',
                                #                                               font_size=12,
                                #                                               font_family='Times New Roman',
                                #                                               font_weight='bold',),
                                  ),
        #图例设置
        legend_opts=opts.LegendOpts(
            pos_left='center',    # 图例放置的位置，分上下左右，可用左右中表示，也可用百分比表示
            pos_top='middle',
            orient='vertical',   # horizontal、vertical #图例放置的方式 横着放or竖着放
            # textstyle_opts=opts.TextStyleOpts(
            #     font_size=16,
            #     color='skyblue',
            #     font_family='Times New Roman',
            # ),
        ),
         xaxis_opts=opts.AxisOpts(
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
#                 坐标轴标签的配置
            axislabel_opts=opts.LabelOpts(
                font_size=12,
                font_family='Times New Roman',
                #rotate=45
            ),
        ),
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
            # axislabel_opts=opts.LabelOpts(
            #     font_size=12,
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

bar.render('豆瓣电影TOP250-国家-地区电影数TOP10.html')

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