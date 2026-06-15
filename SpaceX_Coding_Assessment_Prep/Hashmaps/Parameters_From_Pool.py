"""
You are writing a deployment script that configures network nodes using
pre-defined parameter profiles.

You are given two strings: required_params and available_pool. Each character 
in the strings represents a specific configuration token or hardware resource. 

Your script must determine if the deployment can proceed. It can only proceed 
if the required_params can be constructed entirely using the tokens from 
available_pool. 

The Constraints:
1. Each token in available_pool can only be used once in your required_params.
2. Both strings contain only lowercase English letters.
3. Return True if deployment is possible; otherwise, return False.

Example 1:
required_params = "a", available_pool = "b"
Output: False

Example 2:
required_params = "aa", available_pool = "ab"
Output: False

Example 3:
required_params = "aa", available_pool = "aab"
Output: True
"""

def can_deploy(required_params, available_pool):
    letterFrequency = {}
    # Your barebones python code here
    for letter in available_pool:
        if letter in letterFrequency:
            letterFrequency[letter] += 1
        else:
            letterFrequency[letter] = 1
    if (required_params[0] in letterFrequency and letterFrequency[required_params[0]] == len(required_params)):
        return True
    return False

print(can_deploy(required_params = "a", available_pool = "b"))
print(can_deploy(required_params = "aa", available_pool = "ab"))
print(can_deploy(required_params = "aa", available_pool = "aab"))