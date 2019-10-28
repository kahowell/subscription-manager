# swagger_client.SubscriptionsApi

All URIs are relative to *http://localhost:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach**](SubscriptionsApi.md#attach) | **POST** /operations/attach | Attaches one or more subscription pools to the system.
[**autoattach**](SubscriptionsApi.md#autoattach) | **POST** /operations/autoattach | Automatically attaches the best-matched compatible subscription or subscriptions to the system.
[**get_status**](SubscriptionsApi.md#get_status) | **GET** /operations/get_status | Displays shows the current status of the products and attached subscriptions for the system.
[**list_pool_ids**](SubscriptionsApi.md#list_pool_ids) | **GET** /operations/list_pool_ids | Lists all of the subscriptions that are compatible with a system.
[**list_subscriptions**](SubscriptionsApi.md#list_subscriptions) | **GET** /operations/list_subscriptions | Lists all of the subscriptions that are compatible with a system.
[**redeem**](SubscriptionsApi.md#redeem) | **POST** /operations/redeem | Redeems subscription for systems purchased from third-party vendors that include a subscription.
[**refresh**](SubscriptionsApi.md#refresh) | **GET** /operations/refresh | Pulls the latest subscription data from the server
[**remove**](SubscriptionsApi.md#remove) | **POST** /operations/remove | Removes a subscription from the system.

# **attach**
> SyncResult attach(consumer_id=consumer_id, pool=pool, quantity=quantity)

Attaches one or more subscription pools to the system.

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
consumer_id = 'consumer_id_example' # str |  (optional)
pool = ['pool_example'] # list[str] | Gives the ID for the subscriptions pool (collection of products) to attach to the system. (optional)
quantity = 56 # int | Attaches a specified number of subscriptions to the system. Subscriptions may have certain limits on them, like the number of sockets on the system or the number of allowed virtual guests. It is possible to attach multiple subscriptions (or stacking subscriptions) to cover the number of sockets, guests, or other characteristics. May not be used with an auto-attach. (optional)

try:
    # Attaches one or more subscription pools to the system.
    api_response = api_instance.attach(consumer_id=consumer_id, pool=pool, quantity=quantity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->attach: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**|  | [optional] 
 **pool** | [**list[str]**](str.md)| Gives the ID for the subscriptions pool (collection of products) to attach to the system. | [optional] 
 **quantity** | **int**| Attaches a specified number of subscriptions to the system. Subscriptions may have certain limits on them, like the number of sockets on the system or the number of allowed virtual guests. It is possible to attach multiple subscriptions (or stacking subscriptions) to cover the number of sockets, guests, or other characteristics. May not be used with an auto-attach. | [optional] 

### Return type

[**SyncResult**](SyncResult.md)

### Authorization

[certAuth](../README.md#certAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **autoattach**
> SyncResult autoattach(consumer_id=consumer_id, servicelevel=servicelevel)

Automatically attaches the best-matched compatible subscription or subscriptions to the system.

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
consumer_id = 'consumer_id_example' # str |  (optional)
servicelevel = 'servicelevel_example' # str | Sets the preferred service level to use with subscriptions automatically attached to the system. Service levels are commonly premium, standard, and none, though other levels may be available depending on the product and the contract. (optional)

try:
    # Automatically attaches the best-matched compatible subscription or subscriptions to the system.
    api_response = api_instance.autoattach(consumer_id=consumer_id, servicelevel=servicelevel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->autoattach: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**|  | [optional] 
 **servicelevel** | **str**| Sets the preferred service level to use with subscriptions automatically attached to the system. Service levels are commonly premium, standard, and none, though other levels may be available depending on the product and the contract. | [optional] 

### Return type

[**SyncResult**](SyncResult.md)

### Authorization

[certAuth](../README.md#certAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> SubscriptionStatus get_status(consumer_id=consumer_id)

Displays shows the current status of the products and attached subscriptions for the system.

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
consumer_id = 'consumer_id_example' # str |  (optional)

try:
    # Displays shows the current status of the products and attached subscriptions for the system.
    api_response = api_instance.get_status(consumer_id=consumer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**|  | [optional] 

### Return type

[**SubscriptionStatus**](SubscriptionStatus.md)

### Authorization

[certAuth](../README.md#certAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pool_ids**
> ListPoolIdsResult list_pool_ids(consumer_id=consumer_id, afterdate=afterdate, all=all, available=available, consumed=consumed, ondate=ondate, nooverlap=nooverlap, matchinstalled=matchinstalled, matches=matches)

Lists all of the subscriptions that are compatible with a system.

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
consumer_id = 'consumer_id_example' # str |  (optional)
afterdate = 'afterdate_example' # str | Shows pools that are active on or after the given date. (optional)
all = true # bool | Lists all possible subscriptions that have been purchased, even if they don't match the architecture of the system. (optional)
available = true # bool | Lists available subscriptions which are not yet attached to the system. (optional)
consumed = true # bool | Lists all of the subscriptions currently attached to the system. (optional)
ondate = 'ondate_example' # str | Sets the date to use to search for active and available subscriptions. The default (if not explicitly passed) is today's date; using a later date looks for subscriptions which will be active then. This is only used with the --available option. (optional)
nooverlap = true # bool | Shows pools which provide products that are not already covered. (optional)
matchinstalled = true # bool | Shows only subscriptions matching products that are currently installed; only used with --available option. (optional)
matches = 'matches_example' # str | Limits to only subscriptions or products which contain SEARCH in the subscription or product information, varying with the list requested and the server version. SEARCH may contain the wildcards ? or * to match a single character or zero or more characters, respectively. The wildcard characters may be escaped with a backslash to represent a literal question mark or asterisk. Likewise, to represent a backslash, it must be escaped with another backslash. (optional)

try:
    # Lists all of the subscriptions that are compatible with a system.
    api_response = api_instance.list_pool_ids(consumer_id=consumer_id, afterdate=afterdate, all=all, available=available, consumed=consumed, ondate=ondate, nooverlap=nooverlap, matchinstalled=matchinstalled, matches=matches)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->list_pool_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**|  | [optional] 
 **afterdate** | **str**| Shows pools that are active on or after the given date. | [optional] 
 **all** | **bool**| Lists all possible subscriptions that have been purchased, even if they don&#x27;t match the architecture of the system. | [optional] 
 **available** | **bool**| Lists available subscriptions which are not yet attached to the system. | [optional] 
 **consumed** | **bool**| Lists all of the subscriptions currently attached to the system. | [optional] 
 **ondate** | **str**| Sets the date to use to search for active and available subscriptions. The default (if not explicitly passed) is today&#x27;s date; using a later date looks for subscriptions which will be active then. This is only used with the --available option. | [optional] 
 **nooverlap** | **bool**| Shows pools which provide products that are not already covered. | [optional] 
 **matchinstalled** | **bool**| Shows only subscriptions matching products that are currently installed; only used with --available option. | [optional] 
 **matches** | **str**| Limits to only subscriptions or products which contain SEARCH in the subscription or product information, varying with the list requested and the server version. SEARCH may contain the wildcards ? or * to match a single character or zero or more characters, respectively. The wildcard characters may be escaped with a backslash to represent a literal question mark or asterisk. Likewise, to represent a backslash, it must be escaped with another backslash. | [optional] 

### Return type

[**ListPoolIdsResult**](ListPoolIdsResult.md)

### Authorization

[certAuth](../README.md#certAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_subscriptions**
> ListPoolsResult list_subscriptions(consumer_id=consumer_id, afterdate=afterdate, all=all, available=available, consumed=consumed, ondate=ondate, nooverlap=nooverlap, matchinstalled=matchinstalled, matches=matches)

Lists all of the subscriptions that are compatible with a system.

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
consumer_id = 'consumer_id_example' # str |  (optional)
afterdate = 'afterdate_example' # str | Shows pools that are active on or after the given date. (optional)
all = true # bool | Lists all possible subscriptions that have been purchased, even if they don't match the architecture of the system. (optional)
available = true # bool | Lists available subscriptions which are not yet attached to the system. (optional)
consumed = true # bool | Lists all of the subscriptions currently attached to the system. (optional)
ondate = 'ondate_example' # str | Sets the date to use to search for active and available subscriptions. The default (if not explicitly passed) is today's date; using a later date looks for subscriptions which will be active then. This is only used with the --available option. (optional)
nooverlap = true # bool | Shows pools which provide products that are not already covered. (optional)
matchinstalled = true # bool | Shows only subscriptions matching products that are currently installed; only used with --available option. (optional)
matches = 'matches_example' # str | Limits to only subscriptions or products which contain SEARCH in the subscription or product information, varying with the list requested and the server version. SEARCH may contain the wildcards ? or * to match a single character or zero or more characters, respectively. The wildcard characters may be escaped with a backslash to represent a literal question mark or asterisk. Likewise, to represent a backslash, it must be escaped with another backslash. (optional)

try:
    # Lists all of the subscriptions that are compatible with a system.
    api_response = api_instance.list_subscriptions(consumer_id=consumer_id, afterdate=afterdate, all=all, available=available, consumed=consumed, ondate=ondate, nooverlap=nooverlap, matchinstalled=matchinstalled, matches=matches)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->list_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**|  | [optional] 
 **afterdate** | **str**| Shows pools that are active on or after the given date. | [optional] 
 **all** | **bool**| Lists all possible subscriptions that have been purchased, even if they don&#x27;t match the architecture of the system. | [optional] 
 **available** | **bool**| Lists available subscriptions which are not yet attached to the system. | [optional] 
 **consumed** | **bool**| Lists all of the subscriptions currently attached to the system. | [optional] 
 **ondate** | **str**| Sets the date to use to search for active and available subscriptions. The default (if not explicitly passed) is today&#x27;s date; using a later date looks for subscriptions which will be active then. This is only used with the --available option. | [optional] 
 **nooverlap** | **bool**| Shows pools which provide products that are not already covered. | [optional] 
 **matchinstalled** | **bool**| Shows only subscriptions matching products that are currently installed; only used with --available option. | [optional] 
 **matches** | **str**| Limits to only subscriptions or products which contain SEARCH in the subscription or product information, varying with the list requested and the server version. SEARCH may contain the wildcards ? or * to match a single character or zero or more characters, respectively. The wildcard characters may be escaped with a backslash to represent a literal question mark or asterisk. Likewise, to represent a backslash, it must be escaped with another backslash. | [optional] 

### Return type

[**ListPoolsResult**](ListPoolsResult.md)

### Authorization

[certAuth](../README.md#certAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeem**
> redeem(consumer_id=consumer_id, email=email, locale=locale, org=org)

Redeems subscription for systems purchased from third-party vendors that include a subscription.

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
consumer_id = 'consumer_id_example' # str |  (optional)
email = 'email_example' # str | Gives the email account to send the redemption notification message to. (optional)
locale = 'locale_example' # str | Sets the locale to use for the message. If none is given, then it defaults to the local system's locale. (optional)
org = 'org_example' # str | Identifies the organization which issued the subscription being redeemed. (optional)

try:
    # Redeems subscription for systems purchased from third-party vendors that include a subscription.
    api_instance.redeem(consumer_id=consumer_id, email=email, locale=locale, org=org)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->redeem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**|  | [optional] 
 **email** | **str**| Gives the email account to send the redemption notification message to. | [optional] 
 **locale** | **str**| Sets the locale to use for the message. If none is given, then it defaults to the local system&#x27;s locale. | [optional] 
 **org** | **str**| Identifies the organization which issued the subscription being redeemed. | [optional] 

### Return type

void (empty response body)

### Authorization

[certAuth](../README.md#certAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh**
> SyncResult refresh(consumer_id=consumer_id, last_state_token=last_state_token)

Pulls the latest subscription data from the server

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
consumer_id = 'consumer_id_example' # str |  (optional)
last_state_token = 'last_state_token_example' # str | Opaque token that server uses to track whether it needs to send updated state. (optional)

try:
    # Pulls the latest subscription data from the server
    api_response = api_instance.refresh(consumer_id=consumer_id, last_state_token=last_state_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->refresh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**|  | [optional] 
 **last_state_token** | **str**| Opaque token that server uses to track whether it needs to send updated state. | [optional] 

### Return type

[**SyncResult**](SyncResult.md)

### Authorization

[certAuth](../README.md#certAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove**
> SyncResult remove(consumer_id=consumer_id, serial=serial, pool=pool, all=all)

Removes a subscription from the system.

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
consumer_id = 'consumer_id_example' # str |  (optional)
serial = ['serial_example'] # list[str] | Gives the serial number of the subscription certificate for the specific product to remove from the system. Subscription certificates attached to a system are in a certificate, in /etc/pki/entitlement/<serial_number>.pem. (optional)
pool = ['pool_example'] # list[str] | Removes all subscription certificates for the specified pool id from the system. (optional)
all = true # bool | Removes all of the subscriptions attached to a system. (optional)

try:
    # Removes a subscription from the system.
    api_response = api_instance.remove(consumer_id=consumer_id, serial=serial, pool=pool, all=all)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**|  | [optional] 
 **serial** | [**list[str]**](str.md)| Gives the serial number of the subscription certificate for the specific product to remove from the system. Subscription certificates attached to a system are in a certificate, in /etc/pki/entitlement/&lt;serial_number&gt;.pem. | [optional] 
 **pool** | [**list[str]**](str.md)| Removes all subscription certificates for the specified pool id from the system. | [optional] 
 **all** | **bool**| Removes all of the subscriptions attached to a system. | [optional] 

### Return type

[**SyncResult**](SyncResult.md)

### Authorization

[certAuth](../README.md#certAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

