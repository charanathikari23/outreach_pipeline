def get_email(contact):

    name = contact["name"].lower().replace(" ", ".")

    return f"{name}@company.com"