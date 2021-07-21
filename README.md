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

- Verifying Email(A user can't login until being verified).
  Eg: [`127.0.0.1:8000/api/user/email-verify/`](127.0.0.1:8000/api/user/email-verify/)

- Login.
  Eg: [`127.0.0.1:8000/api/user/login/`](127.0.0.1:8000/api/user/login/)

- Getting Token.
  Eg: [`127.0.0.1:8000/api/token/`](127.0.0.1:8000/api/token/)

- Refreshing Token.
  Eg: [`127.0.0.1:8000/api/token/refresh`](127.0.0.1:8000/api/token/refresh)

- Logout.
  Eg: [`127.0.0.1:8000/api/user/logout/blacklist/`](127.0.0.1:8000/api/user/logout/blacklist/)

- Request Password Reset Email.
  Eg: [`127.0.0.1:8000/api/user/request-reset-email/`](127.0.0.1:8000/api/user/logout/request-reset-email/)

- Verify Password Reset Email.
  Eg: [`127.0.0.1:8000/api/user/password-reset/<uidb64>/<token>/`](127.0.0.1:8000/api/user/password-reset/<uidb64>/<token>/)

- Confirm Password Reset
  Eg: [`127.0.0.1:8000/api/user/password-reset-complete`](127.0.0.1:8000/api/user/password-reset-complete)

- Getting All posts.
  Eg: [`127.0.0.1:8000/api/posts`](127.0.0.1:8000/api/posts)

- Getting An Individual posts.
  Eg: [`127.0.0.1:8000/api/post/id=<id>`](127.0.0.1:8000/api/post/1)

- Getting All Users.
  Eg: [`127.0.0.1:8000/api/user/`](127.0.0.1:8000/api/user/)

- Getting Users by year.
  Eg: [`127.0.0.1:8000/api/user?year=<year>`](127.0.0.1:8000/api/user?year=2019)

- Getting Personal Profile.
  Eg: [`127.0.0.1:8000/api/user/profile/`](127.0.0.1:8000/api/user/profile)

- Getting Other's profile.
  Eg: [`127.0.0.1:8000/api/user/profile/id=<id>/`](127.0.0.1:8000/api/user/profile/1)

- Getting All Meets.
  (A Meet can be created only by the admin)
  Eg: [`127.0.0.1:8000/api/meets/`](127.0.0.1:8000/api/user/meets/)

- Getting An Individual Meet.
  Eg: [`127.0.0.1:8000/api/meets/meet/<int:pk>/`](127.0.0.1:8000/api/user/meets/meet/<int:pk>/)

- Getting All Events.
  (An Event can be created only by the admin)
  Eg: [`127.0.0.1:8000/api/events/`](127.0.0.1:8000/api/user/events/)

- Getting All Tasks.
  (A Task can be created only by the admin)
  Eg: [`127.0.0.1:8000/api/tasks/`](127.0.0.1:8000/api/user/tasks/)

- Getting Individual Task.
  Eg: [`127.0.0.1:8000/api/tasks/task/<int:pk>/`](127.0.0.1:8000/api/user/tasks/task/<int:pk>/)

- Getting All Task of a specific user  
  Eg: [`127.0.0.1:8000/api/tasks?user_id=<int:pk>/`](127.0.0.1:8000/api/user/tasks?user_id=<int:pk>/)

## FOR GETTING OVERVIEW OF SCHEMA VISIT (127.0.0.1:8000/docs/)
