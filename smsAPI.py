<pre class="prettyprint linenums">
from datetime import date
from zang import ZangException, Configuration, ConnectorFactory
sid ='Add yours Here'
authToken ='Add yours Here'
url ='http://api.zang.io/v2'
configuration = Configuration(sid, authToken, url=url)
smsMessagesConnector = ConnectorFactory(configuration).smsMessagesConnector
# send sms message
try:
 while True:
 try:
 smsMessage = smsMessagesConnector.sendSmsMessage(
 to='+972566660009',
 body='Motion is Detected',
 from_='+1 704-445-2979')
 print(smsMessage)
 except ZangException as ze:
 print(ze)</pre>