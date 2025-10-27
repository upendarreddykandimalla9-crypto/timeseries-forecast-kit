import argparse, pickle, pandas as pd
from sklearn.metrics import mean_absolute_error
def main(input_path, model_path, algo):
    df = pd.read_csv(input_path)
    y = df["y"].values
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    pred = model.predict(start=0, end=len(y)-1)
    print("MAE:", mean_absolute_error(y, pred))
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--algo", choices=["arima"], default="arima")
    a = ap.parse_args()
    main(a.input, a.model, a.algo)
