# OfflineTx
_Brodcast bitcoin transactions using text messages_

This project has three parts: 
1. Android App 
2. Web Server 
3. Third party APIs

+ Android app can be used to convert transaction hex in to words and send using text messages

+ Web Server part listens for incoming text messages, saves them in a google sheet (phone number, content, flag etc.). Second part of web server is not implemented yet which will regularly check for new data in google sheet, decode from words to hex, broadcast using [blockstream.info API](https://github.com/Blockstream/esplora/blob/master/API.md), save the trannsaction id and respond by sending text message

+ APIs: Text messaging - [Texlocal](https://api.textlocal.in/docs) Broadcast tx: [Blockstream](https://github.com/Blockstream/esplora/blob/master/API.md)

1. Open the App in Visual Studio, build and run. Copy a transaction hex.

![1](/Screenshots/1.png)

2. Tap "broadcast" which will encode it into words, warning text shows number of messages that will be sent and confirm it will send multi parts message with all the words.

![2](/Screenshots/2.png) ![3](/Screenshots/3.png) ![4](/Screenshots/4.png)

3. I have used [ngrok](https://ngrok.com/) to get a public URL for the web server running on localhost

![5](/Screenshots/5.png)

4. The URL should be saved in the INBOX settings for [textlocal.in](https://control.textlocal.in/)

![6](/Screenshots/6.png)

5. I have commented some code in [ListenandSave.py](/Web%20Server/ListenandSave.py) because you need to buy a dedicated number for receiving random texts. Right now you can test by sending the default keyword for inbox to the specified number. It will save all the details in google sheet.

![7](/Screenshots/7.png)
