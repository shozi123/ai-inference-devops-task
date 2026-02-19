# AI Inference Service DevOps Task

This project was completed as part of a technical assessment for a DevOps/Backend internship role.  
It contains a simple FastAPI mock AI inference service with Docker, CI/CD, monitoring, and auto-recovery.

This was my first DevOps automation project. I implemented containerization, basic CI/CD, monitoring, and auto-recovery. I am actively improving Terraform and Kubernetes skills.

## Project Files
ai_service/
├── main.py
├── Dockerfile
├── requirements.txt
├── monitor.py
├── watchdog.sh
├── tests/test_api.py
├── .github/workflows/ci.yml
└── README.md

## How to Run

#Build Docker image:
docker build -t ai-inference .
#Run container:

docker run -p 8000:8000 ai-inference
#Open in browser:

http://localhost:8000
http://localhost:8000/predict
#Run Tests
python3 pytest
#Monitoring
The monitoring script checks the API every 30 seconds and logs failures.
It simulates an AWS CloudWatch alert.

python3 monitor.py
#Auto Recovery
The watchdog script restarts the container if it stops.

bash watchdog.sh
#CI/CD Pipeline
GitHub Actions pipeline runs tests and builds the Docker image automatically when code is pushed.

## Notes and Limitations

Due to time constraints and this being my first DevOps automation task given through a company for evaluation somehow there is pressure too but i did my best,I was not able to fully implement Terraform-based auto-scaling and advanced production monitoring.   

Instead, I implemented a Bash-based auto-recovery script and a Python monitoring script to simulate real-world failure detection and alerting.  

My focus was on correctly containerizing the application, building a working CI/CD pipeline, and demonstrating automation scripting skills.  

I am actively improving my skills in Terraform, Kubernetes, and cloud infrastructure automation.
