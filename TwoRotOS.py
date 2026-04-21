import time
import msvcrt
import os

# ============================
# VERSION & PATCH NOTES
# ============================

LOCAL_VERSION = "1.0"

PATCH_NOTES = """
Version 1.0
- Initial release of TwoRot OS
- Added RBXTax calculator
- Added version and patchnotes commands
"""

# ============================
# ANIMATION FUNCTIONS
# ============================

def animate(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def loading_bar(text="Loading", length=20, speed=0.05):
    animate(text)
    bar = ""
    for _ in range(length):
        bar += "█"
        print(bar, end="\r", flush=True)
        time.sleep(speed)
    print(bar + "\n")

def get_password(prompt="Password: "):
    animate(prompt)
    password = ""
    while True:
        key = msvcrt.getch()

        if key == b'\r':  # Enter
            print()
            break

        elif key == b'\x08':  # Backspace
            if len(password) > 0:
                password = password[:-1]
                print("\b \b", end="", flush=True)

        else:
            try:
                char = key.decode("utf-8")
                password += char
                print("*", end="", flush=True)
            except:
                pass

    return password

def show_header():
    animate("\033[92mACCESS GRANTED\033[0m")
    animate("Welcome to the TwoRot DataBase.")
    animate("Type 'help' for commands.\n")

# ============================
# CIPHER LANGUAGE (UNCHANGED)
# ============================

cipher_map = {
    "a": "+",
    "b": "-",
    "c": "(",
    "d": ")",
    "e": "£",
    "f": "f",
    "g": "g",
    "h": "\"",
    "i": "/",
    "j": "`",
    "k": "k",
    "l": "%",
    "m": "{",
    "n": "}",
    "o": "@",
    "p": "[",
    "q": "]",
    "r": "^",
    "s": ":",
    "t": "!",
    "u": "<",
    "v": ">",
    "w": "#",
    "x": "~",
    "y": "*",
    "z": "="
}

reverse_cipher_map = {v: k for k, v in cipher_map.items()}

# ============================
# DECODER MODULE (UNCHANGED)
# ============================

def decoder_header():
    animate("\033[92mDECODER ACCESS GRANTED\033[0m")
    animate("Welcome to the TwoRot Decoder Database.")
    animate("Type '!help' for decoder commands.\n")

def show_deview():
    animate("\033[96mDecoder Language View:\033[0m")
    for letter in sorted(cipher_map.keys()):
        symbol = cipher_map[letter]
        animate(f"{letter}  ->  {symbol}")
    print()

def encode_text(text):
    result = ""
    for ch in text:
        lower = ch.lower()
        if lower in cipher_map:
            result += cipher_map[lower]
        else:
            result += ch
    return result

def decode_text(text):
    result = ""
    for ch in text:
        if ch in reverse_cipher_map:
            result += reverse_cipher_map[ch]
        else:
            result += ch
    return result

def decoder_mode():
    os.system("cls")
    animate("\033[96mEntering Decoder Module...\033[0m")
    time.sleep(0.4)

    animate("\033[93mSecondary authentication required.\033[0m")
    second_pass = get_password("Enter decoder password: ")

    if second_pass != "D!C0D#NG":
        animate("\033[91mACCESS DENIED — Returning to main system.\033[0m")
        time.sleep(1)
        os.system("cls")
        show_header()
        return

    os.system("cls")
    decoder_header()

    while True:
        command = input("Decoder> ")

        if command.lower() == "!help":
            animate("\n\033[96mDecoder Commands:\033[0m")
            animate("!help    - Show decoder commands")
            animate("!info    - Show information about this decoder database")
            animate("!deview  - View every letter and its encoded form")
            animate("!encode  - Encode normal text into the custom language")
            animate("!decode  - Decode custom language back into text")
            animate("!clear   - Clear decoder screen but keep header")
            animate("!exit    - Return to main OS\n")

        elif command.lower() == "!info":
            animate("\033[93mDecoder Database Information:\033[0m")
            animate("This is the official Decoder Database of RottyStudios.")
            animate("Within this secure environment, you can encode or decode text using our custom symbolic language.")
            animate("Here, you can also explore the full structure of the language to understand how each letter is represented.")
            animate("This database is designed for private communication, creative encryption, and personal cipher development.\n")

        elif command.lower() == "!deview":
            show_deview()

        elif command.lower() == "!encode":
            animate("Enter text to encode:")
            text = input("Text> ")
            encoded = encode_text(text)
            animate("Encoded output:")
            animate(encoded + "\n")

        elif command.lower() == "!decode":
            animate("Enter text to decode (cipher symbols):")
            text = input("Cipher> ")
            decoded = decode_text(text)
            animate("Decoded output:")
            animate(decoded + "\n")

        elif command.lower() == "!clear":
            os.system("cls")
            decoder_header()

        elif command.lower() == "!exit":
            os.system("cls")
            show_header()
            break

        else:
            animate("\033[91mUnknown decoder command. Type '!help' for commands.\033[0m\n")

# ============================
# RBXTax MODULE
# ============================

def rbx_tax_mode():
    os.system("cls")
    animate("\033[96mEntering RBXTax Calculator...\033[0m")
    time.sleep(0.3)

    animate("Choose mode:")
    animate("1) After Tax  - How much Robux you get after Roblox takes 30%")
    animate("2) Before Tax - How much to charge to get a certain amount after tax\n")

    mode = input("Mode (1/2)> ").strip()

    if mode == "1":
        animate("Enter sale price (Robux):")
        try:
            price = float(input("Price> "))
            net = price * 0.7
            tax = price * 0.3
            animate(f"Roblox tax: {tax:.2f} R$")
            animate(f"You receive: {net:.2f} R$\n")
        except ValueError:
            animate("\033[91mInvalid number.\033[0m\n")

    elif mode == "2":
        animate("Enter desired net Robux (after tax):")
        try:
            net = float(input("Net> "))
            price = net / 0.7
            tax = price * 0.3
            animate(f"List price: {price:.2f} R$")
            animate(f"Roblox tax: {tax:.2f} R$")
            animate(f"You receive: {net:.2f} R$\n")
        except ValueError:
            animate("\033[91mInvalid number.\033[0m\n")

    else:
        animate("\033[91mUnknown mode.\033[0m\n")

# ============================
# VERSION & PATCH NOTES COMMANDS
# ============================

def show_version():
    animate(f"TwoRot OS Version {LOCAL_VERSION}\n")

def show_patch_notes():
    animate("Patch Notes:")
    animate(PATCH_NOTES + "\n")

# ============================
# BOOT SEQUENCE
# ============================

animate("\033[96mBooting TwoRot OS...\033[0m")
time.sleep(0.4)

animate("\033[96mInitializing core modules...\033[0m")
loading_bar("\033[93mProgress:\033[0m ", length=25, speed=0.03)

animate("\033[96mRunning system diagnostics...\033[0m")
time.sleep(0.4)
animate("\033[93m[OK]\033[0m CPU Status: Stable")
animate("\033[93m[OK]\033[0m Memory Check: Passed")
animate("\033[93m[OK]\033[0m Security Modules: Active")
animate("\033[93m[OK]\033[0m Animation Engine: Online\n")
time.sleep(0.4)

animate("\033[96mFinalizing startup...\033[0m")
loading_bar("\033[93mFinalizing:\033[0m ", length=15, speed=0.04)

animate("\033[96mSystem ready.\033[0m\n")
time.sleep(0.5)

# ============================
# LOGIN
# ============================

animate("\033[96m=== LOGIN REQUIRED ===\033[0m")
password = get_password("Enter password: ")

if password == "Rotty.gg":
    os.system("cls")
    show_header()

    while True:
        command = input("TwoRot> ").lower()

        if command == "help":
            animate("\n\033[96mAvailable commands:\033[0m")
            animate("help       - Show all available commands")
            animate("clear      - Clear the screen but keep the header")
            animate("decoder    - Enter the custom TwoRot decoder (password protected)")
            animate("rbxtax     - Open Roblox tax calculator")
            animate("version    - Show current OS version")
            animate("patchnotes - Show patch notes for this version")
            animate("exit       - Close the program\n")

        elif command == "clear":
            os.system("cls")
            show_header()

        elif command == "decoder":
            decoder_mode()

        elif command == "rbxtax":
            rbx_tax_mode()

        elif command == "version":
            show_version()

        elif command == "patchnotes":
            show_patch_notes()

        elif command == "exit":
            animate("\033[93mShutting down...\033[0m")
            break

        else:
            animate("\033[91mUnknown command. Type 'help' for a list of commands.\033[0m\n")

else:
    animate("\033[91mACCESS DENIED\033[0m")
