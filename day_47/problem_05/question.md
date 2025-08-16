Q5. Attachment Checker
Task: Given emails with an "attachments" list, return only those that have attachments.
Example:
emails = [
  {"subject": "Report", "attachments": ["report.pdf"]},
  {"subject": "Hi", "attachments": []}
]
Output: [{"subject": "Report", "attachments": ["report.pdf"]}]
Why: Gmail shows a 📎 icon if an email has an attachment.