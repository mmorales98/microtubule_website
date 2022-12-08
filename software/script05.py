import script01
import script03
import script04

p = iqplot.ecdf(data=c12, q='time to catastrophe (s)',conf_int=True, palette="#2a9d8f",  legend_label='experimental')
t_theor = np.linspace(0, 2000, 200)
cdf = st.gamma.cdf(t_theor, a_mle, loc=0, scale=1/b_mle)
p.line(t_theor, cdf, line_width=2, color='#e76f51', legend_label='theoretical')

bokeh.io.show(p)