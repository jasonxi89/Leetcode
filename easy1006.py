import collections


class Solution:
    """
    @param cpdomains: a list cpdomains of count-paired domains
    @return: a list of count-paired domains
    """
    def subdomainVisits(self,cpdomains):
        # Write your code here
        result = collections.Counter()
        for cpdomain in cpdomains:
            count, domains = cpdomain.split(" ")
            count = int(count)
            while domains:
                result[domains] += count
                indexofdot = domains.find('.')
                if indexofdot != -1:
                    domains = domains[indexofdot +1:]
                else:
                    domains = None

        return [result[domain] + " " + domain for domain in result]


if __name__ == "__main__":
    print(Solution.subdomainVisits())



# class Solution:
#     """
#     @param cpdomains: a list cpdomains of count-paired domains
#     @return: a list of count-paired domains
#     """
#     def subdomainVisits(self, cpdomains):
#         # Write your code here
#         counts = collections.Counter()
#         for cpdomain in cpdomains:
#             count, domain = cpdomain.split(' ')
#             count = int(count)
#             while domain:
#                 counts[domain] += count
#                 indexOfDot = domain.find('.')
#                 domain = domain[indexOfDot + 1:] if indexOfDot != -1 else ''
#         return [str(counts[key]) + ' ' + key for key in counts]
