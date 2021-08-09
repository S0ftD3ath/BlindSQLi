# Blind SQL Injection - Time-Based

These are some scripts to exploit a Time-Based SQL Injection in a login panel. 

## How to know when I can use these scripts

If you type in a field of the login panel this: 

`' or sleep(10)-- -`

And the page takes 10 or more second to respond, then it may be vulnerable to a Time-based SQL injection

## Installation

```
git clone https://github.com/S0ftD3ath/BlindSQLi.git
cd BlindSQLi
pip install -r requirements.txt
```

## Usage

python3 <script.py>

Note: You have to change some information in the global variables of the script

## Order to execute the scripts

```
python3 dumpDB.py
python3 dumpTables.py
python3 dumpColumns.py
python3 dumpDataFromColumns.py
```

