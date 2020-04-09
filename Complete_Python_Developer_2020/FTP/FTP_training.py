
from ftplib import FTP

ftp = FTP("ftp.dlptest.com")
ftp.login(user="dlpuser@dlptest.com", passwd ="SzMf7rTE4pCrf9dV286GuNe4N")
ftp.dir()