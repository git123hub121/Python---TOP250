# Python数据分析可视化项目——豆瓣TOP250爬虫，数据分析项目实战

## 爬虫篇

暂时不写

## 数据分析篇

今天来将代码整理一下，说实话我都是按照别人的思路去修改的，感觉还没有学透彻，但是会用就行，重在举一反三。这也算是我学数据分析的一份作业吧。本来还想加入pie和其它图的。但是不想贪心了，总要留点遗憾来让你们来弥补。



### 1.先导入所有模块

这里我们用pyecharts来数据可视化，pd做数据清洗，jieba分词，collections做统计运算，re正则匹配

**注意事项：**先说好数据我都会给个百度网盘链接，同时我使用的是绝对路径。因为我用的是vscode，但我一直没有去解决这个问题，网上也找过。如果有大佬知道，可以留言告诉我，要详细的那种。 我是用的是新版本pyecharts，与时俱进，追求新事物也是件很快乐的事。

```python
import jieba
import collections
import re
from pyecharts.charts import WordCloud,Page,Bar,Line,Boxplot,TreeMap,Scatter
from pyecharts.globals import SymbolType
from pyecharts import options as opts
from pyecharts.globals import ThemeType, CurrentConfig
import pandas as pd
```

我们先从一个与这个项目无关的词云图开始，主要是我喜欢这首歌：<i style="color:red;">一粒红尘</i>，因为豆瓣爬取的数据没有包括评论（其实是爬虫我从CSDN找的代码)。

```python
#文件路径是绝对路径，命名请自行修改或删除
with open("D:\Python\douban_HTML\一粒红尘评论.txt",encoding="utf-8") as f:
    data = f.read()
newdata = re.findall('[\u4e00-\u9fa5]+',data,re.S)
newdata = ' '.join(newdata)
txt_split = jieba.cut(newdata,cut_all=True)
result_list = []
with open("D:\Python\douban_HTML\停用词大全.txt",encoding="utf-8") as f:
    tyc = f.readlines()
    stop_words = set()
    for i in tyc:
        i = i.replace("\n","")
        for i in tyc:
            stop_words.add(i)
#判断
for word in txt_split:
    if word not in stop_words and len(word)>1:
        result_list.append(word)
word_count = collections.Counter(result_list)
word_count_top100 = word_count.most_common(100)
word1 = WordCloud(
    init_opts=opts.InitOpts(
        width='600px', height='400px', theme=ThemeType.WONDERLAND,)
    )
word1.add('词频', data_pair=word_count_top100,
          word_size_range=[5, 100], textstyle_opts=opts.TextStyleOpts(font_family='cursive'),
          shape=SymbolType.DIAMOND)
word1.set_global_opts(title_opts=opts.TitleOpts('一粒红尘评论词云图'),
                      toolbox_opts=opts.ToolboxOpts(is_show=False, orient='vertical'),
                      tooltip_opts=opts.TooltipOpts(is_show=True, background_color='red', border_color='yellow'))
#word1.render("一粒红尘评论词云图.html")
word1.render_notebook()
```

```txt
Building prefix dict from the default dictionary ... Loading model from cache C:\Users\ADMINI~1\AppData\Local\Temp\jieba.cache Loading model cost 1.920 seconds. Prefix dict has been built successfully. d:\Python\python\lib\site-packages\pyecharts\charts\chart.py:14: PendingDeprecationWarning: pyecharts 所有图表类型将在 v1.9.0 版本开始强制使用 ChartItem 进行数据项配置 :)  super().__init__(init_opts=init_opts)
```

**简要总结一下思路：** 

1.先用pandas读取文件 

2.利用re匹配自己想要的内容，这里我们需要匹配中文 

3.调用jieba库进行分词，这里是精确分词 

4.进阶操作，设置自己的停用词txt，进一步精确分词，去除不想要，不相关的词语 

5.通常使用replace()方法去除不想要的字符，很好理解，他的英文就是“代替” 

6.最终数据我们都需要保存到列表---list里面，这样pyacharts才能读取到数据，要不然会报错，并且折线图的x轴数据需要是字符串str类型，建议你们可以试试x，y都是int时，画出的图会咋样 

7.去参照pyecharts中文文档，自己添加组件，下面给大家整理一些主题 

8.格式化代码，避免缩进格式错误 

9.查看效果，这里推荐使用jupyter，在vscode下载这个插件就ok，因为它特殊的ipynb文件可以实时查看效果

官方主题：thm = ''' | CHALK = 'chalk' #粉笔风 |
| DARK = 'dark' #暗黑风 |
| ESSOS = 'essos' #厄索斯大陆 |
| INFOGRAPHIC = 'infographic' #信息图 |
| LIGHT = 'light' #明亮风格 |
| MACARONS = 'macarons' #马卡龙 |
| PURPLE_PASSION = 'purple-passion' #紫色激情 |
| ROMA = 'roma' #石榴 |
| ROMANTIC = 'romantic' #浪漫风 |
| SHINE = 'shine' #闪耀风 |
| VINTAGE = 'vintage' #复古风 |
| WALDEN = 'walden' #瓦尔登湖 |
| WESTEROS = 'westeros' #维斯特洛大陆 |
| WHITE = 'white' #洁白风 | | WONDERLAND = 'wonderland' #仙境 '''

### 接下来步入正题，先读取数据源douban_250_2.csv

[3]

```python
df = pd.read_csv("D:\Python\douban_HTML\douban250_2.csv",header=0,names=["title","info","score","people"])
```

```txt
<>:1: DeprecationWarning: invalid escape sequence \P <>:1: DeprecationWarning: invalid escape sequence \P <>:1: DeprecationWarning: invalid escape sequence \P <ipython-input-3-d1978264e112>:1: DeprecationWarning: invalid escape sequence \P  df = pd.read_csv("D:\Python\douban_HTML\douban250_2.csv",header=0,names=["title","info","score","people"])
```

[4]

```python
df.head(5)#先展示10条
```

|      |          title |                                      info | score |        people |
| ---: | -------------: | ----------------------------------------: | ----: | ------------: |
|    0 |   肖申克的救赎 |                   1994 / 美国 / 犯罪 剧情 |   9.7 | 2186881人评价 |
|    1 |       霸王别姬 | 1993 / 中国大陆 中国香港 / 剧情 爱情 同性 |   9.6 | 1622453人评价 |
|    2 |       阿甘正传 |                   1994 / 美国 / 剧情 爱情 |   9.5 | 1650384人评价 |
|    3 | 这个杀手不太冷 |         1994 / 法国 美国 / 剧情 动作 犯罪 |   9.4 | 1834962人评价 |
|    4 |     泰坦尼克号 |              1997 / 美国 / 剧情 爱情 灾难 |   9.4 | 1604815人评价 |

**通过数据我们可以从<span style="color:orange">电影名字，年份，国家，电影类型，评论人数</span>去分析** 

1.对年份，国家，类型，评分计数---count 

2.电影排名，评分排名 

3.中外电影作品对比 

4.电影与评论数 大家可以自己画一个关系图去扩展些新的思路，比如环比(适合饼图)，这里推荐用drawio这个软件绘图，思维导图可以用ProcessOn 

**有了思路之后，但是这里面的数据并不是很友好，这也就是说我们还需要进行数据清洗**

 1.我们可以用excel，选中info列，进行批量处理单元格操作，以/作为分隔符拆分数据，注意拆分的数据会放在右侧，记得先将info列放置最右侧。 

2.使用pandas进行数据清洗 哈哈，你会发现，对于info列里面的数据，excel也并不好操作，因为类型有多种



### 2.先来一个柱状图  分析豆瓣电影top250的年份统计

**这里先定义几个列表,以免自己混淆，毕竟是将数据整合到一起，追求简洁** 

dom：爬取年份year 	dom1：bar 第一个图表的数据源列表 	dom2: bar2 第二个图表的数据源列表 	

df_last：boxplot 以中国为行索引 	df_last1：以外国为行索引，这里在中外电影评分对比有用处，可直接调用 	

doms2：bar3 国家计数top10 	dom3:bar4 数据源

[5]

```python
#制作电影年份统计柱形图
dom = []
for i in df['info']:
    dom.append(i.split("/")[0].replace('(中国大陆)',"").strip())
df['year'] = dom
place = df.groupby(['year'])['year'].agg(['count'])
place.reset_index(inplace=True)
place_last = place.sort_index()
dom1 = place_last.sort_values('year', ascending=True)
x = list(dom1['year'])
y = list(dom1['count'])
#制作柱形图
bar = (
    Bar(
        init_opts=opts.InitOpts(theme=ThemeType.MACARONS)#在这里可以设置图表宽高
    )
    .add_xaxis(x)
    .add_yaxis("豆瓣电影TOP250年份统计",y)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="",
                                  subtitle="",),
        #设置滚动条
        datazoom_opts=opts.DataZoomOpts(),
        #图例设置
        legend_opts=opts.LegendOpts(
            pos_left='center', # 图例放置的位置，分上下左右，可用左右中表示，也可用百分比表示
            pos_top='5%',
            orient='horizontal',   # horizontal、vertical #图例放置的方式 横着放or竖着放
            textstyle_opts=opts.TextStyleOpts(
                font_size=16,
                color='skyblue',
                font_family='Times New Roman',
            ),
        ),
        yaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(
                color='skyblue',
            ),
        ),
        #显示工具栏
        #toolbox_opts=opts.ToolboxOpts(is_show=True),
    )
    #.render('豆瓣电影TOP250上映年份分布.html')
)
bar.render_notebook()
```

```
d:\Python\python\lib\site-packages\pyecharts\charts\chart.py:14: PendingDeprecationWarning: pyecharts 所有图表类型将在 v1.9.0 版本开始强制使用 ChartItem 进行数据项配置 :)  super().__init__(init_opts=init_opts)
```

**简单总结：** 

1.先用split以/分隔数据输出为列表格式，strip去掉空格，replace去掉特殊数据，仔细观察数据，其实我们应该手动调整一下这个特殊数据，要不然处理太麻烦，不要过度追求完美。csv第51行数据，也可以去豆瓣top上去看。

 2.新构建year列，并对其分组进行计数统计构建count列，这是pandas里面的特殊格式，自己可以type()一下 3.重置索引，默认排序(升序)，具体方法自行百度，我能力有限

### 3.豆瓣电影评分计数，这也是个柱形图，可以自行尝试一下，举一反三

[6]

```python
plase_s = df.groupby(['score'])['score'].agg(['count'])
plase_s.reset_index(inplace=True)
plase_s_last = plase_s.sort_index()
dom2 = plase_s_last.sort_values('score',ascending=True)
plase_s.reset_index(inplace=True)
plase_s_last = plase_s.sort_index()
dom2 = plase_s_last.sort_values('score',ascending=True)
x = list(dom2['score'])
y = list(dom2['count'])
#制作柱形图
bar2 = (
    Bar(
        init_opts=opts.InitOpts(theme=ThemeType.MACARONS,width="600px",height="400px")
    )
    .add_xaxis(x)
    .add_yaxis("豆瓣电影TOP250评分统计",y)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="",
                                  subtitle="",),
        datazoom_opts=opts.DataZoomOpts(),
        #图例设置
        legend_opts=opts.LegendOpts(
            pos_left='center',    # 图例放置的位置，分上下左右，可用左右中表示，也可用百分比表示
            pos_top='5%',
            orient='vertical',   # horizontal、vertical #图例放置的方式 横着放or竖着放
            textstyle_opts=opts.TextStyleOpts(
                font_size=16,
                # color='skyblue',
                font_family='Times New Roman',
            ),
        ),
        yaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(
            ),
        ),
        # #显示工具栏
        # toolbox_opts=opts.ToolboxOpts(is_show=True),
    )
    #.render('豆瓣电影TOP250评分分布.html')
)
bar2.render_notebook()
```

```
d:\Python\python\lib\site-packages\pyecharts\charts\chart.py:14: PendingDeprecationWarning: pyecharts 所有图表类型将在 v1.9.0 版本开始强制使用 ChartItem 进行数据项配置 :)  super().__init__(init_opts=init_opts)
```

### 4.电影类型分布---树形图，这个有点小难

[7]

```python
#制作树形图
(domt1,domt2,domt3,domt4) = ([],[],[],[])
for i in df['info']:
    i = i.split('/')[2].replace('\xa0','').replace(' 1978(中国大陆) ','')
    domt1.append(i)
count = 0
for j in domt1:
    res = j.split(" ")
    for re in res:
        if re not in domt2:
            domt2.append(re)
            count += 1
        else:
            pass
for k in domt2:
    num = 0
    for j in domt1:
        res = j.split(' ')
        for re in res:
            if re == k:
                num += 1
    domt3.append(num)
#生成字典形式
def dict():
    for p in range(len(domt2)):
        data = {}#把类型作为键，计数作为值
        data['name'] = domt2[p]
        data['value'] = domt3[p]
        yield data
data = dict()
for item in data:
    domt4.append(item)
#树形图
treemap = (
    TreeMap(init_opts=opts.InitOpts())#width="600px", height="400px"
    .add(
        series_name="电影类型",
        data=domt4,
        visual_min=300,
        leaf_depth=1,
        # 标签居中为 position = "inside"
        label_opts=opts.LabelOpts(position="inside"),
    )
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=True),
        title_opts=opts.TitleOpts(
            title="", subtitle="2020/11", pos_left="leafDepth"
        ),
    )
    #.render("豆瓣电影TOP250电影类型图.html")
)
treemap.render_notebook()
```

```
d:\Python\python\lib\site-packages\pyecharts\charts\chart.py:14: PendingDeprecationWarning: pyecharts 所有图表类型将在 v1.9.0 版本开始强制使用 ChartItem 进行数据项配置 :)  super().__init__(init_opts=init_opts)
```

**具体思路：** 

1.先分离数据到列表，再split对列表中的元素进行分离到列表

 2.domt2作为一个空列表，设置判断条件，匹配一致就添加，得到电影类型的类目 

3.再设置判断条件，这里的思维比较逆，大家可以先思维导图，能看懂以后看到能想到这种思维就ok了，对于我来说

 4.生成字典，主要是输出格式，这可能是做树形图的标准格式吧 

5.将数据导入列表，这一步跟之前照应了，要是列表做数据源才行哦

### 5.中外电影年份计数分布对比---难度系数等同于树形图

[8]

```python
(c1,c2,c3,c4) = ([],[],[],[])
for i in df['info']:
    country = i.split("/")[1].split(' ')[0].strip()
    if country in ['中国大陆', '台湾', '香港']:
        c1.append('中国')
    else:
        c1.append('外国')
df['country'] = c1
x_c = list(dom1['year'])
#year前面提取过了，就直接拿过来用
#取索引为'中国'的行 # 对中国电影计数排序
df_last = df.loc[df['country'] == '中国']
place = df_last.groupby(['year'])['year'].agg(['count'])
# print(place)
place.reset_index(inplace=True)
place_c_last = place.sort_index()
c3 = place_c_last.sort_values('year', ascending=True)
# 对外国电影计数排序
df_last1 = df.loc[df['country'] == '外国']
place = df_last1.groupby(['year'])['year'].agg(['count'])
# print(place)
place.reset_index(inplace=True)
place_c_last = place.sort_index()
c4 = place_c_last.sort_values('year', ascending=True)
(c5,c6) = ([],[])
for j in x_c:
    for x, y in zip(c3['year'], c3['count']):
        if x == j:
            aaa = int(y)
            break
        else:
            aaa = int('0')
            continue
    c5.append(aaa)
# 外国电影纵坐标
for j in x_c:
    for x, y in zip(c4['year'], c4['count']):
        if x == j:
            aaa = int(y)
            break
        else:
            aaa = int('0')
            continue
    c6.append(aaa)
#绘制折线图
line = (
    Line(
        init_opts=opts.InitOpts(theme=ThemeType.DARK)  # 设置主题 不知道如何添加宽高
    )
    .add_xaxis(x_c)
    .add_yaxis("中国",c5)
    .add_yaxis("外国",c6)
        #.set_colors(["orange"])  # 柱子的颜色
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="",subtitle="",),
        datazoom_opts=opts.DataZoomOpts(),
        #图例设置
        legend_opts=opts.LegendOpts(
            pos_left='center',    # 图例放置的位置，分上下左右，可用左右中表示，也可用百分比表示
            pos_top='5%',
            orient='vertical',   # horizontal、vertical #图例放置的方式 横着放or竖着放
            textstyle_opts=opts.TextStyleOpts(
                font_size=16,
                # color='skyblue',
                font_family='Times New Roman',
            ),
        ),
        yaxis_opts=opts.AxisOpts(
        ),
        #显示工具栏
        # toolbox_opts=opts.ToolboxOpts(is_show=True),
    )
    #.render('豆瓣电影TOP250中外上映年份分布.html')
)
line.render_notebook()
```

```
d:\Python\python\lib\site-packages\pyecharts\charts\chart.py:14: PendingDeprecationWarning: pyecharts 所有图表类型将在 v1.9.0 版本开始强制使用 ChartItem 进行数据项配置 :)  super().__init__(init_opts=init_opts)
```

**具体思路：**交给你们补充了，偷下懒！写于<span  style="color:deeppink">2020-11-24-星期二</span>

### 6.中外电影评分情况

[9]

```python
x_axis = ['中国', '外国']
y_axis = [list(df_last['score']), list(df_last1['score'])]
#制作箱图
boxplot = Boxplot(init_opts=opts.InitOpts(theme=ThemeType.DARK,)) 
#  # 设置主题 不知道如何添加宽高     
boxplot = (
    boxplot.add_xaxis(x_axis)
    .add_yaxis(series_name="评分", y_axis=boxplot.prepare_data(y_axis))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="",subtitle="",),
        #图例设置
        legend_opts=opts.LegendOpts(
            pos_left='center',    # 图例放置的位置，分上下左右，可用左右中表示，也可用百分比表示
            pos_top='5%',
            orient='vertical',   # horizontal、vertical #图例放置的方式 横着放or竖着放
            textstyle_opts=opts.TextStyleOpts(
                font_size=16,
                color='white',
                font_family='Times New Roman',
            ),
        ),
        yaxis_opts=opts.AxisOpts(
            max_=10,
            min_=8,
            type_="value",
            name="评分",
            name_gap=5,
        ),
        #显示工具栏
        # toolbox_opts=opts.ToolboxOpts(is_show=True),
    )
    #.render('豆瓣电影TOP250中外评分情况.html')
)
boxplot.render_notebook()
```

```
d:\Python\python\lib\site-packages\pyecharts\charts\chart.py:14: PendingDeprecationWarning: pyecharts 所有图表类型将在 v1.9.0 版本开始强制使用 ChartItem 进行数据项配置 :)  super().__init__(init_opts=init_opts)
```

**具体思路：**直接调用上一步写好的df_last，df_last1即可，可以自己调试

### 7.条形图---国家-地区电影数TOP10

[10]

```python
doms = []
# 生成电影国家列表
for i in df['info']:
    country = i.split('/')[1].split(' ')[0].strip()
    print(country)
    doms.append(country)
df['country'] = doms
# 计数排序
place_message = df.groupby(['country'])
place_com = place_message['country'].agg(['count'])
print(place_com)
place_com.reset_index(inplace=True)
place_com_last = place_com.sort_index()
doms2 = place_com_last.sort_values('count', ascending=False)[0:10]
# print(doms2)
# 生成柱状图
attr = list(doms2['country'])
v1 = list(doms2['count'])
attr.reverse()
v1.reverse()
print(attr)
print(v1)
bar3 = (
    Bar(
        init_opts=opts.InitOpts(theme=ThemeType.WONDERLAND,)  # 设置主题 不知道如何添加宽高 写到里面去即可
    )
    .add_xaxis(attr)
    .add_yaxis("count",v1)
    .reversal_axis()
    .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        #.set_colors(["orange"])  # 柱子的颜色
    .set_global_opts(
        title_opts=opts.TitleOpts(title="",subtitle="",pos_left="center", ),
        #图例设置
        legend_opts=opts.LegendOpts(
            pos_left='center',    # 图例放置的位置，分上下左右，可用左右中表示，也可用百分比表示
            pos_top='middle',
            orient='vertical',   # horizontal、vertical #图例放置的方式 横着放or竖着放
        ),
         xaxis_opts=opts.AxisOpts(

#                 坐标轴标签的配置
            axislabel_opts=opts.LabelOpts(
                font_size=12,
                font_family='Times New Roman',
                #rotate=45
            ),
        ),
        yaxis_opts=opts.AxisOpts(
        ),
        #显示工具栏
        #toolbox_opts=opts.ToolboxOpts(is_show=True),
    )
    #.render('豆瓣电影TOP250-国家-地区电影数TOP10.html')
)
bar3.render_notebook()
```

```
美国 中国大陆 美国 法国 美国 意大利 日本 美国 美国 美国 意大利 美国 美国 印度 美国 法国 中国香港 韩国 美国 中国香港 美国 日本 美国 美国 法国 美国 美国 中国大陆 英国 美国 美国 黎巴嫩 美国 印度 美国 美国 美国 美国 ...         

count country                    1 中国台湾         6 中国大陆        15 中国香港        19 丹麦           1 伊朗           2 印度           4 巴西           1 德国           5 意大利          6 新西兰          1 日本          32 法国           8 泰国           1 澳大利亚         3 爱尔兰          1 瑞典           1 美国         112 英国          17 西班牙          1 阿根廷          1 韩国          11 黎巴嫩          1 

['德国', '中国台湾', '意大利', '法国', '韩国', '中国大陆', '英国', '中国香港', '日本', '美国'] [5, 6, 6, 8, 11, 15, 17, 19, 32, 112] 

d:\Python\python\lib\site-packages\pyecharts\charts\chart.py:14: PendingDeprecationWarning: pyecharts 所有图表类型将在 v1.9.0 版本开始强制使用 ChartItem 进行数据项配置 :)  super().__init__(init_opts=init_opts)
```

**注意事项：**柱形图添加reverse()就可以得到条形图了

### 8.豆瓣电影TOP250评价人数分布

[11]

```python
(dom1, dom2) = ([], [])
# 清洗数据,建立评价人数列
for i in df['people']:
    dom1.append(i.replace('人评价', ''))
df['people_last'] = dom1
# print(dom1)
# print(df['people_last'])
# 清洗数据,建立电影名称列(取第一个)
for j in df['title']:
    dom2.append(j)
df['title_last'] = dom2
# 切换为整型
df["people_last"] = df["people_last"].astype("int")
# 计数排序,取前10
dom3 = df[['title_last', 'people_last']].sort_values('people_last', ascending=False)[0:10]
# 生成柱状图
attr = list(dom3["title_last"])
v1 = list(dom3['people_last'])
attr.reverse()
v1.reverse()
print(attr)
print(v1)
bar4 = (
    Bar(
        init_opts=opts.InitOpts(theme=ThemeType.WONDERLAND,))  # 设置主题 不知道如何添加宽高 写到里面去即可
    .add_xaxis(attr)
    .add_yaxis("2019年豆瓣电影TOP10评价人数统计",v1)
    .reversal_axis()
    .set_series_opts(label_opts=opts.LabelOpts(position="right"))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="",subtitle="",),
        #图例设置
        legend_opts=opts.LegendOpts(
            pos_left='center',    # 图例放置的位置，分上下左右，可用左右中表示，也可用百分比表示
            pos_top='bottom',
            orient='vertical',   # horizontal、vertical #图例放置的方式 横着放or竖着放
            textstyle_opts=opts.TextStyleOpts(
                font_size=16,
                # color='skyblue',
                font_family='Times New Roman',
            ),
        ),
         xaxis_opts=opts.AxisOpts(
#                 坐标轴标签的配置
            axislabel_opts=opts.LabelOpts(
                font_size=12,
                font_family='Times New Roman',
                #rotate=45
            ),
        ),
        yaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(
                font_size=12,
                font_family='Times New Roman',
                # color='skyblue',
            ),
        ),
        #显示工具栏
        #toolbox_opts=opts.ToolboxOpts(is_show=False),
    )
   #.render('豆瓣电影TOP250评价人数分布.html') 
)
bar4.render_notebook()
```

### 9.评分维度散点图

[12]

```python
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
       init_opts=opts.InitOpts(theme=ThemeType.WONDERLAND,)  # 设置主题 不知道如何添加宽高 写到里面去即可
    )
    .add_xaxis(x_lst)
    .add_yaxis("评分",y_lst)
    #.add_yaxis("评价人数",extra_data)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="",
        subtitle="",),
        visualmap_opts=opts.VisualMapOpts(
            dimension = extra_data,
            is_show = True,
            series_index = [x_lst,extra_data],
            type_="size",
            min_=min(y_lst),
            max_=max(y_lst),
            range_text = ['High', 'Low'],
            orient = "horizontal",
        ),
         xaxis_opts=opts.AxisOpts(
             interval= max(x_lst)-min(x_lst),  # Optional[Numeric]
             grid_index=0,  # Numeric
             split_number= 50,  # Numeric
            #  boundary_gap='',  # Union[str, bool, None]
             
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
        ),
        yaxis_opts=opts.AxisOpts(
            min_= 8,  # Union[Numeric, str, None]
            max_= 10,  # Union[Numeric, str, None]
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
        #toolbox_opts=opts.ToolboxOpts(is_show=True),
    )
    #.render('豆瓣电影TOP250-排名评分人数三维度.html')
)
sc.render_notebook()
```

**说明：**这个图存在一点问题，功能没有完全实现，本来是三维散点图，但是现版本，我不知道如何画平面的三维散点图。上面是一个二维散点图，还可以进一步修改完善



***最后，就是将这8个表整合到一起了。*** 通过学习pyecharts中文文档，我们可以得知 

overlap：用来实现在一个图表里面添加多种类型，如bar和line，并且设置元件可以有多个y轴(一般是固定x轴) 

grid：用来在一个盒子里装多个图表，是一个整体 

page：实现多个图表可以自由移动，并且都在同一个html里 

所以，这里我们使用**Page方法**

### 10.调用Page方法

[13]

```python
page = Page(layout=Page.DraggablePageLayout)
page.add(
bar,
bar2,
bar3,
bar4,
line,
sc,
word1,
treemap,
boxplot
)
page.render_notebook()
page.render('render.html')
#Page.save_resize_html('render.html',cfg_file='chart_config.json')
```

**注意事项：**这里先注释掉最后一句，然后打开生成的render.html，下载chart_config.json到本地，然后再执行最后一句，会得到一个resize_render.html 二者有区别，大家可以试试

**常见报错解决**

UndefinedError: 'int object' has no attribute 'endswith' 这里是因为给图表设置width，height里面要给字符串，不能是int

项目所有资源我都整理到这里了，请自行下载！

下载链接：https://pan.baidu.com/s/10gBk44MpTimBYHaZ7D6jeQ 
提取码：love 
<!--复制这段内容后打开百度网盘手机App，操作更方便哦-->

github地址：https://github.com/git123hub121/Python---TOP250.git

## 实现可视化效果

在网上找一个模板，放心，我给你了。

对模板进行对应的添加，最好先把各图表的参数都调好，以免反复调试。具体就不多叙述了。

### 最终效果：

<img src="../../Pictures/Python图片/Python截图/可视化豆瓣.png" alt="可视化豆瓣" style="zoom:50%;" />
