#A program that returns live weather data of a particular city

# urllib is a library that allows python to make api calls
# json is a library that allows you to parse data that the api gives you
# what is twilio?
import urllib.request
import json
from twilio.rest import TwilioRestClient

# import twilio keys
acc_sid = 'ACb88767ea9b4cdda25c22229da861da15'
auth_tok = '1cf93a0075945b96add0daeeee000cc4'

# Create a client object with authentication info
client = TwilioRestClient(acc_sid, auth_tok)

# (Add) API key (as a string) is an authentication tool that API providers use to keep track of who is calling their API
key = 'beb10d075f016858431ca7eb8664d997'

# Choose the city to pull data from
city = 'Toronto'

# Add a URL for our python function (urlopen()) to call
url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + key

# Making the GET request (request info from the system)
# Make the request usng the urlopen function
# This returns an object with JSON encoded data inside of it
response = urllib.request.urlopen(url)

# Use the Json library to parse the object into readable json data
# the workaround - decode
parsedData = response.read().decode('utf-8')
parsedData2 = json.loads(parsedData)

# Specify which part of the JSON string we are interested in
# Extracting data - Reference the description element which is inside the weather object
description = parsedData2['weather'][0]['description']
temp = parsedData2['main']['temp'] - 273.15
print (description, temp)

# Customize the message
customMsg = 'The weather in ' + str(city) + ' is ' + str(int(temp)) + ' degrees and ' + str(description)
# Use twilio client object and twilio number to make the api call
message = client.messages.create(to="+16472844490",from_="+16476949844", body=customMsg)
