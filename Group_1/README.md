#Group 1's API Project 

##Restful Reviews _(working title)_

Group 1 will create an app that uses several APIs to return some reviews and possibly (if time permits) NY Sanitation gradings for any restaurant in New York. Users will enter in a restaurant name, and some attribute such as zip code to pinpoint the location, and be able to see the restaurant's overall rating, some reviews, and other misc. information.

*But wait, there's more!* _Restful Reviews_ will be 2 aps in one, as we will give users a book option, and allow them to type in the name of a book and get a rating and some information (and even a preview!) for said book. Another option for this part of the project will allow the user to scroll a list of NYT Bestsellers.

Finally, we will extend this project to allow a simplified version where users can use twilio to get back the rating and sanitation grade of a restaraunt.

*APIs that will be used for this project*
* Factual API -- restaurant reviews and info
* Google Books API -- information about books
* NYT API -- for bestsellers list
* Twilio API -- for texting interface.

*Group assignments*
*David Kurkovskiy - Group Leader & Book API developer
*Bernie Birnbaum - Factual API developer
*Steven Huang - Server Coordinator & Twilio API developer
*Ben Huber - JS, Flask, & HTML coordinator





Our plan is to use the Factu and Twilio APIs to create an app that allows the user to text the name of a restaurant they are contemplating dining at to a number and recieve a 160 character summary of what they need to know. This would include Yelp's numerical rating, parts of reviews, and potentially more. The goal is to enable someone without a smartphone to get vital information on an eatery before they walk in.
<br>

**UPDATE--11/16**
We initially had trouble with the Yelp API, but were able to use Factual API instead!

Please make sure to
* pip install factual-api
* pip install twilio
when running our code!


