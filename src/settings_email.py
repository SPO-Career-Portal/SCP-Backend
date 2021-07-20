EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "mmtp.iitk.ac.in"
EMAIL_USE_TLS = True
EMAIL_PORT = 25
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_SUBJECT = {
    "Activation": "Activation mail for SPO Career Portal",
    "PasswordReset": "Password Reset mail for SPO Career Portal",
    "PlacementConfirmation": "Succesfully Registered for Placement",
    "InternConfirmation": "Successfully Registered for Internship",
    "PlacementMailer": "Placement Application Deadline Approaching",
    "InternMailer": "Internship Application Deadline Approaching",
}
EMAIL_BODY = {
    "Activation": """Hi {name:s}!\n
Click on the following link to Activate your account.
{link:s}.\n
- Students' Placement Office""",

    "PasswordReset": """Hi {name:s}!\n
Click on the following link to reset your password.
{link:s}.\n
- Students' Placement Office""",

    "PlacementConfirmation": """Hi {name:s}!\n
You have successfully registered for the placement offer with the following details:
NAME: {placement_name:s}
COMPANY: {company:s}
ROLE: {role:s}\n
-Students' Placement Office""",

    "InternConfirmation": """Hi {name:s}!\n
You have successfully registered for the internship with the following details:
NAME: {intern_name:s}
COMPANY: {company:s}
ROLE: {role:s}\n
-Students' Placement Office""",

    "PlacementMailer": """Hi {name:s}!\n
Application deadlines of the following Placement offers are round the corner. If you want to apply then hurry up.
{body:s}
-Students' Placement Office""",

    "InternMailer": """Hi {name:s}!\n
Deadlines of the following Internships are round the corner. If you want to apply then hurry up.
{body:s}
-Students' Placement Office""",
}
REDIRECT_LINK = {
    "Activation": "http://127.0.0.1:8000/",
}
EMAIL_LINK = {
    "Activation": "http://127.0.0.1:8000/user/register/verify/code={code:s}/",
    "PasswordReset": "http://127.0.0.1:8000/user/resetpass/code={code:s}/",
}
