import matplotlib.pyplot as plt
import mplcursors
import numpy as np

def start():
    print("Enter a number of probabilities: ", end = "");
    k = int(input());

    return k;


def next():
    print("Enter a number of attempts: ", end = "");
    n = int(input());
    print("Enter a succes probability: ", end = "");
    p = float(input());

    return n, p;


def pascal(n):
    dp = [1 for _ in range(n + 1)];
    
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] * (n - i + 1) / i;

    return dp;


def trials(n, p, dp):
    res = [];
    q = 1 - p;

    for i, c in enumerate(dp):
        prob = c * (p ** i) * (q ** (n - i));
        res.append(prob);
    
    return res;


def show_trials(res):
    # res = list(filter(lambda x: x >= 0.005, res));     
    
    plt.figure(figsize = (12, 8));
    plt.plot(res, '.-');
    mplcursors.cursor(hover=True);

    plt.ylabel("Probability");
    plt.xlabel("Number of");
    plt.show();


if (__name__ == "__main__"):
    k = start();
    res = [];

    for i in range(k):
        n, p = next();
        dp = pascal(n);
        if(len(res) == 0):
            res = [float(1) for _ in range(n + 1)];
        print(res);
        res = list(np.multiply(res, trials(n, p, dp)));

    show_trials(res);    