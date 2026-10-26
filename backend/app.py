"""
FastAPI Server for Price Comparison Application
"""

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import os
import sys

# Ensure backend package can be imported
sys.path.insert(0, os.path.dirname(__file__))
from comparator import estimate_dynamic_pricing, get_all_catalog_products

app = FastAPI(title="PriceDrop - Multi-Store Price Comparator")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

STATIC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "static"))

@app.get("/api/compare")
async def compare_prices(q: str = Query(..., description="Product name to search and compare")):
    if not q or not q.strip():
        return {"error": "Please provide a valid product name."}
    
    result = estimate_dynamic_pricing(q.strip())
    return result

@app.get("/api/catalog")
async def get_catalog():
    """Returns all available benchmark electronics grouped by category."""
    return get_all_catalog_products()

@app.get("/", response_class=HTMLResponse)
async def serve_home():
    index_path = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse("<h1>PriceDrop App Frontend is loading...</h1>")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=5000, reload=True)
