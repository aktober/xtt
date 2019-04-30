**API endpoints:**

`/api/v1/last`  [GET]

`/api/v1/grab_and_save`  [POST]

**View**

`/last` - View for work with /api/v1/last

**CURL examples for testing:**

GET

`curl 0.0.0.0:5000/api/v1/last/`

`curl 0.0.0.0:5000/api/v1/last/?currency=EUR`

`curl 0.0.0.0:5000/api/v1/last/?number=2`

`curl 0.0.0.0:5000/api/v1/last/?currency=UAH&number=2`

POST

`curl -d "currency=EUR&amount=1.209" 0.0.0.0:5000/api/v1/grab_and_save/`

`curl -d "currency=UAH&amount=100" 0.0.0.0:5000/api/v1/grab_and_save/`

`curl -d "currency=BGN&amount=20.5555" 0.0.0.0:5000/api/v1/grab_and_save/`

`curl -d "currency=UAH&amount=250" 0.0.0.0:5000/api/v1/grab_and_save/`

`curl -d "currency=UAH&amount=700.5" 0.0.0.0:5000/api/v1/grab_and_save/`

`curl -d "currency=UAH&amount=70.123456789" 0.0.0.0:5000/api/v1/grab_and_save/`

`curl -d "currency=UAH&amount=234" 0.0.0.0:5000/api/v1/grab_and_save/`
