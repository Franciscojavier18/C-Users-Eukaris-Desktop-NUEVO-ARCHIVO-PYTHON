from matplotlib import rcParams
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st


rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['DejaVu Sans', 'Tahoma']


mu, sigma = 0, 1.0 # media y desvio estandar
datos = np.random.normal(mu, sigma, 10000) #creando muestra de datos
x = np.linspace(-4, 4, num=1000)
y = st.norm.pdf(x, 0, 1)


plt.plot(x, y, 'r--', label=(u"μ={}, σ²={}".format(mu, sigma)))
plt.legend(loc="upper right") 
plt.show()