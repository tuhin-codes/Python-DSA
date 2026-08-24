class Solution:
    def floodFill(self, image, sr, sc, color):
        old = image[sr][sc]
        if old == color:
            return image

        def f(r, c):
            if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == old:
                image[r][c] = color
                f(r+1,c)
                f(r-1,c)
                f(r,c+1)
                f(r,c-1)

        f(sr, sc)
        return image