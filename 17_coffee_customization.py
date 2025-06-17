# Customize a coffee order: "small", "medium", or "large" with an option for "Extra shot" of espresso.

order_size = input("Enter your cofee size (small, medium, large): ").strip().lower()
extra_shot = input("Do you want an extra shot of espresso? (yes/no): ").strip().lower()
if extra_shot == "yes":
    print(f"You have ordered a {order_size} coffee with an extra shot of espresso.")
else:
    print(f"You have ordered a {order_size} coffee without an extra shot of espresso.")
