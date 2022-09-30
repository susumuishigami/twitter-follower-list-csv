fmt:
	black get_follower.py
	isort get_follower.py
	@printf "\e[32;1mfmt ok\e[m\n"

lint:
	black --check get_follower.py
	isort --check-only get_follower.py
	flake8 get_follower.py
	mypy get_follower.py
	@printf "\e[32;1mlint ok\e[m\n"

pip:
	pip install -r requirements-dev.txt -c requirements.lock
