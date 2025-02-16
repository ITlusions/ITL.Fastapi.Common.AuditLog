# FastAPI Audit Logging

Deze README beschrijft hoe je de audit logging functionaliteit in een FastAPI-applicatie kunt gebruiken.

## 📌 Functies
- ✅ Middleware voor audit logging 
- ✅ Automatische **Request-ID** en **Correlation-ID**
- ✅ Server hostname en applicatieversie in response headers
- ✅ Aanpasbare auditlog evenementen
- ✅ Eenvoudig te integreren in bestaande FastAPI-applicaties

---

## 📦 Installatie

1. **Installeer de vereisten**:
   ```bash
   pip install fastapi uvicorn
   ```

2. **Voeg de audit logging middleware toe aan jouw applicatie**

---

## 🚀 Gebruik

### 1️⃣ **Middleware activeren**
Voeg de middleware toe aan je FastAPI-applicatie:

```python
from fastapi import FastAPI
from middleware import AuditLogMiddleware

app = FastAPI()
app.add_middleware(AuditLogMiddleware)
```

### 2️⃣ **Audit event loggen**
Je kunt een specifiek audit event loggen met de `log_audit_event` functie:

```python
from auditlog import log_audit_event

log_audit_event("gebruiker123", "login_poging", "Gebruiker heeft geprobeerd in te loggen")
```

### 3️⃣ **API Requests en logs**

**Voorbeeldverzoek:**
```bash
curl -X GET "http://localhost:8000/" -H "X-Correlation-ID: abc-123"
```

**Response Headers:**
```
X-Request-ID: d39b55f2-4c11-4a60-8e51-bb2e2c6e0d19
X-Correlation-ID: abc-123
X-Server-Hostname: mijnserver
X-App-Version: 1.0.0
```

**Log Output:**
```
INFO: Request: GET http://localhost:8000/ | Request ID: d39b55f2-4c11-4a60-8e51-bb2e2c6e0d19 | Correlation ID: abc-123
INFO: Audit Event | Gebruiker: anoniem | Actie: toegang_home | Details: Gebruiker heeft de startpagina bezocht
INFO: Response: 200 | Request ID: d39b55f2-4c11-4a60-8e51-bb2e2c6e0d19 | Correlation ID: abc-123 | Duration: 0.02s
```

---

## 🎯 Samenvatting
✅ **Registreert alle aanvragen en reacties**
✅ **Unieke request en correlation ID's**
✅ **Applicatieversie en hostname toegevoegd aan response headers**
✅ **Aanpasbare audit event logging**
✅ **Eenvoudig te integreren**

🚀 **Gebruik deze logging om je applicatie beter te monitoren en beveiligen!**

