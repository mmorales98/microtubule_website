import script01
#plot ecdf for all data
p = iqplot.ecdf(data=c12, q='time to catastrophe (s)',conf_int=True, palette="#264653",  legend_label='12 μM')
p = iqplot.ecdf(data=c07, q='time to catastrophe (s)', conf_int=True, palette="#2a9d8f", p=p, legend_label='7 μM')
p = iqplot.ecdf(data=c09, q='time to catastrophe (s)', conf_int=True, palette="#e9c46a", p=p, legend_label='9 μM')
p = iqplot.ecdf(data=c10, q='time to catastrophe (s)', conf_int=True, palette="#f4a261",  p=p, legend_label='10 μM')
p = iqplot.ecdf(data=c14, q='time to catastrophe (s)', conf_int=True, palette="#e76f51", p=p, legend_label='14 μM')
bokeh.io.show(p)