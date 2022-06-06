"""
texts_analyser.py: Prvni projekt do Engeto Online Python Akademie

author: Josef Matoušek
email: jmatousek.jobs@icloud.com
discord: Crazroz#8593
"""

TEXTS = ['''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
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
garpike and stingray are also present.''']

separator = "-"
s_width = 64
users = {"bob":"123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# 1. Vyžádání uživatelského jména a heslo
print(separator * s_width)
user = input("Uživatelské jméno: ")
password = input("Heslo: ")
print(separator * s_width)

# 2. Ověření uživatele ve slovníku uživatelů
if users.get(user) == password:

# 3. Pozdravení registrovaného uživatele    
    print((f"Vítej uživateli {user}!".center(s_width)))

# 4. Upozornění a ukončení programu v případě neregistrovaného uživatele
else:
    print("Tento uživatel není registrovaný. Ukočuji program...")
    print(separator * s_width)
    quit()

# 4. Program nechá uživatele vybrat ze třech textů
print(separator * s_width)
print(("Na konci přehledu zadej číslo vybraného texu k analýze:").center(s_width),separator * s_width, "", sep="\n")
print("1. Text", separator * len("1. Text"), TEXTS[0], "", sep = "\n")
print("2. Text", separator * len("2. Text"), TEXTS[1], "", sep = "\n")
print("3. Text", separator * len("3. Text"), TEXTS[2], "", separator * s_width, sep="\n")
text = input("Zadej číslo vybraného textu a potvrď 'enter': ")
print(separator * s_width)

# úprava stringu na inteager a ukončení programu pokud uživatel zadá jiný vstup než číslo
if text.isnumeric():
    text_number = int(text)
else:
    print("Zadaná neplatná hodnota. Ukončuji program...")
    quit()

# ověření zadání čísla v nabízeném rozsahu a případné upozornění s ukončením programu
if text_number in range(1,4):
    print("Vybrání textu proběhlo úspěšně! Zpracovávám...", separator * s_width, sep="\n")

elif text_number not in range(1,4):
    print("Číslo neodpovídá rozsahu nabídky. Ukončuji program...")
    quit()

# 5. Vyhodnocení vybraného textu - analýza
"""počet slov - zahrnuje číselné údaje jako např. 7500 nebo 30N (znaky: ",. atp. se píší obvykle spulu se slovy a 
v to případě na poštu slov nic nemění - nejsou-li z obou stran odděleny mezerou) v souladu s MS Word
"""
chosed_text = TEXTS[text_number - 1]

letters = []

for letter in chosed_text.split():
    letters.append(letter.strip(".,"))

count_letters = len(letters)
count_title = 0
count_upper = 0
count_lower = 0

for letter_t_u_l in letters:
    # počet slov začínajících velkým písmenem, fce. istitle započítá např. 30N, muselo by se ošetřit a případně upravit i ostatní fce.: isupper a islower (aby seděla suma slov)
    if letter_t_u_l.istitle():
        count_title += 1
    # počet slov psaných velkými písmeny
    elif letter_t_u_l.isupper():
        count_upper += 1
    # počet slov psaných malými písmeny
    elif letter_t_u_l.islower():
        count_lower += 1

# počet čísel a suma čísel
count_numeric = 0
sum_numbers = 0

for letter_n in letters:
    # isnumeric za číslo tvaru např. 30N neuvažuje, uvažuje-li to zadání, možné dále ošetřit
    if letter_n.isnumeric():
        count_numeric += 1
        # sečtení čísel v texu
        sum_numbers += int(letter_n)

# tisk výsledného přehledu + snaha o skloňování při změně hodnot
# počet slov
print(f"V textu je {count_letters} slov.")

# počet slov začínajících velkým písmenem
if count_title == 4:
    print(f"V textu jsou {count_title} slova začínající velkým písmenem.")
else:
    print(f"V textu je {count_title} slov začínajících velkým písmenem.")

# počet slov napsaných velkými písmeny
if count_upper == 1:
    print(f"V textu je {count_upper} slovo napsané velkými písmeny.")
else:
    print(f"V textu je {count_upper} slov napsaných velkými písmeny.")

# počet slov napsaných malým písmem
print(f"V textu je {count_lower} slov napsaných malým písmem.")

# počet čísel (ne cifer)
if count_numeric == 1:
    print(f"V textu je {count_numeric} číslo.")
else:
    print(f"V textu jsou {count_numeric} čísla.")

# sumu všech čísel (ne cifer) v textu
print(f"Součet všech čísel je {sum_numbers}.", separator * s_width, sep="\n")

# 6. Četnost různých délek slov v textu (graf)
length_letters = []
count_length = {}

for letter_len in letters:
    length_letters.append(len(letter_len))

for length in length_letters:
    if length not in count_length:
        count_length[length] = 1
    else:
        count_length[length] += 1

# vypsání hlavičky tabulky
print("+-------+-------------------+--------------+".center(s_width))
print("| DÉLKA |      PŘÍPADY      | PŘÍPADY [ks] |".center(s_width))
print("+-------+-------------------+--------------+".center(s_width))

# vypsání těla tabulky
for key, value in (sorted(count_length.items())):
    print(f"|{key:>7}|{'*' * value:<19}|{value:<14}|".center(s_width))

#vypsání patičky tabulky
print("+-------+-------------------+--------------+".center(s_width), separator * s_width, sep="\n" )
print(("Autor: Josef Matoušek").rjust(s_width), separator * s_width, sep="\n")
input("Pro ukončení stiskni libovolnou klávesu...")