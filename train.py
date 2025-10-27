import argparse, pickle, pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def main(input_path, model_path, algo):
    df = pd.read_csv(input_path)
    y = df["y"].values
    if algo == "arima":
        model = ARIMA(y, order=(2,1,2)).fit()
    else:
        raise ValueError("Unknown algo")
    import os; os.makedirs("artifacts", exist_ok=True)
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    print("Saved", model_path)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--model", default="artifacts/arima.pkl")
    ap.add_argument("--algo", choices=["arima"], default="arima")
    a = ap.parse_args()
    main(a.input, a.model, a.algo)
