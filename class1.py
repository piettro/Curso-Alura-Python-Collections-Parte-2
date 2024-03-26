users_data_science = [15,23,43,56]
users_machine_learning = [13,23,56,42]

all_users = users_data_science.copy()
all_users.extend(users_machine_learning)

print(all_users)

all_users = set(all_users)
print(all_users)

users_data_science = {15,23,43,56}
users_machine_learning = {13,23,56,42}

print(users_data_science | users_machine_learning)
print(users_data_science & users_machine_learning)
print(users_data_science - users_machine_learning)
print(users_data_science ^ users_machine_learning)
print(15 in users_data_science)
print(56 in users_data_science)