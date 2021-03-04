#! usr/bin/env python3
import imapclient, pprint, imaplib, pyzmail
imaplib._MAXLINE=10000000    #imaplib.error when email size more than 10000 bytes
gmail_imapobj=imapclient.IMAPClient('imap.gmail.com',ssl=True)
gmail_imapobj.login('yuhaitao521ok@gmail.com','xyojptclbahgrhwe')
#qq_imapobj=imapclient.IMAPClient('imap.qq.com',ssl=True)
#qq_imapobj.login('413168358@qq.com','xossqpfzyazmcajd')

pprint.pprint(gmail_imapobj.list_folders())
#pprint.pprint(qq_imapobj.list_folders())

select_info=gmail_imapobj.select_folder('INBOX',readonly=False)
#pprint.pprint(gmail_imapobj.search(['ALL']))
print('%d messages in INBOX' %select_info[b'EXISTS'])
pprint.pprint(gmail_imapobj.search(['since','29-OCT-2020']))
UIDs=gmail_imapobj.search(['since','29-OCT-2020'])
#fetch the UIDs email
pprint.pprint(gmail_imapobj.fetch(UIDs,['BODY[]']))


#pyzmail module
rawmessage=gmail_imapobj.fetch(UIDs,['BODY[]'])
message=pyzmail.PyzMessage.factory(rawmessage[1462][b'BODY[]'])
pprint.pprint(message.get_subject())
pprint.pprint(message.get_addresses('from'))
pprint.pprint(message.get_addresses('to'))
pprint.pprint(message.get_addresses('cc'))
pprint.pprint(message.get_addresses('bcc'))

#get the body from a rawmessage
print(message.text_part.get_payload().decode('utf-8'),end='')
#pprint.pprint(message.html_part.get_payload().decode(message.html_part.charset))

#delete emails
gmail_imapobj.delete_messages([1460])  #pass the UID value to delete_message()
gmail_imapobj.expunge()  #gmail has auto expunge, other mail may need this

#log out
gmail_imapobj.logout()  