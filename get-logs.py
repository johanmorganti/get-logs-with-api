import json
from dateutil.parser import parse as dateutil_parser

from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api.logs_api import LogsApi
from datadog_api_client.v2.model.logs_list_request import LogsListRequest
from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
from datadog_api_client.v2.model.logs_sort import LogsSort

from pprint import pprint


# configuration.api_key["apiKeyAuth"] = "*********"
# configuration.api_key["appKeyAuth"] = "*********"

configuration = Configuration()

log_filename = ""

with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = LogsApi(api_client)
    filter_query = "*"  # str | Search query following logs syntax. (optional)
    filter_index = "main"  # str | For customers with multiple indexes, the indexes to search Defaults to '*' which means all indexes (optional)
    filter_from = dateutil_parser('2022-03-08T11:48:36+01:00')  # datetime | Minimum timestamp for requested logs. (optional)
    filter_to = dateutil_parser('2022-03-08T15:55:36+01:00')  # datetime | Maximum timestamp for requested logs. (optional)
    sort = LogsSort("timestamp")  # LogsSort | Order of logs in results. (optional)
    page_limit = 1000  # int | Maximum number of logs in the response. (optional) if omitted the server will use the default value of 10

    try:        
        api_response = api_instance.list_logs_get(filter_query=filter_query, filter_index=filter_index, filter_from=filter_from, filter_to=filter_to, sort=sort, page_limit=page_limit)
        log_filename = str(filter_from) + "-" + str(filter_to) + ".json"
        f = open("data/" + log_filename, "a")
        f.write(str(api_response["data"]))
        f.close()

        while "meta" in api_response:
            i = 0
            api_response = api_instance.list_logs_get(filter_query=filter_query, filter_index=filter_index, filter_from=filter_from, filter_to=filter_to, sort=sort, page_cursor=api_response["meta"]["page"]["after"], page_limit=page_limit)
            log_filename = str(filter_from) + "-" + str(filter_to) + "-" + str(i) + ".json"
            f = open("data/" + log_filename, "a")
            f.write(str(api_response["data"]))
            f.close()
            i = i+1

    except ApiException as e:
        print("Exception when calling LogsApi->list_logs_get: %s\n" % e)