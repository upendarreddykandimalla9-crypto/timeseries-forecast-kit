import argparse, numpy as np, pandas as pd
def main(periods, seasonal):
    rng = np.random.default_rng(7)
    t = np.arange(periods)
    y = 100 + 10*np.sin(2*np.pi*t/seasonal) + rng.normal(0, 3, size=periods)
    df = pd.DataFrame({"y": y})
    df.to_csv("data/series.csv", index=False)
    print("Wrote data/series.csv")
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--periods", type=int, default=365)
    ap.add_argument("--seasonal", type=int, default=7)
    a = ap.parse_args()
    main(a.periods, a.seasonal)
