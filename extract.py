import pymupdf4llm

print("Extracting PDF...")

markdown = pymupdf4llm.to_markdown(
    "data/docs/manual.pdf"
)

with open(
    "data/processed/document.md",
    "w",
    encoding="utf-8"
) as f:
    f.write(markdown)

print("✅ Extraction complete")