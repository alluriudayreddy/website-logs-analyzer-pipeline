Website Logs Analyzer Pipeline Notes

Project Goal

Build a mini backend pipeline that:
- reads website log data
- parses logs into structured dictionaries
- analyzes request data
- generates reports automatically


Architecture Flow

main.py
→ pipeline.py
→ parser.py
→ analyzer.py
→ report.txt


File Responsibilities

main.py
Starts the project and runs the pipeline.

parser.py
Converts raw log strings into structured dictionaries.

analyzer.py
Analyzes parsed log data:
- total requests
- status counts
- top page

pipeline.py
Controls complete workflow:
- reads logs
- parses logs
- analyzes data
- generates report

helpers.py
Contains reusable helper functions like line cleaning.

config.py
Stores centralized configuration values.

tests/
Contains isolated test files for parser and analyzer.


Key Concepts Learned

- loops
- dictionaries
- functions
- file handling
- imports/modules
- execution flow
- pipeline architecture
- testing
- report generation
- append vs overwrite file modes


Debugging Problems Faced

- indentation issues
- return inside loop problem
- module import errors
- unsaved file confusion
- wrong dictionary keys
- empty iterable errors
- execution flow mistakes


Final Output

Project successfully:
- reads logs
- parses logs
- analyzes request data
- generates reports
- saves reports to file
- supports isolated testing