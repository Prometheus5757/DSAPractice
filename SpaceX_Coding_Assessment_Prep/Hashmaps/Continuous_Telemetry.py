'''
LEETCODE EASY 

The Problem: Continuous Telemetry Validation
You are building an integration layer for a ground station tracking an experimental aircraft. The aircraft streams data packets sequentially, and each packet has a unique integer identifier called a packet_id. Because of atmospheric conditions and network jitter, packets can arrive scattered or duplicated.

Your software maintains a strict rolling data window. You are given an array of integers packet_ids representing the incoming stream, and an integer k. You need to determine if there are any duplicate packets processed within your moving index window of size k.

Specifically, return True if there are two distinct indices i and j in the array such that packet_ids[i] == packet_ids[j] and the absolute difference between i and j is at most k (|i - j| <= k). Otherwise, return False.

Test Cases to Keep in Mind
Case 1: packet_ids = [1, 2, 3, 1], k = 3 -> Should return True (Packet 1 is at index 0 and 3. |0 - 3| = 3, which is = k)
Case 2: packet_ids = [1, 2, 3, 1, 2, 3], k = 2 -> Should return False (Packet 1 is at index 0 and 3. |0 - 3| = 3, which is > k, and the same applies to all other duplicates)
'''

def contains_nearby_duplicate(packet_ids, k):
    dictid = {}

    for idx, id in enumerate(packet_ids):
        dictid.setdefault(id, []).append(idx)


    for keyid in dictid:
        if len(dictid[keyid]) > 1:
            if((dictid[keyid][-1] - dictid[keyid][0]) > k):
                kmatch = False
            else:
                kmatch = True

    return kmatch

print(contains_nearby_duplicate(packet_ids = [1, 2, 3, 1], k = 3))
print(contains_nearby_duplicate(packet_ids = [1, 2, 3, 1, 2, 3], k = 2))
print(contains_nearby_duplicate(packet_ids = [1, 9, 9, 1], k = 1))