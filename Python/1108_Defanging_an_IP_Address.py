"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
"""
class Solution:
    def defangIPaddr(self, address: str) -> str:

        """Use sub method applied to regular expressions to swap one characters for the other"""
        return re.sub('\.', '[.]', address)

# Alternatively, use may use 'replace' string method
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')