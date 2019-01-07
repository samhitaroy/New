def paretoplt(alphas):
    import numpy as np
    from matplotlib import pyplot as plt
    from scipy.stats import pareto

    xm = 1 # scale 
    x = np.linspace(0, 5, 1000)
    output = np.array([pareto.pdf(x, scale = xm, a) for a in alphas])
    plt.plot(x, output.T)
    plt.show()
    return;

alphas = [1,2.5,5]
paretoplt(alphas)

