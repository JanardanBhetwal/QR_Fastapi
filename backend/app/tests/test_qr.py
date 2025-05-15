# backend/app/tests/test_qr.py

import io
import pytest
from fastapi.testclient import TestClient
from PIL import Image

from app.main import app

client = TestClient(app)


def test_generate_qr_png():
    # 1) Call the QR endpoint with a simple string
    resp = client.get("/api/v1/utils/qr", params={"data": "FastAPI"})
    assert resp.status_code == 200, resp.text
    assert resp.headers["content-type"] == "image/png"

    # 2) Load it with PIL to confirm it’s a valid PNG
    img = Image.open(io.BytesIO(resp.content))
    assert img.format == "PNG"
    # It should be square (size × size)
    assert img.size[0] == img.size[1]


def test_generate_qr_missing_data():
    # Missing the required 'data' query → 422 Unprocessable Entity
    resp = client.get("/api/v1/utils/qr")
    assert resp.status_code == 422
