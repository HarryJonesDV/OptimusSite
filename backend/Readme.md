# OptimusSite
# README

* Optimus Site API


  This API acts as the source of truth for exposing our raw and also optimized data for buttons so that we can kill A/B testing. Our front end will send data on client interactions to Optimus Site API and data science draws on this data to discover an optimized model so that we can provide designers, engineers and the growth team, given an industry and demographic, information for an ideal layout and content for a button would look like in our demo. This API hopes to be an integral part in serving a relevant and persuasive experience to someone in the long term, saving designers, growth and engineering teams time from the very beginning. Most of all though, it is to give people what they want.

* Ruby version


  Install the appropriate Ruby and Rails versions.
  - Ruby ```2.5.3``` and Rails ```5.2.1```
  - We are using a Rails API backend for speed of generating an API to interact with our front end and data science flask app, separating these out into microservices.

* Configuration


  Using the standard Rails API middleware (and a puma rack web server). Our API responds with json. In dev, our puma web server listens on port 3000.

* Launching development server
  - ```rails server```
  - Can use postman to GET and POST data

  ```http://localhost:3000/ add-the-relevant-endpoint-route-here```

* API Base URL:
```optimus-production.ef3fapxyeu.us-east-1.elasticbeanstalk.com```

* API Endpoints:
  - ```GET``` a list of all the buttons data: ```/buttons ```
  - ```POST``` a new data point for a button to optimize: ```/buttons```
  - ```GET``` a list of all the optimized data models for buttons, as computed by our data science app: ```/models```

* Gem Management
  We used ```Bundler``` to provide a consistent environment for our Ruby gems used. Bundler helps track and install the exact gems and verisons used by our API in dev and prod. Please make sure that is installed, along with the dependencies. ```gem install bundler``` and ```bundle install```, ```bundle update```.

* Database


  On production: RDS AWS hosted Postgresql database (version 10.6).

* Thoughts on refactoring for later on


  Would use the interactor gem to handle business logic. This will help us avoid fat controllers and extract out business logic into a seperate interactors folder. This way we can conveniently test our API's behaviour using rspec, with our business logic nicely separated into interactors with singular responsibilities. They will be easily readable so that anyone can glance at the interactors folder and see what our API does. For the moment, it would have been a bit overkill to refactor such simple controllers.

* Testing


  There are no tests written to save time in this hackathon. We would use rspec to write our unit tests. We would also use shoulda-matchers and factory bot to handle some nice syntactical test matchers and creation of/managing test fixtures.

* Deployment Instructions


  This Rails API is deployed on Elastic Beanstalk.

  To deploy, use the awsebcli


  The command: ```eb deploy```


  DB migrations automatically run on deployment.

* Other best practices not forgotten, just not implemented for the hackathon:
  - dotenv rails gem to manage environment variables
  - locking down CORS.
  - can see notes about the interactor gem for refactoring business logic as well
