# KAFKA STARTED BY FLASK

Create Your env and run 
```
pip install -r requirements.txt
```

## ENVIRONMENT
set env service consumer and service publisher
```
cp .env.example .env
```

## STARTING CONSUMER
```
python service_consumer/consumer.py
```

## STARTING PUBLISHER
```
python service_publisher/manage.py server
```

## STARTING KAFKA
```
cd kafka
docker-compose up 
```

## CURL 
```
curl -X POST \
  http://127.0.0.1:5000/api/email \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Length: 293' \
  -H 'Content-Type: multipart/form-data; boundary=--------------------------371365105175957996588594' \
  -H 'Host: 127.0.0.1:5000' \
  -H 'Postman-Token: 9c45dab4-ccce-463a-99e4-fc2fe398189d,abc95c95-49d4-4679-8b5c-6d182bfe71bf' \
  -H 'User-Agent: PostmanRuntime/7.15.2' \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F email=mail@gmail.com \
  -F messages=Testing
```
