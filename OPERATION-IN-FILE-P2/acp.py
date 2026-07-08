import os

with open("Sample_File.txt", "w") as file:
    file.write("My name is Arindam. I am learning Python programming.\n")




with open("Sample_File.txt", "r") as file:
    content = file.read()
    words = content.split()

print("Words in the file:")
for word in words:
    print(word)

if os.path.exists("My_File.txt"):
    print("\nMy_File.txt already exists.")
else:
    print("\nMy_File.txt does not exist.")
with open("My_File.txt", "w") as file:
        file.write("My hobbies are cycling and coding")


if os.path.exists("sample_doc.txt"):
    os.remove("sample_doc.txt")
    print("sample_doc.txt has been deleted.")
else:
    print("sample_doc.txt does not exist.")

# 6. Files are automatically closed because 'with' is used.
