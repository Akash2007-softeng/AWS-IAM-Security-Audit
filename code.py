import boto3
from datetime import datetime

# Create IAM client
iam = boto3.client("iam")

# Open report file
report = open("report.txt", "w")

print("=" * 60)
print(" AWS IAM SECURITY AUDIT ")
print("=" * 60)

report.write("=" * 60 + "\n")
report.write("AWS IAM SECURITY AUDIT REPORT\n")
report.write("=" * 60 + "\n")
report.write("Generated : " + str(datetime.now()) + "\n\n")

# -------------------------------
# IAM USERS
# -------------------------------
print("\nChecking IAM Users...\n")
report.write("IAM USERS\n")

users = iam.list_users()["Users"]

if len(users) == 0:
    print("No IAM Users Found")
    report.write("No IAM Users Found\n")
else:
    for user in users:
        print("User :", user["UserName"])
        report.write("User : " + user["UserName"] + "\n")

report.write("\n")

# -------------------------------
# IAM GROUPS
# -------------------------------
print("\nChecking IAM Groups...\n")
report.write("IAM GROUPS\n")

groups = iam.list_groups()["Groups"]

if len(groups) == 0:
    print("No IAM Groups Found")
    report.write("No IAM Groups Found\n")
else:
    for group in groups:
        print("Group :", group["GroupName"])
        report.write("Group : " + group["GroupName"] + "\n")

report.write("\n")

# -------------------------------
# IAM ROLES
# -------------------------------
print("\nChecking IAM Roles...\n")
report.write("IAM ROLES\n")

roles = iam.list_roles()["Roles"]

if len(roles) == 0:
    print("No IAM Roles Found")
    report.write("No IAM Roles Found\n")
else:
    for role in roles:
        print("Role :", role["RoleName"])
        report.write("Role : " + role["RoleName"] + "\n")

report.write("\n")

# -------------------------------
# PASSWORD POLICY
# -------------------------------
print("\nChecking Password Policy...\n")
report.write("PASSWORD POLICY\n")

try:
    policy = iam.get_account_password_policy()["PasswordPolicy"]

    report.write("Minimum Password Length : " +
                 str(policy["MinimumPasswordLength"]) + "\n")
    report.write("Require Symbols : " +
                 str(policy["RequireSymbols"]) + "\n")
    report.write("Require Numbers : " +
                 str(policy["RequireNumbers"]) + "\n")
    report.write("Require Uppercase : " +
                 str(policy["RequireUppercaseCharacters"]) + "\n")
    report.write("Require Lowercase : " +
                 str(policy["RequireLowercaseCharacters"]) + "\n")

    print("Password Policy Found")

except Exception:
    print("No Password Policy Found")
    report.write("No Password Policy Found\n")

report.write("\n")

# -------------------------------
# ACCESS KEYS
# -------------------------------
print("\nChecking Access Keys...\n")
report.write("ACCESS KEYS\n")

for user in users:
    username = user["UserName"]

    keys = iam.list_access_keys(UserName=username)["AccessKeyMetadata"]

    if len(keys) == 0:
        report.write(username + " : No Access Keys\n")
    else:
        for key in keys:
            report.write(
                username +
                " | Key ID : " +
                key["AccessKeyId"] +
                " | Status : " +
                key["Status"] +
                "\n"
            )

report.write("\n")

# -------------------------------
# MFA STATUS
# -------------------------------
print("\nChecking MFA Status...\n")
report.write("MFA STATUS\n")

for user in users:
    username = user["UserName"]

    mfa = iam.list_mfa_devices(UserName=username)["MFADevices"]

    if len(mfa) == 0:
        report.write(username + " : MFA Disabled\n")
    else:
        report.write(username + " : MFA Enabled\n")

report.write("\n")

# -------------------------------
# ADMINISTRATOR ACCESS
# -------------------------------
print("\nChecking Administrator Access...\n")
report.write("ADMINISTRATOR ACCESS\n")

for user in users:
    username = user["UserName"]

    policies = iam.list_attached_user_policies(
        UserName=username
    )["AttachedPolicies"]

    admin = False

    for policy in policies:
        if policy["PolicyName"] == "AdministratorAccess":
            admin = True

    if admin:
        report.write(username + " : Administrator Access\n")
    else:
        report.write(username + " : Normal User\n")

report.write("\n")

# -------------------------------
# AUDIT COMPLETED
# -------------------------------
report.write("Audit Completed Successfully.\n")
report.close()

print("\nAudit Completed Successfully.")
print("Report saved as report.txt")