import script01

#Model 2: The arrival of two successive Poisson processes (with different rates) immediately trigger microtubule #catastrophe.


#the function for the log likelihood of the model 2 function
def log_like(beta1, t):
    """Compute the log likelihood for a given value of β1,
    assuming Δβ is set so that the dervitive of the log
    likelihood with respect to β1 vanishes."""
    n = len(t)
    tbar = np.mean(t)
    beta1_tbar = beta1 * tbar
    
    if beta1_tbar > 2 or beta1_tbar < 1:
        return np.nan

    if np.isclose(beta1_tbar, 2):
        return -2 * n * (1 + np.log(tbar) - np.log(2)) + np.sum(np.log(t))
        
    if np.isclose(beta1_tbar, 1):
        return -n * (1 + np.log(tbar))
            
    delta_beta = beta1 * (2 - beta1 * tbar) / (beta1 * tbar - 1)

    ell = n * (np.log(beta1) + np.log(beta1 + delta_beta) - np.log(delta_beta))
    ell -= n * beta1_tbar
    ell += np.sum(np.log(1 - np.exp(-delta_beta * t)))
    
    return ell


def dlog_like_dbeta1(beta1, t):
    """Returns the derivative of the log likelihood w.r.t. Δβ
    as a function of β1, assuming Δβ is set so that the dervitive 
    of the log likelihood with respect to β1 vanishes."""
    n = len(t)
    tbar = np.mean(t)
    beta1_tbar = beta1 * tbar
    
    if beta1_tbar > 2 or beta1_tbar < 1:
        return np.nan

    if np.isclose(beta1_tbar, 2) or np.isclose(beta1_tbar, 1):
        return 0.0
            
    delta_beta = beta1 * (2 - beta1 * tbar) / (beta1 * tbar - 1)
    
    exp_val = np.exp(-delta_beta * t)
    sum_term = np.sum(t * exp_val / (1 - exp_val))
    
    return -n / delta_beta + n / (beta1 + delta_beta) + sum_term


def mle_two_step(t, nbeta1=500):
    """Compute the MLE for the two-step model."""
    # Compute ∂ℓ/∂Δβ for values of beta_1
    tbar = np.mean(t)
    beta1 = np.linspace(1 / tbar, 2 / tbar, nbeta1)
    deriv = np.array([dlog_like_dbeta1(b1, t) for b1 in beta1])
    
    # Add the roots at the edges of the domain
    beta1_vals = [1 / tbar, 2 / tbar]
    ell_vals = [log_like(beta1_vals[0], t), log_like(beta1_vals[1], t)]
    
    # Find all sign flips between the edges of the domain
    sign = np.sign(deriv[1:-1])
    inds = np.where(np.diff(sign))[0]
    
    # Perform root finding at the sign flips
    for i in inds:
        b1 = scipy.optimize.brentq(dlog_like_dbeta1, beta1[i+1], beta1[i+2], args=(t,))
        beta1_vals.append(b1)
        ell_vals.append(log_like(b1, t))
        
    # Find the value of beta1 that gives the maximal log likelihood
    i = np.argmax(ell_vals)
    beta1 = beta1_vals[i]

    # Compute beta 2
    if np.isclose(beta1, 1 / tbar):
        delta_beta = np.inf
    else:
        delta_beta = beta1 * (2 - beta1 * tbar) / (beta1 * tbar - 1)

    beta2 = beta1 + delta_beta
    
    return np.array([beta1, beta2])