# digital-notepad-180896-180939

Notes Backend (Django + DRF)

Overview
- Provides RESTful CRUD endpoints for Notes.
- Runs in the preview environment on port 3001 (pre-configured by the platform).
- Swagger docs UI: /docs (e.g., http://localhost:3001/docs)

Environment variables
Provide the following via .env (handled by the orchestrator):
- DJANGO_SECRET_KEY: Secret key for Django.
- DEBUG: "True" or "False"

Example .env.example:
DJANGO_SECRET_KEY=change-me
DEBUG=True

Endpoints (base path /api/)
- GET /api/health/ -> {"message":"Server is up!"}
- POST /api/notes/
- GET /api/notes/
- GET /api/notes/{id}/
- PUT /api/notes/{id}/
- PATCH /api/notes/{id}/
- DELETE /api/notes/{id}/

Example curl
- Create:
  curl -s -X POST http://localhost:3001/api/notes/ -H "Content-Type: application/json" -d '{"title":"Test","content":"Hello"}'
- List:
  curl -s http://localhost:3001/api/notes/
- Retrieve:
  curl -s http://localhost:3001/api/notes/1/
- Update:
  curl -s -X PUT http://localhost:3001/api/notes/1/ -H "Content-Type: application/json" -d '{"title":"Updated","content":"World"}'
- Patch:
  curl -s -X PATCH http://localhost:3001/api/notes/1/ -H "Content-Type: application/json" -d '{"content":"Patched"}'
- Delete:
  curl -s -X DELETE http://localhost:3001/api/notes/1/

Development notes
- Apply migrations (CI/preview usually runs these automatically):
  python notes_backend/manage.py makemigrations
  python notes_backend/manage.py migrate

- Optional seed data:
  python notes_backend/manage.py seed_notes

- Run tests:
  python notes_backend/manage.py test

CORS is permissive for development via django-cors-headers.
