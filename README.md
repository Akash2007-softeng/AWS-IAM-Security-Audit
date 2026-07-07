# AWS IAM Security Audit

## Project Overview

AWS IAM Security Audit is a beginner-level cloud computing project developed using Python and the AWS SDK (Boto3). The project audits AWS Identity and Access Management (IAM) resources and generates a security report. It helps administrators review IAM configurations and identify basic security issues.

---

## Features

* List all IAM users
* List IAM groups
* List IAM roles
* Check account password policy
* Check IAM access keys
* Verify Multi-Factor Authentication (MFA) status
* Identify users with Administrator Access
* Generate a `report.txt` file containing the audit results

---

## Technologies Used

* Python 3
* AWS IAM
* AWS CLI
* Boto3

---

## Project Structure

```
AWS-IAM-Security-Audit/
│── audit.py
│── report.txt
│── requirements.txt
└── README.md
```

---

## Prerequisites

* Python 3.x
* AWS Account
* AWS CLI installed
* Boto3 library

Install Boto3:

```bash
pip install boto3
```

---

## Configure AWS Credentials

Run the following command:

```bash
aws configure
```

Enter:

* AWS Access Key ID
* AWS Secret Access Key
* Default Region (Example: ap-south-1)
* Output Format (json)

---

## Run the Project

Execute the following command:

```bash
python audit.py
```

After successful execution, a file named `report.txt` will be created in the project folder.

---

## Sample Output

```
============================================================
 AWS IAM SECURITY AUDIT
============================================================

Checking IAM Users...
Checking IAM Groups...
Checking IAM Roles...
Checking Password Policy...
Checking Access Keys...
Checking MFA Status...
Checking Administrator Access...

Audit Completed Successfully.
Report saved as report.txt
```

---

## Project Workflow

1. Connect to AWS IAM using Boto3.
2. Retrieve IAM users, groups, and roles.
3. Check password policy.
4. Verify access keys.
5. Check MFA status.
6. Identify administrator users.
7. Generate the audit report.

---

## Future Improvements

* Check unused IAM users.
* Detect inactive access keys.
* Display last login details.
* Export reports in PDF format.
* Add a graphical user interface.
* Send audit reports through email.

---

## Author

**NAME:** Akash Balaji
**DOMAIN:** cloud computing
**INTERID:** CITS6087

B.Tech Information Technology

Cloud Computing Mini Project
