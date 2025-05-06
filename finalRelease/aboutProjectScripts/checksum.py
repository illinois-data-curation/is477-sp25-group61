import hashlib
import os

files_to_check = [
    "data/stroke.csv",
    "data/ruralurbancodes2023.csv"
]

# Get output path from Snakemake (if available)
try:
    output_file = snakemake.output[0]
except NameError:
    # fallback if running manually
    output_file = "CHECKSUMS.md"

def sha256_checksum(filename):
    sha256 = hashlib.sha256()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(4096), b""):
            sha256.update(block)
    return sha256.hexdigest()

# Ensure output directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

with open(output_file, "w") as out:
    out.write("# ✅ SHA-256 Checksums\n\n")
    for file in files_to_check:
        if os.path.exists(file):
            checksum = sha256_checksum(file)
            out.write(f"- `{file}`: `{checksum}`\n")
            print(f"{file}: {checksum}")
        else:
            out.write(f"- `{file}`: **File not found**\n")
            print(f"{file}: File not found")

print(f"\nChecksums saved to {output_file}")

