class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        rom=""
        dic= [[1000, 'M'],[900,'CM'], [500, 'D'],[400,'CD'], [100, 'C'],[90,'XC'], [50, 'L'],[40,'XL'],[10, 'X'],[9,'IX'], [5, 'V'], [4,'IV' ], [1, 'I']]
        for i in range (len(dic)):
            # print(key)
            while num>=dic[i][0] and num>0:
                num=num-dic[i][0]
                rom=rom+dic[i][1]
                # print(num)
        return rom