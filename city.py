from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType

c = Geo()
c.add_schema(
            maptype="china",
            itemstyle_opts=opts.ItemStyleOpts(color="#323c48", border_color="gray"),
            is_roam=True,
            zoom=1,
        )
c.add("港口",
            [("天津", 27),
             ("唐山",10),
             ("沧州",6),
             ("日照",5),
             ("大连",5),
             ("秦皇岛",4),
             ("连云港",4),
             ("青岛",3),
             ("镇江",3),
             ("福州",3),
             ("潍坊",2),
             ("广州",2),
             ("厦门",2),
             ("北海",1),
             ("黄埔",1),
             ("秦皇岛",1),
             ("南通",1),
             ("杭州",1),
             ("上海",1),
             ("香港",1),
             ("澳门",1),
             ("深圳",1),
             ("汕头",1),
             ("烟台",1),
             ("威海",1),
             ("芜湖",1),
             ("南京",1),
             ("温州",1),
             ("嘉兴",1),
            ],type_=ChartType.EFFECT_SCATTER,color="gold")
c.add("机场",
        [("北京",6),
        ("呼和浩特",4),
         ("南昌",4),
         ("贵州",4),
         ("成都",4),
         ("哈尔滨",2),
         ("乌鲁木齐",1),
         ("郑州",1),
         ("沈阳",2),
         ("长春",1),
        ],type_=ChartType.EFFECT_SCATTER,color="deepskyblue")
c.set_series_opts(label_opts=opts.LabelOpts(is_show=False)).set_global_opts(title_opts=opts.TitleOpts(title="港口机场分布图"))
c.render_notebook()
