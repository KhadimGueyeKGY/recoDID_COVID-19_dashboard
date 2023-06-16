# recoDID_COVID-19_dashboard


https://www.ebi.ac.uk/ena/pathogens/v2/cohorts

## Usage: 
```
git clone https://github.com/KhadimGueyeKGY/recoDID_COVID-19_dashboard.git
cd recoDID_COVID-19_dashboard
python main.py
```

## Docker commands 

```
docker build -t khadimgueyekgy/ena-cohort-dashboard .
docker run -d --rm --interactive --tty --init --publish=3000:8050 --name ena-cohort-dashboard khadimgueyekgy/ena-cohort-dashboard
docker logs ena-cohort-dashboard
docker exec -it ena-cohort-dashboard bash
docker push khadimgueyekgy/ena-cohort-dashboard:latest
```

## view

  * http://127.0.0.1:3000/Cohort-Dashboard 

## Docker images 

  * https://hub.docker.com/r/khadimgueyekgy1/ena-cohort-dashboard
  * https://hub.docker.com/r/khadimgueyekgy/ena-cohort-dashboard
  


