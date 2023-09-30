from direnumerate import PayLoad

url = "testphp.vulnweb.com/login.php"

pl = PayLoad(url)
pl.start_inject(verbose=True, rocket5=True, term="name")

