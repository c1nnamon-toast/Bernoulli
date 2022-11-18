import matplotlib.pyplot as plt
import mplcursors
import numpy as np

def start():
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
    res = [[], []];
    q, prob, i = 1 - p, 0, 0;

    while(True):
        prob = dp[i] * (p ** i) * (q ** (n - i)); # dp[i] as C(n, i);
        if(prob >= 0.005):
            break;
        i += 1;
    
    while(prob >= 0.005):
        res[1].append(prob);
        res[0].append(i);
        prob = dp[i] * (p ** i) * (q ** (n - i));
        i += 1;
    
    return res;


def show_trials(res):   
    plt.figure(figsize = (12, 8));

    plt.plot(res[0], res[1], ".-");
    mplcursors.cursor(hover=True);

    plt.legend(['by CEO of Abibas for BBS community']);
    plt.ylabel("Probability");
    plt.xlabel("Number of characters");
    plt.show();


if (__name__ == "__main__"):
    
    n, p = start();
    dp = pascal(n);
    res = trials(n, p, dp);

    show_trials(res);    