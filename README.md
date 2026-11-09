# Job Search Agent
A Python script that pulls live job listings from the Adzuna API, filters by salary threshold, and logs results to a file. Built as the foundation for a full job search automation agent.


## What it does

* Pulls DevOps Engineer listings in New York from the Adzuna API
* Filters out any role below $130,000
* Formats salary as clean dollar amounts
* Parses and displays posting date in readable format
* Appends matching results to a local log file on every run
* Tracks seen listings to avoid duplicate results across runs

## Stack

* Python 3.9+
* Adzuna Jobs API
* `requests` — HTTP library for API calls
* `python-dotenv` — loads API credentials from a local `.env` file
* `datetime` — date parsing and formatting

## How to run

1. Clone the repo
2. Install dependencies: `pip3 install -r requirements.txt`
3. Get a free API key at [developer.adzuna.com](https://developer.adzuna.com/)
4. Copy the example env file and add your credentials:
   ```bash
   cp .env.example .env
   ```
   Then fill in `ADZUNA_APP_ID` and `ADZUNA_APP_KEY` in `.env`. This file is gitignored and never committed.
5. Run: `python3 job_search.py`
6. Results print to terminal and append to `jobs_log.txt`

## Example output

```
DevOps Engineer
Jean Martin, Inc
https://www.adzuna.com/land/ad/...
Salary: $186,607 - $186,607
October 21, 2026
---
```

The script creates two files locally on first run:

* `jobs_log.txt` — running history of every matching listing
* `seen_urls.txt` — listings already shown, so they're skipped on future runs

## Roadmap

- [ ] Score listings against a target skill set
- [ ] Add email or Slack notification for new matches
- [ ] Schedule with cron to run daily automatically
