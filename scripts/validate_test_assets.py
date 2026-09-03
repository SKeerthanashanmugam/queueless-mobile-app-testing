import csv
from pathlib import Path


root = Path(__file__).resolve().parents[1]
path = root / "test-cases" / "manual-test-cases.csv"
with path.open(newline="", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))

required = {"Test_Case_ID", "Module", "Title", "Steps", "Expected_Result", "Priority", "Requirement", "Status"}
missing_columns = required.difference(rows[0] if rows else {})
assert not missing_columns, f"Missing columns: {sorted(missing_columns)}"
assert len(rows) == 70, f"Expected 70 cases, found {len(rows)}"
ids = [row["Test_Case_ID"] for row in rows]
assert len(ids) == len(set(ids)), "Duplicate test case IDs found"
for row in rows:
    missing = [column for column in required if not row[column].strip()]
    assert not missing, f"{row['Test_Case_ID']} missing required values: {missing}"
print(f"Validated {len(rows)} unique manual test cases.")

