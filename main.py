import os; os.system("cls" if os.name == "nt" else "clear")

VERSION = "1.2"

try:
    print(f"\x1b[38;5;1m[+] Import required modules... (if you stuck on this screen reopen program!)")
    from pyrogram.enums import ChatType
    from pyrogram import Client
    import time
    import clipboard
    import colorama
    import pygame
    import requests
    import json
    import ctypes
    import emoji
    from pick import pick
    print(f"\x1b[38;5;1m[+] Import required modules done")
except ModuleNotFoundError:
    import os
    try:
        from pick import pick
        install = pick(["Yes", "No"], "[-] Uninstalled modules found, do you want to install them?", indicator=" >> ")[1] == 0
    except ModuleNotFoundError:
        install = input("[-] Uninstalled modules found, do you want to install them? Y/n:").lower() == "y"
    
    if install:
        os.system("cls" if os.name == "nt" else "clear")
        print("[+] Installing required modules...")
        os.system("python -m pip install --upgrade pip")
        os.system("pip install requests");os.system("python -m pip install requests");os.system("py -m pip install requests")
        os.system("pip install pick");os.system("python -m pip install pick");os.system("py -m pip install pick")
        os.system("pip install pygame");os.system("python -m pip install pygame");os.system("py -m pip install pygame")
        os.system("pip install clipboard");os.system("python -m pip install clipboard");os.system("py -m pip install clipboard")
        os.system("pip install pyrogram");os.system("python -m pip install pyrogram");os.system("py -m pip install pyrogram")
        os.system("pip install colorama");os.system("python -m pip install colorama");os.system("py -m pip install colorama")
        os.system("pip install emoji");os.system("python -m pip install emoji");os.system("py -m pip install emoji")
        os.system("cls" if os.name == "nt" else "clear")
        input(f"\x1b[38;5;1m[+] Successfully installed required modules. Reopen the program to continue...")
        exit()
    else:
        input("[-] Installing modules denied. Press \"enter\" to leave...")
        exit()

colorama.init()

if os.name == "nt":
    try:
        ctypes.windll.kernel32.SetConsoleTitleW("TeleSniper")
    except:
        pass

    embed = """                                                                    by deadlysilence.#7583
            ▄▄▄█████▓▓█████  ██▓    ▓█████   ██████  ███▄    █  ██▓ ██▓███  ▓█████ ██▀███   
            ▓  ██▒ ▓▒▓█   ▀ ▓██▒    ▓█   ▀ ▒██    ▒  ██ ▀█   █ ▓██▒▓██░  ██▒▓█   ▀▓██ ▒ ██▒ 
            ▒ ▓██░ ▒░▒███   ▒██░    ▒███   ░ ▓██▄   ▓██  ▀█ ██▒▒██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
            ░ ▓██▓ ░ ▒▓█  ▄ ▒██░    ▒▓█  ▄   ▒   ██▒▓██▒  ▐▌██▒░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
            ▒██▒ ░ ░▒████▒░██████▒░▒████▒▒██████▒▒▒██░   ▓██░░██░▒██▒ ░  ░░▒████▒░██▓ ▒██▒  
            ▒ ░░   ░░ ▒░ ░░ ▒░▓  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▓  ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░  
                ░     ░ ░  ░░ ░ ▒  ░ ░ ░  ░░ ░▒  ░ ░░ ░░   ░ ▒░ ▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
            ░         ░     ░ ░      ░   ░  ░  ░     ░   ░ ░  ▒ ░░░          ░     ░░   ░   
                        ░  ░    ░  ░   ░  ░      ░           ░  ░              ░  ░   ░     
"""

config_template = {
    "api_hash": "PUT_UR_API_HASH",
    "api_id": "PUT_UR_API_ID",
    "limit_channels": 15
}

flag = False
arr = list()
file_path = os.path.dirname(__file__)

def get_error(content):
    print(f"[-] {content} Closing in 5 seconds..." + colorama.Style.RESET_ALL)
    time.sleep(5)
    exit()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def copy_to_clipboard(content):
    try:
        clipboard.copy(content)
    except Exception:
        print("failed to copy text!" + colorama.Style.RESET_ALL)

def play_sound(sound_path):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()
        time.sleep(0.5)
    except Exception:
        get_error("No such file in this directory!")

if any([not os.path.exists(f"{file_path}/sound.mp3"), not os.path.exists(f"{file_path}/config.json")]):
    print("[+] Downloading required files...")
    if not os.path.exists(f"{file_path}/config.json"):
        with open(f"{file_path}/config.json", "w") as config_file:
            json.dump(config_template, config_file, indent=4)

    if not os.path.exists("sound.mp3"):
        res = requests.get("https://s3.filebin.net/filebin/4a4fd535b199714cee7275c0fc9fb9de82f136abbc72dd6011c8490e7c4c8078/1d8c3d4c3f66eea01fb3cf8687e062c4d60b913e3eff2e92b9b068040a260753?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=7pMj6hGeoKewqmMQILjm%2F20240216%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240216T181916Z&X-Amz-Expires=300&X-Amz-SignedHeaders=host&response-cache-control=max-age%3D300&response-content-disposition=filename%3D%22sound.mp3%22&response-content-type=audio%2Fmpeg&X-Amz-Signature=4d66f4f1b8843c4686751857d2a660c97b038d2b006163784f9cb82ef4cc9caf")
        if res.status_code == 200:
            with open(f"{file_path}/sound.mp3", "wb") as sound_file:
                sound_file.write(res.content)
        else:
            print("[-] Failed to load mp3 file")

with open(f"{file_path}/config.json", "r") as config_file:
    try:
        config = json.load(config_file)
    except json.JSONDecodeError:
        get_error("JSON decode error!")

limit = config.get("limit_channels", int())
api_hash = config.get("api_hash")
api_id = config.get("api_id")

clear()
if api_hash == "PUT_UR_API_HASH" or api_id == "PUT_UR_API_ID":
    get_error("Api hash and api id are empty!")
else:
    if not os.path.exists(f"bot.session"):
        input(colorama.Fore.RED + "[-] You did not register yet! Press \"enter\" to register...\n" + colorama.Style.RESET_ALL)
        try:
            app = Client(f"bot", api_hash=api_hash, api_id=api_id)
        except ValueError:
            get_error("Wrong api hash and api id were parsed!")
    else: 
        try:
            app = Client(f"bot")
        except Exception:
            get_error(f"Some unknown error: ({Exception}).")

def check_update():
    res = requests.get("https://raw.githubusercontent.com/cofiprofim/TelegramSniper/main/main.py").content.decode()
    try:
        version = res.split("VERSION = \"")[1].split("\"")[0]
    except IndexError:
        print("[-] Could not get a valid version")

    if version != VERSION:
        update = pick(["Yes", "No"], "New update found, do you want to update?", indicator=" >> ")[1]
        if update == 0:
            with open("main.py", "w", encoding="utf-8") as main_file:
                main_file.write(res)
            print("[+] Updated code! restart the sniper to use the newest version")
            exit(0)
        if update == 1:
            print("[-] Updates skipped")
    else:
        print("[+] No updates found.")

def get_groups(dialogs):
    for dialog in dialogs:
        chat_type = dialog.chat.type
        if len(name := "".join(char for char in (dialog.chat.title if dialog.chat.title else dialog.chat.first_name if not dialog.chat.last_name else f"{dialog.chat.first_name} {dialog.chat.last_name}") if not emoji.is_emoji(char))) > 29:
            name = name[:26] + "..."
        num = (30 - (len(name) + 1)) if len(name) < 30 else 1
        if chat_type in [ChatType.GROUP, ChatType.SUPERGROUP]:
            arr.append(f"{name} " + " " * num + "| group")
        elif chat_type == ChatType.PRIVATE:
            arr.append(f"{name} " + " " * num + "| dms")
        elif chat_type == ChatType.BOT:
            arr.append(f"{name} " + " " * num + "| bot")
        elif chat_type == ChatType.CHANNEL:
            arr.append(f"{name} " + " " * num + "| channel")

def choose_mode():
    global flag, choosedMod
    choosedMod = pick(arr, embed, indicator="                    >> ")
    flag = True
    print("┌─ [+] Watching...")

try:
    app.start()
except NameError:
    get_error("Client name were not found!")
except Exception:
    get_error("TeleSniper is already running!")

print(colorama.Fore.RED + "[+] Setting up everything...")
get_groups(app.get_dialogs(limit=limit))
clear()

app.stop()

@app.on_message()
async def handle_messages(client, message):
    global flag, choosedMod
    if flag and choosedMod[0].startswith(message.chat.first_name if message.chat.first_name else message.chat.title):
        try:
            print(f"""│
└─ Message by {message.from_user.first_name if message.from_user else "unkown user"}:
┌─ {message.text}
│""")
        except Exception as e:
            print(e)
        copy_to_clipboard(message.text)
        play_sound(f"{file_path}/sound.mp3")

if __name__ == "__main__":
    check_update()
    choose_mode()
    app.run()
