push:
	git add -A ; git commit -am. ; git push
pull:
	git pull
html:
	cd doc/source/apidoc ; make apidoc ; cd ../.. ; make html
open:
	open doc/build/html/index.html
