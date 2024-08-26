author_name = "Chancy Tsonga"
author_email = "effortbuildingcontractors@gmail.com"

with open("AUTHORS", "a") as file:
    file.write(f"- {author_name} <{author_email}>\n")

print("Author added successfully.")

