# arrayinfo

array 및 tensor의 manipulation 팁을 담은 저장소입니다.

## DB 기여 예시

아래와 같은 명령어를 사용하여 DB에 접속하여 정보를 추가할 수 있습니다.

![image](https://user-images.githubusercontent.com/38157496/124503341-53aac980-de00-11eb-9498-301b05ffcc14.png)

### 명령어 일람

```
--action : 어떤 행동(CRUD)을 할지에 대해 입력 (예 : --action ct)

ct : 테이블 생성
cr : 레코드 생성 (사전 조건 : 테이블이 먼저 생성되어야 함)
rr : 레코드 조회
dr : 레코드 삭제

--lib_name : 라이브러리 이름 (예 : 'mxnet')

--db_tool : 데이터베이스 이름 (기본값 :sqlite, 이 인자값은 생략되어도 무방함. 추후 타 DB 플랫폼 적용시 입력될 수 있음)

--idx : 인덱스 숫자 (레코드 추가시 생략을 권장함.)

--f_name : 함수 이름 (예 : "'torch.zeros()'")

--f_info : 함수 정보 (예 : "'모든 요소가 0으로 설정된 텐서를 만듭니다.'")

--del_all : 전체 삭제 : (기본 : None), 숫자, 혹은 문자열 입력시 삭제됨
```

### 테이블 추가 (예: mxnet이라는 라이브러리 테이블 추가)

`python CRUD.py --action ct --lib_name 'mxnet'`

---

### 레코드 추가 (예: mxnet에 다음과 같은 정보 추가)

- 문자를 입력할때는 큰따옴표-작은따옴표 순으로 입력되어야 합니다!

`python CRUD.py --action cr --lib_name 'mxnet' --f_name "'테스트입니다'" --f_info "'안녕하세요'"`

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

- **주의: 본 명령어는 이슈, PR 등 관리자의 승인을 받은 후 사용해주세요.**

![image](https://user-images.githubusercontent.com/38157496/124503838-493cff80-de01-11eb-9852-eb70b5f27acd.png)
