
# Final Presentation

## Team Info

- **Name:** RAMESH KONDALA
- **Worked:** Alone

## Presentation Overview

This presentation discusses the four testing assignments completed in class: Unit Testing, Postman API Testing, JMeter Performance Testing, and Selenium UI Testing. It also explains how I developed the testing applications, the AI tools I utilized, and the insights I gained from the results.

## Target Testing Applications

My testing applications were built around small, focused examples so I could demonstrate each testing method clearly.

- **Project 1: Unit Testing** — a small Python or Java program with functions that could be tested individually.
- **Project 2: Postman** — a Triangle API that supported endpoint testing with different request types.
- **Project 3: JMeter** — the Triangle API tested for performance using endurance, load, or stress-style requests.
- **Project 4: Selenium** — a web application with forms or user actions that could be tested in a browser.

## How I Coded It

I coded each project to match the testing goal.

- For **Project 1**, I wrote small functions and then created unit tests for expected and edge-case behavior.
- For **Project 2**, I built or used a REST API and tested its endpoints in Postman.
- For **Project 3**, I used JMeter to simulate repeated requests and measure performance.
- For **Project 4**, I automated browser actions with Selenium to test UI behavior.

The code was intentionally small and testable so I could focus on correctness, repeatability, and clear results.

## AI Tools Used

I used AI tools to make brainstorming quicker, troubleshoot errors more easily, and generate starting code and explanations. Agentic AI tools are great for helping create test cases faster, automating repetitive testing tasks, and adapting to changes in the application. However, they still require human review to double-check business rules and handle edge cases, ensuring everything works perfectly.

- **ChatGPT / Perplexity-style assistant:** helped explain concepts, debug commands, and draft markdown.
- **AI coding help:** helped generate boilerplate code and test structure.
- **Human review:** I checked whether the generated code actually matched the assignment requirements.



## Project Results

### Project 1: Unit Testing

This project centered on testing individual functions. I learned to verify expected results, check edge cases, and ensure the code worked correctly with different inputs. The key finding was that small, isolated tests helped identify bugs more easily and early.
![Valid scalene triangle run](./Project1/screenshots/scalene.png)


### Project 2: Postman

This project concentrated on API testing. I learned to send GET, POST, PUT, and DELETE requests and examine status codes and response bodies. The key takeaway was that API testing provided immediate feedback on the proper functioning of endpoints.
![Logged Out State](/Project2/triangle-api/screenshots/img_1.png)

### Project 3: JMeter

This project focused on performance testing. I learned how to simulate repeated traffic using thread groups and observe how the API behaved under load. The main result was that performance testing helped me understand how the system responds over time, not just whether it works once.
![Endurance Thread Group](/Project3/screenshots/Endurance.png)

### Project 4: Selenium

This project centered on browser automation. I learned to interact with page elements, submit forms, and verify the expected UI outcomes. The key result was that Selenium enabled consistent repetition of browser actions and helped identify UI regressions.
[Cart Verification Results](/Project4/screenshots/verification.png)

## Demo of One Test






## Agentic AI Analysis

Agentic AI tools are valuable as they can accelerate repetitive testing, create initial tests, and determine testing priorities based on recent updates or past failures. They are particularly useful for generating quick boilerplate code, suggesting test ideas, or assisting with documenting test coverage.

The drawback is that AI tools might overlook context, make assumptions, or produce tests that seem correct but don't fully meet the assignment criteria. They may also miss edge cases, business rules, or unusual behaviors that a human tester would catch. Some sources explicitly caution that AI-generated testing remains unreliable in complex workflows and still needs human supervision.

### Pros

- Faster test creation.
- Helpful for repetitive or boilerplate work.
- Good at generating starting points and examples.
- Can support regression testing and test prioritization.

### Cons

- May miss edge cases.
- May misunderstand requirements.
- Can produce tests that pass without really validating the feature.
- Needs human review to confirm correctness and relevance.

## Special Testing Considerations

When using Agentic AI tools for testing, I need to think about several things:

- **Does the test actually meet the requirement?**
- **Does it cover edge cases, not just the happy path?**
- **Does it verify business logic, not just syntax?**
- **Does it still work if the UI or API changes?**
- **Is a human reviewing the results?**

The main takeaway is that AI can speed up test creation, but it shouldn't be relied on blindly. It performs best when I use it as a helper and then verify all outputs myself.

## Closing

These four projects advanced my understanding of testing from various perspectives: unit tests, API testing, performance testing, and UI automation. They demonstrated that testing isn't merely about verifying functionality once; it's about ensuring it continues to work reliably across different conditions. While Agentic AI can assist in this process, effective testing still relies heavily on human judgment.


