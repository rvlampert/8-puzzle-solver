run:
	@echo "--> Running"
	@python3 main.py $(board)

install-dependencies:
	@echo "--> Installing Python dependencies"
	@pip install -r requirements.txt