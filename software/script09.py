import script01
import script03
import script06
import script07

a_mle_c12, b_mle_c12 = gamma_mle(c12)
a_mle_c07, b_mle_c07 = gamma_mle(c07)
a_mle_c09, b_mle_c09 = gamma_mle(c09)
a_mle_c10, b_mle_c10 = gamma_mle(c10)
a_mle_c14, b_mle_c14 = gamma_mle(c14)
alphas=np.array([a_mle_c07,a_mle_c09, a_mle_c10, a_mle_c12, a_mle_c14])
betas=np.array([b_mle_c07,b_mle_c09, b_mle_c10, b_mle_c12, b_mle_c14])

conc=np.array([7,9,10,12,14])
res=pd.DataFrame({'Concentration of tubulin (μM)':conc, 'alpha MLE': alphas, 'beta MLE':betas})
res