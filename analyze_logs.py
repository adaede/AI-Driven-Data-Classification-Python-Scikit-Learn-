# src/analyze_logs.py
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

DB_PATH = "data/network_logs.db"

def load_logs():
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT timestamp, latency_ms FROM logs"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def analyze(df: pd.DataFrame):
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")

    print("Latency summary:")
    print(df["latency_ms"].describe())

    plt.figure(figsize=(10, 5))
    plt.plot(df["timestamp"], df["latency_ms"])
    plt.xlabel("Time")
    plt.ylabel("Latency (ms)")
    plt.title("Network Latency Over Time")
    plt.tight_layout()
    plt.savefig("latency_trend.png")
    print("Saved plot to latency_trend.png")

if __name__ == "__main__":
    df_logs = load_logs()
    analyze(df_logs)
