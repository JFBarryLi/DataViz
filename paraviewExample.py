import numpy as np
import pandas as pd

def paraviewExample():
	'''
	NACA 23018 Airfoil
	'''
	
	# Resolution
	n = 100000
	
	# Init arrays
	x = np.arange(0,1, 1/n)
	yt = np.zeros(n)
	yc = np.zeros(n)
	ytop = np.zeros(n)
	ybot = np.zeros(n)
	
	for i in range(0, n):
		# Thickness
		yt[i] = 0.18/0.2*(0.2969*np.sqrt(x[i])-0.126*x[i]-0.3516*x[i]**2+0.2843*x[i]**3-0.1015*x[i]**4)
		
		# Camber Line
		if x[i] < 0.2025:
			yc[i] = (15.957/6)*((x[i]**3)-(3*0.2025)*(x[i]**2)+(0.2025**2)*(3-0.2025)*x[i])
		else:
			yc[i] = (15.957/6)*(0.2025)**3*(1-x[i])
		
		# Resultant Geometry
		ytop[i] = yc[i] + yt[i]
		ybot[i] = yc[i] - yt[i]
		
	
	dataset = pd.DataFrame({'x':x, 'Camber':yc, 'ytop':ytop, 'ybot':ybot})
	dataset.to_csv('paraviewExample.csv', index = None, header=True)
	
	return dataset
	
paraviewExample()