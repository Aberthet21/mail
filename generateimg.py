import shutil
with open("emaillist", "r") as f:
    emails = [line.strip() for line in f]

for email in emails:
    name = email.replace ("@", "_at_").replace(".","_")
    shutil.copy("template.png", f"/var/www/html/media/signature_{name}.png")

print(f"{len(emails)} images créées dans /var/www/html/media/")