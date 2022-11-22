class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_string = address.replace(".", "[.]" )
        return new_string