import random
from itertools import product

class UserAgent:
    def __init__(self):
        self.browsers = ["Chrome", "Firefox", "Safari", "Edge", "Opera", "Brave", "Mozilla", "IE"]
        self.os = ["Windows", "Macintosh", "Linux", "iOS", "Android", "Unix", "BlackBerry"]
        self.versions = ["91.0.4472.124", "91.0.864.59", "14.1.1", "12.0.1", "8.0.0", "5.0.2", "3.2.1"]

        # Generate permutations of components
        self.user_agents = list(product(self.browsers, self.os, self.versions))

    def __call__(self):
        browser, os, version = random.choice(self.user_agents)
        return f"Mozilla/5.0 ({self.get_os_string(os)}; {os} {self.get_os_version_string(os, version)}) AppleWebKit/537.36 (KHTML, like Gecko) {browser}/{version} Safari/537.36"

    def get_os_string(self, os):
        return {"Windows": "Win64; x64", "Macintosh": "Intel Mac OS X 10_15_7"}.get(os, "")

    def get_os_version_string(self, os, version):
        return {"Windows": f"NT 10.0; {version}", "Macintosh": f"Version/{version}"}.get(os, "")

# Create an instance of the UserAgent class
useragent = UserAgent()

# Example of usage
random_user_agent = useragent()
print(f"Random User-Agent: {random_user_agent}")
