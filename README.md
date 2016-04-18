#Calendar42 Sample proxy   
This repository contains a sample project for the Calendar43 api.

##Documentation
The following pages include documentation for design and workings of this application.

- [Design](design.md)


##Usage
This api combines two calls to the backend and combines these into one response.

### Installation
to install this app:
```
> git clone git@github.com:rolfst/C42.git
> cd C42
> pip install -r requirements.txt
```

### Running the application
To start the application:
```
> cd C42_subscribedevents
> python manage.py runserver
```
open a browser to http://127.0.0.1:8000/event-with-subscriptions/<id>

