#20192827 김민재
print("20192827 김민재\n")

from file_write import *
from time_module import *
from tweepy_module import *
from wantpassword_module import *


a = (str(time1()) + "/" + "a temporary password: " + Wantpassword() + "  "+ "/20192827/kim min jae\n")
write(a)
send_to_twitter(a)





