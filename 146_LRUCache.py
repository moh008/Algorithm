class Node:
    def __init__(self, key, val):           #노드의 초기화
        self.key, self.val = key, val       #노드의 key와 val를 할당
        self.prev = self.next = None        #노드의 방향 할당. 전방향과 후방향은 None으로 초기화

class LRUCache:
    def __init__(self, capacity:int):       #전체판 초기화: capacity와 hashmap 그리고 LRU, MRU 노드세팅 각 LRU, MRU의 방향세팅
        self.cap = capacity
        self.cache = {}

        self.LRU = Node(0, 0)
        self.MRU = Node(0, 0)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU
    
    def get(self, key) -> int:              #get의 기능, key가 cache 해시맵에 있을경우, 해당 value를 리턴함(포인터로 돼있음)
        if key in self.cache:               #해당 key를 가진 value가 있을경우, 해당 값을 리턴하고 Double LinkedList에서 순서를 바꿔줘야함
            self.remove(self.cache[key])    #LinkedNode 제거
            self.insert(self.cache[key])    #Node 삽입
            return self.cache[key].val      #key를 가진 해시맵 요소의 value를 리턴
        else:
            return -1
    
    def remove(self, node):                 #Linked Node의 삭제기능 구현
        prev, next = node.prev, node.next   #존재하는 노드의 이전, 다음 노드는 연결돼있는 노드의 이전과 다음 노드
        prev.next = next                    #prev 노드의 다음노드는 원래 연결됐던 node의 다음노드
        next.prev = prev                    #next 노드의 이전노드는 원래 연결됐던 node의 이전노드
    
    def insert(self, node):                 # LinkedList에 Node 추가기능 구현
        prev, next = self.MRU.prev, self.MRU# 추가하기전 그나마 MRU에 가까운 노드가 prev로, MRU 자체가 next로
        prev.next = next.prev = node        # prev의 다음은 삽입되는 노드, 마찬가지로 next의 이전은 삽입되는 노드
        node.prev = prev                    # 삽입되는 노드의 이전노드는 prev
        node.next = next                    # 삽입되는 노드의 다음노드는 next (가장 최근 접근되는 노드이므로 MRU)
    
    def put(self, key: int, value: int):    # 해시맵에 노드를 박아주는 기능 구현
        if key in self.cache:               # 만약 이미 존재하는 노드면
            self.remove(self.cache[key])    # LinkedList에서 제거
        self.cache[key] = Node(key, value)  # 새로운 노드 들어간다 입벌려
        self.insert(self.cache[key])        # 새로운노드를 LinkedList에 삽입

        if len(self.cache) > self.cap:      # 만약 존재하는 노드가 Capacity보다 많아진다면
            lru = self.LRU.next             # LRU에 해당하는 노드를 self.LRU.next로 가져옴
            self.remove(lru)                # LinkedList에서 제거하고
            del self.cache[lru.val]         # 역시 Hashmap에서도 제거한다.
        