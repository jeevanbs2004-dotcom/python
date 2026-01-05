web_development = ["Ravi", "Neha", "Amit"]
data_science = ["Karan", "Asha", "Priya"]
ui_ux_design = ["Meera", "Sonal", "Rohit"]

all_participants = [web_development, data_science, ui_ux_design]

web_development.append("Anil")

data_science.insert(1, "Vikram")

ui_ux_design.pop()

data_science_copy = data_science.copy()
data_science.clear()

print(web_development[:2])

name_lengths = [len(name) for name in data_science_copy]
print(name_lengths)

asha_present = (
    "Asha" in web_development or
    "Asha" in data_science or
    "Asha" in ui_ux_design
)
print(asha_present)

first_participants = (
    web_development[0],
    data_science_copy[0],
    ui_ux_design[0]
)
print(first_participants)
