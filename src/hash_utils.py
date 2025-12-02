from pathlib import Path
import hashlib

def compute_file_hash(file_path : Path, algo: str = "sha256") -> str:
    file_path = Path(file_path)
    if not file_path.is_file():
        raise FileNotFoundError("Dosya bulunamadı: {file_path}")
    if algo == "sha256":
        hasher = hashlib.sha256()
    elif algo == "md5":
        hasher = hashlib.md5()
    else:
        raise ValueError(f"Desteklenmeyen algoritma: {algo}")

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)

    return hasher.hexdigest()

def verify_file_hash(file_path: Path, expected_hash: str, algo: str = "sha256") -> bool:

    file_path = Path(file_path)
    actual_hash = compute_file_hash(file_path, algo).lower()
    expected_hash = expected_hash.strip().lower()
    return actual_hash == expected_hash





