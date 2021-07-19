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
url : /user/auth/login/
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
url : /user/auth/logout/
method : POST
parameters = {}
```
```
Successful : 200_OK
Unsuccessful : 401_UNAUTHORIZED
```

#### Registeration
```
url : /user/register/
method : POST
parameters = {
         "roll" : "<roll>"
          }
```
```
Successful : 202_ACCEPTED
Unsuccessful : 403_FORBIDDEN / 400_BAD_REQUEST
```
#### Activation Mail
```
Method : POST
Parameters = {
           "roll" = <"roll">
           }
```
```
Successful : Send_mail
Unsuccessful : 206_PARTIAL_CONTENT / 400_BAD_REQUEST
```
#### Set Password And activate
```
url : /user/register/verify/code=<str:token>/
Method : POST
Parameters = {
          "password" : <"password">
           }
```
```
Successful : 200_OK
Unsuccessful : 401_UNAUTHORIZED
```
#### Reset Password Email
```
url : /user/resetpassemail/
Method : POST
Parameters = {
           "roll" : <"roll">
           }
```
```
successful : send_mail
Unsuccessful : 206_partial_content
```
#### Reset Password
```
url : /user/resetpass/code=<str:token>/
Method: POST
Parameters = {
            new1 : <"new_password_1">
            new2 : <"new_password_2">
            old  : <"old_password">
            verification code : <"token">
```
```
Successful : 200_OK
Unsuccessful : 401_UNAUTHORIZED
``` 
=======
#### Intern Registration
```
url: /intern/register/
method: POST 
parameters:{
                "key",
                "resume"<resume1/resume2>
            }    
Successful : 200_OK
Response : {
                "message"
           }
Unsuccessful : 401_UNAUTHORIZED/400_BAD_REQUEST
```
#### Placement Registration
```
url: /placement/register/
method: POST
parameters:{
                "key",
                "resume"<resume1/resume2>
            }    
Successful : 200_OK
Response : {
                "message"
           }
Unsuccessful : 401_UNAUTHORIZED/400_BAD_REQUEST
```
#### Editing User Profile
```
url: /user/edit/
method: post
parameters:{
                "github",
                "linkedin",
                "mastercv",
                "resume1",
                "resume2",
           }

Successful: 200_OK
Response:{
            "message"
         }
Unsuccessful: 400_BAD_REQUEST / 401_UNAUTHORIZED
```

### Admin


#### Login
```
url : /admin/login/
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
url : /admin/logout/
method : POST
parameters = {}
```
```
Successful : 200_OK
Unsuccessful : 401_UNAUTHORIZED
```
#### View Placements
```
url : /admin/placements/
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

Note : Admin needs to be logged in to use this API.
```
#### View Interns
```
url : /admin/interns/
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

Note : Admin needs to be logged in to use this API.
```
#### Add Placements
```
url: /admin/addPlacement/
method: POST

Parameters: {
                "placement_name", 
                "company", 
                "role", 
                "description", 
                "deadline",
                "eligible_batches",
                "eligible_branches",
                "eligible_programmes"
            }

Successfull : 200_OK
Unsuccessful: 400_BAD_REQUEST / 401_UNAUTHORIZED
```
#### Add Interns
```
url: /admin/addIntern/
method: POST

Parameters: {
                "intern_name", 
                "company", 
                "role", 
                "description",
                "duration", 
                "deadline",
                "eligible_batches",
                "eligible_branches",
                "eligible_programmes",
                "intern_start_month",
                "intern_end_month"
            }

Successfull : 200_OK
Unsuccessful: 400_BAD_REQUEST / 401_UNAUTHORIZED
```
#### Delete Placement
```
url: /admin/deletePlacement/
method: DELETE

Parameters: {
                "key"
            }

Successfull : 200_OK
Unsuccessful: 400_BAD_REQUEST / 401_UNAUTHORIZED
```
#### Delete Internship
```
url: /admin/deleteIntern/
method: DELETE

Parameters: {
                "key"
            }

Successful : 200_OK
Unsuccessful: 400_BAD_REQUEST / 401_UNAUTHORIZED
```
#### Download Placement CSV
```
url: /admin/downloadPlacement/<str:key>/
method: GET

Response: Respective csv file gets downloaded

Successful: 200_OK
Unsuccessful: 401_UNAUTHORIZED / 400_BAD_REQUEST
```
#### Download Intern CSV
```
url: /admin/downloadIntern/<str:key>/
method: GET

Response: Respective csv file gets downloaded

Successful: 200_OK
Unsuccessful: 401_UNAUTHORIZED / 400_BAD_REQUEST
```