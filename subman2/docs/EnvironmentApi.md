# swagger_client.EnvironmentApi

All URIs are relative to *http://localhost:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_environments**](EnvironmentApi.md#list_environments) | **GET** /operations/list_environments | Lists all of the environments that have been configured for an organization.
[**list_orgs**](EnvironmentApi.md#list_orgs) | **GET** /operations/list_orgs | Lists all of the organizations which are available to the specified user account.

# **list_environments**
> list[str] list_environments(org=org)

Lists all of the environments that have been configured for an organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'# Configure HTTP basic authorization: certAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnvironmentApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Identifies the organization for which to list the configured environments. (optional)

try:
    # Lists all of the environments that have been configured for an organization.
    api_response = api_instance.list_environments(org=org)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->list_environments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Identifies the organization for which to list the configured environments. | [optional] 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth), [certAuth](../README.md#certAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orgs**
> list[str] list_orgs()

Lists all of the organizations which are available to the specified user account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'# Configure HTTP basic authorization: certAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnvironmentApi(swagger_client.ApiClient(configuration))

try:
    # Lists all of the organizations which are available to the specified user account.
    api_response = api_instance.list_orgs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->list_orgs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth), [certAuth](../README.md#certAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

