curl -X POST http://localhost/users -H "Content-Type: application/json" -d '{"name": "Vladimir", "email": "admin@example.com"}'

curl http://localhost/users

curl -X PUT http://localhost/users/1 -H "Content-Type: application/json" -d '{"email": "new@example.com"}'

curl -X DELETE http://localhost/users/1

curl http://localhost/users

curl http://localhost/users?check=real