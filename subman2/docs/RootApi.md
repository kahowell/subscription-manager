# swagger_client.RootApi

All URIs are relative to *http://localhost:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_open_api_json**](RootApi.md#get_open_api_json) | **GET** /openapi.json | 
[**get_open_api_yaml**](RootApi.md#get_open_api_yaml) | **GET** /openapi.yaml | 

# **get_open_api_json**
> str get_open_api_json()



Get the OpenAPI spec in JSON format.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RootApi()

try:
    api_response = api_instance.get_open_api_json()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootApi->get_open_api_json: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_api_yaml**
> str get_open_api_yaml()



Get the OpenAPI spec in YAML format.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RootApi()

try:
    api_response = api_instance.get_open_api_yaml()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootApi->get_open_api_yaml: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

