class FreqStack:

    def __init__(self):
        #push(5) push(7) push(5) push(7) push(4) push(5)
        self.val_freq = {} #  記錄每個value的頻率 (key is val,value is freq) val_freq = {5: 3, 7: 2, 4: 1}
        self.freq_group = {} # 記錄頻率出現過的每個值 (key is freq,value is val_list) freq_group = {1: [5, 7, 4], 2: [5, 7], 3: [5]}
        self.max_freq = 0 # Maximum frequency

    def push(self, val: int) -> None:
        freq = self.val_freq.get(val, 0) + 1 # 從val_freq中獲取val的當前頻率 ， { 5: 2} 遇到第三次push(5) +1， freq =2+1
                                             # 若val不存在於val_freq中則返回0並將這個頻率加1， 遇到第一次push(7) ，freq =0+1
        self.val_freq[val] = freq # 在val_freq中 更新val的頻率 {5: 2, 7: 1}  ，變成 {5: 3, 7: 1} 
        

        self.max_freq = max(self.max_freq, freq) # 確保max_freq是當前的最大頻率

        if freq not in self.freq_group: # 首次遇到這個頻率
            self.freq_group[freq] = [val]  # 建一個新的array，其中只有val
        else:                           # 已存在這個頻率
            self.freq_group[freq].append(val) # 將val加到已存在頻率的array

    def pop(self) -> int:
        # 從freq_group字典中獲取當前最大頻率max_freq的array freq_group = {1: [5, 7, 4], 2: [5, 7]} ，max_freq是2 ，
                                                #  array [5, 7] pop移除並獲取該列表的最後一個元素 7
        val = self.freq_group[self.max_freq].pop()
        
        self.val_freq[val] -= 1 # 移除了一個val，更新其在val_freq字典中的頻率，將其減少1。 7: 2變 7: 1

        if not self.freq_group[self.max_freq]: # 如果最大頻率的列表已經為空，沒有其他的值具有這個頻率，需要將max_freq減少1，以反映下一個最高的頻率
                                               # {1: [5, 7], 2: [5, 7], 3: [5]} max_freq會是3
                                               # pop移除freq_group中頻率為3的列表的最後一個元素，即5 {1: [5, 7], 2: [5, 7], 3: []}
                                               # 最大頻率的列表已經為空 3: []
            self.max_freq -= 1                 # max_freq減少1  max_freq 從3變2

        
        return val