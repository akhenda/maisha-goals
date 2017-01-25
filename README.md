[![Build Status](https://travis-ci.org/andela-akhenda/maisha-goals.svg?branch=develop)](https://travis-ci.org/andela-akhenda/maisha-goals)
[![Coverage Status](https://coveralls.io/repos/github/andela-akhenda/maisha-goals/badge.svg?branch=develop)](https://coveralls.io/github/andela-akhenda/maisha-goals?branch=develop)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/fa80aca7df2b4df0b12340b14f0f4426)](https://www.codacy.com/app/joseph-akhenda/maisha-goals?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=andela-akhenda/maisha-goals&amp;utm_campaign=Badge_Grade)
[![Code Health](https://landscape.io/github/andela-akhenda/maisha-goals/develop/landscape.svg?style=flat)](https://landscape.io/github/andela-akhenda/maisha-goals/develop)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/andela-akhenda/cp1a/blob/master/LICENSE)
[![PyPI](https://img.shields.io/badge/Python-3.3%2C%203.4%2C%203.5-blue.svg)](https://www.python.org/downloads/release/python-2712/)

# Maisha Goals
Maisha Goals is a RESTful bucket list API built with `Flask`. A bucket list is a list of things you'd like to do before you die, like visiting the Grand Canyon, falling in love or falling into the Grand Canyon. This API allows a person to register as a user, login, create and manage bucket lists together with their corresponding items.

## Installation

Clone this repo:
```
$ git clone https://github.com/andela-akhenda/maisha-goals.git
```

Navigate to the `maisha-goals` directory:
```
$ cd maisha-goals
```

Create a vitual environment:
> Use [this guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/) to create and activate a virtual environment.

Install the required packages:
```
$ pip install -r requirements.txt
```

Set the required environment key

`export MAISHA_SECRET='something-really-secret'`

## Usage

Run ```python run.py```.

To test the API, use an API Client such as [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en) for Google Chrome to test the endpoints.

### API Endpoints 


| Actions        | Description           | Requires Authentication |
| ------------- |:-------------:| -------------:|
| POST auth/login    | Log a user in | False |
| POST auth/register     | Register a new user | False |
| POST api/v1/bucketlists/ | Create a new bucketlist   | True |
| GET /bucketlists/      | List all created bucketlists | True |
| GET /bucketlists/id     | get single bucketlist | True |
| PUT /bucketlists/id | update single bucketlist | True |
| DELETE bucketlists/id      | Delete a single bucketlist | True |
| POST bucketlists/id/items/      | Create a new item in a bucketlist | True |
| PUT bucketlists/id/items/item_id | Update an item in a bucketlist | True |
| DELETE bucketlists/id/items/item_id      | Delete an item in a bucketlist | True |
| GET users/        |   Get all users       | True |
| GET users/id  |   Get a single user   | True |
| PUT users/id  |   Update a user       | True |
| DELETE users/id   | Delete a user | True |

## Sample Requests

**Registering a new user:**
To register a new user, hit the `/auth/register` POST endpoint passing a json payload containing the `username` and `password`. 
![Alt text](/source/registe_new_user.png?raw=true "Optional Title")


**Authenticating a user (Login)**
To authenticate a user, hit the `/auth/login` GET endpoint using HTTP Basic Auth standards i.e. sending a Base64 encoded string containing the username and password in the `Authorization` header.
![Alt text](/source/login_users.png?raw=true "Optional Title")

**Sending a token to protected endpoints**
To send a token with the requests, base64 encode it and send it in the `Authorization` header prefixed with 'Basic ' as shown below. 
![Alt text](/source/login_users.png?raw=true "Optional Title")

**Creating a Bucket list:**
To create a bucket list, hit the `/api/v1/bucketlists/` POST endpoint passing a json payload containing the `name` and an optional `description`.   
![Alt text](/source/create_bucketlist.png?raw=true "Optional Title")

**Updating a Bucket list:**
To update a bucket list, hit the `/api/v1/bucketlists/<id>` PUT endpoint passing a json payload containing the new `name` and/or `description`.   
![Alt text](/source/create_bucketlist.png?raw=true "Optional Title")

**Show a single Bucket list:**
To show a single bucket list, hit the `/api/v1/bucketlists/<id>` GET endpoint.   
![Alt text](/source/create_bucketlist.png?raw=true "Optional Title")

**Listing all Bucket lists:**  
To list all bucket lists under a the current user, hit the `/api/v1/bucketlists/` GET endpoint.  
![Alt text](/source/list_all_bucketlists.png?raw=true "Optional Title")

**Creating a Bucket list item:**  
To create a bucket list item, hit the `/api/v1/bucketlists/<id>/items/` POST endpoint passing a json payload containing the `name` and an optional `description`. 
![Alt text](/source/create_bucketlist_item.png?raw=true "Optional Title")

**Listing all items in a Bucket lists:**  
To list all bucket lists under a the current user, hit the `/api/v1/bucketlists/<id>/items/` GET endpoint.
![Alt text](/source/list_all_bucketlists.png?raw=true "Optional Title")

**Update user information e.g. the password:**  
To update/edit a user's information, hit the `/api/v1/users/<id>` PUT endpoint with a payload containing the information to be updated. NB: Editing usernames is not allowed.
![Alt text](/source/list_all_bucketlists.png?raw=true "Optional Title")

**Deleting a resource:**
To delete a resource, whether bucket list, bucket list item or a user, hit the respective route with the resource `id` as a DELETE request.   
![Alt text](/source/create_bucketlist.png?raw=true "Optional Title")

## Testing

Run tests using one of the following commands:
```
$ python setup.py test

running pytest
running egg_info
writing top-level names to Maisha_Goals.egg-info/top_level.txt
writing Maisha_Goals.egg-info/PKG-INFO
writing requirements to Maisha_Goals.egg-info/requires.txt
writing dependency_links to Maisha_Goals.egg-info/dependency_links.txt
reading manifest file 'Maisha_Goals.egg-info/SOURCES.txt'
writing manifest file 'Maisha_Goals.egg-info/SOURCES.txt'
running build_ext
================================================================================ test session starts ================================================================================
platform darwin -- Python 3.5.2, pytest-3.0.6, py-1.4.32, pluggy-0.4.0 -- /Users/hendaz/.virtualenvs/maisha-venv/bin/python
cachedir: .cache
rootdir: /Users/hendaz/Projects/Checkpoints/maisha-goals, inifile: setup.cfg
plugins: cov-2.4.0
collected 37 items

tests/test_auth.py::TestAuth::test_registration_wwithout_password PASSED
tests/test_auth.py::TestAuth::test_successful_login PASSED
tests/test_auth.py::TestAuth::test_successful_registration PASSED
tests/test_auth.py::TestAuth::test_unsuccessful_login PASSED
tests/test_auth.py::TestAuth::test_unsuccessful_registration PASSED
tests/test_bucketlist_items.py::TestBucketlistItems::test_add_bucketlist_item PASSED
tests/test_bucketlist_items.py::TestBucketlistItems::test_add_bucketlist_item_with_empty_name_string_or_no_name PASSED
tests/test_bucketlist_items.py::TestBucketlistItems::test_add_duplicate_bucketlist_item PASSED
tests/test_bucketlist_items.py::TestBucketlistItems::test_bucketlist_item_operations_on_another_users_bucketlist PASSED
tests/test_bucketlist_items.py::TestBucketlistItems::test_delete_bucketlist_item PASSED
tests/test_bucketlist_items.py::TestBucketlistItems::test_get_bucketlist_item PASSED
tests/test_bucketlist_items.py::TestBucketlistItems::test_get_bucketlist_items PASSED
tests/test_bucketlist_items.py::TestBucketlistItems::test_non_existent_bucketlists_and_items PASSED
tests/test_bucketlist_items.py::TestBucketlistItems::test_operations_on_invalid_bucketlist_item PASSED
tests/test_bucketlist_items.py::TestBucketlistItems::test_update_bucketlist_item PASSED
tests/test_bucketlists.py::TestBucketlists::test_add_bucketlist PASSED
tests/test_bucketlists.py::TestBucketlists::test_add_bucketlist_with_empty_name_string PASSED
tests/test_bucketlists.py::TestBucketlists::test_add_duplicate_bucketlist PASSED
tests/test_bucketlists.py::TestBucketlists::test_bucketlists_pagination PASSED
tests/test_bucketlists.py::TestBucketlists::test_delete_bucketlist PASSED
tests/test_bucketlists.py::TestBucketlists::test_get_bucketlist PASSED
tests/test_bucketlists.py::TestBucketlists::test_get_bucketlists PASSED
tests/test_bucketlists.py::TestBucketlists::test_methods_on_invalid_bucketlist PASSED
tests/test_bucketlists.py::TestBucketlists::test_operation_on_another_user_bucketlist PASSED
tests/test_bucketlists.py::TestBucketlists::test_search_bucketlist PASSED
tests/test_bucketlists.py::TestBucketlists::test_update_bucketlist PASSED
tests/test_endpoints.py::TestEndpoints::test_allowed_url_methods PASSED
tests/test_endpoints.py::TestEndpoints::test_api_index PASSED
tests/test_endpoints.py::TestEndpoints::test_invalid_query_parameters PASSED
tests/test_endpoints.py::TestEndpoints::test_invalid_urls PASSED
tests/test_endpoints.py::TestEndpoints::test_malformed_post_and_put_requests PASSED
tests/test_endpoints.py::TestEndpoints::test_requests_with_invalid_tokens PASSED
tests/test_endpoints.py::TestEndpoints::test_requests_with_no_token PASSED
tests/test_users.py::TestUsers::test_delete_user_account PASSED
tests/test_users.py::TestUsers::test_get_user PASSED
tests/test_users.py::TestUsers::test_get_users PASSED
tests/test_users.py::TestUsers::test_update_user PASSED
```
or
```
$ nosetests --verbose

test_registration_wwithout_password (tests.test_auth.TestAuth) ... ok
Test successful user login ... ok
Test successful user registration ... ok
Test unsuccessful user login with invalid credentials ... ok
Register a user with a username already in the DB ... ok
Test for new item creation ... ok
test_add_bucketlist_item_with_empty_name_string_or_no_name (tests.test_bucketlist_items.TestBucketlistItems) ... ok
Test creation of a bucketlist item with an existing name ... ok
Test that users cannot access other users' bucketlist items ... ok
Test deletion of a bucketlist item ... ok
Test that we can fetch a specific bucket list item ... ok
Test that all bucketlist items are returned ... ok
Tests to cover all invalid bucketlists scenarios ... ok
Tests to cover all invalid bucketlist items scenarios ... ok
Test for updating an item ... ok
test_add_bucketlist (tests.test_bucketlists.TestBucketlists) ... ok
test_add_bucketlist_with_empty_name_string (tests.test_bucketlists.TestBucketlists) ... ok
Test creation of a bucketlist with an existing name ... ok
test_bucketlists_pagination (tests.test_bucketlists.TestBucketlists) ... ok
Test deletion of a bucketlist ... ok
Test that we can fetch a specific bucket list ... ok
Test that all bucket lists are displayed ... ok
Tests to cover all invalid bucketlists scenarios ... ok
Test that users cannot access other users' bucketlists ... ok
test_search_bucketlist (tests.test_bucketlists.TestBucketlists) ... ok
Test editing of bucket lists ... ok
test_allowed_url_methods (tests.test_endpoints.TestEndpoints) ... ok
test_api_index (tests.test_endpoints.TestEndpoints) ... ok
test_invalid_query_parameters (tests.test_endpoints.TestEndpoints) ... ok
test_invalid_urls (tests.test_endpoints.TestEndpoints) ... ok
test_malformed_post_and_put_requests (tests.test_endpoints.TestEndpoints) ... ok
test_requests_with_invalid_tokens (tests.test_endpoints.TestEndpoints) ... ok
Test that tokens are required for secured endpoints ... ok
Test deletion of a user account ... ok
Test that we can fetch a single user ... ok
test_get_users (tests.test_users.TestUsers) ... ok
Test editing of user information ... ok

----------------------------------------------------------------------
Ran 37 tests in 2.612s

OK
```
or
```
$ make test
```

## Built With...
* [Flask](http://flask.pocoo.org/)
* [Flask-RESTful](http://flask-restful-cn.readthedocs.io/en/0.3.4/)
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/)

## License

### The MIT License (MIT)

Copyright (c) 2016 [Joseph Akhenda](https://github.com/andela-akhenda).

> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in
> all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
> THE SOFTWARE.
