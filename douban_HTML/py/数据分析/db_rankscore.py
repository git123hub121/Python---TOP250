import pandas as pd
from pyecharts.charts import Scatter
from pyecharts import options as opts
from pyecharts.globals import ThemeType
# 读取文件
df = pd.read_csv('douban250.csv', header=0, names=["title", "year", "score", "people"])
(dom2, dom3) = ([], [])
# 生成电影排名列表
dom1 = ["{}".format(i) for i in range(1, 251)]
# 生成电影评分列表
for i in df['score']:
    dom2.append(i)
# 生成电影评价人数列表
for i in df['people']:
    dom3.append(i.replace('人评价', ''))
# 生成数据列表
data = [list(i) for i in zip(dom1, dom2, dom3)]
# 生成散点图
x_lst = [int(v[0]) for v in data]
y_lst = [v[1] for v in data]
extra_data = [int(v[2]) for v in data]
# print(x_lst)
# print(y_lst)
# print(extra_data)
sc = (
    Scatter(
        #init_opts=opts.InitOpts(theme=ThemeType.WONDERLAND,)  # 设置主题 不知道如何添加宽高 写到里面去即可width='900px',height='600px'
    )
    .add_xaxis(x_lst)
    # .add_yaxis("评分",y_lst)
    .add_yaxis("评价人数",extra_data)
    #.set_colors(["orange"])  # 柱子的颜色
    .set_global_opts(
        title_opts=opts.TitleOpts(title="散点图",
                                  subtitle="豆瓣电影TOP250-排名评分人数三维度",
                                #   title_textstyle_opts=opts.TextStyleOpts(color='red',
                                #                                               font_size=12,
                                #                                               font_family='Times New Roman',
                                #                                               font_weight='bold',),
                                  ),
        visualmap_opts=opts.VisualMapOpts(
            dimension = extra_data,
            is_show = True,
            series_index = [x_lst,extra_data],
            type_="size",
            min_=min(extra_data),
            max_=max(extra_data),
            range_text = ['High', 'Low'],
            orient = "horizontal",
            # out_of_range = opts.visualMap(
            #      symbolSize = 20,
            #      color = "skyblue",
            # ),
           
        ),
        # #图例设置
        # legend_opts=opts.LegendOpts(
        #     pos_left='center',    # 图例放置的位置，分上下左右，可用左右中表示，也可用百分比表示
        #     pos_top='top',
        #     orient='vertical',   # horizontal、vertical #图例放置的方式 横着放or竖着放
        #     textstyle_opts=opts.TextStyleOpts(
        #         font_size=16,
        #         color='skyblue',
        #         font_family='Times New Roman',
        #     ),
        # ),
         xaxis_opts=opts.AxisOpts(
             interval= max(x_lst)-min(x_lst),  # Optional[Numeric]
             grid_index=0,  # Numeric
            #  position='',  # Optional[str]
            # offset = ,  # Numeric
             split_number= 50,  # Numeric
            #  boundary_gap='',  # Union[str, bool, None]
             min_= min(x_lst),  # Union[Numeric, str, None]
             max_= max(x_lst),  # Union[Numeric, str, None]
            #  min_interval=0,  # Numeric
            #  max_interval=0,  # Optional[Numeric]
#             name='Type',
#             name_location='middle',
             #name_gap=50,
#                 x轴名称的格式配置
            # name_textstyle_opts=opts.TextStyleOpts(
            #     font_family= 'Times New Roman',
            #     font_size=14,
            # ),
#                 坐标轴刻度配置项
            axistick_opts=opts.AxisTickOpts(
                is_show=True,  # 是否显示
                # is_inside=True,  # 刻度线是否在内侧
                
            ),
#                 坐标轴线的配置
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    # width=50,
                    # color='black',
                )
            ),
# #                 坐标轴标签的配置
#             axislabel_opts=opts.LabelOpts(
#                 font_size=12,
#                 font_family='Times New Roman',
#                 #rotate=45
#             ),
        ),
        yaxis_opts=opts.AxisOpts(
            # max_=max(extra_data), 
            # min_=min(extra_data),
            # name='Proportion(%)',
            # name_location='middle',
            # name_gap=30,
            # name_textstyle_opts=opts.TextStyleOpts(
            #     font_family= 'Times New Roman',
            #     font_size=50,
            #     color='skyblue',
            #     font_weight='bolder',
            # ),
            axistick_opts=opts.AxisTickOpts(
                # is_show=False,  # 是否显示
                # is_inside=True,  # 刻度线是否在内侧     
            ),
            axislabel_opts=opts.LabelOpts(
                font_size=16,
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

sc.render('豆瓣电影TOP250-排名评分人数三维度.html')

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
 #三维散点图不会，不搞了