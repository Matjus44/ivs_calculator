.PHONY: all initialization pack clean test doc profile run install

all: initialization run
	chmod +x gui.py

initialization:
	sudo apt-get install python3-tk
	sudo apt-get install python3-pytest
	sudo apt-get install doxygen

profile:
	python3 profiling.py <../profiling/data.txt

run:
	python3 gui.py

test: mathlib_test.py
	pytest mathlib_test.py