# swagger_client.InfoApi

All URIs are relative to *http://localhost:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_version**](InfoApi.md#get_version) | **GET** /operations/get_version | Displays information about the subscription management server.

# **get_version**
> CandlepinVersion get_version()

Displays information about the subscription management server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InfoApi()

try:
    # Displays information about the subscription management server.
    api_response = api_instance.get_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->get_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CandlepinVersion**](CandlepinVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

