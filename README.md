# TimeSeries Forecast Kit

A tiny framework for benchmarking classical forecasters (Naive, SMA, ARIMA) on synthetic or CSV data.

## Quickstart
```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python generate.py --periods 730 --seasonal 7
python train.py --input data/series.csv --model artifacts/arima.pkl --algo arima
python evaluate.py --input data/series.csv --model artifacts/arima.pkl --algo arima
```


---
