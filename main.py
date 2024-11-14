import json
import subprocess

# Import json file
with open("Population_data.json", "r") as file:
    data = json.load(file)

# Remove rows with Country Code as UUE

data_cleared = []

for row in data:
    if row["Country Code"] != "UUE":
        data_cleared.append(row)

# Convert year into integer
for row in data_cleared:
    row["Year"] = int(row["Year"])


# Print the value for Vietnam in 2000
for row in data_cleared:
    if row["Country Name"] == "Zimbabwe" and row["Year"] == 2004:
        print(row["Value"])
        break

# Write the data into a new json file
with open("Population_data_cleared.json", "w") as file:
    json.dump(data_cleared, file)


# define a function to run a command
def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode != 0:
        print(f"Erreur : {result.stderr}")
    else:
        print(result.stdout)


# function for push the changes
def new_changes():
    commands = [
        "git add ./main.py",
        "git add ./Population_data.json",
        "git add ./Population_data_cleared.json",
        f"git commit -m '{input('Enter the commit message: ')}'",
        "git push -u origin main",
    ]
    for command in commands:
        run_command(command)


# function for initialize the repository
def init_repo():
    commands = [
        "git init",
        "git add ./main.py",
        "git commit -m 'Initial commit'",
        f"git remote add origin {input('Enter the repository URL: ')}",
        "git branch -M main",
        "git push -u origin main",
    ]

    # Run the commands
    for command in commands:
        run_command(command)


# Create the repo if it doesn't exist or push the changes if it does

try:
    with open(".git/config", "r") as file:
        if "github.com" in file.read():
            new_changes()
        else:
            init_repo()
except:
    init_repo()
