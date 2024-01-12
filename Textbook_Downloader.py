website = 'website URL '
accont = 'your accont'
password = 'your password'
destDir = 'your destnition to download files'

with open('.credential/website') as wb:
    website = wb.readline()

with open('.credential/accont') as ac:
    accont = ac.readline()

with open('.credential/password') as pw:
    password = pw.readline()

with open('.credential/destDir') as dd:
    destDir = dd.readline()
