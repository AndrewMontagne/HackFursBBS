.PHONY: build-container sh

sh: build-container
	-docker rm -f hackfursbbs
	docker run -it --rm --mount type=bind,source=$(PWD),target=/app -p2022:2022 --name hackfursbbs andrewmontagne/hackfursbbs

build-container:
	docker build . -t andrewmontagne/hackfursbbs
