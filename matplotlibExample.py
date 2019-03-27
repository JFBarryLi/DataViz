import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def matplotlibExample():

	# Number of interior points
	nx = 100
	ny = 100
	
	# Geometry
	x_max = 0.05
	x_min = -0.05
	y_max = 0.05
	y_min = -0.05
	
	deltax = (x_max-x_min)/(nx+1)
	deltay = (y_max-y_min)/(ny+1)
	
	X = np.zeros([nx,ny])
	Y = np.zeros([nx,ny])
	Z = np.zeros([nx,ny])
	
	for i in range(0,nx):
		for j in range(0,ny):
			X[i,j] = x_min + (i+1)*deltax
			Y[i,j] = y_min + (j+1)*deltay
			
	# Boundary
	Tb = 20
	
	# Constant
	k = 0.25
	
	# Matrix
	num = nx*ny
	
	A = np.zeros([num,num])
	T = np.zeros([num,1])
	S = np.zeros([num,1])
	BC = np.zeros([num,1])
	
	
	for j in range(0,ny):
		for i in range(0,nx):
							
			# Global index
			index = i + nx*(j-1)
			
			# Coolant area
			x_cord = x_min + (i+1)*deltax
			y_cord = y_min + (j+1)*deltay
			# coolant_range1 for configuration 1 and coolant_range2 for configuration 2
			if coolant_range2(x_cord, y_cord):
				A[index,index] = 1
				S[index] = 0
				BC[index] = 5
			else:			
				# Diagonal terms
				A[index,index] = k*(2/deltax**2+2/deltay**2)
				
				# x-dir terms
				if i == 0:
					BC[index] = BC[index]+k*Tb/deltax**2
				else:
					A[index,index-1] = -k/deltax**2

				if i == nx-1:
					BC[index] = BC[index]+k*Tb/deltax**2
				else:
					A[index,index+1] = -k/deltax**2
					
				# y-dir terms
				if j == 0:
					BC[index] = BC[index]+k*Tb/deltay**2
				else:
					A[index,index-nx] = -k/deltay**2
					
				if j == ny-1:
					BC[index] = BC[index]+k*Tb/deltay**2
				else:
					A[index,index+nx] = -k/deltay**2
				
				# Source
				x = X[i,j]
				y = Y[i,j]
				S[index] = source(x,y)
			
			

	RHS = S + BC
	T = np.linalg.solve(A, RHS)
	
	print('nx = '+str(nx)+', ny = '+str(ny)+', Max T = '+str(max(T))+' degrees Celsius')
		
	# Plot
	for j in range(0,ny):
		for i in range(0,nx):
			Z[i,j] = T[i+j*nx]
			
	fig = plt.figure(1)
	ax = plt.subplot(111)
	cs = ax.contourf(X,Y,Z, cmap=cm.coolwarm)
	fig.colorbar(cs)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Temperature Distribution', weight='bold')
	
	fig2 = plt.figure(2)
	ax = fig2.gca(projection='3d')
	surf = ax.plot_surface(X,Y,Z, cmap=cm.coolwarm)
	fig2.colorbar(surf)
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	ax.set_zlabel('T')
	plt.title('Temperature Distribution', weight='bold')
	
	plt.show(block=False)
			
			
def source(x,y):

	if abs(x) < 0.01 and abs(y) < 0.01:
		output = 125000.0
	else:
		output = 0.0
		
	return output
				
def coolant_range1(x,y):
	if np.sqrt((-0.025-x)**2 + (-0.025-y)**2) <= 0.01:
		return True
	elif np.sqrt((0.025-x)**2 + (0.025-y)**2) <= 0.01:
		return True
	else:
		return False
	
def coolant_range2(x,y):
	if np.sqrt((-0.025-x)**2 + (-0.025-y)**2) <= 0.01:
		return True
	elif np.sqrt((0.025-x)**2 + (0.025-y)**2) <= 0.01:
		return True
	elif np.sqrt((-0.025-x)**2 + (0.025-y)**2) <= 0.01:
		return True
	elif np.sqrt((0.025-x)**2 + (-0.025-y)**2) <= 0.01:
		return True
	else:
		return False
				
matplotlibExample()