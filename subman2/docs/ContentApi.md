# swagger_client.ContentApi

All URIs are relative to *http://localhost:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_repo_overrides**](ContentApi.md#list_repo_overrides) | **GET** /operations/list_repo_overrides | Lists all overrides from repositories specified with the repo option.
[**list_repos**](ContentApi.md#list_repos) | **GET** /operations/list_repos | Lists all of the repositories that are available to a system.
[**update_repo_overrides**](ContentApi.md#update_repo_overrides) | **POST** /operations/update_repo_overrides | Allows the user to manage custom content repository settings.
[**update_repos**](ContentApi.md#update_repos) | **POST** /operations/update_repos | Enable or disable repositories.

# **list_repo_overrides**
> list[str] list_repo_overrides(consumer_id=consumer_id, repo=repo)

Lists all overrides from repositories specified with the repo option.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: certAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ContentApi(swagger_client.ApiClient(configuration))
consumer_id = 'consumer_id_example' # str |  (optional)
repo = ['repo_example'] # list[str] | The repositories to list repo overrides for (optional)

try:
    # Lists all overrides from repositories specified with the repo option.
    api_response = api_instance.list_repo_overrides(consumer_id=consumer_id, repo=repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->list_repo_overrides: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**|  | [optional] 
 **repo** | [**list[str]**](str.md)| The repositories to list repo overrides for | [optional] 

### Return type

**list[str]**

### Authorization

[certAuth](../README.md#certAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_repos**
> list[Repo] list_repos(consumer_id=consumer_id, enabled=enabled, disabled=disabled)

Lists all of the repositories that are available to a system.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: certAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ContentApi(swagger_client.ApiClient(configuration))
consumer_id = 'consumer_id_example' # str |  (optional)
enabled = true # bool | Lists all of the enabled repositories that are provided by the content service used by the system. (optional)
disabled = true # bool | Lists all of the disabled repositories that are provided by the content service used by the system. (optional)

try:
    # Lists all of the repositories that are available to a system.
    api_response = api_instance.list_repos(consumer_id=consumer_id, enabled=enabled, disabled=disabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->list_repos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**|  | [optional] 
 **enabled** | **bool**| Lists all of the enabled repositories that are provided by the content service used by the system. | [optional] 
 **disabled** | **bool**| Lists all of the disabled repositories that are provided by the content service used by the system. | [optional] 

### Return type

[**list[Repo]**](Repo.md)

### Authorization

[certAuth](../README.md#certAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repo_overrides**
> update_repo_overrides(consumer_id=consumer_id, repo=repo, add=add, remove=remove, removeall=removeall)

Allows the user to manage custom content repository settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: certAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ContentApi(swagger_client.ApiClient(configuration))
consumer_id = 'consumer_id_example' # str |  (optional)
repo = ['repo_example'] # list[str] | The repositories to update repo overrides for (optional)
add = ['add_example'] # list[str] | Adds a named override with the provided value to repositories specified with the repo option (NAME:VALUE) (optional)
remove = ['remove_example'] # list[str] | Removes a named override from the repositories specified. (optional)
removeall = true # bool | Removes all overrides from repositories specified. (optional)

try:
    # Allows the user to manage custom content repository settings.
    api_instance.update_repo_overrides(consumer_id=consumer_id, repo=repo, add=add, remove=remove, removeall=removeall)
except ApiException as e:
    print("Exception when calling ContentApi->update_repo_overrides: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**|  | [optional] 
 **repo** | [**list[str]**](str.md)| The repositories to update repo overrides for | [optional] 
 **add** | [**list[str]**](str.md)| Adds a named override with the provided value to repositories specified with the repo option (NAME:VALUE) | [optional] 
 **remove** | [**list[str]**](str.md)| Removes a named override from the repositories specified. | [optional] 
 **removeall** | **bool**| Removes all overrides from repositories specified. | [optional] 

### Return type

void (empty response body)

### Authorization

[certAuth](../README.md#certAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repos**
> update_repos(consumer_id=consumer_id, enable=enable, disable=disable)

Enable or disable repositories.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: certAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ContentApi(swagger_client.ApiClient(configuration))
consumer_id = 'consumer_id_example' # str |  (optional)
enable = ['enable_example'] # list[str] | Enables the specified repository, which is made available by the content sources identified in the system subscriptions. (optional)
disable = ['disable_example'] # list[str] | Disables the specified repository, which is made available by the content sources identified in the system subscriptions. (optional)

try:
    # Enable or disable repositories.
    api_instance.update_repos(consumer_id=consumer_id, enable=enable, disable=disable)
except ApiException as e:
    print("Exception when calling ContentApi->update_repos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**|  | [optional] 
 **enable** | [**list[str]**](str.md)| Enables the specified repository, which is made available by the content sources identified in the system subscriptions. | [optional] 
 **disable** | [**list[str]**](str.md)| Disables the specified repository, which is made available by the content sources identified in the system subscriptions. | [optional] 

### Return type

void (empty response body)

### Authorization

[certAuth](../README.md#certAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

