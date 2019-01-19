push:
	git add -A ; git commit -am. ; git push
pull:
	git pull
doc:
	cd doc ; make html
opendoc:
	open doc/build/html/index.html
