curl -X POST http://localhost/users -H "Content-Type: application/json" -d '{"name": "Vladimir", "email": "admin@example.com"}'

curl http://localhost/users

curl -X PUT http://localhost/users/1 -H "Content-Type: application/json" -d '{"email": "new@example.com"}'

curl -X DELETE http://localhost/users/1

curl http://localhost/users

curl http://localhost/users?check=real


docker logs dz5-web-1
docker exec -it dz5-db-1 psql -U user -d flask_db
\dt
\d "user"

wrk -t12 -c400 -d180s http://localhost/users



1. ansible-playbook -i ansible/inventory.ini ansible/deploy.yml

2. https://192.168.122.239:30696

3. sudo /usr/local/bin/k3s kubectl logs -l app=flask-backend -n default

4. curl -X POST http://192.168.122.239:30080/users -H "Content-Type: application/json" -d '{"name": "Vladimir", "email": "vlad@sirius.ru", "phone": "79001234567"}'

4.2. curl -v http://192.168.122.239:30080/users

5. sudo /usr/local/bin/k3s kubectl describe pod -l app=flask-backend -n default | grep Image:
