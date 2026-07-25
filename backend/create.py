from pathlib import Path

BASE_DIR = Path(__file__).parent

folders = [
    "api",
    "services",
]

files = {
    "app.py": "",

    "api/__init__.py": "",
    "api/routes.py": "",
    "api/schemas.py": "",

    "services/__init__.py": "",
    "services/rag_service.py": "",
}

for folder in folders:
    (BASE_DIR / folder).mkdir(exist_ok=True)

for file, content in files.items():
    path = BASE_DIR / file

    if not path.exists():
        path.write_text(content, encoding="utf-8")
        print(f"Created: {file}")
    else:
        print(f"Exists : {file}")

print("\nProject structure created successfully.")