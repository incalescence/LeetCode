class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        partitions = []
        
        # store last index of each character 
        last_instance = {}
        for i, c in enumerate(s):
            last_instance[c] = i
        
        # go through string
        partition_size = 0 
        end_index = 0
        for i, c in enumerate(s):
            partition_size += 1
            end_index = max(last_instance.get(c), end_index)
            
            # ending partition 
            if i == end_index:
                partitions.append(partition_size)
                partition_size = 0 
        
        return partitions;
        
        