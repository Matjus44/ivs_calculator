.PHONY: run clean all pack profile help test

run:
	python3 -m calc.py

clean:
	rm -rf *.pyc

test:
	python3 -m mathlib_test.py

profile:
	python profiling.py

data_profile:
	@read filename; \
	cat $$filename | python profiling.py

doc:
	rm -rf ../doc
	mkdir ../doc
	cd ../doc && doxygen ../src/Doxyfile