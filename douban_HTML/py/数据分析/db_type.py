
import pandas as pd
from pyecharts.charts import TreeMap
#导入设置系列配置和全局配置，下面会说到用法
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# 读取文件
df = pd.read_csv('D:\Python\douban_HTML\douban250_2.csv', header=0, names=["title", "info", "score", "people"])
(dom1, dom2, dom3, dom4) = ([], [], [], [])
# 获取每部电影类型数据
for i in df['info']:
    dom1.append(i.split('/')[2].replace('\xa0', '').replace(' 1978(中国大陆) ', ''))#有个特殊数据    
# print(dom1)
# 获取电影类型类别
for j in dom1:
    res = j.split(' ')
    for re in res:
        if re not in dom2:
            dom2.append(re)
        else:
            pass
# 电影类型类别对应数量
for k in dom2:
    num = 0
    for j in dom1:
        res = j.split(' ')
        for re in res:
            if re == k:
                num += 1
    dom3.append(num)
def message():
    # 生成字典形式
    for p in range(len(dom2)):
        data = {}
        data['name'] = dom2[p] + ' ' + str(dom3[p])
        data['value'] = dom3[p]
        yield data
# 生成类型图
data = message()
# print(data)#字典遍历出来的对象还是字典，这一点要注意哦
for item in data:
    dom4.append(item)
    print(item)
print(dom4)
treemap = (
    TreeMap(init_opts=opts.InitOpts(width="1280px", height="720px"))
    .add(
        series_name="电影类型",
        data=dom4,
        visual_min=300,
        leaf_depth=1,
        # 标签居中为 position = "inside"
        label_opts=opts.LabelOpts(position="inside"),
    )
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        title_opts=opts.TitleOpts(
            title="豆瓣电影TOP250电影类型图", subtitle="2020/11", pos_left="leafDepth"
        ),
    )
    #.render("豆瓣电影TOP250电影类型图.html")
)