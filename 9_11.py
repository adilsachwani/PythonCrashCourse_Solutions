from user import Admin

admin_privileges = ['can add post','can delete post','can ban user']

my_admin = Admin("adil","sachwani",21,"BCIT - NEDUET",admin_privileges)

my_admin.privileges.display_privileges()