# swagger_client.ProfileApi

All URIs are relative to *http://localhost:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_level**](ProfileApi.md#get_service_level) | **GET** /operations/list_servicelevels | Displays the current configured service level preference for products installed on the system.
[**list_releases**](ProfileApi.md#list_releases) | **GET** /operations/list_releases | Lists the available OS versions and the currently set release version (if any).
[**set_release**](ProfileApi.md#set_release) | **POST** /operations/set_release | Sets a sticky OS version to use when installing or updating packages.
[**set_service_level**](ProfileApi.md#set_service_level) | **POST** /operations/set_servicelevel | Set a service-level preference for this system.
[**update_profile**](ProfileApi.md#update_profile) | **POST** /operations/update_profile | Updates the system information.

# **get_service_level**
> ListServiceLevelsResult get_service_level(consumer_id=consumer_id)

Displays the current configured service level preference for products installed on the system.

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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))
consumer_id = 'consumer_id_example' # str |  (optional)

try:
    # Displays the current configured service level preference for products installed on the system.
    api_response = api_instance.get_service_level(consumer_id=consumer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->get_service_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**|  | [optional] 

### Return type

[**ListServiceLevelsResult**](ListServiceLevelsResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [certAuth](../README.md#certAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_releases**
> ListReleasesResult list_releases(consumer_id=consumer_id)

Lists the available OS versions and the currently set release version (if any).

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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))
consumer_id = 'consumer_id_example' # str |  (optional)

try:
    # Lists the available OS versions and the currently set release version (if any).
    api_response = api_instance.list_releases(consumer_id=consumer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->list_releases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**|  | [optional] 

### Return type

[**ListReleasesResult**](ListReleasesResult.md)

### Authorization

[certAuth](../README.md#certAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_release**
> set_release(consumer_id=consumer_id, release=release)

Sets a sticky OS version to use when installing or updating packages.

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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))
consumer_id = 'consumer_id_example' # str |  (optional)
release = 'release_example' # str | Sets the minor (Y-stream) release version to use, such as 6.3. (optional)

try:
    # Sets a sticky OS version to use when installing or updating packages.
    api_instance.set_release(consumer_id=consumer_id, release=release)
except ApiException as e:
    print("Exception when calling ProfileApi->set_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**|  | [optional] 
 **release** | **str**| Sets the minor (Y-stream) release version to use, such as 6.3. | [optional] 

### Return type

void (empty response body)

### Authorization

[certAuth](../README.md#certAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_service_level**
> set_service_level(consumer_id=consumer_id, release=release)

Set a service-level preference for this system.

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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))
consumer_id = 'consumer_id_example' # str |  (optional)
release = 'release_example' # str | Sets the minor (Y-stream) release version to use, such as 6.3. (optional)

try:
    # Set a service-level preference for this system.
    api_instance.set_service_level(consumer_id=consumer_id, release=release)
except ApiException as e:
    print("Exception when calling ProfileApi->set_service_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**|  | [optional] 
 **release** | **str**| Sets the minor (Y-stream) release version to use, such as 6.3. | [optional] 

### Return type

void (empty response body)

### Authorization

[certAuth](../README.md#certAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile**
> SyncResult update_profile(body=body, consumer_id=consumer_id)

Updates the system information.

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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))
body = swagger_client.SystemProfile() # SystemProfile |  (optional)
consumer_id = 'consumer_id_example' # str |  (optional)

try:
    # Updates the system information.
    api_response = api_instance.update_profile(body=body, consumer_id=consumer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->update_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SystemProfile**](SystemProfile.md)|  | [optional] 
 **consumer_id** | **str**|  | [optional] 

### Return type

[**SyncResult**](SyncResult.md)

### Authorization

[certAuth](../README.md#certAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

