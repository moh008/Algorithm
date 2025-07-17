class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        unique_sums = []                        #rhombus 합들을 저장해놓을 list
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                rhombus_sum = grid[r][c]        #Up 한칸값을 미리저장 (size 1칸짜리용)
                unique_sums.append(rhombus_sum) #1칸 짜리도 rhombus이니 저장
                size = 1                        #사이즈 늘려나감 
                while r + size < ROWS and c - size >= 0 and c + size < COLS:    #각 r와 c에 대해 grid boarder까지 사이즈가 늘려질수 있을때
                    left = c - size             #Up기준 왼쪽아래
                    right = c + size            #Up기준 오른쪽 아래
                    bottom = r + size           #Up기준 한칸 밑
                    rhombus_sum += grid[bottom][left] + grid[bottom][right]     #아래를 제외하고 현재 오른쪽 아래와 왼쪽아래 합을 더함
                    bottom_sum = 0              #아직 아래값이 나오지않았으므로 unique_sum append는 안함
                    while left < right:         #마름모 절반아래는 축소
                        left += 1               #왼쪽아래는 +1
                        right -= 1              #오른쪽아래는 -1 
                        bottom += 1             #아래는 더 한칸 아래로 아래꼭지점을 향함
                        if bottom >= ROWS or left >= COLS or right < 0: #위의 연산이 border 이상으로 튀어나올경우
                            break               #반복문 탈출
                        elif left == right:       #left와 right가 같다는말은 축소가 끝나서 아래꼭지점에 다다랐을때
                            bottom_sum += grid[bottom][left]    #아래 꼭지점의 값을 더해줌
                            unique_sums.append(rhombus_sum + bottom_sum)    #연산이 끝났으므로 unique_sum에 append
                        else:                   #아직 축소가 끝나지않았다(아래꼭지점에 닿지못함)
                            bottom_sum += grid[bottom][left] + grid[bottom][right]  #아래 왼쪽/오른쪽 합을 누적
                    size += 1                   #더 큰 마름모를 찾으러 사이즈업
        unique_sums = sorted(set(unique_sums), reverse=True) #unique_sums list를 set으로 바꿔 reverse sorted를 실행 (내림차순정렬)
        return unique_sums[:3]                  #내림차순 정렬된 값들을 3개 꺼내서 리턴