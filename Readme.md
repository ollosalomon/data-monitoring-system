# Data Monitoring System 🚀📊

[![GitHub stars](https://img.shields.io/github/stars/yourusername/data-monitoring-system?style=social)](https://github.com/yourusername/data-monitoring-system)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![MinIO](https://img.shields.io/badge/MinIO-C72E49?logo=minio&logoColor=white)](https://min.io/)
[![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?logo=prometheus&logoColor=white)](https://prometheus.io/)
[![Grafana](https://img.shields.io/badge/Grafana-F46800?logo=grafana&logoColor=white)](https://grafana.com/)

---

## 🌟 Project Overview

A comprehensive monitoring system with:

* 📥  **File generation and upload to MinIO (via Python FastAPI)** .
* 📊  **Metrics collection via Prometheus (from FastAPI)** .
* 📈  **Data visualization through Grafana dashboards** .

---

## 🏗️ Global Architecture

![Architecture Diagram](https://chatgpt.com/c/assets/img/architecture.png)

### 📊 Key Components

| Component            | Technologies     | Description                           |
| -------------------- | ---------------- | ------------------------------------- |
| **API Server** | FastAPI (Python) | Generates files and exposes metrics.  |
| **Storage**    | MinIO            | Stores CSV files uploaded by the API. |
| **Metrics**    | Prometheus       | Collects metrics from the API.        |
| **Dashboard**  | Grafana          | Visualizes Prometheus metrics.        |

---

## 📝 File Structure

```
/data-monitoring-system
│
├── docker-compose.yml
├── PythonApp/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
├── prometheus/
│   └── prometheus.yml
```

---

## 🚀 Quick Start

### 📋 Prerequisites

* Docker & Docker Compose installed.
* Python 3.10+ (for local development).

### 🔧 Build and Run

```bash
git clone https://github.com/ollosalomon/data-monitoring-system.git
cd data-monitoring-system
docker-compose up -d
```

---

## 🔗 Access Services

| Service    | URL                                          | Credentials       |
| ---------- | -------------------------------------------- | ----------------- |
| MinIO      | [http://localhost:9001](http://localhost:9001/) | admin/password123 |
| Prometheus | [http://localhost:9090](http://localhost:9090/) | N/A               |
| Grafana    | [http://localhost:3000](http://localhost:3000/) | grafana/grafana   |
| API Server | [http://localhost:8000](http://localhost:8000/) | N/A               |

---

## 📊 Monitoring & Visualization

### 📈 Prometheus

* Metrics collected by Prometheus: `requests_total`
* Access via: [http://localhost:9090](http://localhost:9090/)

### 📊 Grafana Dashboard

* Connect Grafana to Prometheus via Data Source.
* Add visualizations like Counter Metrics (`requests_total`).

---

## 📜 License & Contact

📄  **License** : [MIT](https://choosealicense.com/licenses/mit/)
📧  **Contact** : ollosalomon@gmail.com
👨💻  **Author** : [Pale Ollo Salomon](https://www.linkedin.com/in/ollo-salomon-pale-1a7576152/ "PALE OLLO SALOMON")

---

**[⬆ Back to top](https://chatgpt.com/c/67d572e1-dc7c-8001-abd2-ecd87a73667d#data-monitoring-system)**

*✨ Made with passion for data monitoring and visualization!*
