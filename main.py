data = [
    {"user_id": 1, "amount": "100"},
    {"user_id": 2, "amount": "200"},
    {"user_id": 1, "amount": "50"}
]

# Convert amount to integer
for item in data:
    item["amount"] = int(item["amount"])

# Aggregate amount per user_id
amount_per_user = {}
for item in data:
    user_id = item["user_id"]
    amount_per_user[user_id] = amount_per_user.get(user_id, 0) + item["amount"]

print(amount_per_user)
