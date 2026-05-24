from auth import register_user, login_user

# Register test user
register_user(
    username="admin",
    password="admin123",
    role="Support"
)

print("User Registered Successfully")

# Login test
user = login_user(
    username="admin",
    password="admin123"
)

print(user)