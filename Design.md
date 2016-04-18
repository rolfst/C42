#Design

##Purpose
This application shows an example of doing multiple calls to the c42 api and combine the results for ease of use for mobile devices.  


##Conciderations
The question from C42 was to write this application in python.
The api shall expose it's functionality as a REST-api.IL = demo+4729602343@calendar42.com
The api shall also cache the results for 4.2 minutes.

##Decisions
For ease of use we shall use the django framework.
This framework is chosen because of the plethora of added features. Not because of it's lightweight implementation.
Django is also responsible for caching the request.

##example raw request  
EMAIL = demo+4729602343@calendar42.com  
TOKEN='382881befdd87ef2782f495241ac16ccd7932216'  

EVENT_ID='811003bb26ce6df198a6f6ad77aadcbb_14601157609581'  
 - Get the event details (including title)  
 ```
 curl --request GET \
 --header "Accept: application/json" \
 --header "Content-type: application/json" \
 --header "Authorization: Token $TOKEN" \
 "https://demo.calendar42.com/api/v2/events/$EVENT_ID/"
 ```

 -  Get the event subscriptions (participants including the name)  
 ```
 curl --request GET \
 --header "Accept: application/json" \
 --header "Content-type: application/json" \
 --header "Authorization: Token $TOKEN" \
     --globoff \
     "https://demo.calendar42.com/api/v2/event-subscriptions/?event_ids=[$EVENT_ID]" 
 ```

## Steps how to develop
I downloaded the responses from the c42 api
and stored these as stubs for the api
