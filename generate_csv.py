import pandas as pd
from complexity import *

def Triangle(n):

    PT = [[1] for _ in range(n + 1)];

    for i in range(1, n + 1):
        for j in range (1, i):
            PT[i].append(PT[i - 1][j - 1] + PT[i - 1][j]);
        
        PT[i].append(1);
    
    return PT;

if __name__ == '__main__' :
    _ = Calculate(time.perf_counter());    

    PascalsTriangle = Triangle(1000);  

    # Save as a DF

    df = pd.DataFrame(PascalsTriangle);
    df.to_csv("triangle.csv");

    # print(pd.read_csv("triangle.csv")["2"][5]);
    
    _.time(time.perf_counter());