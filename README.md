# Algorithm_Python
파이썬 알고리즘 공부기록


## 1. Python 계단밟기(Wikidocs)

Basic of Python Code

📂 [Helloworld](https://github.com/SoyeonHH/Algorithm_Python/tree/main/Helloworld)




## 2. 파이썬 알고리즘 인터뷰

[LeetCode](https://github.com/SoyeonHH/Algorithm_Python/tree/main/LeetCode) 기출문제 분석을 통한 코딩테스트 준비

✏️ **6장 문자열 조작**

  * [유효한 팰린드롬](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/125.py) | 슬라이싱
  * [문자열 뒤집기](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/344.py) | s.reverse()
  * [로그 파일 재정렬](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/937.py) | 람다 표현식 정렬
  * [가장 흔한 단어](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/819.py) | 입력값 전처리, 리스트 컴프리헨션, collection.Counter()
  * [그룹 애너그램](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/49.py) | 정렬하여 딕셔너리에 추가, sorted(), ' '.join(s)
  * [가장 긴 팰린드롬 부분 문자열](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/5.py) | 슬라이딩 윈도우, 투 포인터 확장

>  파이썬의 정렬 알고리즘 : **팀소트(Timosrt)** (삽입 정렬과 병합 정렬을 휴리스틱하게 조합하여 사용하는 정렬 알고리즘으로, 가장 빠른 시간 복잡도를 보인다.

✏️ **7장 배열**

 * [두 수의 합](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/1.py) | 시간복잡도
 * [빗물 트래핑](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/42.py) | 투 포인터 이동, 난이도 상 ⭐⭐⭐
 * [세 수의 합](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/15.py) | 투 포인터
 * [배열 파티션1](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/561.py) | Pythonic Way
 * [자신을 제외한 배열의 곱](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/238.py) | 아이디어 문제
 * [주식을 사고팔기 가장 좋은 시점](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/121.py) | 최대, 최소 갱신

✏️ **8장 연결 리스트**

 * [팰린드롬 연결 리스트](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/234.py) | 데크(Deque), 런너(Runner), 다중 할당
 * [두 정렬 리스트의 병합](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/21.py) | 변수 스왑
 * [역순 연결 리스트](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/206.py) | 반복이 재귀보다 공간복잡도, 실행 속도 면에서 우수하다.
 * [두 수의 덧셈](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/2.py) | 전가산기(Full Adder), divmod, functools.reduce()
 * [페어의 노드 스왑](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/24.py) | 스왑(swap), 반복구조와 재귀구조
 * [홀짝 연결 리스트](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/328.py) | 문제 이해의 중요성
 * [역순 연결 리스트2](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/92.py) | 반복 구조로 노드 뒤집기

✏️ **9장 스택, 큐**

 * [유효한 괄호](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/20.py) |스택 일치 여부 판별
 * [중복 문자 제거](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/316.py) | 재귀를 이용한 분리, 스택을 이용한 문자 제거
 * [일일 온도](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/739.py) | 시각화, 스택 값과 현재 값 비교
 * [큐를 이용한 스택 구현](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/225.py) | push(x), pop(), top(), empty()
 * [스택을 이용한 큐 구현](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/232.py) | push(x), pop(), peek(), empty()
 * [원형 큐 디자인](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/622.py) | enQueue(), deQueue(), Front(), Rear(), isEmpty(), isFull()


> **스택(Stack)** 은 LIFO(Last-In-First-Out)(후입선출), **큐(Queue)** 는 FIFO(FIrst-In-First-Out)(선입선출)로 처리된다.
> 
> 파이썬의 리스트는 스택과 큐의 모든 연산을 지원하지만, 동적 배열로 구현되어 있어 큐의 연산을 수행하기에는 데크(Deque)라는 별도의 자료형을 사용해야 더 좋은 성능을 낼 수 있다.

✏️ **10장 데크, 우선순위 큐**

 * [원형 데크 디자인](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/641.py)
 * [k개 졍렬 리스트 병합](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/23.py) | PriorityQueue vs heapq

> **데크(Deque)** 는 더블 엔디드 큐(Double-Ended Queue)의 줄임말로, 양쪽 끝을 모두 추출할 수 있는, 큐를 일반화한 형태의 추상 자료형(ADT)이다. 구현은 배열이나 연결 리스트 모두 가능하지만, **이중 연결 리스트(Doubly Linked List)** 로 구현하는 편이 가장 잘 어울린다.


> **우선순위 큐** 는 큐 또는 스택과 같은 추상 자료형과 유사하지만 추가로 각 요소의 '우선순위'와 연관되어 있다. **힙(Heap)**  자료구조와 관련이 깊다.

> **파이썬 전역 인터프리터 락(GIL)** : 하나의 스레드가 자원을 독점하는 형태로 실행된다.

✏️ **11장 해시 테이블**

> **해시 테이블** 또는 **해시 맵** 은 키를 값에 매핑할 수 있는 구조인, 연관 배열 추상 자료형(ADT)을 구현하는 자료구조다. **해시 함수** 란 임의 크기 데이터를 고정 크기 값으로 매핑하는 데 사용할 수 있는 함수를 말한다.

  ✅ 성능 좋은 해시 함수의 특징
  
    * 해시 함수 값 충돌의 최소화 -> **비둘기집 원리**
    * 쉽고 빠른 연산
    * 해시 테이블 전체에 해시 값이 균일하게 분포
    * 사용할 키의 모든 정보를 이용하여 해싱
    * 해시 테이블 사용 효율이 높을 -> **로드 팩터** 낮을수록 효율이 좋다.
    
> **비둘기집 원리**
> 
> n개 아이템을 m개 컨테이너에 넣을 때, n>m이라면 적어도 하나의 컨테이너에는 반드시 2개 이상의 아이템이 들어 있다는 원리

> **로드 팩터(Load Factor)**
> 
> 해시 테이블에 저장된 데이터 개수 n을 버킷의 개수 k로 나눈 것

> **31**
> 
> 정수형 해싱 기법인 모듈로 연산을 이용한 나눗셈 방식(Modulo-Division Method)에서, m 값으로 가장 적절한 **매직 넘버(Magic Number)** 이자 **메르센 소수(Mersenne Prime)**(2의 거듭제곱에서 1이 모자란 수 중 소수로 매우 신비한 성질을 지닌다)

    // C
    /* hash: 문자열 s에 대한 해시 값 구성 */
    unsigned hash(char *s) {
        unsigned hashval;
        
        for (hashval = 0; *s != '/0'; s++)
            hashval = *s + 31 * hashval;
        return hashval % HASHSIZE;
    }
    
    // Java
    hashCode = 31 * hashCode + (e == null ? 0 : e.hashCode());


## 3. [baekjoon](https://www.acmicpc.net/user/sodus1102)

파이썬으로 백준 알고리즘 문제 풀이

📎 **단계별로 풀어보기**

단계|제목|설명|풀이
---|---|---|---
1|입출력과 사칙연산|입력, 출력과 사칙연산을 연습해 봅시다. Hello World!|[Helloworld](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/2557.py) / [We love kriii](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/10718.py) / [고양이](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/10171.py) / [개](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/10172.py) / [A+B](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/1000.py) / [사칙연산](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/10869.py) / [나머지](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/10430.py) / [곱셈](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/2588.py)
2|if문|if문을 사용해 봅시다.|[두 수 비교하기](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/1330.py) / [시험 성적](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/9498.py) / [윤년](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/2753.py) / [사분면 고르기](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/14681.py) / [알람시계](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/2884.py)
3|for문|for문을 사용해 봅시다.| / [구구단](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/2739.py) / [A+B_3](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/10950.py) / [합](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/8389.py) / [빠른A+B](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/15552.py) / [N찍기](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/2741.py) / [기찍N](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/2742.py) / [A+B_7](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/11021.py) / [A+B_8](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/11022.py) / [별찍기1](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/2438.py) / [별찍기2](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/2439.py) / [X보다작은수](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/10871.py)
4|while문|while문을 사용해 봅시다.|[A+B_5](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/10952.py) / [A+B_4](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/10951.py) / [더하기사이클](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/1110.py)
5|1차원 배열|배열을 사용해 봅시다.|[최소, 최대](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/10818.py) / [최댓값](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/2562.py) / [숫자의 개수](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/2577.py) / [나머지](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/3052.py) / [평균](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/1546.py) / [OX퀴즈](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/8958.py) / [평균은 넘겠지](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/4344.py)
6|함수|함수를 정의하면 코드가 깔끔해지고 관리하기 쉬워집니다.|[정수 N개의 합](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/15596.py) / [셀프 넘버](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/4673.py) / [한수](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/1065.py)
7|문자열|문자열을 다루는 문제들을 해결해 봅시다.|[아스키코드](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/11654.py) / [숫자의 합](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/11720.py) / [알파벳 찾기](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/10809.py) / [문자열 반복](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/2675.py) / [단어 공부](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/1157.py) / [단어의 개수](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/1152.py) / [상수](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/2908.py) / [다이얼](https://github.com/SoyeonHH/Algorithm_Python/blob/main/baekjoon/5622.py)



## 4. [LeetCode](https://leetcode.com/sodus1102/)

리트코드 문제 풀이 챌린지

🏆 **Challenge**

Steps|Title|Solutions
 ---|---|---
 1|May LeetCoding Challenge 2021|[Super Palindromes](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/906.py) / [Valid Number](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/65.py) / [Find and Replace Pattern](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/890.py)
