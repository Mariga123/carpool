Carpool

Car-Pooling is intended to help the user to share car rides with other users traveling on the same route. The user may intend to share his car or else ride with another user who is willing to share.

The carpooling software is designed and developed in Django framework using GoogleMaps API.

Carpool is aimed toward a person who is a frequent traveller and is looking for cheap and comfortable mode of transport. It will prove beneficial for office commuters who are headed on a common route and are willing to share the travel cost. Anyone can opt to provide a drive, thus reducing his/her expense. 


:::info
Github Repo: **[Carpool](https://github.com/Mariga123/carpool.git)**
:::
## Table of Contents

[TOC]

## Setup
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See getting started for notes on how to deploy the project on a live system.

### Prerequisites
You need to install:
1. [Python 3.6 or above](https://www.python.org/downloads/)
2. [Django 3.0 or above](https://docs.djangoproject.com/en/3.0/intro/install/)
3. [GoogleMaps API](https://developers.google.com/maps/documentation)

---
### Getting Started

Once django is installed, all you need to do is clone this repository.

```bash
$ git clone https://github.com/Mariga123/carpool.git
```

After this, enter the following commands to run the webserver:
```bash
$ python manage.py migrate
$ python manage.py runserver
```

---
## Technologies Used

### Google APIs Used
* **Directions API** - It is used to display route between two points. Route similarity is inferred based on this to broadcast ride request to specific drivers.
* **Distance Matrix API** - It is used to get distance between two points. This is used to decide fare of ride.
* **Geocoding API** - It is used to convert a place name(For eg: Uhuru Park, Nairobi) to its corresponding coordinates(latitude and longitude). 
* **Maps JavaScript API** - The API is used to make calls to different APIs using JavaScript.
* **Places API** - The API is used to get suggestions of places when user types a string.

* Jquery
* Javascript
* Bootstrap
* Python
* Python Google Maps API
* Django Rest-Framework
## Functionality

There are two cateogories of users: 
* **Driver** - A user who wants to share his ride with other people along the same route or is a full-time driver.

* **Rider** - A user(other than driver) sharing a ride. He can book in realtime and will be assigned a driver from the pool of drivers available.

### Known Bugs
* Still working on passenger and driver Dashboards
* Create a communication between drivers,and also passenger to passenger who would like to share a ride.
* Improve on Google maps and locations.
* Add more U.I features

### To contribute contact us on 
* [johnmariga8@gmail.com](https://mail.google.com/mail/u/0/#inbox)
* [carolwambuidaystar@gmail.com](https://mail.google.com/mail/u/0/#inbox)


## Authors

* [John Mariga](https://github.com/Mariga123)
* [Carol Wambui](https://github.com/carol-wambui)
