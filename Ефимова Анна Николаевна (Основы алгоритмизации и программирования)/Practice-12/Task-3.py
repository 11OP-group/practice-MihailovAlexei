users = ["Admin", "Guest", "User", "Bot"]

users[users.index("User")] = "Moderator"
users[users.index("Bot")] = "SuperAdmin"
users.append("Newbie")
print(*users, sep=(", "))