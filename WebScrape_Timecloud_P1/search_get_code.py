import imaplib
import email
import time
 
user_g = 'cosmin.turculeanu@dandsltd.com'
password_g = 'Holocaust0@@@'
imap_url = 'imap.gmail.com'

def get_code():
    # Connect to the IMAP server
    imap_server = imaplib.IMAP4_SSL(imap_url)
    imap_server.login(user_g, password_g)
    imap_server.select('INBOX')
    
    count = 0
    max_count = 15
    sleep_time = 5
    while count < max_count:
        # Search for unread emails with the subject "ACTION REQUIRED By User"
        status, msg_ids = imap_server.search(None, 'UNSEEN', 'SUBJECT "ACTION REQUIRED By User"')
        
        if msg_ids[0]:
            break
        else:
            count += 1
            time.sleep(sleep_time)  
            print(f'Waiting {sleep_time} seconds for email to arrive')

    if count == max_count:
        print("timeout")
        imap_server.logout()
        return None
    else:
        msg_ids = msg_ids[0].split()
        msg_ids.sort(reverse=True)
        for msg_id in msg_ids:
            status, msg = imap_server.fetch(msg_id, '(RFC822)')
            if status == 'OK':
                msg = email.message_from_bytes(msg[0][1])
                for part in msg.walk():
                    if part.get_content_type() in ['text/plain', 'text/html']:
                        body = part.get_payload(decode=True)
                        break
                code_pos = body.find(b'CODE: ')
                if code_pos != -1:
                    code_end_pos = code_pos+12
                    code = body[code_pos+6:code_end_pos]
                    print(f'Found code: {code}')
                    imap_server.logout()
                    return code
        imap_server.logout()
        return None


