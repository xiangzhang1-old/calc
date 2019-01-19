push:
	git add -A ; git commit -am. ; git push
pull:
	git pull
html:
	cd doc ; make html
open:
	open doc/build/html/index.html
