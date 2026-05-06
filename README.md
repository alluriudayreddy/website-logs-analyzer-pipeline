Website Logs Analyzer Pipeline

A mini backend pipeline project built in Python that processes website log data, analyzes requests, and generates reports automatically.


Features

- Read website log data from file
- Parse raw logs into structured dictionaries
- Analyze request statistics
- Count status codes
- Find top visited page
- Generate report.txt automatically
- Isolated testing for parser and analyzer


Project Structure

website-logs-analyzer-pipeline/
│
├── data/
│   ├── input/
│   └── output/
│
├── docs/
│
├── src/
│   ├── parser.py
│   ├── analyzer.py
│   ├── pipeline.py
│   ├── helpers.py
│   └── config.py
│
├── tests/
│
├── main.py
└── README.md


How To Run

Run full pipeline:
python3 main.py