from pathlib import Path

raw_path = Path("data/raw/school_census_sample.csv")

if raw_path.exists():
    print(f"Extract step complete. File found: {raw_path}")
else:
    raise FileNotFoundError(f"File not found: {raw_path}")