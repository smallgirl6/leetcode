class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0  # 追蹤當前文件夾相對於主文件夾的深度
        for log in logs:
            if log == "../":
                # 只有當不在主文件夾時，才移到父文件夾
                depth = max(0, depth - 1)
            elif log == "./":
                # 停留在同一個文件夾，深度不變
                continue
            else:
                # 移動到子文件夾，深度增加 1
                depth += 1
        return depth