# 실행방법  
1. build_by_docker.sh를 "sh build_by_docker"로 실행해서 docker image 생성 (초기 1번만)
2. 1번이 완료된 후에 run_by_docker.sh에서 '현재 서버에 열려있는 포트':8080으로 문장 수정. "sh run_by_docker"로 실행하면 image기반 container 생성되고 서버에 자동으로 띄어지게 됨
3. "서버 host ip:열려있는 포트/docs"로 인터넷 접속하면 api 결과 쉽게 확인이 가능하고 다운도 받을 수 있음.
