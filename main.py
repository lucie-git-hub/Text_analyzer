# USER LOGIN

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

print("Hello, welcome to the text analyzer! Please log in.")

print("-" * 100)

username = input("Username: ").lower()
password = input("Password: ")

print("-" * 100)

if users.get(username) == password:
    print("Welcome to the text database. Below are the texts available for analysis.")
else:
    print("Sorry, you are not a registered user.")
    quit()

# TEXT SELECTION

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

print(f"There are currently {len(TEXTS)} texts available for analysis.")
print("Please choose which one you'd like to analyze:")

for i, _ in enumerate(TEXTS, start=1):
    print(f"{i}. Text number {i}")

print("-" * 100)

text_choice = input("Enter the number of the text: ")

print("-" * 100)

if text_choice.isdigit() and 1 <= int(text_choice) <= len(TEXTS):
    print("Starting analysis of the selected text...")
else:
    print("Invalid input or text number out of range.")
    quit()

# TEXT ANALYSIS

selected_text = TEXTS[int(text_choice) - 1]

words = selected_text.split()

cleaned_words = [word.strip(",.:;?!()") for word in words]

word_count = len(cleaned_words)

titlecase_words = [word for word in cleaned_words if word.istitle()]
uppercase_words = [word for word in cleaned_words if word.isupper()]
lowercase_words = [word for word in cleaned_words if word.islower()]
numeric_values = [int(word) for word in cleaned_words if word.isdigit()]

print("-" * 100)

print(f"The text contains {word_count} words.")
print(f"Number of words starting with a capital letter: {len(titlecase_words)}")
print(f"Number of words written in UPPERCASE: {len(uppercase_words)}")
print(f"Number of words written in lowercase: {len(lowercase_words)}")
print(f"Number of numeric strings: {len(numeric_values)}")
print(f"Sum of all numbers: {sum(numeric_values)}")

print("-" * 100)

word_lengths = {}

for word in cleaned_words:
    length = len(word)
    if length in word_lengths:
        word_lengths[length] += 1
    else:
        word_lengths[length] = 1

print("LENGTH | COUNT | GRAPH")
print("-" * 100)

for length, count in sorted(word_lengths.items()):
    print(f"{str(length).rjust(6)} | {str(count).rjust(5)} | {'*' * count}")

print("-" * 100)

print("Thank you for using the text analyzer!")

print("-" * 100)