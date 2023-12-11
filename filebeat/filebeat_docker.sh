#!/bin/bash
docker run -d --name filebeat_backend \
--user=root \
-v $(pwd)/filebeat.docker.yml:/usr/share/filebeat/filebeat.yml:ro \
-v backend_logs:/var/log/dmp-networks-dataset-api \
-v /var/lib/docker/containers:/var/lib/docker/containers:ro \
-v /var/run/docker.sock:/var/run/docker.sock:ro \
docker.elastic.co/beats/filebeat:7.2.1