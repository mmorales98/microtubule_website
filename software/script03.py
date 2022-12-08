import scipt01

#Model 1: Gamma

#the function for the log likelihood of the gamma function
def log_like_gamma(params, t):
    """Log likelihood for a Gamma distribution."""
    alpha, beta = params
    
    if alpha <= 0 or beta <= 0:
        return -np.inf
    
    return st.gamma.logpdf(t, alpha, loc=0, scale=1/beta).sum()

#gamma mle function
def gamma_mle(t):
    # Initial guess
    t_bar = np.mean(t)
    beta_guess = t_bar / np.var(t)
    alpha_guess = t_bar * beta_guess

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        # We need to crank up the tolerance for this one
        res = scipy.optimize.minimize(
            lambda params, t: -log_like_gamma(params, t),
            (alpha_guess, beta_guess),
            args=(t,),
            method="powell",
            tol=1e-7,
        )

    if res.success:
        return res.x
    else:
        raise RuntimeError('Convergence failed with message', res.message)

