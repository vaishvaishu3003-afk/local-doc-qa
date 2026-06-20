import json

with open(
    "data/processed/document.md",
    "r",
    encoding="utf-8"
) as f:
    content = f.read()

chunk_size = 2000

sections = []

for i in range(0, len(content), chunk_size):
    chunk = content[i:i + chunk_size]

    sections.append({
        "id": len(sections),
        "title": f"Chunk {len(sections)}",
        "content": chunk
    })

with open(
    "data/processed/sections.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        sections,
        f,
        indent=2
    )

print(f"✅ {len(sections)} chunks saved")