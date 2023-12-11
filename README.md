# 요약
## Fastapi Backend with Filebeat (Sidecar Designed)
(2023.12.11 작성 중..)
### Abstract
작성중...
### Fastapi

### filebeat
- ELK Stack의 대표적인 로그 수집기. logstash 또는 Elasticsearch에 전송.
- file 단위로 수집하며 거의 즉각적으로 변화를 감지.
- 매우 가벼우나, parsing 등은 logstash로 전송하여 처리
- Application 단과 sidecar pattern으로 연결되는 구조가 선호됨.

### 실행방법  
1. 이전에 배포된 volume이 없을 때, docker volume create backend_logs
2. docker compose up --build -d
3. docker compose logs -f 를 통해 logstash 또는 Elastic Search와의 연결과정을 확인
