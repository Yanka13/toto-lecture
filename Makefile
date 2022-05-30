install:
	@pip install -e .


github:
	@git add . && git commit --m "ok" && git push origin master
