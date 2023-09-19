def maxDepth(s: str) -> int:
    count = 0  # 定義計數器，用於統計嵌套深度
    max_count = 0  # 定義最大嵌套深度，用於記錄最終結果
    for c in s:  # 遍歷字符串 s 中的每個字符
        if c == '(':  # 如果當前字符是左括號 "("，則將 count 加一
            count += 1
        elif c == ')':  # 如果當前字符是右括號 ")"，則將 count 減一
            count -= 1
        max_count = max(max_count, count)  # 更新最大嵌套深度
    return max_count  # 返回最大嵌套深度