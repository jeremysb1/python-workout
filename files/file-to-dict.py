def password_to_dict(filename):
    users = {}
    with open(filename) as password:
        for line in password:
            if not line.startswith(('#', '\n')):
                user_info = line.split(':')
                users[user_info[0]] = int(user_info[2])
    return users
