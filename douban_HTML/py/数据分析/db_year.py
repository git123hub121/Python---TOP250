import pandas as pd
from pyecharts.charts import Bar
#导入设置系列配置和全局配置，下面会说到用法
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# 读取文件
df = pd.read_csv('D:\Python\douban_HTML\douban250_2.csv', header=0, names=["title", "year", "score", "people"])
# 清洗数据,获取电影年份,增加年份列
# dom = []
# for i in df['info']:
    # dom.append(i.split('/')[0].replace('(中国大陆)', '').strip())
# df['year'] = dom
# 计数排序
place_message = df.groupby(['year'])
place_com = place_message['year'].agg(['count'])
place_com.reset_index(inplace=True)
place_com_last = place_com.sort_index()
dom1 = place_com_last.sort_values('year', ascending=True)
# 生成柱状图
v1 = list(dom1['year'])
# print(v1)
attr = list(dom1['count'])
# bar = Bar("豆瓣电影TOP250-电影上映年份分布", title_pos='center', title_top='18', width=800, height=400)
# bar.add("", v1, attr, is_label_show=True, is_datazoom_show=True)  新版本已经不能使用add方法了！
bar = (
    Bar(
        init_opts=opts.InitOpts(theme=ThemeType.MACARONS)  # 设置主题 不知道如何添加宽高
    )
    .add_xaxis(v1)
    .add_yaxis("2019年豆瓣电影TOP250上映年份统计",attr)
        #.set_colors(["orange"])  # 柱子的颜色
    .set_global_opts(
        title_opts=opts.TitleOpts(title="豆瓣电影上映年份分布",
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


bar.render('豆瓣电影TOP250上映年份分布.html')

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