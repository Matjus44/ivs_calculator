

.PHONY: run clean all pack profile help test
TEAM_NAME = xhuska03_xjanek05_xgorc
run:
	python3 -m calc.py

clean:
	rm -rf *.pyc rm -rf __pycache__ ../doc ../../$(TEAM_NAME) doxygen_warn_logfile.log

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
	
pack:clean doc
	mkdir -p ../../$(TEAM_NAME)/doc && cp -a ../doc/. ../../$(TEAM_NAME)/doc
	mkdir -p ../../$(TEAM_NAME)/install && cp -a ../../install/install/. ../../$(TEAM_NAME)/install
	mkdir -p ../../$(TEAM_NAME)/repo &&  cp -a ../. ../../$(TEAM_NAME)/repo
	rm -rf ../../$(TEAM_NAME)/repo/doc ../../$(TEAM_NAME)/repo/venv
	rm -rf ../../$(TEAM_NAME)/repo/Pipfile ../../$(TEAM_NAME)/repo/Pipfile.lock
	rm -rf ../../$(TEAM_NAME)/repo/.idea  ../../$(TEAM_NAME)/repo/src/doxygen_warn_logfile.log
	cd ../.. && zip -qr $(TEAM_NAME).zip $(TEAM_NAME)