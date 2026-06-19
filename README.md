I built my own testing environment for web application security analysis, based on OWASP Juice Shop running in Docker.
I used Burp Suite to simulate attacks such as SQL injection, XSS, and simple command injection payloads.
HTTP traffic was intercepted by an Nginx proxy, which also served as a Web Application Firewall implemented rules to block characteristic attack patterns, such as OR 1=1 or <script>.
Application logs were recorded by Nginx and processed using Promtail, then sent to Loki, and visualized in Grafana.
In Grafana, I created a dashboard that displays potentially malicious activity in real time, such as spikes corresponding to SQL injection or XSS.
Additionally, I wrote a simple Python script that analyzes logs and generates alerts based on attack patterns.
This allowed me to go through the entire process: from simulating an attack, to detecting it in the logs, to visualizing it and blocking it at the WAF level.



<img width="1081" height="388" alt="image" src="https://github.com/user-attachments/assets/77591c4f-ff06-4e37-8314-a323b4e54c41" />


<img width="889" height="168" alt="image" src="https://github.com/user-attachments/assets/a766316b-a9b5-4617-88e0-7a5488f56919" />

Kibana was launched via Docker containers and configured to capture logs.

<img width="1064" height="563" alt="image" src="https://github.com/user-attachments/assets/84deff14-6d62-40b0-9c51-28ec89b0c2d2" />


Grafana has been configured and capture in visual mode SQL injection and XSS.

<img width="1047" height="488" alt="image" src="https://github.com/user-attachments/assets/a5a804dd-c86d-4bae-9a20-bc9a611533a4" />

In Burp several times used XSS and it is visible in Grafana 

<img width="986" height="450" alt="image" src="https://github.com/user-attachments/assets/86a4d367-1814-492f-804d-b4559dbcf161" />


<img width="283" height="178" alt="image" src="https://github.com/user-attachments/assets/6ec2382d-f434-493b-af20-eb23a6459207" />


I have added rules to WAF for block XSS and SQL injection.

<img width="785" height="427" alt="image" src="https://github.com/user-attachments/assets/7d695392-1bb4-4d0f-8b36-1680e1573557" />


After SQL injection it returns 403 forbidden what is visible for Red person and Blue person in logs.

<img width="2107" height="876" alt="image" src="https://github.com/user-attachments/assets/219a9225-3b1a-45ff-add7-c02619c66137" />
