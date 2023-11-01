from flask import render_template, request
from randomuser import RandomUser


def _create(users: int):
    r = RandomUser()
    user_list = []
    generated_users = r.generate_users(users)
    for user in generated_users:
        user_list.append(
            {
                "Name": user.get_full_name(),
                "Gender": user.get_gender(),
                "City": user.get_city(),
                "State": user.get_state(),
                "Email": user.get_email(),
                "DOB": user.get_dob(),
                "Picture": user.get_picture()
            }
        )
    return user_list


def create():
    if request.method == "POST":
        num_of_users = request.form.get("users", 1)
        try:
            num_of_users = int(num_of_users)
        except ValueError:
            return "Must be an int"

        user_list = _create(num_of_users)
        return render_template("users.html", users=user_list)
