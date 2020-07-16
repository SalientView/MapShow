from pyecharts import options as opts
from pyecharts.charts import Map


world_map = Map(init_opts=opts.InitOpts(bg_color="#FFFAFA"))

data = {
    "系列1":[['Denmark',1],
      ['Uruguay',7],
      ['Canada',5],
      ['New Zealand',27],
      ['Chile',1],
      ['France',2],
      ['Australia',57],
      ['Ireland',2],
      ['Spain',2],
      ['Argentina',2],
      ['United States',2]],
    "系列2":[["China",105]],
}

world_map.add("系列1",data["系列1"],"world",is_map_symbol_show=False)
world_map.add("系列2",data["系列2"],"world",is_map_symbol_show=False)

world_map.set_series_opts(label_opts=opts.LabelOpts(position="right",is_show=False))

world_map.set_global_opts(
     title_opts=opts.TitleOpts(title="世界热力图"),
     visualmap_opts=opts.VisualMapOpts(max_=105,is_piecewise=True),
 )

world_map.render_notebook()
