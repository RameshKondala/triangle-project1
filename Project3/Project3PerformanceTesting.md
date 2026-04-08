
# Project 3: Performance Testing

## Introduction

This project centers on performance testing with Apache JMeter. Its aim is to analyze how an application responds under various user loads and to demonstrate how JMeter can mimic real-world traffic. Conducting performance tests is crucial because it reveals slow responses, bottlenecks, and potential failures before deployment. JMeter proves useful in this context as it can emulate numerous virtual users, send HTTP requests, and gather data for analysis.

For this project, I explored how to test a web application using JMeter, where I set up different thread groups and HTTP requests. I also took some time to review the main types of performance testing, key JMeter components, and the Application Performance Index (APDEX). This experience really helped me connect load behavior with practical testing tools and gave me a clearer understanding of how to assess an application’s responsiveness.

***

## Part 1: Research on Performance Testing and JMeter

### Types of Performance Tests

Performance testing assesses how a system responds under various load levels and patterns. The three primary types discussed here are load testing, endurance testing, and stress or spike testing.

#### Load Testing

Load testing evaluates how the system performs under typical or expected traffic. Its goal is to ensure the application stays stable and responsive when many users are active simultaneously.

A typical load test gradually increases users and then maintains the load for a period of time. This helps measure response times, throughput, and error rates under realistic conditions.

#### Endurance Testing

Endurance testing, also called soak testing, checks how the system performs over a long period of time. The goal is to determine whether the application slows down, consumes excessive memory, or encounters problems during prolonged use.

This test is useful for finding memory leaks and long-term stability problems that may not appear in shorter tests.

#### Stress or Spike Testing

Stress testing involves pushing the system beyond its normal capacity to identify its breaking point. Spike testing, a related method, examines the system's response to sudden, rapid fluctuations in traffic.

These tests are valuable for understanding how the system responds to unexpected demand, sudden traffic spikes, and recovery after overload.

***

### Performance Graphs

Below are example graph descriptions The rubric asks for graphs with **Time** on the X-axis and **Number of Threads** on the Y-axis. Y

#### Load Test Graph
- X-axis: Time
- Y-axis: Number of Threads
- Shape: Gradual increase, steady plateau, gradual decrease
![Load Test Graph](/Project3/screenshots/LoadTest.png)
#### Endurance Test Graph
- X-axis: Time
- Y-axis: Number of Threads
- Shape: Steady line for a long duration
![Endurance Test Graph](/Project3/screenshots/EnduranceTest.png)
#### Stress/Spike Test Graph
- X-axis: Time
- Y-axis: Number of Threads
- Shape: Sharp spikes and drops
![Stress/Spike Test Graph](/Project3/screenshots/StressTest.png)


***

### JMeter Components

JMeter is organized around several main components that work together to build a test plan.

#### Thread Groups

A thread group defines the number of virtual users, ramp-up time, and loop count. It is the starting point for simulating user traffic in JMeter.

In my test plan, I used a thread group to represent the users participating in the endurance and load tests.

#### HTTP Request Sampler

An HTTP request sampler sends a specific HTTP request to the target server. It can be used for GET, POST, PUT, or DELETE requests.

For this project, I used a GET request sampler to call the application endpoint and measure response behavior.

#### Config Elements

Config elements define settings used by samplers, such as HTTP header managers, default request values, cookies, and parameters.

I used the HTTP Header Manager to add request headers so the server could interpret the request correctly.

#### Listeners

Listeners display and store test results. The View Results Tree listener is especially useful because it shows request details, response data, and any errors.

I used the View Results Tree listener to confirm that requests were being sent correctly and that responses were received from the server.

***

### Application Performance Index

Application Performance Index, or APDEX, is a standard metric that assesses user satisfaction with application performance by combining response time thresholds into a score ranging from 0.0 to 1.0. A higher APDEX score indicates a superior user experience.

APDEX is useful because it provides a quick performance summary rather than requiring the tester to manually inspect every response time. It is commonly used to compare baseline performance and to identify whether a system is improving or worsening over time.

***

## Part 2: JMeter Demo

### Test Plan Overview

For the JMeter demo, I created a test plan and built two different performance scenarios. One scenario was an endurance test, and the other was a second performance type such as load or stress testing. Each test included a thread group, an HTTP request sampler, an HTTP header manager, and a View Results Tree listener.

### Endurance Test Setup

For the endurance test, I created a thread group with a steady user load over a longer period of time. This test was used to observe whether the application remained stable without slowing down or failing.

#### Steps followed:
1. Opened JMeter and create a new test plan.
2. Added a **Thread Group** and name it `Endurance Test`.
3. Set the number of threads, ramp-up time, and loop count or duration.
4. Added an **HTTP Request Sampler** under the thread group.
5. Set the request method to **GET**.
6. Entered the server name or URL path for the application under test.
7. Added a **HTTP Header Manager** under **Config Elements**.
8. Entered the required headers, such as `Content-Type: application/json`.
9. Added **View Results Tree** under **Listeners**.
10. Run the test and review the response details.

#### Screenshot Placeholders
- Thread Group setup: 
![Endurance Thread Group](/Project3/screenshots/Endurance.png)
- HTTP Request Sampler: 
![HTTP Request Sampler](/Project3/screenshots/Endurance1.png)
- Header Manager: 
![Header Manager](/Project3/screenshots/Endurance2.png)
- View Results Tree: 
![View Results Tree](/Project3/screenshots/Endurance3.png)
- View Results Tree: 
![View Results Tree](/Project3/screenshots/Endurance4.png)
***

### Second Test Type

For the second test, I used a different performance scenario such as load testing or stress testing. This helped compare normal behavior with heavier traffic conditions.

#### Steps followed:
1. Created a new thread group named `Load Test` or `Stress Test`.
2. Added another HTTP Request Sampler.
3. Configured the request as a GET request.
4. Added the HTTP Header Manager again if needed.
5. Added View Results Tree.
6. Run the test and compare the results with the endurance test.

#### Screenshot Placeholders
- Second Thread Group: 
[Second Thread Group](/Project3/screenshots/load-thread-group.png)
- Results: 
![Second Results](/Project3/screenshots/load-results-tree.png)

***

## Extra Credit

Linux commands that can be used to test and evaluate performance on a virtual machine or server include:

- `top` or `htop` to view CPU and memory usage.
- `free -h` to check available memory.
- `df -h` to view disk usage.
- `vmstat` to monitor system performance.
- `iostat` to inspect input/output activity.
- `uptime` to see load average.
- `sar` to collect historical performance data if installed.

These commands are useful for checking whether high traffic is affecting the machine during performance tests.

***

## Conclusion

This project really opened my eyes to how performance testing helps us see how software behaves under various user loads. I enjoyed learning the differences between load, endurance, and stress testing, and I found it fascinating to see how JMeter components work together in a test plan. The Thread Group, HTTP Request Sampler, Config Elements, and Listeners all come together to create meaningful performance tests that really make a difference.

I also discovered that APDEX is a useful metric for quantifying user satisfaction with a simple score. The most difficult aspect of this assignment was figuring out how to properly set up the test plan and interpret the results. Overall, this project enhanced my knowledge of performance testing and demonstrated how JMeter can assess application stability and responsiveness.

***



