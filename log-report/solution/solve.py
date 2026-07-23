import json
import re
from collections import Counter

paths = Counter()
ips = set()
total = 0

# Local testing path
with open("/app/access.log", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        total += 1

        # IP Address
        ips.add(line.split()[0])

        # URL Path
        match = re.search(r'"(?:GET|POST|PUT|DELETE|PATCH|HEAD)\s+(\S+)', line)
        if match:
            paths[match.group(1)] += 1

# Create report
report = {
    "total_requests": total,
    "unique_ips": len(ips),
    "top_path": paths.most_common(1)[0][0]
}

# Save report
with open("/app/report.json", "w") as f:
    json.dump(report, f, indent=2)

print("✅ report.json created successfully!")