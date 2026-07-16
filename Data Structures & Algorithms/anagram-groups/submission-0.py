class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = list()

        for s in strs:
            flag = False
            for r in result:
                #如果找到了，那么加到相应的格子，跳出两层循环
                if sorted(s) == sorted(r[0]):
                    r.append(s)
                    flag = True
                    break
            #如果没找到 那么增加一个大格子
            if flag == True:
                continue
            result.append([s]) 
        return result

        