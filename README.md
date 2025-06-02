# PsychdAI

An AI coaching app that builds and uses a dynamic knowledge graph per user.

## Tech Stack
- FastAPI (backend)
- PostgreSQL (auth DB)
- Neo4j (knowledge graph)
- React (frontend)
- Local LLM (via FastAPI API)

## Project Goals
- Dynamic user memory via Neo4j
- LLM grounded in structured personal knowledge


## ✅ Project Checklist: PsychdAI (4 Weeks)

### Week 1 – Backend (FastAPI + PostgreSQL + Auth)
- [x] Setup FastAPI and test `/ping` endpoint
- [x] Connect PostgreSQL via SQLAlchemy
- [x] Create User model and database schema
- [x] Implement password hashing with bcrypt
- [x] Build `/register` endpoint
- [x] Build `/login` endpoint and JWT token generation
- [x] Add JWT authentication dependency (`get_current_user`)
- [x] Build `/me` protected route
- [x] Test auth flow end-to-end (Postman or curl)
- [x] Refactor code into app/ folder

---

### Week 2 – Frontend (React + Chat UI)
- [ ] Set up React app (Vite or CRA) + routing
- [ ] Create login/register forms
- [ ] Connect forms to backend via fetch/axios
- [ ] Store JWT in localStorage and redirect on login
- [ ] Build chat UI with input + message history
- [ ] Connect chat input to backend `/chat` route
- [ ] Display assistant reply in UI
- [ ] Add message timestamps and username display
- [ ] Test full flow: Register → Login → Chat
- [ ] Stub LLM backend to prep for Week 3

---

### Week 3 – LLM + Neo4j
- [ ] Set up local LLM API (e.g. FastAPI around llama.cpp)
- [ ] Test sending user input → get LLM output
- [ ] Install & run Neo4j locally (Desktop or Docker)
- [ ] Connect Python backend to Neo4j
- [ ] Learn Cypher: CREATE, MATCH, MERGE
- [ ] Store simple triples (user → goal, trait, etc.)
- [ ] Query facts for a given user
- [ ] Transform facts into context string
- [ ] Inject context into prompt before sending to LLM
- [ ] Test memory-based replies

---

### Week 4 – Coaching Logic + Graph Evolution
- [ ] Add `is_current=false` for outdated traits/goals
- [ ] Track fact timestamps and sources
- [ ] Add mood logging schema + journal endpoint
- [ ] Connect mood/journal form to frontend
- [ ] Track goal progress over time (Cypher + UI)
- [ ] Show current user graph state in UI or as summary
- [ ] (Optional) Visualize graph with pyvis or D3.js
- [ ] Final test: Register → Chat → Memory updates
- [ ] Polish: error handling, docs, README
- [ ] Final GitHub commit + project wrap-up
