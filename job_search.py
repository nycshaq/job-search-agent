import requests
from datetime import datetime

url = f"https://api.adzuna.com/v1/api/jobs/us/search/1"

params = {
    "app_id": "ae542a3d",
    "app_key": "6bdfd021f7a181b09afae73cc01f104a",
    "what": "devops engineer",
    "where": "new york",
    "results_per_page": 5
}

response = requests.get(url, params=params)
date = datetime
data = response.json()

for job in data["results"]:
    if job.get("salary_min", 0) >= 130000:
        print(job["title"])
        print(job["company"]["display_name"])
        print(job["redirect_url"])
        print(f"Salary: ${job.get('salary_min', 'Not listed'):,.0f} - ${job.get('salary_max', 'Not listed'):,.0f}")
        clean_date = job["created"].removesuffix("Z") 
        parsed = datetime.strptime(clean_date, "%Y-%m-%dT%H:%M:%S")
        print(parsed.strftime("%B %d, %Y"))
        print("---")
        with open ("jobs_log.txt", "a") as f:
            f.write(job["title"]+ "\n")
            f.write(job["company"]["display_name"]+ "\n")
            f.write(job["redirect_url"]+ "\n")
            f.write(f"Salary: ${job.get('salary_min', 'Not listed'):,.0f} - ${job.get('salary_max', 'Not listed'):,.0f}"+ "\n")
            f.write(parsed.strftime("%B %d, %Y")+ "\n")
            f.write("---"+ "\n")