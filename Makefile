##
##
SRC:=$(shell pwd)/src

help: # show help
	@echo ""
	@grep "^##" $(MAKEFILE_LIST) | grep -v grep
	@echo ""
	@grep "^[0-9a-zA-Z\-]*:" $(MAKEFILE_LIST) | grep -v grep
	@echo ""

build: clean # make jar
	ant

clean: # clean
	find src -iname *.class | xargs -n 1 rm -frv
	ant clean

run: # Run texture-packer with jython
	jython -Dpython.path=$(SRC):lib/x.jar -c "import main; main.main()"

test: # Run unittest
	jython -Dpython.path=lib/x.jar:src -m unittest discover
