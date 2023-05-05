# UrlShortener

To run the project simply create .env file in the same directory as your settings.py (/shortener by default), and run the docker-compose up command

### Project description

I did my best to keep the amount of code to be as low as possible with providing all the necessary functionalities, along with some of the best practices. I decided not to use any fancy cryptographic algorithms to shorten the URL, because after some research i determined that it doesn't decrease probability of collision, and simple random string allows us freedom in configuring desired length of the short URL. 

I've written some basic tests to ensure core functionality works at all times. 

### Notes about possible improvements
I've decided not to implement any of the things I've described below, as the description of the task incentivized simplicity, but i think the app can be improved by including simple authorization, and removing URLs created by anonymous users with a celery task after certain amount of time.
