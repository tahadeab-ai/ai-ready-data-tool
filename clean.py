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
