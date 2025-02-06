# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dict = defaultdict(int)

        # outer loop splits the elements of cpdomains to count and domain
        for comb_domains in cpdomains:
            count, domain = comb_domains.split()
            count = int(count)

            # fragments = ["discuss", "leetcode", "com"]
            fragments =  domain.split(".")

            for i in range(len(fragments)):
                dict[".".join(fragments[i:])] += count
        
        return [f"{count} {domain}" for domain, count in dict.items()]
