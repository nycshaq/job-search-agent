# Job Search Agent
A Python script that pulls live job listings from the Adzuna API, filters by salary threshold, and logs results to a file. Built as the foundation for a full job search automation agent.


## What it does

* Pulls DevOps Engineer listings in New York from the Adzuna API
* Filters out any role below $130,000
* Formats salary as clean dollar amounts
* Parses and displays posting date in readable format
* Appends matching results to a local log file on every run

## Stack

* Python 3
* Adzuna Jobs API
* `requests` — HTTP library for API calls
* `datetime` — date parsing and formatting

## How to run

1. Clone the repo
2. Install dependencies: `pip3 install requests`
3. Add your Adzuna `app_id` and `app_key` to `job_search.py`
4. Run: `python3 job_search.py`
5. Results print to terminal and append to `jobs_log.txt`

## Roadmap

- [ ] Save results with deduplication — skip listings already seen
- [ ] Score listings against a target skill set
- [ ] Add email or Slack notification for new matches
- [ ] Schedule with cron to run daily automatically
