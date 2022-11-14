# from django.contrib.auth.models import User

# # exec(open(r"G:\code_files\New_Django\demo_library\third\db_shell.py").read())
# # print(User.objects.all)
# User.objects.create_user(username="Ram", password="python@123", email="a@gmail.com")


from django.core.mail import send_mail
from django.conf import settings
send_mail("Python job oppotunity", 
            "Hello I am looking for an job opportunity for python developer", from_email=settings.EMAIL_HOST_USER, recipient_list=["dongardive.arnav244@gmail.com","dongardive.avinash7@gmail.com"], fail_silently = False)