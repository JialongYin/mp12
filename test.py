import requests
import json
url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp12-grader"
payload = {
            "accountId": 152442585149,
            "submitterEmail": 'jialong2@illinois.edu',
            "secret": '29eueXpp2HcaopTL',
            "ipaddress": '192.168.0.103:5000'
    }
r = requests.post(url, data=json.dumps(payload))
print(r.status_code, r.reason)
print(r.text)
