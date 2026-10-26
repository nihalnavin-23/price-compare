"""
Launcher for PriceDrop Application
Starts FastAPI server on http://127.0.0.1:5000 and opens the browser.
"""

import uvicorn
import webbrowser
import threading
import time
import os
import sys

if sys.platform.startswith('win'):
    sys.stdout.reconfigure(encoding='utf-8')

def open_browser():
    time.sleep(1.5)
    print("\n" + "="*50)
    print("PriceDrop App is LIVE at http://127.0.0.1:5000")
    print("Opening your browser now...")
    print("="*50 + "\n")
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    backend_dir = os.path.join(os.path.dirname(__file__), "backend")
    sys.path.insert(0, backend_dir)

    threading.Thread(target=open_browser, daemon=True).start()
    uvicorn.run("app:app", host="127.0.0.1", port=5000, app_dir=backend_dir)
