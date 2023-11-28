/restaurant -> for viewing static resources
/restaurant/menu -> CRUD api route for Menu model
/restaurant/booking/tables/ -> CRUD api route for Bookings model ** requires authentication **
/auth/users -> api to create users by using POST method with email, username, and password -> user registration
/auth/login -> api to login user and obtain token -> user authentication

Clone project locally on your computer
In the terminal make sure you are inside the littleLemonCapstone directory 
run pwd and you should see something like anythinghere/anythinghere/littleLemonCapstone there may be fewer or more anythinghere's (anythinghere meaning any name may be there) depending on how deep the littleLemonCapstone is on your computer
pipenv shell (I use pipenv for my virtual environment)
pipenv install (installs dependencies in my pipfile)
python manage.py test tests -> my tests are held in the tests directory. This will run both of my unit tests.
python manage.py makemigrations
python manage.py migrate
python manage.py runserver -> can test routes and static resources in the browser