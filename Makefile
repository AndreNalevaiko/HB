VERSION = 1.0.5
CONTAINER_NAME = landing_page
IMAGE_NAME = gorillas/$(CONTAINER_NAME)

build_prod:
	docker build -t $(IMAGE_NAME):$(VERSION) --rm .

build_develop:
	docker build -t $(IMAGE_NAME):develop --rm .

push: build_prod
	git push --all
	git push --tags
	docker tag $(IMAGE_NAME):$(VERSION) docker.gorillascode.com/$(IMAGE_NAME):$(VERSION)
	docker tag $(IMAGE_NAME):$(VERSION) docker.gorillascode.com/$(IMAGE_NAME):latest
	docker push docker.gorillascode.com/$(IMAGE_NAME):$(VERSION)
	docker push docker.gorillascode.com/$(IMAGE_NAME):latest

push_develop: build_develop
	docker tag $(IMAGE_NAME):develop docker.gorillascode.com/$(IMAGE_NAME):develop
	docker push docker.gorillascode.com/$(IMAGE_NAME):develop