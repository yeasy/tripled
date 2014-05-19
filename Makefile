TRIPLED = tripled/*.py
TEST = test/*.py
BIN = bin/tripled
PYSRC = $(TRIPLED) $(TEST) $(BIN)
MANPAGES = tripled.1
P8IGN = E251,E201,E302,E202
BINDIR = /usr/bin
MANDIR = /usr/share/man/man1
DOCDIRS = doc/html doc/latex
PDF = doc/latex/refman.pdf

CFLAGS += -Wall -Wextra

all: codecheck test

clean:
	rm -rf build dist *.egg-info *.pyc $(MANPAGES) $(DOCDIRS)

codecheck: $(PYSRC)
	-echo "Running code check"
	util/versioncheck.py
	pyflakes $(PYSRC)
	pylint --rcfile=.pylint $(PYSRC)
	pep8 --repeat --ignore=$(P8IGN) $(PYSRC)

errcheck: $(PYSRC)
	-echo "Running check for errors only"
	pyflakes $(PYSRC)
	pylint -E --rcfile=.pylint $(PYSRC)

test: $(TRIPLED) $(TEST)
	-echo "Running tests"

#install: $(MANPAGES)
install:
	#install $(MANPAGES) $(MANDIR)
	python setup.py install

develop: $(MANPAGES)
	# Perhaps we should link these as well
	install $(MANPAGES) $(MANDIR)
	python setup.py develop

man: $(MANPAGES)

tripled.1: $(BIN)
	PYTHONPATH=. help2man -N -n "Easy OpenvSwitch Bridge Operation Platform." $< -o $@

.PHONY: doc

doc: man
	doxygen doc/doxygen.cfg
	make -C doc/latex
