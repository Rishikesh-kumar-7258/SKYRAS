# SKYRAS

**Bridging the Gap Between Government Schemes and Rural Beneficiaries**

---

## Table of Contents

1. [Overview](#overview)
2. [Problem Statement](#problem-statement)
3. [Our Solution](#our-solution)
4. [Tech Stack](#tech-stack)
5. [Features](#features)
6. [Architecture](#architecture)
7. [Getting Started](#getting-started)
    - Installation
    - Running Locally
8. [Contributing](#contributing)
9. [Team](#team)
10. [License](#license)

---

## 1. Overview

**SKYRAS** is an initiative to ensure that the benefits of government welfare schemes effectively reach the rural poor. Our vision: a system where beneficiaries can self-register using a unique identifier and be seamlessly tracked across schemes they qualify for.

---

## 2. Problem Statement

Currently, beneficiary selection for welfare schemes follows a _top-down_ approach. Ministries and agencies determine eligibility, which can lead to delays and omissions—leaving many deserving individuals without access to benefits.

We aim to flip this: allowing beneficiaries to register themselves and be proactively considered for schemes through reliable tracking.

---

## 3. Our Solution

-   **User-centric registration**: Beneficiaries use a unique ID to register, enabling direct scheme matching.
-   **Unique Identifier Tracking**: Ensures clarity and avoids duplication across schemes.
-   **Centralized dashboard**: Administrators and NGOs can monitor applicant progress and scheme eligibility.

---

## 4. Tech Stack

| Layer    | Technologies                    |
| -------- | ------------------------------- |
| Frontend | React.js, JavaScript, HTML, CSS |
| Backend  | Django (Python)                 |
| Database | MongoDB                         |

---

## 5. Features _(Planned / In-Progress)_

-   Beneficiary registration portal with unique ID issuance
-   Admin dashboard for tracking scheme enrollment
-   RESTful API integration for interoperability
-   Real-time eligibility filtering
-   Extensible architecture for future module additions

---

## 6. Architecture

1. **Frontend (React)**

    - Handles user and admin interfaces
    - Communicates with the backend APIs

2. **Backend (Django)**

    - Core business logic, authentication, data validation
    - Exposes RESTful endpoints

3. **Database (MongoDB)**
    - Stores beneficiary profiles, scheme information, tracking logs

---

## 7. Getting Started

### Prerequisites

-   Python 3.x
-   Node.js / npm
-   MongoDB instance (local or remote)

### Installation

```bash
# Clone the repo
git clone https://github.com/Rishikesh-kumar-7258/SKYRAS.git
cd SKYRAS

# Backend setup
cd backend
pip install -r requirements.txt

# Frontend setup (in separate terminal)
cd ../frontend
npm install
```

### Running Locally

```bash
# Start backend
cd backend
python manage.py migrate
python manage.py runserver

# Start frontend
cd ../frontend
npm start
```

Both services should now be running—Django on `http://localhost:8000` and React on `http://localhost:3000`.

---

## 8. Contributing

We welcome your contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to your fork: `git push origin feature/YourFeature`
5. Open a Pull Request describing your improvements

Be sure to adhere to our code style and include tests where appropriate.

---

## 9. Team

| Name                 | Role                          |
| -------------------- | ----------------------------- |
| Karn Tiwari (Leader) | Frontend Developer & Research |
| Abhilasha Kumari     | Frontend Developer            |
| Yukta Watti          | UI Designer                   |
| Shudhanshu Kumar     | Documentation & Research      |
| Shreyash Gaurav      | Documentation & UI Support    |
| Rishikesh Kumar      | Full Stack Developer          |

---

## 10. License

This project is currently **unlicensed**. Please include a suitable open-source license (e.g., MIT, Apache 2.0) if you’d like to clarify usage rights and community contributions.

---

## Final Thoughts

SKYRAS tackles a critical challenge—ensuring fair access to government welfare for those who need it most. With streamlined registration and centralized tracking, it’s a step toward a more inclusive and efficient delivery of benefits.

Let me know if you'd like help expanding sections or adding visuals, documentation templates, or deployment guides!
