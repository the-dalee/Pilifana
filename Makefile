install:
	pip3 install . --upgrade

uninstall:
	pip3 uninstall pilifana

install-daemon: install
	cp scripts/init.d/pilifana /etc/init.d/pilifana
	chmod 744 /etc/init.d/pilifana
	update-rc.d pilifana defaults
	update-rc.d pilifana enable
	/etc/init.d/pilifana start

uninstall-daemon:
	/etc/init.d/pilifana stop
	update-rc.d pilifana disable
	rm /etc/init.d/pilifana
