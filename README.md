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

 * [해시맵 디자인](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/706.py) | put(key, value), get(key), remove(key)
 * [보석과 돌](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/771.py) | defaultdict, Counter, Pythonic Way
 * [중복 문자 없는 가장 긴 부분 문자열](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/3.py) | 슬라이딩 윈도우, 투 포인터
 * [상위 K 빈도 요소](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/347.py) | zip(), 아스테리스크(*), Unpacking/Packing

> **해시 테이블** 또는 **해시 맵** 은 키를 값에 매핑할 수 있는 구조인, 연관 배열 추상 자료형(ADT)을 구현하는 자료구조다. **해시 함수** 란 임의 크기 데이터를 고정 크기 값으로 매핑하는 데 사용할 수 있는 함수를 말한다.

  ✅ **성능 좋은 해시 함수의 특징**
  
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
    
 ✅ **충돌(Collusion) 발생 시**
 
  * 개별 체이닝(Separate Chaining) : 충돌 발생 시 연결 리스트로 연결
  * 오픈 어드레싱(Open Addressing) : 충돌 발생 시 탐사(Probing)를 통해 빈 공간을 찾아나서는 방식 *(파이썬에서 사용되는 방식)


✏️ **12장 그래프**

 * [섬의 개수](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/200.py) | dfs 재귀 호출, 파이썬 중첩함수
 * [전화 번호 문자 조합](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/17.py) | dfs 재귀 호출, dictionary 활용
 * [순열](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/46.py) | dfs, 객체 복사[:], itertools.permuatations()
 * [조합](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/77.py) | dfs, itertools.combinations()
 * [조합의 합](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/39.py) | dfs
 * [부분집합](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/78.py) | 트리를 구성하여 dfs
 * [일정 재구성](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/332.py) | 재귀 vs 반복
 * [코스 스케줄](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/207.py) | DFS로 순환 구조 판별, 가지치기, defaultdict 순회 문제

> **그래프** 란, 객체의 일부 쌍(pair)들이 '연관되어' 있는 객체 집합 구조를 말한다.

> **오일러 경로** 
> 
> 모든 edge를 한 번씩 방문하는 유한 그래프
> 
> **오일러의 정리**에 의하면, 모든 vertex가 짝수 개의 degree를 갖는다면, 모든 다리를 한 번씩 건너서 도달하는 것이 성립 가능하다.

> **해밀턴 경로(Hamiltonian Path)**
> 
> 각 vertex를 한 번씩 방문하는 무향 또는 유향 그래프
> 
> 대표적인 **NP-complete 문제**로, 최적 알고리즘이 없다.


> **외판원 문제(TSP)**
> 
> 해밀턴 순환의 최단거리를 찾는 문제
> 
> NP-난해 문제이다.

> **NP문제**
> 
> 비결정론적 튜닝 기계(NTM)로 다항 시간 안에 풀 수 있는 판정 문제의 집합
> 
> "P 집합은 NP 집합의 부분집합이다. P=NP 인지는 아직 알려지지 않았다."
> 
> NP 문제이면서 NP-난해 문제 : **NP-완전 문제**

**그래프 순회(그래프 탐색)** : 그래프의 각 vertex를 방문하는 과정으로, 깊이 우선 탐색(DFS)과 너비 우선 탐색(BFS) 방법이 있다.

**DFS(깊이 우선 탐색)**

    // 재귀
    
    // Sudo Code
    DFS(G, V)
        label v as discoverd
        for all directed edges from v to w that are in G.adjacentEdges(v) do
            if vertex w is not labeled as discoverd then
                recursively call DFS(G, w)
                
    // Python
    def recursive_dfs(v, discovered=[]):
        discovered.append(v)
        for w in gragh[v]:
            if w not in discovered:
                discovered = recursive_dfs(w, discovered)
        return discovered
        
    
    // 스택
    
    // Sudo Code
    DFS-iterative(G, v)
        let S be a stack
        S.push(v)
        while S is not empty do
            v = S.pop()
            if v is not labeled as discovered then
                label v as discovered
                for all edges from v to w in G.adjacentEdges(v) do
                    S.push(w)
                    
     // Python
     def iterative_dfs(start_v):
         discovered = []
         stack = [start_v]
         while stack:
             v = stack.pop()
             if v not in discovered:
                 discovered.append(v)
                 for w in graph[v]:
                     stack.append(w)
         return discovered


**BFS(너비 우선 탐색)**

    //큐
    
    // Sudo Code
    BFS(G, start_v)
        let Q be a queue
        label start_v as discovered
        Q.enqueue(start_v)
        while Q is not empty do
            v := Q.dequeue()
            if v is the goal then
                return v
            for all edges from v to w in G.adjacentEdges(v) do
                if w is not labeled as discovered then
                label w as discovered
                w.parent := v
                Q.enqueue(w)
                
     // Python
     def iterative_bfs(start_v):
         discovered = [start_v]
         queue = [start_v]
         while queue:
             v = queue.pop(0)
             for w in graph[v]:
                 discovered.append(w)
                 queue.append(w)
         return discovered


> BFS는 재귀로 동작하지 않는다.

> **백트래킹(Backtracking)**
> 
> 해결책에 대한 후보를 구축해 나아가다 가능성이 없다고 판단되는 즉시 후보를 포기(backtrack)해 정답을 찾아가는 범용적인 알고리즘으로, 제약 충족 문제에 특히 유용하다.
> 
> 트리의 가지치기(Pruning)에 해당한다.

> **제약 충족 문제(CSP)**
> 
> 수많은 제약 조건을 충족하는 상태를 찾아내는 수학 문제


✏️ **13장 최단 경로 문제**

 * [네트워크 딜레이 타임](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/743.py) | 다익스트라 알고리즘, 우선순위 큐
 * [K 경유지 내 가장 저렴한 항공권](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/787.py) | 다익스트라 알고리즘, 우선순위 큐, 경유지 제한

> **최단 경로 문제**는 각 간선의 가중치 합이 최소가 되는 두 정점(또는 노드) 사이의 경로를 말한다.

> **오컴의 면도날(Occam's Razor)**
> 
> 어떤 현상을 설명할 때 필요 이상의 가정과 개념들은 면도날로 베어낼 필요가 있다는 권고로 쓰이는 용어이다. 사고의 절약을 요구하는 이 원리는 과학 분야에서 널리 응용되는 일반적인 지침이다.


    // Dijkstra Algorithm Sudo Code
    
    function Dijkstra(Graph, source):
        dist[source] <- 0
        
        create vertex priority queue Q
        
        for each vertex v in Graph:
            if v != source
                dist[v] <- INFINITY
                prev[v] <- UNDEFINED
                
            Q.add_with_priority(v, dist[v])
            
        while Q is not empty:
            u <- Q.extract_min()
            for each neighbor v of u:
                alt <- dist[u] + length(u, v)
                if alt < dist[v]
                    dist[v] <- alt
                    prev[v] <- u
                    Q.decrease_priority(v, alt)
                    
        return dist, prev


✏️ **14장 트리**

 * [이진 트리의 최대 깊이](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/104.py) | 반복 구조로 BFS 풀이
 * [이진 트리의 직경](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/543.py) | 상태값 누적 트리 DFS, 중첩 함수에서 클래스 변수 사용
 * [가장 긴 동일 값의 경로](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/687.py) | 상태값 거리 계산 DFS

> **트리(Tree)**는 계층형 트리 구조를 시뮬레이션 하는 추상 자료형(ADT)으로, 루트 값과 부모-자식 관계의 서브트리로 구성되며, 서로 연결된 노드의 집합이다.

> **서브트리(Subtree)**
> 
> 재귀로 정의된(recursively defined) 자기 참조(self-referential) 자료구조

> **그래프 vs 트리**
> 
> 1. 트리는 순환 구조(Cyclic)를 갖지 않는 그래프이다.
> 
> 2. 그래프는 단방향과 양방향 모두 가능하지만, 트리는 부모 노드에서 자식 노드를 가리키는 단방향뿐이다.
> 
> 3. 트리는 하나의 부모 노드를 갖고, 루트 또한 하나여야 한다.

<img src="https://github.com/SoyeonHH/Algorithm_Python/blob/main/Binary%20Trees.jpg" width="70%" height="70%">

> **이진 트리(Binary Tree)** : 모든 노드의 차수가 2 이하일 때 (다진 트리에 비해 훨씬 간결하고, 여러 알고리즘 구현을 간단하게 처리할 수 있다.)
> 
> **정 이진 트리(Full Binary Tree)** : 모든 노드가 0개 또는 2개의 자식 노드를 갖는다.
> 
> **완전 이진 트리(Complete Binary Tree)** : 마지막 레벨을 제외하고 모든 레벨이 완전히 채워져 있으며, 마지막 레벨의 모든 노드는 가장 왼쪽부터 채워져 있다.
> 
> **포화 이진 트리(Perfect Binary Tree)** : 모든 노드가 2개의 자식 노드를 갖고 있으며, 모든 리프 노드가 동일한 깊이 또는 레벨을 갖는다.


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
 2|July LeetCoding Challenge 2021|[Isomorphic String](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/205.py) / [Custom Sort String](https://github.com/SoyeonHH/Algorithm_Python/blob/main/LeetCode/791.py)
