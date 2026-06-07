# outreach_pipeline
Built an automated outreach pipeline using Python that identifies similar companies, discovers decision-makers, retrieves work emails, and automates email outreach. Designed a modular architecture with workflow automation, error handling, and scalable API integration support.
# Automated Outreach Pipeline

## Overview

The Automated Outreach Pipeline is a Python-based application that automates the complete outreach process from company discovery to email delivery. The system accepts a company domain as input and automatically identifies similar companies, discovers decision-makers, retrieves their email addresses, and sends outreach emails.

The project is designed using a modular architecture, where each stage of the workflow is separated into individual modules for better maintainability, scalability, and ease of integration with real-world APIs.

---

## Features

* Company discovery from a seed domain
* Decision-maker identification
* Email address resolution
* Automated outreach email delivery
* Modular and scalable architecture
* Error handling and validation
* Safety confirmation before sending emails

---

## Project Structure

```text
outreach_pipeline/
│
├── main.py
├── ocean.py
├── prospeo.py
├── eazyreach.py
├── brevo.py
├── requirements.txt
└── README.md
```

---

## Workflow

```text
User Input (Company Domain)
            ↓
      Ocean Module
            ↓
   Similar Companies Found
            ↓
     Prospeo Module
            ↓
 Decision Makers Retrieved
            ↓
     Eazyreach Module
            ↓
    Work Emails Resolved
            ↓
       Brevo Module
            ↓
      Outreach Sent
```

---

## Modules

### main.py

Acts as the controller of the application and coordinates the complete workflow.

### ocean.py

Responsible for finding similar companies based on the input domain.

### prospeo.py

Responsible for discovering decision-makers such as CEOs, CTOs, and VP-level contacts.

### eazyreach.py

Responsible for resolving contact information into professional email addresses.

### brevo.py

Responsible for sending outreach emails.

---

## Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project directory

```bash
cd outreach_pipeline
```

3. Run the application

```bash
python main.py
```

---

## Example Usage

Input:

```text
openai.com
```

Output:

```text
John Smith (CTO) -> john.smith@company.com
Sarah Lee (VP Engineering) -> sarah.lee@company.com

Summary
Companies Found: 3
Emails Found: 6
```

---

## Safety Check

Before sending emails, the system displays a summary and requests user confirmation to prevent accidental email delivery.

---

## Technologies Used

* Python
* API Integration
* JSON
* Modular Programming
* Automation
* Error Handling

---

## Future Enhancements

* Integration with Ocean.io API
* Integration with Prospeo API
* Integration with Eazyreach API
* Integration with Brevo API
* Logging and Monitoring
* Database Support
* Bulk Campaign Management

---

## Author

Charan Venkat

Software Engineering Assignment – Automated Outreach Pipeline
