users = {1,5,76,34,52,13,17}
print(len(users))

users.add(13)
print(users)

users = frozenset(users)

my_text = "I wanted to take a moment to express my gratitude for the opportunity to be here. It's truly an honor to be part of this community and to have the chance to connect with each of you. I believe that together, we can achieve great things and make a positive impact on the world. Let's continue to support and inspire one another as we journey forward. Thank you for your time and support."
set(my_text.split())