import script01
import script03
import script06


a_mle_c12, b_mle_c12 = gamma_mle(c12)
a_mle_c07, b_mle_c07 = gamma_mle(c07)
a_mle_c09, b_mle_c09 = gamma_mle(c09)
a_mle_c10, b_mle_c10 = gamma_mle(c10)
a_mle_c14, b_mle_c14 = gamma_mle(c14)

p = iqplot.ecdf(data=c07, q='time to catastrophe (s)',conf_int=True, palette="#264653",  legend_label='7 μM')
p = iqplot.ecdf(data=c09, q='time to catastrophe (s)',conf_int=True, palette="#2a9d8f",  legend_label='9 μM',p=p)
p = iqplot.ecdf(data=c10, q='time to catastrophe (s)',conf_int=True, palette="#e9c46a",  legend_label='10μM',p=p)
p = iqplot.ecdf(data=c12, q='time to catastrophe (s)',conf_int=True, palette="#f4a261",  legend_label='12μM',p=p)
p = iqplot.ecdf(data=c14, q='time to catastrophe (s)',conf_int=True, palette="#e76f51",  legend_label='14 μM',p=p)

t_theor = np.linspace(0, 2000, 200)
cdf_7 = st.gamma.cdf(t_theor, a_mle_c07, loc=0, scale=1/b_mle_c07)
cdf_9 = st.gamma.cdf(t_theor, a_mle_c09, loc=0, scale=1/b_mle_c09)
cdf_10 = st.gamma.cdf(t_theor, a_mle_c10, loc=0, scale=1/b_mle_c10)
cdf_12 = st.gamma.cdf(t_theor, a_mle_c12, loc=0, scale=1/b_mle_c12)
cdf_14 = st.gamma.cdf(t_theor, a_mle_c14, loc=0, scale=1/b_mle_c14)

p.line(t_theor, cdf_7, line_width=2, color='#1e3842')
p.line(t_theor, cdf_9, line_width=2, color='#217b71')
p.line(t_theor, cdf_10, line_width=2, color='#dfac29')
p.line(t_theor, cdf_12, line_width=2, color='#ef7c1d')
p.line(t_theor, cdf_14, line_width=2, color='#d7421d')

bokeh.io.show(p)
