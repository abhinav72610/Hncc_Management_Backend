# API FOR HNCC_MANAGEMENT WEB/APP

## Steps to run it locally

- clone it
- make a virtual env
- install the dependencies in the virtual env(pip install -r requirements.txt)
- cd backend
- run it using python manage.py runserver


Available values for `endpoint`

- Registartion.
  Eg: [`127.0.0.1:8000/api/user/create/`](127.0.0.1:8000/api/user/create/)

- Getting Token.
  Eg: [`127.0.0.1:8000/api/token/`](127.0.0.1:8000/api/token/)

- Refreshing Token.
  Eg: [`127.0.0.1:8000/api/token/refresh`](127.0.0.1:8000/api/token/refresh)

- Logout.
  Eg: [`127.0.0.1:8000/api/user/logout/blacklist/`](127.0.0.1:8000/api/user/logout/blacklist/)

- Getting All pots.
  Eg: [`127.0.0.1:8000/api/posts`](127.0.0.1:8000/api/posts)

- Getting Individual posts.
  Eg: [`127.0.0.1:8000/api/post/id=<id>`](127.0.0.1:8000/api/post/1)

- Getting All Users.
  Eg: [`127.0.0.1:8000/api/user/`](127.0.0.1:8000/api/user/)

- Getting Users by year.
  Eg: [`127.0.0.1:8000/api/user?year=<year>`](127.0.0.1:8000/api/user?year=2019)

- Getting Personal Profile.
  Eg: [`127.0.0.1:8000/api/user/profile/`](127.0.0.1:8000/api/user/profile)

- Getting Other's profile.
  Eg: [`127.0.0.1:8000/api/user/profile/id=<id>/`](127.0.0.1:8000/api/user/profile/1)

## FOR GETTING OVERVIEW OF SCHEMA VISIT (127.0.0.1:8000/docs/)
