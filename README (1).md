# 🌾 Kadak Bhav

### AI-Powered Agricultural Market Linkage & Price Discovery Platform

> **Turning agricultural data into actionable selling decisions — Where, When & Whom to Sell.**

---

## 📌 Overview

**Kadak Bhav** is an AI-powered agricultural decision-support platform designed to help farmers make better selling decisions.

Instead of considering only the highest market price, Kadak Bhav aims to estimate the **expected net realization** by considering factors such as:

* Predicted market price
* Market arrivals and demand
* Transportation cost
* Storage cost
* Crop perishability
* Buyer reliability
* Selling time
* Farmer-specific constraints

The system combines **machine learning, data analytics, optimization, and market intelligence** to generate a personalized:

**WHERE → WHEN → WHOM**

recommendation.

---

## 🎯 Problem

Farmers often face:

* Price fluctuations across markets
* Lack of timely market information
* High transportation costs
* Crop perishability
* Difficulty identifying reliable buyers
* Fragmented market information
* Uncertainty about the best time and place to sell

A higher market price does not always mean higher profit.

### Example

```text
Market A
Price: ₹3500
Transport: ₹800
Expected Loss: ₹400

Net Realization: ₹2300
```

```text
Market B
Price: ₹3300
Transport: ₹200
Expected Loss: ₹100

Net Realization: ₹3000
```

Therefore:

> **Highest Price ≠ Highest Net Realization**

Kadak Bhav focuses on this decision-making gap.

---

## 💡 Proposed Solution

```text
Market Data
     +
Farmer Data
     +
Buyer Data
     +
Weather Data
     +
Logistics Data
     +
Historical Trends
     ↓
Data Processing & Validation
     ↓
Price Prediction
     ↓
Net Realization Calculation
     ↓
Market + Buyer + Time Ranking
     ↓
Personalized Recommendation
```

The goal is to help farmers determine:

* **WHERE** to sell
* **WHEN** to sell
* **WHOM** to sell to

---

## 🧠 Core Features

### 1. Price Prediction

Use machine learning to estimate future agricultural prices using features such as:

* Historical prices
* Market arrivals
* Demand indicators
* Crop
* Market
* Seasonality
* Recent price trends
* Weather information

**Initial model:** XGBoost Regression

---

### 2. Net Realization Engine

Instead of displaying only the predicted price:

```text
Expected Revenue
       -
Transportation Cost
       -
Storage Cost
       -
Expected Perishability Loss
       -
Other Costs
       =
Expected Net Realization
```

---

### 3. Perishability Intelligence

The system considers:

* Crop type
* Harvest date
* Storage availability
* Transportation time
* Environmental conditions
* Expected spoilage

This helps prevent choosing a distant market only because it offers a higher price.

---

### 4. Buyer Reliability

Potential buyer reliability indicators include:

* Payment completion
* Cancellation history
* Fulfillment history
* Dispute history
* Farmer feedback
* Transaction consistency

A reliability score can influence the final recommendation.

---

### 5. Logistics Intelligence

Transportation factors include:

* Distance
* Estimated travel time
* Transportation cost
* Route information
* Crop perishability

---

### 6. Where–When–Whom Recommendation

The recommendation engine evaluates:

```text
Market × Buyer × Selling Time
```

and ranks feasible options using expected net realization and risk-related factors.

---

### 7. Explainable Recommendations

Instead of only showing:

> "Sell at Market B"

the system aims to show:

```text
Recommended Market: Market B

✓ Better expected net realization
✓ Lower transportation cost
✓ Lower expected spoilage
✓ Reliable buyer
✓ Suitable selling time

Expected Net Realization: ₹XXXX
Confidence: XX%
Risk: Low / Medium / High
```

---

## 🏗️ System Architecture

```text
                         FARMER
                           │
                           ▼
                  Farmer Information
                           │
                           ▼
                  ┌────────────────┐
                  │  DATA SOURCES  │
                  └───────┬────────┘
                          │
       ┌──────────────────┼──────────────────┐
       ▼                  ▼                  ▼
  Market Data        Farmer/FPO Data     Buyer Data
       │                  │                  │
       └──────────────────┼──────────────────┘
                          │
                  Weather / Logistics
                          │
                          ▼
                 Data Validation
                          │
                          ▼
                  Data Processing
                          │
                          ▼
                Feature Engineering
                          │
                          ▼
                    XGBoost Model
                          │
                          ▼
                  Price Prediction
                          │
                          ▼
               Net Realization Engine
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
   Perishability      Logistics        Buyer Reliability
        │                 │                 │
        └─────────────────┼─────────────────┘
                          ▼
                Recommendation Engine
                          │
                          ▼
                 WHERE – WHEN – WHOM
                          │
                          ▼
                    Farmer Dashboard
```

---

## 🤖 Machine Learning

The initial machine learning problem is formulated as a **supervised regression problem**.

### Input

```text
Crop
Market
Historical Prices
Market Arrivals
Demand Indicators
Season
Month
Weather
Recent Price Trends
```

### Output

```text
Predicted Future Market Price
```

### Model

**XGBoost Regression**

XGBoost is selected as the initial model because the project primarily works with structured/tabular agricultural data.

---

## 📊 Model Evaluation

The model will be evaluated using:

### MAE

**Mean Absolute Error**

Measures the average absolute prediction error.

### RMSE

**Root Mean Squared Error**

Penalizes larger prediction errors more strongly.

### MAPE

**Mean Absolute Percentage Error**

Measures prediction error in percentage terms.

Additional evaluation may include:

* R² Score
* Confidence estimation

Time-based validation will be used where appropriate to reduce future-data leakage.

---

## 🌐 Multi-Source Data

Kadak Bhav is **not designed to depend on a single government data source**.

Potential sources include:

```text
Government / Public Data
          +
Market / Partner Data
          +
Farmer / FPO Data
          +
Buyer Data
          +
Weather Data
          +
Logistics Data
          ↓
   Data Fusion Layer
          ↓
 Validation & Reliability
          ↓
      AI Pipeline
```

If a data source becomes unavailable or stale, the system can use other validated sources or cached historical information, while reducing recommendation confidence when appropriate.

---

## 🛠️ Technology Stack

### Frontend

* React
* JavaScript
* HTML5
* CSS
* Charting libraries
* Map integration

### Backend

* Python
* FastAPI
* REST APIs

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Matplotlib

### Database

* PostgreSQL

### Deployment

* Docker
* Cloud deployment
* CI/CD

---

## 📁 Project Structure

```text
kadak-bhav/
│
├── frontend/
├── backend/
├── ml/
│   ├── data/
│   ├── notebooks/
│   ├── src/
│   └── models/
│
├── recommendation/
├── data_pipeline/
├── database/
├── tests/
├── docs/
│
├── README.md
├── .gitignore
├── .env.example
└── docker-compose.yml
```

---

## 🔄 Development Pipeline

```text
Data Collection
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Net Realization
      ↓
Recommendation Engine
      ↓
FastAPI
      ↓
Frontend
      ↓
Integration Testing
      ↓
Deployment
```

---

## 🚀 Development Roadmap

### Phase 1 — Data

* [ ] Collect agricultural datasets
* [ ] Clean data
* [ ] Standardize crop and market names
* [ ] Handle missing values
* [ ] Create processed dataset

### Phase 2 — Machine Learning

* [ ] Exploratory Data Analysis
* [ ] Feature Engineering
* [ ] Baseline model
* [ ] XGBoost model
* [ ] Model evaluation
* [ ] Model saving/loading

### Phase 3 — Recommendation Engine

* [ ] Net realization calculation
* [ ] Transportation cost
* [ ] Perishability estimation
* [ ] Buyer reliability
* [ ] Market ranking
* [ ] Where–When–Whom recommendation
* [ ] Confidence scoring

### Phase 4 — Backend

* [ ] PostgreSQL
* [ ] FastAPI
* [ ] Prediction API
* [ ] Recommendation API
* [ ] Market API
* [ ] Buyer API

### Phase 5 — Frontend

* [ ] Farmer dashboard
* [ ] Crop input
* [ ] Market comparison
* [ ] Recommendation interface
* [ ] Maps
* [ ] Charts
* [ ] Explainability panel

### Phase 6 — Deployment

* [ ] Dockerization
* [ ] Backend deployment
* [ ] Frontend deployment
* [ ] Database deployment
* [ ] Integration testing
* [ ] Performance testing

---

## 🧪 Testing

The project will include:

### Unit Testing

```text
Price Prediction
Net Realization
Perishability
Buyer Score
Market Ranking
```

### Integration Testing

```text
Frontend
   ↓
FastAPI
   ↓
Database
   ↓
ML Model
   ↓
Recommendation Engine
```

### End-to-End Testing

```text
Farmer Input
     ↓
AI Processing
     ↓
Market Analysis
     ↓
Recommendation
```

---

## 🔐 Reliability & Security

The system will follow basic security and reliability practices:

* Environment variables for secrets
* Input validation
* API authentication where required
* Database access controls
* Error handling
* Logging
* Data validation
* No hard-coded API keys

---

## 🎯 Expected Outcome

Kadak Bhav aims to transform agricultural market information into an actionable selling decision.

Instead of:

> **"Market A has the highest price."**

Kadak Bhav aims to answer:

> **"Considering price, transportation, perishability, buyer reliability and other constraints, which option is expected to provide the best net realization?"**

---

## 👥 Project

**Project Name:** Kadak Bhav
**Domain:** Agriculture & Artificial Intelligence
**Focus:** Market Linkage, Price Discovery & Decision Support

---

## 📜 License

This project is currently developed for educational, research and hackathon purposes.
