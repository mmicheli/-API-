# Warning
> Whatsapp blocks numbers now. Framework wont work properly until next version
1. Clone this repository (with submodules since it uses tgalal's yowsup library)
```sh

```
2. Run setup.sh (Most likely on sudo since its going to install some libraries)
```sh
> sudo ./setup.sh
```

3. Register your phone and get a password with like this:
```sh
# Replace CC with your country code (See https://countrycode.org)
> yowsup-cli registration --requestcode sms --phone CCXXXXXXXX --cc CC -E android
# After getting the sms code (in this example: 123456)
> yowsup-cli registration --register 123456 --phone CCXXXXXXXX --cc CC -E android
```


4. Open **config.py** and add set your credentials

5. Ready to go! (Now you can add your own whatsapp modules)
```sh
> ./start.sh
```


```python
# modules/hi_module.py

from app.mac import mac, signals

@signals.message_received.connect
def handle(message):
    if message.text == "hi":
        mac.send_message("Hello", message.conversation)
        
        # Can also send media
        #mac.send_image("path/to/image.png", message.conversation)
        #mac.send_video("path/to/video.mp4", message.conversation)
```

```python
# modules/__init__.py
...
from modules import hi_module
...


# Updates
The project is not submoduling yowsup now due to a lot of the modifications made are focused for this project only and to make things simpler.
- [x] Notification on messages receipt (received and blue check marks)
- [x] Get contacts statuses
- [x] Get contacts profile picture (also from groups)
- [x] Set profile picture (also from groups)
- [x] Send videos (needs ffmpeg installed)
- [x] Add support for @tag messages
- [x] Add support for reply messages
- [x] Add support for receiving images
- [x] Add support for big receiving big files (downloading and decryption done in chunks)
- [x] Add support for sending images
- [ ] Add support for encrypting images in chunks (_TODO_)
- [ ] Add pickle support to remember the messages when mac its turned off(_TODO_)

# Example screenshots:
![](https://i.imgur.com/ZRlk5Uj.png)
![](https://i.imgur.com/JmPbPXB.png)
![](https://i.imgur.com/L4ebZql.png)
<img src="https://i.imgur.com/pLiwAm5.png" width="253px" height="450px">
<img src="https://i.imgur.com/poLpmAR.png" width="253px" height="450px">
<img src="https://i.imgur.com/CRNKfHj.png" width="253px" height="450px">
