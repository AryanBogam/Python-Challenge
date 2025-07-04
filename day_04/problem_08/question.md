 Question 8: Domain Watcher – Competitive Analysis Tool

Scenario: You’re building a tool that tracks domains owned by companies:

Your Company Domains: {"aiworld.com", "buildai.io", "futuretools.ai"}
Competitor Domains: {"futuretools.ai", "visionchain.io", "hyperai.net"}
Recently Registered Domains: {"buildai.io", "hyperai.net", "skyai.co"}

Determine:

Which of your domains were recently registered?
Which competitor domains overlap with yours?
Which newly registered domains are new threats (not owned by either)?

Expected Logic:

Use intersection()
Use difference() to spot unknown competitors
Think like an AI-powered domain watcher