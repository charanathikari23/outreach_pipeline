from ocean import get_similar_companies
from prospeo import get_contacts
from easyreach import get_email
from brevo import send_email

domain = input("Enter company domain: ")

companies = get_similar_companies(domain)

all_emails = []

for company in companies:

    contacts = get_contacts(company)

    for contact in contacts:

        email = get_email(contact)

        all_emails.append(email)

        print(
            f"{contact['name']} "
            f"({contact['title']}) -> "
            f"{email}"
        )

print("\nSummary")
print(f"Companies Found: {len(companies)}")
print(f"Emails Found: {len(all_emails)}")

confirm = input(
    "\nSend emails? (yes/no): "
)

if confirm.lower() == "yes":

    for email in all_emails:
        send_email(email)

