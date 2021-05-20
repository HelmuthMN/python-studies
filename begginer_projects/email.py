pop_domains={
    "gmail":"Google",
    "outlook":"Microsoft",
    "hotmail":"Microsoft",
    "yahoo":"Yahoo"
}

email = input("Enter your email address: ").strip()

username = email.split('@')[0]
domain = email.split('@')[-1]
domain = domain.split('.')[0]

if domain in pop_domains.keys():
    result = f"Your username = {username}\nYour domain = {pop_domains[domain]}"
else:
    result = f"Your username = {username}\nYour domain = {domain}"

print(result)