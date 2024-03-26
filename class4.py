from collections import defaultdict, Counter

my_text = "I wanted to take a moment to express my gratitude for the opportunity to be here. It's truly an honor to be part of this community and to have the chance to connect with each of you. I believe that together, we can achieve great things and make a positive impact on the world. Let's continue to support and inspire one another as we journey forward. Thank you for your time and support."
my_text = my_text.lower()

appers = {}

for word in my_text.split():
    until_now = appers.get(word,0)
    appers[word] = until_now + 1

print(appers)

appers = defaultdict(int)

for word in my_text.split():
    appers[word] += 1

print(appers)

appers = Counter(my_text.split())
print(appers)