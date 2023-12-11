# 요약
## dmp_dataset_api
### Dataset API System Flow
Dataset API는 각 고객사별 유저를 인증하기 위해 API key, CORS와 User info를 활용합니다.

- API KEY: api-key는 고객사별로 유니크한 값으로 발급되며, DMP 관리자가 생성합니다. api-key는 api 요청 시 HTTP 헤더에 포함되어야 합니다.
- CORS: CORS는 서버가 리소스에 액세스할 수 있는 사용자(즉, origin)를 지정할 수 있는 메커니즘으로, 고객사 별 domain을 origin으로 저장합니다. api 사용자는 api 요청 시 origin을 HTTP 헤더에 포함시켜 요청을 보내야 하며, Dataset API는 api-key와 쌍으로 존재하는 origin인지 검사한 후 이상이 없을 경우 인증되어 결과를 전달합니다.
- USER INFO: user-info는 각 고객사별 유저를 구분할 수 있는 key 값 혹은 hash 값으로 암호화하여 api 요청 시 파라미터에 포함되어야 합니다. 필요한 목적은 고객사별로 api에 접근하는 고객이 이상인지 아닌지 검사하기 위함입니다.

전체 System Flow는 다음과 같습니다. 
1. 초기 고객사에서 API KEY 생성 요청 
2. DMP-Master(관리자)가 API KEY 생성 (master access Controller) 
3. 고객사의 애플리케이션은 API KEY(HTTP 헤더), origin(HTTP 헤더), user info(파라미터)와 함께 post 요청
4. DatasetAPI 미들웨어에서 origin 및 API KEY 불일치 시 deny 
5. req, res에 관한 로그는 별도 디렉토리에 저장 

이런식의 엄격한 auth을 적용하는 이유는 다음과 같습니다. 
- Origin, API-Key를 사용함으로써 엄격한 Whitelist 설정. 타 회사의 도용을 방지 가능. (Origin Whitelist가 사용 유저 자체를 제한하는 방식이라 API-Key의 낮은 보안성을 보완) 
- 고객사는 개인정보를 직접 제공할 필요가 없으며, DMP-Networks는 암호화된 user-info만을 관리합니다. 추후 사용량 상호 검증 시에는 암호화된 값을 전달하면 고객사 측에서 암호화된 값을 해석하여 API-Key 유출 탐지 또는 비정상 사용 유저를 추정할 수 있습니다. 
- API-Key 유출 의심 시, DMP 관리자 단에서 손쉽게 api-key를 재발급하여 차단할 수 있습니다. 

### 구조 특징
- Python FastAPI 기반 백엔드 프레임워크. Gunicorn으로 worker process 다중 생성.
- middleware 단에서 request header의 origin, apikey(Authorization) valid. invalid 할 경우 거부 (CORS 및 Authorization)
- 클라이언트 용 Controller는 모두 post 기반. (/dmp_dataset_api/project/routers/dataset_api_query.py => 최종 라우터 엔드포인트)
- API는 ORM 없이 쿼리에 바로 포매팅
- 로그는 접근 성공/거부로 나눠서 저장. log 사용량으로 값을 매기므로 디테일하게 저장. (access.log는 Controller 단에서 기록, denied.log는 middleware 단에서 기록)
- master(관리자)용으로 api-key를 생성, 편집 삭제하기 위해 따로 backdoor 마련. (/dmp_dataset_api/project/routers/master_access.py 참고)

## filebeat
- ELK Stack의 대표적인 로그 수집기. logstash 또는 Elasticsearch에 전송.
- file 단위로 수집하며 거의 즉각적으로 변화를 감지.
- 매우 가벼우나, parsing 등은 logstash로 전송하여 처리
- Application 단과 sidecar pattern으로 연결되는 구조가 선호됨.

## 실행방법  
1. 이전에 배포된 volume이 없을 때, docker volume create datasetapi_log
2. docker compose up --build -d
3. docker compose logs -f 를 통해 logstash 또는 Elastic Search와의 연결과정을 확인
