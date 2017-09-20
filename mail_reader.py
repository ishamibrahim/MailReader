import poplib
import string, random
import StringIO, rfc822
import logging
from speaker import speak_the_sentence
from bs4 import BeautifulSoup
import time

SERVER = "pop.gmail.com"
USER = "isham1697@gmail.com"
PASSWORD = "poiuytrewq0987654321"


def read_new_mail():
    p = poplib.POP3_SSL(SERVER)  # or "POP3" if SSL is not supported
    try:
        p.user(USER)
        p.pass_(PASSWORD)
    except poplib.error_proto, e:
        print "Login failed:", e
    else:
        mail_count, mail_size = p.stat()
        if mail_count:
            resp, items, octets = p.list()
            latest_id = items[-1].split()[0]

            response, lines, octets = p.retr(latest_id)

            for mailline in lines:
                speak_the_sentence("You have received a new message.")
                if mailline.startswith("From: "):
                    speak_the_sentence(mailline)
                if mailline.startswith("Subject: "):
                    speak_the_sentence(mailline)
                if mailline.startswith("<div"):
                    speak_the_sentence("The mail contents are.")
                    mesg_start = lines.index(mailline)
                    new_hlist = list()
                    if mesg_start:
                        new_hlist = lines[mesg_start:-2]

                        content_html = " ".join(new_hlist)
                        soup = BeautifulSoup(content_html)
                        speak_the_sentence(soup.get_text())
                    break

    finally:
        p.quit()


if __name__ == '__main__':
    while True:
        read_new_mail()
        time.sleep(10)
