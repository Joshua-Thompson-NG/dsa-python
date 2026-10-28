import json
import os
from flask import Flask,jsonify, request

app = Flask(__name__)

STATS_FILE = "/home/thompson/day9_app/stats.json"

def load_stats():
    if os.path.exists(STATS_FILE):
        try:
            with open(STATS_FILE) as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass

    return {"total_visits":0, "ip_frequency":{}}

def save_stats(data):
    with open(STATS_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/")
def home():
    stats = load_stats()

    visitor_ip = request.remote_addr

    stats["total_visits"] += 1

    ip_map = stats["ip_frequency"]
    ip_map[visitor_ip] = ip_map.get(visitor_ip, 0) + 1

    save_stats(stats)

    return jsonify({
        "status":"online",
        "message":"Hello from my Azure VM",
        "your_ip": visitor_ip,
        "total_visits": stats["total_visits"],
        "ip_leaderboard": stats["ip_frequency"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

