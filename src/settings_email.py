EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "mmtp.iitk.ac.in"
EMAIL_USE_TLS = True
EMAIL_PORT = 25
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_SUBJECT = {
    "Activation": "Activation mail for SPO Career Portal",
    "PasswordReset": "Password Reset mail for SPO Career Portal",
}
EMAIL_BODY = {
    "Activation": """Hi {name:s}!
                Click on the following link to Activate your account.
                {link:s}.""",
    "PasswordReset": """Hi {name:s}!
                 Click on the following link to reset your password.
                 {link:s}.""",
}
REDIRECT_LINK = {
    "Activation": "http://127.0.0.1:8000/",
}
EMAIL_LINK = {
    "Activation": "http://127.0.0.1:8000/user/register/verify/code={code:s}/",
    "PasswordReset": "http://127.0.0.1:8000/user/resetpass/code={code:s}/",
}
