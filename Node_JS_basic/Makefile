.PHONY: test lint full-test

# Run the tests
test:
	docker exec -it nodejs-container npm run test

# Run the full tests
full-test:
	docker exec -it nodejs-container npm run full-test

# Run the linter
lint:
	docker exec -it nodejs-container npm run lint

# build the docker image
build:
	docker build --no-cache -t nodejs-image .

# Run the docker container
run:
	docker run -d -t --name nodejs-container -p 1245:1245 nodejs-image

# Start the docker container
start:
	docker start nodejs-container

# Stop the docker container
stop:
	docker stop nodejs-container

# Copy files to the running container
copy:
	docker cp . nodejs-container:/app

# Copy file 0-console.js to the running container
copy-0:
	docker cp 0-console.js nodejs-container:/app

# Copy file 1-stdin.js to the running container
copy-1:
	docker cp 1-stdin.js nodejs-container:/app

# Copy file 2-read_file.js to the running container
copy-2:
	docker cp 2-read_file.js nodejs-container:/app

# Copy file 3-read_file_async.js to the running container
copy-3:
	docker cp 3-read_file_async.js nodejs-container:/app

# Copy file 4-http.js to the running container
copy-4:
	docker cp 4-http.js nodejs-container:/app

# Copy file 5-http.js to the running container
copy-5:
	docker cp 5-http.js nodejs-container:/app

# Copy file 6-http_express.js to the running container
copy-6:
	docker cp 6-http_express.js nodejs-container:/app

# Copy file 7-http_express.js to the running container
copy-7:
	docker cp 7-http_express.js nodejs-container:/app

# Install dependencies in the running container
install:
	docker exec -it nodejs-container npm install

# Shell into the running container
shell:
	docker exec -it nodejs-container /bin/bash

# Run a script in the running container
task-0:
	docker exec -it nodejs-container node 0-console.js

# Run task 1
task-1:
	docker exec -it nodejs-container node 1-stdin.js

# Run task 2
task-2:
	docker exec -it nodejs-container node 2-read_file.js

# Run task 3
task-3:
	docker exec -it nodejs-container node 3-read_file_async.js

# Run task 4
task-4:
	docker exec -it nodejs-container node 4-http.js

# Run task 5
task-5:
	docker exec -it nodejs-container node 5-http.js

# Run task 6
task-6:
	docker exec -it nodejs-container node 6-http_express.js

# Run task 7
task-7:
	docker exec -it nodejs-container node 7-http_express.js
