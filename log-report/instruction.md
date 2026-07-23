There is an Apache-style access log at /app/access.log.

Analyze the log and write a JSON report to:

/app/report.json

Your report must contain the following fields:

1. total_requests: the total number of log entries.
2. unique_ips: the number of unique client IP addresses.
3. top_path: the most frequently requested URL path.

The output must be valid JSON.
Do not create any additional output files.