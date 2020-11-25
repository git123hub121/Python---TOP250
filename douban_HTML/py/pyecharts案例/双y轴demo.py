# coding: utf-8
# 需要安装最新的pyecharts才可以运行.
from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from pyecharts.globals import ThemeType
def overlap_bar_line(v1, v2, v3, v4, v5):
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK)) # 这里可以选择主题
        .add_xaxis(v1)
        .add_yaxis("总用户量", v2)
        .add_yaxis("完成输入用户量", v3)
        .extend_axis(
            yaxis=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value}%"), interval=5
            )
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="周数据模拟"),
            yaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value}/人")
            ),
        )
    )
    line = Line()
    line.add_xaxis(v4).add_yaxis("覆盖率", v5, yaxis_index=1, )
    bar.overlap(line)
    bar.render('123.html')
    
    
v1 = ["10月30日", "10月31日", "11月01日", "11月02日", "11月03日", "11月04日", "11月05日"]  # x轴坐标
v2 = [46, 39, 40, 34, 48, 54, 57] # 总用户量
v3 = [9, 6, 6, 9, 9, 5, 10] # 完成输入用户量
v4 = [i for i in range(0, 101)] # y轴
v5 = [19.57, 15.38, 15, 26, 18, 9.2, 17.5, 17.42]
 # y对应的数据

overlap_bar_line(v1, v2, v3, v4, v5)
# 第一个参数是日期
# 第二个参数是总用户量
# 第三个参数是完成输入的用户量
# 第四个参数是折线图的y轴
# 第五个参数是覆盖率