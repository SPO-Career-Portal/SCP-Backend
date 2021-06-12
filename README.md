# SCP-Backend
## API Endpoints
A description of all the API endpoints, their URL and request parameters.
### Users
#### View Users
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
