# README

## Details

* Python version
    - 3.6.1

* Flask version
    - 0.12.2

* System dependencies
    - virtualenv -v 15.1.0

* Configuration
    - FLASK_APP=kingsearch
    - FLASK_DEBUG=true

* Database creation
    - No DB required

* Database initialization
    - N/A

* How to run the test suite
    - N/A

* Development instructions
    - Set environment variables in Configuration
    - install dependencies & run with:
```
    cd kingsearch
    pip install --editable .
    flask run
```

* Usage
    - search is performed as a post request on root path '/'
    - pass query parameter with search string.
```
    post '/', query: 'search string'
```

* Good to know
    - Containing sentence is not returned.


## Considerations

* Best Practices
    - There does not seem to be a agreed upon organization to Flask apps. I may be missing something being new to the language/framework.
    - I tried to follow the Python linter in SublimeText as much as possible for style.
    - Would be interested in reading well written projects & documentation to better organize both.
* Currently no tests are implemented.
    - Corner cases:
        + Results spanning multi lines will not be returned.
        + May be missing other corner cases.
* Route documentation:
    - While there isn't much to the application, I found there does not seem to be great examples of how to document routes for Flask. I would love to see examples of how to best model documentation for python/flask.
* Data Structures:
    - I am not using any complex data structures at this point. Just an array of strings.
        + Scaling is limited by memory at this point.
        + To scale to larger texts I would index the text within a database, indexing on paragraph & line numbers, as well as tokenize each word. I assume that a natural language parser might perform a good deal of these tasks.
* Rest Status codes:
    - I am not explicitly using any status codes. I possibly would return a 204 if the request is parsed and no data matching query is found.
* Deployment:
    - I would likely opt to deploy to AWS Lambda as it can be run serverless as a simple endpoint, enabling the service to remain lightweight. This would permit storing source texts in S3 or a database.
* NLTK (WIP):
    - Included some of the code experimenting with the toolkit as comments.


