import csv 
def read_rows(path):

    if not os.path.exists(path):
        print(f"warning: input file not found: {path}", file=sys.stderr)
        return [], []
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        rows = [r for r in reader if any(cell.strip() for cell in r)]
    if not rows:
        return [], []
    return rows[0], rows[1:]

def read_rows(path):
    
    if not os.path.exists(path):
        print(f"warning: input file not found: {path}", file=sys.stderr)
        return [], []
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        rows = [r for r in reader if any(cell.strip() for cell in r)]
    if not rows:
        return [], []
    return rows[0], rows[1:]


def write_rows(header, rows, path):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        writer.writerows(rows)



def normalize_columns(header):

    out = []
    for name in header:
        name = name.strip().lower()
        name = re.sub(r"[^\w\s]", "", name) 
        name = re.sub(r"\s+", "_", name.strip())
        out.append(name.strip("_"))
    return out

