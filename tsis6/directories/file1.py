import os

path = os.path.abspath("olzhas")

print("Only directories: ")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))])
print("\nAll directories and files: ")
print([name for name in os.listdir(path)])