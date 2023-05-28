# Bypass captcha and register account
![изображение](https://github.com/MrBonjur/AutoRegVime/assets/55990897/da54550a-1e24-4ee7-b6b3-a194eaba8337)

### Dependencies:
* python 3.7+
* pip install 2captcha-python
* buy balance -> https://rucaptcha.com/enterpage
---
# Easy and fast
1) Fill config.py using token from https://rucaptcha.com/

2) Start in code:
```
register_account(nick="ExampleNick")
```

Modify the code for multi-register:
```
for i in range(1, 400):
    register_account(nick=f"ExampleNick{i}")
```

that's all =)
