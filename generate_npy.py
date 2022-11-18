import numpy as np
from complexity import *

def Triangle(n):

    # PT = np.empty([n + 1, n + 1]);
    PT = np.zeros((n + 1, n + 1));

    for i in range(0, n + 1):
        PT[i][0] = 1;
        
        for j in range (1, i):
            PT[i][j] = PT[i - 1][j - 1] + PT[i - 1][j];
        
        PT[i][i] = 1;

    return PT;

if __name__ == '__main__' :
    _ = Calculate(time.perf_counter());  

    PascalsTriangle = np.array(Triangle(1000));  

    # Save as a numpy file

    np.save("triangle", PascalsTriangle);
    # print(np.load("triangle.npy")[5][2]);    

    _.time(time.perf_counter());