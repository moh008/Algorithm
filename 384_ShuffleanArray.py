"""
self 주의보!!
함수 하나만을 불러서 리턴하는게 아니라
object 를 생성하여 연속적으로 부르는것이기 때문에 각 함수안에서 정의시 self가 필수
"""
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = list(nums)  #reset 전용 original list 생성. 그냥 nums가 아닌 이유는 call by reference가 되버리면 다른함수에서 original의 값들도 바뀌게됨
    def reset(self) -> List[int]:   #그래서 새로운 리스트를 만들어 nums를 저장하는 방식으로 가야함 물론 list(nums)도 되고 list(self.nums)도 됨
        return self.original
    def shuffle(self) -> List[int]:
        n = len(self.nums)
        for i in range(0, n):       #랜덤한 index j를 생성
            j = random.randrange(i, n)  #i부터 n-1 까지 element중 하나를 골라서
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i] #swap 진행
        return self.nums