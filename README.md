# arrayinfo
array 및 tensor의 manipulation 팁을 담은 저장소입니다.


## DB 기여 예시

아래와 같은 명령어를 사용하여 DB에 접속하여 정보를 추가할 수 있습니다.

![image](https://user-images.githubusercontent.com/38157496/124503341-53aac980-de00-11eb-9498-301b05ffcc14.png)

### 테이블 추가 (예: mxnet이라는 라이브러리 테이블 추가)
`python CRUD.py --action ct --lib_name 'mxnet'`

---

### 레코드 추가 (예: mxnex의 1번 인덱스에 다음과 같은 정보 추가)

- 문자를 입력할때는 큰따옴표-작은따옴표 순으로 입력되어야 합니다!

`python CRUD.py --action cr --lib_name 'mxnet' --idx 1 --f_name "'테스트입니다'" --f_info "'안녕하세요'"`

![image](https://user-images.githubusercontent.com/38157496/124503462-940a4780-de00-11eb-8989-154bca85fc8b.png)

---

### 레코드 조회 (예 : mxnet 테이블의 레코드를 터미널에서 조회)

`python CRUD.py --action rr --lib_name 'mxnet'`

![image](https://user-images.githubusercontent.com/38157496/124503770-2dd1f480-de01-11eb-97b2-02e87884ebcb.png)

---

### 레코드 삭제

- 1번 index를 가진 레코드 삭제

`python CRUD.py --action dr --lib_name 'mxnet' --idx 1`

![image](https://user-images.githubusercontent.com/38157496/124503660-f8c5a200-de00-11eb-8860-9a90468f8510.png)


- 전체 삭제

`python CRUD.py --action dr --lib_name 'mxnet' --del_all 'y'`

- 주의: 본 명령어는 이슈, PR 등 관리자의 승인을 받은 후 사용해주세요.

![image](https://user-images.githubusercontent.com/38157496/124503838-493cff80-de01-11eb-9852-eb70b5f27acd.png)


