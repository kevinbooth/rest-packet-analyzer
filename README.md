# REST API Packet Analyzer

## Bored REST API
This application uses an example REST API called Bored API which can be found [here](https://www.boredapi.com/).

## Utility Purpose
Show the content of a return network packet when interacting with a RESTful API.

## Educational Purpose
* Understand the Representation State Transfer architecture
* Gain experience with maintaining a client-server relationship over the internet
* Dissect the return network packet sent from the server via a REST API
* Learn where JSON is stored in the packet
* Learn to parse out the JSON API response

## Limitations
* Because I used the requests package, I was limited to how much I could see of the packet.
  * However, I was still able to gain a lot of insight on REST API packet construction
* In the future, I would update the program to utilize a package like scapy to gain more information on network packets
  * I tried implementing this initially, but it required a lot of work up front to get working

## Test Run
```
$ python main.py
Welcome to the REST API Packet Analyzer
Courtesy of The Bored REST API
---------------------------------------

Please select one of the nine types of
activities that you may be interested
in. (recreational, relaxation, cooking,
busywork, education, social, DIY, 
music, and charity): charity

-------- Here's Your Activity --------
Volunteer at a local animal shelter
  Participants Needed: 1
  Price (0-1 [0-$$$]): 0.1
  Accessibility (0-1 [easy-hard]): 0.1

Would you like to see the developer 
information regarding the API request? 
[Y/N]: y

--- API Packet Response Information ----
Status Code: 200
Response History Status Codes: []
Server URL Requested: https://www.boredapi.com/api/activity?type=charity
Packet Size (bytes): 142
Headers (JSON): 
{
   "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept",
   "Access-Control-Allow-Origin": "*",
   "Connection": "keep-alive",
   "Content-Length": "142",
   "Content-Type": "application/json; charset=utf-8",
   "Date": "Mon, 09 Dec 2019 15:10:43 GMT",
   "Etag": "W/\"8e-/RUat9nJ276aFkErTWRY0ABZAf0\"",
   "Server": "Cowboy",
   "Via": "1.1 vegur",
   "X-Powered-By": "Express"
}

Content (JSON): 
{
   "accessibility": 0.5,
   "activity": "Volunteer at a local animal shelter",
   "key": "1382389",
   "link": "",
   "participants": 1,
   "price": 0.1,
   "type": "charity"
}

```

## Setup Local Environment:
1. Install the Pyt  hon package requirements
```
pip install -r requirements.txt
```
2. Run the Python file main.py
```
python3 main.py
```