import matplotlib.pyplot as plt
import mplcursors
# import numpy as np

def start():
    # implement try

    n = int(input("Enter a number of attempts: "));
    p = float(input("Enter a succes probability: ")); 

    return n, p;


def pascal(n):
    dp = [1 for _ in range(n + 1)];
    
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] * (n - i + 1) / i;

    return dp;


def trials(n, p, dp, minprob):
    res = [[], []];
    q, prob, i = 1 - p, 0, 0;

    while(True):
        prob = dp[i] * (p ** i) * (q ** (n - i)); # dp[i] as C(n, i);
        if(prob >= minprob):
            break;
        i += 1;
    
    while(prob >= minprob):
        res[1].append(prob);
        res[0].append(i);
        prob = dp[i] * (p ** i) * (q ** (n - i));
        i += 1;
    
    return res;


def show_trials(res):   
    plt.figure(figsize = (12, 8));

    plt.plot(res[0], res[1], ".-");
    mplcursors.cursor(hover=True);

    plt.legend(["by opium"]);
    plt.ylabel("Probability");
    plt.xlabel("Number of characters");
    plt.show();


if __name__ == "__main__":
    n, p = start();
    dp = pascal(n);
    minprob = 0.005;
    res = trials(n, p, dp, minprob);

    show_trials(res);    