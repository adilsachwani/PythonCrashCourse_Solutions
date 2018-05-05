current_users = ["adil","saba","naveed","rija","amna","admin"]
new_users = ["alina","SABA","yolo"]

for user in new_users:
    if user.lower() in current_users:
        print("Username " + user.lower() + " already in use")
    else:
        print("Username " + user.lower() + " available")