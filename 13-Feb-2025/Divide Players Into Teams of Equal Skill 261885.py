# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        i = 0
        j = len(skill) - 1

        output = 0
        checker = skill[i] + skill[j]
        validator = True
        
        while i < j:
            output += skill[i] * skill[j]
            if checker != skill[i] + skill[j]:
                validator = False
            i += 1
            j -= 1
        
        
        if not validator:
            return -1

        return output

        