import regex as re
import requests
from user.models import User


class Populate:
    def populate(batches):
        r = requests.get("https://search.pclub.in/api/students")
        students = r.json()
        try:
            for student in students:
                cnt = student["i"]
                for key in student:
                    if student[key] == "":
                        student[key] = str(cnt)
                regex = "^[Y]"
                if re.search(regex, student["i"]):
                    batch = student["i"][:2]
                else:
                    batch = "Y" + student["i"][:2]
                if batch not in batches:
                    continue
                try:
                    q = User.objects.get(username=student["u"])
                    q.name = student["n"]
                    q.username = student["u"]
                    q.roll = student["i"]
                    q.batch = batch
                    q.program = student["p"]
                    q.department = student["d"]
                    q.email = student["u"] + "@iitk.ac.in"
                except:
                    q = User(
                        name=student["n"],
                        username=student["u"],
                        roll=student["i"],
                        batch=batch,
                        program=student["p"],
                        department=student["d"],
                        email=student["u"] + "@iitk.ac.in",
                    )
                q.save()
            print("Done")
        except:
            print("Error")
