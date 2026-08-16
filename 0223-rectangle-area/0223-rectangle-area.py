class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def compute_area_of_rectange(x1, x2, y1, y2):
            length = x2 - x1
            breadth = y2 - y1

            return length * breadth
        
        area_r1 = compute_area_of_rectange(ax1, ax2, ay1, ay2)        
        area_r2 = compute_area_of_rectange(bx1, bx2, by1, by2)

        common_area = 0
        cx1 = max(ax1, bx1)
        cx2 = min(ax2, bx2)
        cy1 = max(ay1, by1)
        cy2 = min(ay2, by2)
        if cx1 < cx2 and cy1 < cy2:
            common_area = compute_area_of_rectange(cx1, cx2, cy1, cy2)

        return area_r1 + area_r2 - common_area