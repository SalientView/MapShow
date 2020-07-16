from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType

a = Geo()

a.add_schema(
            maptype="china",
            itemstyle_opts=opts.ItemStyleOpts(color="#323c40", border_color="gray"),
            is_roam=True,
            zoom=1,)

a.add("",[("广州", 44), ("北京", 66), ("杭州", 77), ("重庆", 88), ("西安", 99)],  #后边的数字代表每个城市的数据
            type_=ChartType.EFFECT_SCATTER,
            color="white",)

a.add("",[("广州", "上海"), ("广州", "北京"), ("广州", "杭州"), ("广州", "重庆"),("广州", "西安")],
            type_=ChartType.LINES,
            effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW, symbol_size=6, color="gold"),
            linestyle_opts=opts.LineStyleOpts(curve=0.1),)

a.set_series_opts(label_opts=opts.LabelOpts(is_show=False)).set_global_opts(title_opts=opts.TitleOpts(title="航线图"))

a.render_notebook()
