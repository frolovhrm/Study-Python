from class_admin import Admin

three = Admin('Alex', 'Lee', 44)

Admin.greet_user(three)
three.privileges.show_privileges()