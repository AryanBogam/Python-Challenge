Q8. Empty Slide Detector
Task: Identify slides that have no content (empty title & no bullets).
slides = [{"title": "", "bullets": []},
          {"title": "Agenda", "bullets": ["Topic 1"]}]
Output: ["Slide 1 is empty"]
Why: PowerPoint warns if you have empty slides.