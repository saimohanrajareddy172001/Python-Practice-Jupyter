class Check_Dublicate:
    @staticmethod
    def Contains_Dublicate(nums):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
            return False
print(Check_Dublicate.Contains_Dublicate([1,2,3,4,1]))