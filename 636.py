class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        result = [0] * n
        prev_time = 0
        for log in logs:
            parts = log.split(":")
            function_id = int(parts[0])
            status = parts[1]
            timestamp = int(parts[2])


            if status == "start":
                if stack:
                    # 若出現新的function_id則計算剛剛(上個)function_id的TIME到result
                    result[stack[-1]] += timestamp - prev_time 
                stack.append(function_id)
                prev_time = timestamp #更新上個時間
            else:#END加1的原因是要加上結束的時間
                # 結束了所以function_id從STACK內POP出來 並把TIME加到function_id對應的result中
                result[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1 #更新上個時間
            
        return result