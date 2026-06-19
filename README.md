I set up a lab on a virtual machine using the Juice Shop API, which is built on a Docker container.
I carried out simulated SQL injection and XSS attacks, and then captured the traffic visible from the terminal in the logs. 
I also used Burp for testing and intercepting requests, and finally, I added rules to the WAF web firewall.



<img width="1081" height="388" alt="image" src="https://github.com/user-attachments/assets/77591c4f-ff06-4e37-8314-a323b4e54c41" />


Kibana was launched via Docker containers and configured to capture logs.

<img width="1064" height="563" alt="image" src="https://github.com/user-attachments/assets/84deff14-6d62-40b0-9c51-28ec89b0c2d2" />


Grafana has been configured and capture in visual mode SQL injection and XSS.

<img width="1047" height="488" alt="image" src="https://github.com/user-attachments/assets/a5a804dd-c86d-4bae-9a20-bc9a611533a4" />



I have added rules to WAF for block XSS and SQL injection.

<img width="785" height="427" alt="image" src="https://github.com/user-attachments/assets/7d695392-1bb4-4d0f-8b36-1680e1573557" />


After SQL injection it returns 403 forbidden what is visible for Red person and Blue person in logs.

<img width="2107" height="876" alt="image" src="https://github.com/user-attachments/assets/219a9225-3b1a-45ff-add7-c02619c66137" />
