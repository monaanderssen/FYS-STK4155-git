# Plotting:
# Importing necessary packages for plotting
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
#from matplotlib.pyplot import figure, show, plot
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.ticker import LinearLocator, FormatStrFormatter #, MaxNLocator
#import matplotlib.ticker as ticker

#def plotStatistics()

def plotMSE():#mse_OLS, mse_Ridge, mse_Lasso):
    file = open('data.txt', 'r')
    alpha = float(file.readline())
    i = 0
    mse_OLS = np.zeros(15)
    for line in file:
        line_ = line.split()
        mse_OLS[i] = line_[0]
        i += 1
    print(mse_OLS)

"""
    poly = [i+1 for i in range(len(mse_OLS))]
    plt.plot(poly,mse_OLS)
    plt.plot(poly, mse_Ridge)
    plt.plot(poly,mse_Lasso)
    plt.legend(['OLS', 'Ridge', 'Lasso'])
    plt.title('Mean squared error calculated with different methods')
    plt.xlabel('Polynomial degree')
    plt.ylabel('Mean squared error')
    plt.show()
"""
def plotBias(bias_OLS,bias_Ridge,bias_Lasso):
    poly = [i+1 for i in range(len(mse_OLS))]
    plt.plot(poly,bias_OLS)
    plt.plot(poly, bias_Ridge)
    plt.plot(poly,bias_Lasso)
    plt.legend(['OLS', 'Ridge', 'Lasso'])
    plt.title('Bias calculated with different methods')
    plt.xlabel('Polynomial degree')
    plt.ylabel('Bias')
    plt.show()  

def plotVariance(var_OLS,var_Ridge,var_Lasso):
    poly = [i+1 for i in range(len(mse_OLS))]
    plt.plot(poly,var_OLS)
    plt.plot(poly, var_Ridge)
    plt.plot(poly,var_Lasso)
    plt.legend(['OLS', 'Ridge', 'Lasso'])
    plt.title('Variance calculated with different methods')
    plt.xlabel('Polynomial degree')
    plt.ylabel('Variance')
    plt.show()

def plotR2(r2_OLS, r2_Ridge, r2_Lasso):
    poly = [i+1 for i in range(len(r2_OLS))]
    plt.plot(poly, r2_OLS)
    plt.plot(poly, r2_Ridge)
    plt.plot(poly, r2_Lasso)
    plt.legend(['OLS','Ridge','Lasso'])
    plt.title('R2 score calculated with different methods')
    plt.xlabel('Polynomial degree')
    plt.ylabel('R2 score')
    plt.show()


def plotFrankeFunction(x, y, z, type):
    #x = np.sort(x)
    #y = np.sort(y)
    #x, y = np.meshgrid(x, y)
    #x = x.reshape(-1,1)
    #y = y.reshape(-1,1)
    #z = z.reshape(-1,1)
    print(x.shape)
    print(z.shape)
    #z = FrankeFunction(x,y)
    #n,m = x.shape 
    #z = z.reshape(n,m)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    if type==1:
        plt.title('Franke function with actual z')
    elif type==2:
        plt.title('Franke function with our prediction of z')
    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()

    # Customize the z axis.
    #ax.set_zlim(-0.10, 1.40)
    #ax.zaxis.set_major_locator(LinearLocator(10))
    #ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f')) 
    return surf

# Plotting Franke function with actual z:
#plotFrankeFunction(x, y, z, type=1)

# Plotting Franke function with our prediction of z:
#plotFrankeFunction(x, y, zpredict, type=2)
"""
# Plotting Ridge:
def plotRidge(x,y):
    # Sorting
    sort_ind = np.argsort(x[:,0])

    x_plot = x[sort_ind,0]
    x_centered_plot = x_[sort_ind,0]

    pred_ls_plot = pred_ls[sort_ind,0]
    pred_ridge_plot = pred_ridge[sort_ind,:]
    pred_ridge_centered_plot = pred_ridge_centered[sort_ind,:]

    # Plott not centered
    plt.plot(x_plot,pred_ls_plot,label='ls')

    for i in range(num_values):
        plt.plot(x_plot,pred_ridge_plot[:,i],label='ridge, lmb=%g'%lmb_values[i])

    plt.plot(x,y,'ro')

    plt.title('linear regression on un-centered data')
    plt.legend()

    # Plott centered
    plt.figure()

    for i in range(num_values):
        plt.plot(x_centered_plot,pred_ridge_centered_plot[:,i],label='ridge, lmb=%g'%lmb_values[i])

    plt.plot(x_,y,'ro')

    plt.title('linear regression on centered data')
    plt.legend()


    # 2.

    pred_ridge_scikit =  np.zeros((n_samples,num_values))
    for i,lmb in enumerate(lmb_values):
        pred_ridge_scikit[:,i] = (Ridge(alpha=lmb,fit_intercept=False).fit(X,y).predict(X)).flatten() # fit_intercept=False fordi bias er allerede i X

    plt.figure()

    plt.plot(x_plot,pred_ls_plot,label='ls')

    for i in range(num_values):
        plt.plot(x_plot,pred_ridge_scikit[sort_ind,i],label='scikit-ridge, lmb=%g'%lmb_values[i])

    plt.plot(x,y,'ro')
    plt.legend()
    plt.title('linear regression using scikit')

    plt.show()
    return 

plotRidge(x, y)
"""

"""
plt.scatter(X,z,color='green', label="Training Data")
plt.plot(X, predl, color='blue', label="Lasso")
plt.legend()
plt.show()
"""
