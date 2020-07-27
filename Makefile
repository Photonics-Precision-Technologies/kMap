.SILENT: ;

setup:
	rm -rf venv build dist *.egg-info
	python -m venv venv

install: 
	pip install --upgrade pip
	python -m pip install -r requirements.txt
	python setup.py install

clean:
	rm -rf build dist *.egg-info *.log report.tar.gz

uninstall:
	rm -rf venv build dist *.egg-info
	find . -type d -name '__pycache__' -exec rm -r {} +

run:
	python -m map

test-all:
	python -m unittest discover

report:
	rm -f report.tar.gz report.tar
	tar -cf report.tar *.log 
	tar -rf report.tar -C ./map/config/ logging.ini settings.ini
	-python -m unittest discover 2> test_results.txt
	tar -rf report.tar test_results.txt
	gzip report.tar
	rm test_results.txt

# Pleae don't use unless you know what you are doing
freeze:
	pip freeze > requirements.txt

# Pleae don't use unless you know what you are doing
include-config:
	git update-index --no-skip-worktree map/config/*.ini
	git update-index --no-skip-worktree map/resources/misc/*.json

# Pleae don't use unless you know what you are doing
exclude-config:
	git update-index --skip-worktree map/config/*.ini
	git update-index --skip-worktree map/resources/misc/*.json

# Requires additional installs
generate-uml:
	pyreverse -o png -p Map ./map
	
help:
	echo 'Usage:'   
	echo '    make <command> [options]'
	echo 'Commands:'
	echo '    setup        Sets up a fresh virtual environment.'
	echo '    install      Installs necessary packages.'
	echo '    clean        Removes dist and build directories.'
	echo '    uninstall    Removes the virtual environment, dist, build and all __pycache__ directories.'
	echo '    run          Starts the application.'
	echo '    test-all     Runs all available tests.'