import twocaptcha  # pip install 2captcha-python
import requests
import config

api_key = config.api_key  # https://rucaptcha.com/enterpage
solver = twocaptcha.TwoCaptcha(api_key)


def get_captcha_code() -> str:
    result = solver.recaptcha(sitekey='6Lc35vYgAAAAAN-KKANPfYYt6des4ZS4ClD9bfQp',
                              url='https://cp.vimeworld.com/register')
    return result['code']


def is_exists(nick) -> bool:
    result = requests.get(f"https://cp.vimeworld.com/api/user?register=1&name={nick}").json()
    if result['response']['exists']:
        return True  # nick already registered
    return False


def register_account(nick, password="", email="") -> bool:
    if 3 > len(nick) > 20:
        print("Incorrect len nick")
        return False

    if is_exists(nick):
        print(f"Nick {nick} already registered")
        return False

    if not password:
        password = nick

    if not email:
        email = nick + "@gmail.com"

    print(f"Starting: {nick}:{password} {email}")
    captcha_code = get_captcha_code()

    data = {
        "email": email,
        "password": password,
        "recaptcha_response": captcha_code,
        "username": nick,
    }

    headers = {
        "origin": "https://cp.vimeworld.com",
        "referer": "https://cp.vimeworld.com/register",
    }

    response = requests.post("https://cp.vimeworld.com/api/register",
                             headers=headers,
                             json=data).json()

    if response.get('success'):
        print(f"Successfully registered account: {nick}:{password}")
        return True

    print(f"Error: {response}")
    return False


register_account(nick="ExampleNick")
# register_account(nick="ExampleNick", password="ExamplePassword", email="test@gmail.com")
