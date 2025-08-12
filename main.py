import os
import json
import subprocess
import time
import requests
import tkinter as tk
from tkinter import simpledialog, messagebox

CONFIG_PATH = os.path.join(os.getenv("APPDATA"), "wifi_auto_login_config.json")
CAPTIVE_PORTAL_URL = "http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://example.com"

def gui_setup():
    """Show a Tkinter popup to collect SSID, username, password."""
    root = tk.Tk()
    root.withdraw()  # hide main window

    ssid = simpledialog.askstring("Setup", "Enter Wi-Fi SSID:")
    if not ssid:
        messagebox.showerror("Error", "SSID cannot be empty")
        root.destroy()
        exit()

    username = simpledialog.askstring("Setup", "Enter User ID:")
    if not username:
        messagebox.showerror("Error", "User ID cannot be empty")
        root.destroy()
        exit()

    password = simpledialog.askstring("Setup", "Enter Password:", show="*")
    if not password:
        messagebox.showerror("Error", "Password cannot be empty")
        root.destroy()
        exit()

    config = {"ssid": ssid, "user": username, "pass": password}
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f)

    messagebox.showinfo("Saved", "Configuration saved successfully.")
    root.destroy()

def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    return None

def is_connected():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except:
        return False

def current_wifi():
    try:
        output = subprocess.check_output("netsh wlan show interfaces", shell=True, text=True)
        for line in output.split("\n"):
            if "SSID" in line and "BSSID" not in line:
                return line.split(":")[1].strip()
    except:
        return None

def connect_wifi(ssid):
    subprocess.call(f'netsh wlan connect name="{ssid}"', shell=True)

def login_captive_portal(user, password):
    payload = {
        "userId": user,
        "password": password,
        "serviceName": "ProntoAuthentication"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http://phc.prontonetworks.com",
        "Referer": "http://phc.prontonetworks.com/cgi-bin/authlogin",
        "User-Agent": "Mozilla/5.0"
    }
    try:
        r = requests.post(CAPTIVE_PORTAL_URL, data=payload, headers=headers, timeout=5)
        if r.status_code == 200:
            print("[INFO] Captive portal login successful.")
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    config = load_config()
    if config is None:
        gui_setup()
        config = load_config()

    while True:
        wifi = current_wifi()
        if wifi != config["ssid"] or not is_connected():
            connect_wifi(config["ssid"])
            time.sleep(5)
            login_captive_portal(config["user"], config["pass"])
            time.sleep(5)
        time.sleep(30)
