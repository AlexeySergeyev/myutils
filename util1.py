import numpy as np
import matplotlib.pyplot as plt
# from scipy import stats

def init(isshow=False):
    x = 15 + np.random.random(N) * 9
    y = np.random.normal(loc = 0.0, scale=0.1, size=N) / (x.max()*1.1 - x)
    if isshow:
        plt.scatter(x, y)
        plt.show()
    return x, y

def seq(isshow=False):
    sn = 10
    sx = np.linspace(x.min(), x.max(), sn+1)
    # sy = np.zeros(sn)
    print(sx)
    h2 = (sx[1]-sx[0])/2
    # print(sx)
    med = np.zeros(sn, dtype=float)
    sig = np.zeros(sn, dtype=float)
    for i in range(sn):
        sy = y[((x>=sx[i]) & (x<sx[i+1]))]

        med[i] = np.median(sy)
        sig[i] = np.std(sy)

    if isshow:
        # plt.scatter(sx, sy)
        plt.scatter(x, y)
        plt.plot(sx[:-1]+h2, med, 'r:')
        plt.errorbar(sx[:-1]+h2, med, sig, fmt='r.', markersize=10)
        plt.show()
    #
    # print(med[:], sig)


if __name__ == '__main__':
    N = 10000
    x, y = init(False)
    seq(True)

