# Goals

This code will help customers to download their logs currently being indexed on Datadog platform.
Leveraging Datadog API : https://docs.datadoghq.com/api/latest/logs/#search-logs
And pagination : https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination/?tab=v1api

Logs will be put in files

# Installation

1. Clone the repo
2. Install dependencies :
```
pip install -r requirements.txt
```

3. Set up env vars DD_API_KEY and DD_APP_KEY
    * Note : DD_SITE is optional, defaults to `datadoghq.com`
* Or remove the commented part of the code
```
configuration.api_key["apiKeyAuth"] = "*********"
configuration.api_key["appKeyAuth"] = "*********"
```
4. Change your search scope