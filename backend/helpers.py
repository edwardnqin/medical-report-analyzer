import os, io, json, base64
import fitz          # PyMuPDF
import docx          # python-docx
from PIL import Image

# ---------------- File reading ----------------

def pdf_to_text(file_bytes: bytes) -> str:
    pdf = fitz.open(stream=file_bytes, filetype="pdf")
    return "\n".join(page.get_text() for page in pdf)

def docx_to_text(file_bytes: bytes) -> str:
    buf = io.BytesIO(file_bytes)
    d = docx.Document(buf)
    return "\n".join(p.text for p in d.paragraphs)

def image_to_base64_png(file_bytes: bytes) -> str:
    img = Image.open(io.BytesIO(file_bytes)).convert("RGB")
    out = io.BytesIO()
    img.save(out, format="PNG")
    return "data:image/png;base64," + base64.b64encode(out.getvalue()).decode()

def text_from_upload(filename: str, file_bytes: bytes) -> str:
    name = filename.lower()
    if name.endswith(".pdf"):
        return pdf_to_text(file_bytes)
    if name.endswith(".docx"):
        return docx_to_text(file_bytes)
    if name.endswith((".txt", ".md", ".csv")):
        return file_bytes.decode("utf-8", errors="ignore")
    if name.endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tif", ".tiff")):
        return image_to_base64_png(file_bytes)
    # Fallback: best-effort decode
    try:
        return file_bytes.decode("utf-8", errors="ignore")
    except Exception:
        return ""

# ---------------- Single JSON store ----------------

DATA_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data.json"))

def load_data() -> dict:
    """Load entire JSON store."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_data(data: dict) -> None:
    """Save entire JSON store."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
