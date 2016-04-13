#Design

##Purpose
This application shows an example of doing multiple calls to the c42 api and combine the results for ease of use for mobile devices.  


##Conciderations
The question from C42 was to write this application in python.
The api shall expose it's functionality as a REST-api.
The api shall also cache the results for 5 minutes.

##Descisions
For ease of use we shall use the django framework.
This framework is chosen because of the plethora of added features. Not because of it's lightweight implementation.
Django is also responsible for caching the request.