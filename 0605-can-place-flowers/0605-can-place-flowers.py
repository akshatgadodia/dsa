class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for idx, value in enumerate(flowerbed):
            if n <= 0:
                break

            if value == 1:
                continue
            
            can_place_flower = True
            if idx > 0 and flowerbed[idx - 1] == 1:
                can_place_flower = False
            if idx < len(flowerbed) -1 and flowerbed[idx + 1] == 1:
                can_place_flower = False

            print()

            if can_place_flower:
                n -= 1
                flowerbed[idx] = 1
            
        return n == 0
        