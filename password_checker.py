# use this script before setting a new password to check if your password has ever been breeched. 

import requests
import hashlib

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
  
    if res.status_code != 200:
        raise RuntimeError(f'{res.status_code} please check API and try again')
   
    return res.content

def hacked_pass_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1password[0:5], sha1password[5:]

if __name__ == "__main__":
    password_breached = False
   
    prefix, suffix = hacked_pass_check(input("Enter Password: "))
    password_breach_list = request_api_data(prefix).split()
    for item in password_breach_list:
        value, count = item.decode('utf-8').split(":")
        if suffix == value:
            password_breached= True
            print(f"your paasword has been breached {count} times")
            break
    if password_breached == False:
        print("well-done your password has never been breached!")

        
