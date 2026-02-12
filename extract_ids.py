import json, sys
data = json.load(sys.stdin)
# The result is a JSON array with schema [{type, text}], get the text content
text = data[0]['text'] if isinstance(data, list) else data
result = json.loads(text) if isinstance(text, str) else text
# Navigate to results
results = result.get('results', [])
print(f'Total unenriched jobs: {len(results)}')
print()
for r in results:
    page_id = r.get('id', 'N/A')
    props = r.get('properties', {})
    # Company Name is title type
    company = props.get('Company Name', {})
    title_arr = company.get('title', [])
    company_name = title_arr[0]['plain_text'] if title_arr else 'N/A'
    # Job Title is rich_text type
    job = props.get('Job Title', {})
    job_arr = job.get('rich_text', [])
    job_title = job_arr[0]['plain_text'] if job_arr else 'N/A'
    print(f'{company_name} | {job_title} | {page_id}')