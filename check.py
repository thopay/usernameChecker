import requests, re, json, time
from colorama import init, Fore
init(autoreset=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarypY0ZR04TrrTRUxDC',
    'Accept': '*/*',
    'Origin': 'https://github.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Language': 'en-US,en;q=0.9'
}

def checkUsername(username):
    s = requests.Session()

    r = s.get("https://github.com/" + username, headers=headers)
    if (r.status_code == 404):
        return ("Username Available")
    elif (r.status_code == 200):
        return ("Username Unavailable")
    elif (r.status_code == 429):
        return ("Too Many Requests")
    else:
        return ("Unknown Error")


if __name__ == "__main__":
    with open('words.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    for word in content:
        resp = checkUsername(word)
        if resp == "Username Available":
            print(Fore.GREEN + "Username Available: " + word)
        elif resp == "Username Unavailable":
            print(Fore.RED + "Username Unavailable: " + word)
        elif resp == "Too Many Requests":
            print(Fore.WHITE + "Too Many Requests - Sleeping")
            time.sleep(10000)
        else:
            print(Fore.YELLOW + "Unknown Error")
            time.sleep(10000)
