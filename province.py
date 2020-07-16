from pyecharts.charts import Map

c = Map()
c.add("省份", [("天津", 27),
             ("河北",10),
             ("山东",6),
             ("江苏",5),
             ("辽宁",5),
             ("北京",4),
             ("福建",4),
             ("内蒙古",3),
             ("广东",3),
             ("黑龙江",3),
             ("浙江",2),
             ("新疆",2),
             ("吉林",2),
             ("河南",1),
             ("广西",1),
            ],"china")
c.set_global_opts(title_opts=opts.TitleOpts(title="省份分布图"),
                  visualmap_opts=opts.VisualMapOpts(max_=20),)
    


c.render_notebook()
