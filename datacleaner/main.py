import csv
import sys
from pathlib import Path

def preview_csv(path_str, max_rows=5):
    path = Path(path_str)
    if not path.exists():
        print(f"File not found: {path}")
        return
    
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        print("Empty file.")
        return
    
    header = rows[0]
    data_rows = rows[1:]

    print(f"File: {path}")
    print(f"Columns: {len(header)}")
    print(f"Rows (excluding header): {len(data_rows)}")
    print()
    print("Header:")
    print(header)
    print()
    print(f"First {min(max_rows, len(data_rows))} rows:")
    for row in data_rows[:max_rows]:
        print(row)


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m datacleaner <csv_files>")
        sys.exit(1)

    csv_path = sys.argv[1]
    preview_csv(csv_path)
    analyze_csv(csv_path)
    clean_csv(csv_path, empty_threshold=0.5, output_filename="cleaned_sample.csv")

def clean_csv(path_str, empty_threshold=0.5, output_filename="cleaned.csv"):
    path = Path(path_str)

    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        print("Cannot clean: empty file.")
        return

    header = rows[0]
    data_rows = rows[1:]

    num_rows = len(data_rows)
    num_cols = len(header)

    
    keep_indices = []
    removed_columns = []
    kept_columns = []

    for col_idx, col_name in enumerate(header):
        column_values = [row[col_idx].strip() for row in data_rows]
        empty_count = sum(1 for x in column_values if x == "")
        empty_ratio = empty_count / num_rows if num_rows else 0

        if empty_ratio <= empty_threshold:
            keep_indices.append(col_idx)
            kept_columns.append(col_name)
        else:
            removed_columns.append((col_name, empty_ratio))

    if not keep_indices:
        print("All columns would be removed based on threshold. Aborting clean.")
        return

    
    cleaned_rows = []

    
    new_header = [header[i] for i in keep_indices]
    cleaned_rows.append(new_header)

    
    for row in data_rows:
        new_row = [row[i] for i in keep_indices]
        cleaned_rows.append(new_row)

    
    output_path = Path(output_filename)
    with output_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(cleaned_rows)

    print(f"Cleaned CSV saved to {output_path}")


    with open("report.txt", "a", encoding="utf-8") as rep:
        rep.write("\n=== Cleaning Summary ===\n")
        rep.write(f"Empty threshold: {empty_threshold * 100:.0f}%\n")
        rep.write(f"Kept columns: {', '.join(kept_columns)}\n")
        if removed_columns:
            rep.write("Removed columns:\n")
            for name, ratio in removed_columns:
                rep.write(f"  - {name} ({ratio * 100:.1f}% empty)\n")
        else:
            rep.write("Removed columns: none\n")


if __name__ == "__main__":
    main()


def analyze_csv(path_str):
    path = Path(path_str)

    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)

    header = rows[0]
    data_rows = rows[1:]

    report_lines = []
    report_lines.append("=== CSV Analysis Report ===\n")
    report_lines.append(f"File: {path}\n")
    report_lines.append(f"Columns: {len(header)}\n")
    report_lines.append(f"Rows (excluding header): {len(data_rows)}\n\n")

    for col_idx, col_name in enumerate(header):
        column_values = [row[col_idx].strip() for row in data_rows]
        empty_count = sum(1 for x in column_values if x == "")
        unique_values = set(x for x in column_values if x != "")

        total = len(column_values)
        empty_percent = (empty_count / total) * 100 if total else 0

        report_lines.append(f"Column: {col_name}")
        report_lines.append(f"  Empty values: {empty_count} ({empty_percent:.1f}%)")
        report_lines.append(f"  Unique values: {len(unique_values)}")
        report_lines.append("")

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    print("Report saved to report.txt")
