# swagger_client.RegistrationApi

All URIs are relative to *http://localhost:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**regenerate_identity**](RegistrationApi.md#regenerate_identity) | **POST** /operations/regenerate_identity | Requests that the subscription management service issue a new identity certificate for the system, using an existing UUID in the original identity certificate.
[**register**](RegistrationApi.md#register) | **POST** /operations/register | Registers a new system to the subscription management service.
[**unregister**](RegistrationApi.md#unregister) | **POST** /operations/unregister | Removes a system&#x27;s subscriptions and removes it from the subscription management service.

# **regenerate_identity**
> SyncResult regenerate_identity(consumer_id=consumer_id)

Requests that the subscription management service issue a new identity certificate for the system, using an existing UUID in the original identity certificate.

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
api_instance = swagger_client.RegistrationApi(swagger_client.ApiClient(configuration))
consumer_id = 'consumer_id_example' # str |  (optional)

try:
    # Requests that the subscription management service issue a new identity certificate for the system, using an existing UUID in the original identity certificate.
    api_response = api_instance.regenerate_identity(consumer_id=consumer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationApi->regenerate_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**|  | [optional] 

### Return type

[**SyncResult**](SyncResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [certAuth](../README.md#certAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register**
> SyncResult register(body=body, name=name, consumerid=consumerid, activationkey=activationkey, autoattach=autoattach, servicelevel=servicelevel, org=org, environment=environment, release=release)

Registers a new system to the subscription management service.

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
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RegistrationApi(swagger_client.ApiClient(configuration))
body = swagger_client.SystemProfile() # SystemProfile | system profile, including facts and installed products (optional)
name = 'name_example' # str | Sets the name of the system to register. This defaults to the hostname. (optional)
consumerid = 'consumerid_example' # str | References an existing system inventory ID to resume using a previous registration for this system. The ID is used as an inventory number for the system in the subscription management service database. If the system's identity is lost or corrupted, this option allows it to resume using its previous identity and subscriptions. (optional)
activationkey = ['activationkey_example'] # list[str] | Gives a comma-separated list of product keys to use to redeem or apply specific subscriptions to the system. This is used for preconfigured systems which may already have products installed. Activation keys are issued by an on-premise subscription management service, such as Subscription Asset Manager. When the activationkey option is used, it is not necessary to use the username and password options, because the authentication information is implicit in the activation key. (optional)
autoattach = true # bool | Automatically attaches compatible subscriptions to this system. (optional)
servicelevel = 'servicelevel_example' # str | Sets the preferred service level to use with subscriptions added to the system. Service levels are commonly premium, standard, and none, though other levels may be available depending on the product and the contract. (optional)
org = 'org_example' # str | Assigns the system to an organization. Infrastructures which are managed on-site may be multi-tenant, meaning that there are multiple organizations within one customer unit. A system may be assigned manually to one of these organizations.  When a system is registered with the Customer Portal, this is not required. When a system is registered with an on-premise application such as Subscription Asset Manager, this argument is required, unless there is only a single organization configured. (optional)
environment = 'environment_example' # str | Registers the system to an environment within an organization. (optional)
release = 'release_example' # str | Release version to use during registration (optional)

try:
    # Registers a new system to the subscription management service.
    api_response = api_instance.register(body=body, name=name, consumerid=consumerid, activationkey=activationkey, autoattach=autoattach, servicelevel=servicelevel, org=org, environment=environment, release=release)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationApi->register: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SystemProfile**](SystemProfile.md)| system profile, including facts and installed products | [optional] 
 **name** | **str**| Sets the name of the system to register. This defaults to the hostname. | [optional] 
 **consumerid** | **str**| References an existing system inventory ID to resume using a previous registration for this system. The ID is used as an inventory number for the system in the subscription management service database. If the system&#x27;s identity is lost or corrupted, this option allows it to resume using its previous identity and subscriptions. | [optional] 
 **activationkey** | [**list[str]**](str.md)| Gives a comma-separated list of product keys to use to redeem or apply specific subscriptions to the system. This is used for preconfigured systems which may already have products installed. Activation keys are issued by an on-premise subscription management service, such as Subscription Asset Manager. When the activationkey option is used, it is not necessary to use the username and password options, because the authentication information is implicit in the activation key. | [optional] 
 **autoattach** | **bool**| Automatically attaches compatible subscriptions to this system. | [optional] 
 **servicelevel** | **str**| Sets the preferred service level to use with subscriptions added to the system. Service levels are commonly premium, standard, and none, though other levels may be available depending on the product and the contract. | [optional] 
 **org** | **str**| Assigns the system to an organization. Infrastructures which are managed on-site may be multi-tenant, meaning that there are multiple organizations within one customer unit. A system may be assigned manually to one of these organizations.  When a system is registered with the Customer Portal, this is not required. When a system is registered with an on-premise application such as Subscription Asset Manager, this argument is required, unless there is only a single organization configured. | [optional] 
 **environment** | **str**| Registers the system to an environment within an organization. | [optional] 
 **release** | **str**| Release version to use during registration | [optional] 

### Return type

[**SyncResult**](SyncResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister**
> unregister(consumer_id=consumer_id)

Removes a system's subscriptions and removes it from the subscription management service.

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
api_instance = swagger_client.RegistrationApi(swagger_client.ApiClient(configuration))
consumer_id = 'consumer_id_example' # str |  (optional)

try:
    # Removes a system's subscriptions and removes it from the subscription management service.
    api_instance.unregister(consumer_id=consumer_id)
except ApiException as e:
    print("Exception when calling RegistrationApi->unregister: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[certAuth](../README.md#certAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

