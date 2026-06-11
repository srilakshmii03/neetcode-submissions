class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".","")
            result.add(local + "@" + domain)
        return len(result)
        