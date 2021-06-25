# SCP-Backend
## API Endpoints
A description of all the API endpoints, their URL and request parameters.
### Users
#### View User Profile
```
url: /user/profile/
method: GET

Successful : 200_OK
Response : {
             "name"
             "username"
             "roll"
             "batch"
             "program"
             "department"
             "github"
             "linkedin"
             "mastercv"
             "resume1"
             "resume2"
            }
Unsuccessful : 400_BAD_REQUEST / 401_UNAUTHORIZED

NOTE : User needs to be logged in to use this API.                         
```
#### View Placements
```
url : /user/placements/
method : GET

Successful : 200_OK
Response : [
                {
                    "key",
                    "placement_name", 
                    "company", 
                    "role", 
                    "description", 
                    "deadline"
                },
                ...
           ]

Unsuccessful : 400_BAD_REQUEST / 401_UNAUTHORIZED

Note : User needs to be logged in to use this API.
```
#### View Interns
```
url : /user/interns/
method : GET

Successful : 200_OK
Response : [
                {
                    "key",
                    "intern_name", 
                    "company", 
                    "duration", 
                    "role", 
                    "description", 
                    "deadline", 
                    "intern_start_month", 
                    "intern_end_month"
                },
                ...
           ]

Unsuccessful : 400_BAD_REQUEST / 401_UNAUTHORIZED

Note : User needs to be logged in to use this API.
```

#### Login
```
url : /users/auth/login/
method : POST
parameters = {
    "username" : "<username>",
    "password" : "<password>"
    }
```
```
Successful : 200_OK
Unsuccessful : 400_BAD_REQUEST / 401_UNAUTHORIZED
```
#### Logout
```
url : /users/auth/logout/
method : POST
parameters = {}
```
```
Successful : 200_OK
Unsuccessful : 401_UNAUTHORIZED
```
#### Intern Registration
```
url: /intern/register/
method: POST 
parameters:{
                "token"
            }    
Successful : 200_OK
Response : {
                "message"
           }
Unsuccessful : 401_UNAUTHORIZED
```
#### Placement Registration
```
url: /placement/register/
method: POST
parameters:{
                "token"
            }    
Successful : 200_OK
Response : {
                "message"
           }
Unsuccessful : 401_UNAUTHORIZED
```
