# SQL 튜토리얼

SQL은 데이터베이스에 엑세스하기위한 표준 언어이다. 

<br/>
## SQL기본 알고가기
### SQL은..

- 구조화된 쿼리언어리다. 
- 데이터베이스에 액세스하고 조작할 수 있다. 
- ANSI 표준 언어이다.

--
### SQL은 무엇을 할 수 있을까..?

- 데이터베이스에 대해 쿼리를 실행할 수 있다. 
- 데이터를 검색할 수 있다. 
- 레코드를 삽입할 수 있다.
- 레코드를 업데이트할 수 있다. 
- 레코드를 삭제할 수 있다. 
- 새로운 테이블을 생성할 수 있다.
... 기타등등.

--
### 웹 사이트에서 SQL을 사용하려면,

- RDBMS데이터베이스 프로그램(ex/ MS access, SQL server, MySQL)
- PHP또는 ASP와 같은 서버측 스크립팅 언어를 사용하려면?
- SQL을 사용하여 원하는 데이터를 얻으려면?
- HTML / CSS를 사용하려면?

--
### RDBMS

RDBMS는 관계형 데이터베이스 관리 시스템의 약자이다.

RDBMS는 SQL과 MS SQL Server, IBM DB2, Oracle, MySQL 및,   
Microsoft Access와 같은 모든 최신 데이터베이스 시스템의 기초이다. 

RDBMS의 데이터는 테이블이라는 데이터베이스 오브젝트에 저장된다. 

테이블은 관련 데이터 항목의 모음이며, 열과 행으로 구성된다.

--
### 데이터베이스는 대개 하나 이상의 테이블(표)을 포한함다.   
각 테이블은 이름(열)으로 식별되고, 데이터가 있는 레코드(행)을 포함한다.

아래는 '지인'테이블의 내용이다. 
(모든 ex/는 이 테이블이 변경되어가는 내역으로 볼 예정이다)

<table>
  <tr>
    <td>번호</td>
    <td>분류</td>
    <td>이름</td>
    <td>성별</td>
    <td>생년월일</td>
    <td>전화번호</td> 
    <td>도시</td>   
  </tr>
  <tr>
    <td>1</td>  
    <td>웹 프로그래밍스쿨 학생</td>
    <td>서보람</td>
    <td>여자</td>   
    <td>1990.06.13</td>
    <td>010.</td>
    <td>안산</td>
  </tr>
  <tr>
    <td>2</td>  
    <td>프론트엔드 디자인 강사</td>
    <td>이^형</td>
    <td>남자</td>    
    <td>1982.06.17</td>
    <td>010.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>3</td>  
    <td>롤 하는 아이</td>
    <td>최@#</td>
    <td>여자</td>    
    <td>1990.07.07</td>
    <td>010.</td>
    <td>화성</td>
  </tr>
  <tr>
    <td>4</td>  
    <td>취준생</td>
    <td>$민#</td>
    <td>여자</td>    
    <td>1990.12.26</td>
    <td>010.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>5</td>  
    <td>군인</td>
    <td>#휘#</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>평택</td>    
  </tr>
    <tr>
    <td>6</td>    
    <td>공부중인 편돌이</td>
    <td>서#덕</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>7</td>  
    <td>직장인겸 예비신부</td>
    <td>서@!</td>
    <td>여자</td>    
    <td>1991.11.19</td>
    <td>011.</td>
    <td>안산</td>    
  </tr>    
</table>

위를 예로 들었을 때,

**7개의 레코드**(각 사람 당 하나)와, **7개의 열**(번호, 분류, 이름, 성별, 생년월일, 전화번호, 도시)이 들어있다고 말할 수 있다.

--

### 데이터베이스에서 수행해야하는 대부분은 SQL문으로 완료된다.  
> ex/ 

>```SQL
SELECT 이름 FROM 지인; 
   //- SELECT(선택한다.) 이름 FROM(에서) 지인;  
   //- 지인 테이블에서 이름을 선택한다.  
```   
   
>결과값

><table>
  <tr>
    <td>이름</td>
  </tr>
  <tr>
    <td>서보람</td>
  </tr>
  <tr>
    <td>이도형</td>
  </tr>
  <tr>
    <td>최@#</td>
  </tr>
  <tr>
    <td>$민#</td>
  </tr>
    <td>#휘#</td>
  </tr>
  <tr>
    <td>서#덕</td>
  </tr>
  <tr>
    <td>서@!</td>
  </tr>
</table>

--

- SQL은 대소문자를 구분하지 않는다. 
- 일부 데이터베이스 시스템에선 SQL문 끝에 ;(세미콜론)을 붙인다.
    + ;(세미콜론)은 데이터베이스 시스템에서 각 SQL문을 분리하여   
     서버에 대한 동일한 호출에서 둘 이상의 SQL문을 실행할 수 있도록 하는 표준 방법이다. 

--
<br/>
### 가장 중요한 SQL명령어중 일부   
 
SELECT - 데이터를 추출    
UPDATE - 데이터를 업데이트    
DELETE - 데이터를 삭제   
INSERT INTO - 새로운 데이터를 삽입   

CREATE DATABASE - 새 데이터베이스 생성    
ALTER DATABASE - 데이터베이스를 수정    

CREATE TABLE - 새로운 테이블 수정  
ALTER TABLE - 테이블을 수정  
DROP TABLE - 테이블 삭제  
  
CREATE INDEX - 인덱스(검색 키)를 생성  
DROP INDEX - 인덱스를 삭제  


<br/>
## SELECT문

데이터베이스에서 데이터를 선택하는데 사용된다. 
결과는 결과세트라고 하는 결과 테이블에 저장된다. 

>ex/ 

>```SQL
SELECT 이름, 성별 FROM 지인;   
   //- SELECT(선택한다.) 이름, 성별 FROM(에서) 지인;  
   //- 지인 테이블에서 이름과, 성별을 선택한다.  
```   
>결과값

><table>
  <tr>
    <td>이름</td>
    <td>성별</td>
  </tr>
  <tr>
    <td>서보람</td>
    <td>여자</td>
  </tr>
  <tr>
    <td>이도형</td>
    <td>남자</td>
  </tr>
  <tr>
    <td>최@#</td>
    <td>여자</td>
  </tr>
  <tr>
    <td>$민#</td>
    <td>여자</td>
  </tr>
    <td>#휘#</td>
    <td>남자</td>
  </tr>
  <tr>
    <td>서#덕</td>
    <td>남자</td>
  </tr>
  <tr>
    <td>서@!</td>
    <td>여자</td>
  </tr>
</table>


`SELECT * FROM 테이블명;` 은 테이블에서 모든 컬럼을 선택해서 보여준다.

<br/>
### SELECT DISTINCT 
테이블에서 열은 많은 중복값을 포함할 수 있다.   
중복되는 값을 제외하고 불러올 때 사용한다. 

>ex/ 

>```SQL
SELECT DISTINCT 도시 FROM 지인;  
  //- 중복되는 값을 제외하고 지인 테이블에서 도시를 불러온다.
```
>결과값

><table>
  <tr>
    <td>도시</td>
  </tr>
  <tr>
    <td>안산</td>
  </tr>
  <tr>
    <td>화성</td>
  </tr>
  <tr>
    <td>평택</td>
  </tr>
</table>

<br/>
### WHERE
지정된 기준을 충족하는 레코드만 불러와서 보여준다.

>ex/ 

>```SQL
SELECT * FROM 지인  
WHERE 성별='남자';  
  //- 지인 테이블에서 성별이 남자인 모든 사람을 불러와 보여준다. 
```

>결과값

><table>
  <tr>
    <td>번호</td>
    <td>분류</td>
    <td>이름</td>
    <td>성별</td>
    <td>생년월일</td>
    <td>전화번호</td> 
    <td>도시</td>   
  </tr>
  <tr>
    <td>2</td>  
    <td>프론트엔드 디자인 강사</td>
    <td>이^형</td>
    <td>남자</td>    
    <td>1982.06.17</td>
    <td>010.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>5</td>  
    <td>군인</td>
    <td>#휘#</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>평택</td>    
  </tr>
    <tr>
    <td>6</td>    
    <td>공부중인 편돌이</td>
    <td>서#덕</td>
    <td>남자</td>    
    <td>1982.06.17</td>
    <td>011.</td>
    <td>안산</td>    
  </tr>   
</table>

텍스트 값에는 ' '(작은 따옴표)를 사용해야한다. 
하지만 숫자는 따옴표로 감싸지 않는다. 

<br/>
**WHETE에서 사용할 수 있는 연산자 모음**
<table>
<tr>
  <td> Operator </td>
  <td> Desctoption </td>
</tr>
<tr>
  <td> = </td>
  <td> Equal </td>
</tr>
<tr>
  <td> < > </td>
  <td> Not equal. Note: in some versions of SQL this operator may be written as != </td>
</tr>
<tr>
  <td> > </td>
  <td> Greater than </td>
</tr>
<tr>
  <td> < </td>
  <td> less than </td>
</tr>
<tr>
  <td> >= </td>
  <td> Greater than or equal </td>
</tr>
<tr>
  <td> <= </td>
  <td> Less than or equal </td>
</tr>
<tr>
  <td> BETWEEN </td>
  <td> Between an inclusive range </td>
</tr>
<tr>
  <td> LIKE </td>
  <td> Search for a pattern </td>
</tr>
<tr>
  <td> IN </td>
  <td> To specify multiple possible values for a column </td>
</tr>
</table>


<br/>
## AND & OR 연산자
둘 이상의 조건에 따라 레코드를 필터링하는데 사용된다. 

AND - 첫 번째 조건과 두번째 조건이 **모두 참일 경우**의 레코드를 보여준다  
OR - 첫 번째 **또는** 두번째 조건이 참일 경우 레코드를 보여준다

<br/>
### 모두 참일 경우엔 `AND 연산자`
>ex/

>``` SQL
SELECT * FROM 지인   //- 지인 테이블에서 *(모두)선택한다.
WHERE 성별='남자'     //- 그 중에서 성별이 '남자'인 레코드를 추출한다.
AND 도시='안산';      //- 그 중에서 도시가 '안산'인 레코드를 추출한다.
```
<table>
  <tr>
    <td>번호</td>
    <td>분류</td>
    <td>이름</td>
    <td>성별</td>
    <td>생년월일</td>
    <td>전화번호</td> 
    <td>도시</td>   
  </tr>
  <tr>
    <td>2</td>
    <td>프론트엔드 디자인 강사</td>
    <td>이^형</td>
    <td>남자</td>    
    <td>1982.06.17</td>
    <td>010.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>6</td>  
    <td>공부중인 편돌이</td>
    <td>서#덕</td>
    <td>남자</td>    
    <td>1982.06.17</td>
    <td>011.</td>
    <td>안산</td>    
  </tr>
</table>

<br/>
### 첫번째 또는 두번째가 참일 경우엔 `OR 연산자`
>ex/

>```SQL
SELECT * FROM 지인   //- 지인 테이블에서 *(모두)를 선택한다.
WHERE 도시='평택'     //- 그 중에서 도시가 '평택'인 레코드를 추출한다. 
OR 도시='화성'        //- 또는 도시가 '화성'인 레코드를 추출한다.
```
 
><table>
  <tr>
    <td>번호</td>
    <td>분류</td>
    <td>이름</td>
    <td>성별</td>
    <td>생년월일</td>
    <td>전화번호</td> 
    <td>도시</td>   
  </tr>
  <tr>
    <td>5</td>
    <td>군인</td>
    <td>#휘#</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>평택</td>    
  </tr>
  <tr>
    <td>3</td>  
    <td>롤 하는 아이</td>
    <td>최@#</td>
    <td>여자</td>    
    <td>1990.07.07</td>
    <td>011.</td>
    <td>화성</td>
  </tr>
</table>

<br/>
### AND AND OR
AND와 OR를 결합해서 사용할 수 있다.
()(괄호)를 사용해서 복잡한 표현식을 형성할 수도 있다.

>ex/

>```SQL
SELECT * FROM 지인   //- 지인 테이블을 모두 선택한다  
WHERE 성별='여자'     //- 그 중에서 성별이 여자인 레코드를 추출한다.
AND (번호=7 OR 전화번호=010.);  
                   //- 그 중에서 (번호가 7이거나, 전화번호가 010.인 레코드를 추출한다.)
```
><table>
  <tr>
    <td>번호</td>
    <td>분류</td>
    <td>이름</td>
    <td>성별</td>
    <td>생년월일</td>
    <td>전화번호</td> 
    <td>도시</td>   
  </tr>
  <tr>
    <td>1</td>  
    <td>웹 프로그래밍스쿨 학생</td>
    <td>서보람</td>
    <td>여자</td>   
    <td>1990.06.13</td>
    <td>010.</td>
    <td>안산</td>
  </tr>
  <tr>
    <td>7</td>  
    <td>직장인겸 예비신부</td>
    <td>서@!</td>
    <td>여자</td>    
    <td>1991.11.19</td>
    <td>011.</td>
    <td>안산</td>    
  </tr>    
</table>



<br/>
## 결과 집합을 정렬하는데엔 `ORDER BY`
하나 이상의 열을 기준으로 결과 집합을 정렬하는데 사용된다.  
기본적으로 오름차순으로 정렬한다.  
내림차순으로 정렬하려면 `DESC`키워드를 사용한다.  

```SQL
SELECT FROM 
ORFER BY ADC|DESC, ASC|DESC;
```

<br/>
### 정렬시키는 `ORDER BY`
>ex/

>```SQL
SELECT * FROM 지인 
ORFER BY 번호;
```
><table>
  <tr>
    <td>번호</td>
    <td>분류</td>
    <td>이름</td>
    <td>성별</td>
    <td>생년월일</td>
    <td>전화번호</td> 
    <td>도시</td>   
  </tr>
  <tr>
    <td>1</td>  
    <td>웹 프로그래밍스쿨 학생</td>
    <td>서보람</td>
    <td>여자</td>   
    <td>1990.06.13</td>
    <td>010.</td>
    <td>안산</td>
  </tr>
  <tr>
    <td>2</td>  
    <td>프론트엔드 디자인 강사</td>
    <td>이^형</td>
    <td>남자</td>    
    <td>1982.06.17</td>
    <td>010.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>3</td>  
    <td>롤 하는 아이</td>
    <td>최@#</td>
    <td>여자</td>    
    <td>1990.07.07</td>
    <td>010.</td>
    <td>화성</td>
  </tr>
  <tr>
    <td>4</td>  
    <td>취준생</td>
    <td>$민#</td>
    <td>여자</td>    
    <td>1990.12.26</td>
    <td>010.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>5</td>  
    <td>군인</td>
    <td>#휘#</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>평택</td>    
  </tr>
    <tr>
    <td>6</td>    
    <td>공부중인 편돌이</td>
    <td>서#덕</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>7</td>  
    <td>직장인겸 예비신부</td>
    <td>서@!</td>
    <td>여자</td>    
    <td>1991.11.19</td>
    <td>011.</td>
    <td>안산</td>    
  </tr>    
</table>


<br/>
### 내림차순 정렬 `DESC`
>ex/

>```SQL
SELECT * FROM 지인 
ORFER BY 번호 DESC;
```

><table>
  <tr>
    <td>번호</td>
    <td>분류</td>
    <td>이름</td>
    <td>성별</td>
    <td>생년월일</td>
    <td>전화번호</td> 
    <td>도시</td>   
  </tr>
  <tr>
    <td>7</td>  
    <td>직장인겸 예비신부</td>
    <td>서@!</td>
    <td>여자</td>    
    <td>1991.11.19</td>
    <td>011.</td>
    <td>안산</td>    
  </tr>  
  <tr>
    <td>6</td>    
    <td>공부중인 편돌이</td>
    <td>서#덕</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>안산</td>    
  </tr>  
  <tr>
    <td>5</td>  
    <td>군인</td>
    <td>#휘#</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>평택</td>    
  </tr>
  <tr>
    <td>4</td>  
    <td>취준생</td>
    <td>$민#</td>
    <td>여자</td>    
    <td>1990.12.26</td>
    <td>010.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>3</td>  
    <td>롤 하는 아이</td>
    <td>최@#</td>
    <td>여자</td>    
    <td>1990.07.07</td>
    <td>010.</td>
    <td>화성</td>
  </tr>
  <tr>
    <td>2</td>  
    <td>프론트엔드 디자인 강사</td>
    <td>이^형</td>
    <td>남자</td>    
    <td>1982.06.17</td>
    <td>010.</td>
    <td>안산</td>    
  </tr>      
  <tr>
    <td>1</td>  
    <td>웹 프로그래밍스쿨 학생</td>
    <td>서보람</td>
    <td>여자</td>   
    <td>1990.06.13</td>
    <td>010.</td>
    <td>안산</td>
  </tr>
</table>

<br/>
### 두 가지를 기준으로 정렬하기
>ex/

>```SQL
SELECT * FROM 지인
ORDERBY 전화번호, 생년월일; 
//- 전화번호가 겹치면 생년월일을 기준으로 또 정렬해준다
```

><table>
  <tr>
    <td>번호</td>
    <td>분류</td>
    <td>이름</td>
    <td>성별</td>
    <td>생년월일</td>
    <td>전화번호</td> 
    <td>도시</td>   
  </tr>
  <tr>
    <td>2</td>  
    <td>프론트엔드 디자인 강사</td>
    <td>이^형</td>
    <td>남자</td>    
    <td>1982.06.17</td>
    <td>010.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>1</td>  
    <td>웹 프로그래밍스쿨 학생</td>
    <td>서보람</td>
    <td>여자</td>   
    <td>1990.06.13</td>
    <td>010.</td>
    <td>안산</td>
  </tr>
  <tr>
    <td>3</td>  
    <td>롤 하는 아이</td>
    <td>최@#</td>
    <td>여자</td>    
    <td>1990.07.07</td>
    <td>010.</td>
    <td>화성</td>
  </tr>
  <tr>
    <td>4</td>  
    <td>취준생</td>
    <td>$민#</td>
    <td>여자</td>    
    <td>1990.12.26</td>
    <td>010.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>7</td>  
    <td>직장인겸 예비신부</td>
    <td>서@!</td>
    <td>여자</td>    
    <td>1991.11.19</td>
    <td>011.</td>
    <td>안산</td>    
  </tr>    
  <tr>
    <td>5</td>  
    <td>군인</td>
    <td>#휘#</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>평택</td>    
  </tr>
    <tr>
    <td>6</td>    
    <td>공부중인 편돌이</td>
    <td>서#덕</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>안산</td>    
  </tr>          
</table>

<br/>
### 하나의 기준은 오름차순, 나머지 하나는 내림차순으로 정렬하기
>ex/

>```SQL
SELECT * FROM 지인
ORDERBY 전화번호 ASC, 생년월일 DESC;
//- 전화번호는 오름차순 정렬, 생년월일은 내림차순 정렬해준다
```

><table>
  <tr>
    <td>번호</td>
    <td>분류</td>
    <td>이름</td>
    <td>성별</td>
    <td>생년월일</td>
    <td>전화번호</td> 
    <td>도시</td>   
  </tr>
  <tr>
    <td>4</td>  
    <td>취준생</td>
    <td>$민#</td>
    <td>여자</td>    
    <td>1990.12.26</td>
    <td>010.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>3</td>  
    <td>롤 하는 아이</td>
    <td>최@#</td>
    <td>여자</td>    
    <td>1990.07.07</td>
    <td>010.</td>
    <td>화성</td>
  </tr>
  <tr>
    <td>1</td>  
    <td>웹 프로그래밍스쿨 학생</td>
    <td>서보람</td>
    <td>여자</td>   
    <td>1990.06.13</td>
    <td>010.</td>
    <td>안산</td>
  </tr>  
  <tr>
    <td>2</td>  
    <td>프론트엔드 디자인 강사</td>
    <td>이^형</td>
    <td>남자</td>    
    <td>1982.06.17</td>
    <td>010.</td>
    <td>안산</td>    
  </tr>  
  <tr>
    <td>7</td>  
    <td>직장인겸 예비신부</td>
    <td>서@!</td>
    <td>여자</td>    
    <td>1991.11.19</td>
    <td>011.</td>
    <td>안산</td>    
  </tr>  
  <tr>
    <td>5</td>  
    <td>군인</td>
    <td>#휘#</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>평택</td>    
  </tr>
    <tr>
    <td>6</td>    
    <td>공부중인 편돌이</td>
    <td>서#덕</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>안산</td>    
  </tr>     
</table>

<br/>
## INSERT INTO문
테이블에 새 레코드를 삽입하는데에 사용한다

두 가지 형식으로 INSERT INTO문을 작성할 수 있다. 

- 데이터가 삽입될 열 이름을 지정하지 않고 값만 지정한다. 
    
    ```SQL
    INDERT INTO 테이블이름
    VALUES (값2, 값2, 값3, ...);
    ```
- 열 이름과 삽입할 값을 모두 지정한다. 
    
    ```SQL
    INDERT INTO 테이블이름(컬럼1, 컬럼2, 컬럼3, ...)
    VALUES (값2, 값2, 값3 ...);
    ```

<br/>
###데이터가 삽입될 열 이름을 지정하지 않고 값만 지정하는 경우
>ex/ 

>```SQL
INSERT INTO 지인 (분류, 이름, 성별, 생년월일,전화번호, 도시)
VALUES ('사랑해 유자','최유!', '여자', '1990,12,08', '012.', '기억안나')
//- 지인 테이블에 레코드 한 줄 생성함. 
    모든 열에대한 항목을 나열하고 그에 대한 값을 기입한다. 
```
><table>
  <tr>
    <td>번호</td>
    <td>분류</td>
    <td>이름</td>
    <td>성별</td>
    <td>생년월일</td>
    <td>전화번호</td> 
    <td>도시</td>   
  </tr>
  <tr>
    <td>1</td>  
    <td>웹 프로그래밍스쿨 학생</td>
    <td>서보람</td>
    <td>여자</td>   
    <td>1990.06.13</td>
    <td>010.</td>
    <td>안산</td>
  </tr>
  <tr>
    <td>2</td>  
    <td>프론트엔드 디자인 강사</td>
    <td>이^형</td>
    <td>남자</td>    
    <td>1982.06.17</td>
    <td>010.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>3</td>  
    <td>롤 하는 아이</td>
    <td>최@#</td>
    <td>여자</td>    
    <td>1990.07.07</td>
    <td>010.</td>
    <td>화성</td>
  </tr>
  <tr>
    <td>4</td>  
    <td>취준생</td>
    <td>$민#</td>
    <td>여자</td>    
    <td>1990.12.26</td>
    <td>010.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>5</td>  
    <td>군인</td>
    <td>#휘#</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>평택</td>    
  </tr>
    <tr>
    <td>6</td>    
    <td>공부중인 편돌이</td>
    <td>서#덕</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>7</td>  
    <td>직장인겸 예비신부</td>
    <td>서@!</td>
    <td>여자</td>    
    <td>1991.11.19</td>
    <td>011.</td>
    <td>안산</td>    
  </tr>    
  <tr>
    <td>8</td>  
    <td>사랑해 유자</td>
    <td>최유!</td>
    <td>여자</td>    
    <td>1990.11.08</td>
    <td>012.</td>
    <td>기억안나</td>    
  </tr>
</table>

번호 필드에는 따로 숫자를 지정하지 않아도 각 레코드레 고유 번호로 자동 업뎃된다

<br/>
###열 이름과 삽입할 값을 모두 지정한다.
>ex/ 

>```SQL
INSERT INTO 지인 (분류, 이름, 생년월일)
VALUES ('사랑해 유자','최유!', '1990,12,08')
//- 지인 테이블에 레코드 한 줄 생성함. 적어넣을 열을 나열하고, 그에 대한 값을 기입한다.
```
><table>
  <tr>
    <td>번호</td>
    <td>분류</td>
    <td>이름</td>
    <td>성별</td>
    <td>생년월일</td>
    <td>전화번호</td> 
    <td>도시</td>   
  </tr>
  <tr>
    <td>1</td>  
    <td>웹 프로그래밍스쿨 학생</td>
    <td>서보람</td>
    <td>여자</td>   
    <td>1990.06.13</td>
    <td>010.</td>
    <td>안산</td>
  </tr>
  <tr>
    <td>2</td>  
    <td>프론트엔드 디자인 강사</td>
    <td>이^형</td>
    <td>남자</td>    
    <td>1982.06.17</td>
    <td>010.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>3</td>  
    <td>롤 하는 아이</td>
    <td>최@#</td>
    <td>여자</td>    
    <td>1990.07.07</td>
    <td>010.</td>
    <td>화성</td>
  </tr>
  <tr>
    <td>4</td>  
    <td>취준생</td>
    <td>$민#</td>
    <td>여자</td>    
    <td>1990.12.26</td>
    <td>010.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>5</td>  
    <td>군인</td>
    <td>#휘#</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>평택</td>    
  </tr>
    <tr>
    <td>6</td>    
    <td>공부중인 편돌이</td>
    <td>서#덕</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>7</td>  
    <td>직장인겸 예비신부</td>
    <td>서@!</td>
    <td>여자</td>    
    <td>1991.11.19</td>
    <td>011.</td>
    <td>안산</td>    
  </tr>    
  <tr>
    <td>8</td>  
    <td>사랑해 유자</td>
    <td>최유!</td>
    <td>null</td>    
    <td>1990.11.08</td>
    <td>null</td>
    <td>null</td>    
  </tr>
</table>



<br/>
## UPDATE
기존 레코드를 업데이트하는데 사용된다.   
(ex/는 갱신한 내용으로 이어간다.)

```SQL
UPDATE 테이블이름
SET 열1=값1, 열2=값2,...
WHERE 어떤 열에=어떤 값을 가진 레코드를 변경시키겠다;
```
<br/>
###'여러 열'을 업뎃할때
>ex/ 

>```SQL
UPDATE 지인
SET 성별='여자', 도시='안양'  
    //- 성별, 도시 두 개의 열을 '여자', '안양'의 값을 줘서 기존에 있던 값을 변경한다.
WHERE 번호=8;  
    //- 갱신할 레코드를 지정한다. 이걸 생략하면 모든 레코드가 업뎃된다.
```
><table>
  <tr>
    <td>번호</td>
    <td>분류</td>
    <td>이름</td>
    <td>성별</td>
    <td>생년월일</td>
    <td>전화번호</td> 
    <td>도시</td>   
  </tr>
  <tr>
    <td>1</td>  
    <td>웹 프로그래밍스쿨 학생</td>
    <td>서보람</td>
    <td>여자</td>   
    <td>1990.06.13</td>
    <td>010.</td>
    <td>안산</td>
  </tr>
  <tr>
    <td>2</td>  
    <td>프론트엔드 디자인 강사</td>
    <td>이^형</td>
    <td>남자</td>    
    <td>1982.06.17</td>
    <td>010.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>3</td>  
    <td>롤 하는 아이</td>
    <td>최@#</td>
    <td>여자</td>    
    <td>1990.07.07</td>
    <td>010.</td>
    <td>화성</td>
  </tr>
  <tr>
    <td>4</td>  
    <td>취준생</td>
    <td>$민#</td>
    <td>여자</td>    
    <td>1990.12.26</td>
    <td>010.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>5</td>  
    <td>군인</td>
    <td>#휘#</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>평택</td>    
  </tr>
    <tr>
    <td>6</td>    
    <td>공부중인 편돌이</td>
    <td>서#덕</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>7</td>  
    <td>직장인겸 예비신부</td>
    <td>서@!</td>
    <td>여자</td>    
    <td>1991.11.19</td>
    <td>011.</td>
    <td>안산</td>    
  </tr>    
  <tr>
    <td>8</td>  
    <td>사랑해 유자</td>
    <td>최유!</td>
    <td>여자</td>    
    <td>1990.11.08</td>
    <td>null</td>
    <td>안양</td>    
  </tr>
</table>
8번인 유자의 데이터가 바뀐 걸 알 수있다.

<br/>
###'여러 레코드'를 업뎃할때
>ex/ 

>```SQL
UPDATE 지인
SET 전화번호=018  
    //-  전화번호 열을 '018' 값을 줘서 기존에 있던 값을 변경한다.
WHERE 성별='여자';  
    //- 성별이 '여자'인 레코드를 가진 열은 모두 전화번호가 018이된다
```
><table>
  <tr>
    <td>번호</td>
    <td>분류</td>
    <td>이름</td>
    <td>성별</td>
    <td>생년월일</td>
    <td>전화번호</td> 
    <td>도시</td>   
  </tr>
  <tr>
    <td>1</td>  
    <td>웹 프로그래밍스쿨 학생</td>
    <td>서보람</td>
    <td>여자</td>   
    <td>1990.06.13</td>
    <td>018</td>
    <td>안산</td>
  </tr>
  <tr>
    <td>2</td>  
    <td>프론트엔드 디자인 강사</td>
    <td>이^형</td>
    <td>남자</td>    
    <td>1982.06.17</td>
    <td>010.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>3</td>  
    <td>롤 하는 아이</td>
    <td>최@#</td>
    <td>여자</td>    
    <td>1990.07.07</td>
    <td>018</td>
    <td>화성</td>
  </tr>
  <tr>
    <td>4</td>  
    <td>취준생</td>
    <td>$민#</td>
    <td>여자</td>    
    <td>1990.12.26</td>
    <td>018</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>5</td>  
    <td>군인</td>
    <td>#휘#</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>평택</td>    
  </tr>
    <tr>
    <td>6</td>    
    <td>공부중인 편돌이</td>
    <td>서#덕</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>7</td>  
    <td>직장인겸 예비신부</td>
    <td>서@!</td>
    <td>여자</td>    
    <td>1991.11.19</td>
    <td>018</td>
    <td>안산</td>    
  </tr>    
  <tr>
    <td>8</td>  
    <td>사랑해 유자</td>
    <td>최유!</td>
    <td>null</td>    
    <td>1990.11.08</td>
    <td>018</td>
    <td>null</td>    
  </tr>
</table>

<br/>
###모든 레코드를 업뎃할때 (이건 주의해서 사용할 것!)
>ex/ 

>```SQL
UPDATE 지인
SET 도시='부산'  
    //- 지인 테이블의, '도시' 열의 값을 모두 '부산'으로 갱신한다
```
><table>
  <tr>
    <td>번호</td>
    <td>분류</td>
    <td>이름</td>
    <td>성별</td>
    <td>생년월일</td>
    <td>전화번호</td> 
    <td>도시</td>   
  </tr>
  <tr>
    <td>1</td>  
    <td>웹 프로그래밍스쿨 학생</td>
    <td>서보람</td>
    <td>여자</td>   
    <td>1990.06.13</td>
    <td>010.</td>
    <td>부산</td>
  </tr>
  <tr>
    <td>2</td>  
    <td>프론트엔드 디자인 강사</td>
    <td>이^형</td>
    <td>남자</td>    
    <td>1982.06.17</td>
    <td>010.</td>
    <td>부산</td>    
  </tr>
  <tr>
    <td>3</td>  
    <td>롤 하는 아이</td>
    <td>최@#</td>
    <td>여자</td>    
    <td>1990.07.07</td>
    <td>010.</td>
    <td>부산</td>
  </tr>
  <tr>
    <td>4</td>  
    <td>취준생</td>
    <td>$민#</td>
    <td>여자</td>    
    <td>1990.12.26</td>
    <td>010.</td>
    <td>부산</td>    
  </tr>
  <tr>
    <td>5</td>  
    <td>군인</td>
    <td>#휘#</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>부산</td>    
  </tr>
    <tr>
    <td>6</td>    
    <td>공부중인 편돌이</td>
    <td>서#덕</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>부산</td>    
  </tr>
  <tr>
    <td>7</td>  
    <td>직장인겸 예비신부</td>
    <td>서@!</td>
    <td>여자</td>    
    <td>1991.11.19</td>
    <td>011.</td>
    <td>부산</td>    
  </tr>    
  <tr>
    <td>8</td>  
    <td>사랑해 유자</td>
    <td>최유!</td>
    <td>여자</td>    
    <td>1990.11.08</td>
    <td>null</td>
    <td>부산</td>    
  </tr>
</table>

<br/>
## DELETE

테이블의 레코드를 삭제하는 데 사용한다

```SQL
DELETE FROM 테이블 이름
WHERE 어떤 열의=어떤 값을 선택;
      //- WHERE는 삭제될 레코드를 지정한다. 이걸 생략하면 모든 레코드가 날아간다!! 주의!!
```

<br/>
###'어떤 레코드'를 삭제할 때
>ex/ 

>```SQL
DELETE FROM 지인
WHERE 분류='웹 프로그래밍 스쿨 학생' AND 이름='서보람';
     //- 지인 테이블에서 웹프스 학생으로 분류되고 이름이 서보람인 레코드를 삭제한다
```
><table>
  <tr>
    <td>번호</td>
    <td>분류</td>
    <td>이름</td>
    <td>성별</td>
    <td>생년월일</td>
    <td>전화번호</td> 
    <td>도시</td>   
  </tr>
  <tr>
    <td>2</td>  
    <td>프론트엔드 디자인 강사</td>
    <td>이^형</td>
    <td>남자</td>    
    <td>1982.06.17</td>
    <td>010.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>3</td>  
    <td>롤 하는 아이</td>
    <td>최@#</td>
    <td>여자</td>    
    <td>1990.07.07</td>
    <td>010.</td>
    <td>화성</td>
  </tr>
  <tr>
    <td>4</td>  
    <td>취준생</td>
    <td>$민#</td>
    <td>여자</td>    
    <td>1990.12.26</td>
    <td>010.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>5</td>  
    <td>군인</td>
    <td>#휘#</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>평택</td>    
  </tr>
    <tr>
    <td>6</td>    
    <td>공부중인 편돌이</td>
    <td>서#덕</td>
    <td>남자</td>    
    <td>1994.09.30</td>
    <td>011.</td>
    <td>안산</td>    
  </tr>
  <tr>
    <td>7</td>  
    <td>직장인겸 예비신부</td>
    <td>서@!</td>
    <td>여자</td>    
    <td>1991.11.19</td>
    <td>011.</td>
    <td>안산</td>    
  </tr>    
  <tr>
    <td>8</td>  
    <td>사랑해 유자</td>
    <td>최유!</td>
    <td>여자</td>    
    <td>1990.11.08</td>
    <td>null</td>
    <td>안양</td>    
  </tr>
</table>


<br/>
###'모든 레코드'를 삭제할 때
>ex/ 

>```SQL
DELETE FROM 지인;  
or 
DELETE * FROM 지인;
//- 테이블을 삭제하지 않고 테이블의 모든 행을 삭제. 이것은 실행취소 할 수 없다.
```
><table>
  <tr>
    <td>번호</td>
    <td>분류</td>
    <td>이름</td>
    <td>성별</td>
    <td>생년월일</td>
    <td>전화번호</td> 
    <td>도시</td>   
  </tr>
</table>



