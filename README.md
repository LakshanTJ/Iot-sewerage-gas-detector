# IoT Sewerage Multi-Gas Detection System

An IoT-based multi-gas detection and monitoring system designed for sewage-side and other high-risk environments. The system provides early warning of hazardous gas exposure and poor air conditions using multiple gas sensors connected to an ESP32, with real-time alerts and cloud-based monitoring.

---

## 🚨 Problem Statement

People living near sewage systems and sanitation workers are frequently exposed to harmful and sometimes fatal gases such as hydrogen sulfide, methane, and carbon monoxide.  
Traditional manual checks are unsafe, infrequent, and unreliable, leading to health risks, accidents, and fatalities.

---

## 💡 Proposed Solution

This project implements a **real-time IoT gas monitoring system** that:
- Continuously monitors multiple toxic and hazardous gases
- Detects unsafe environmental conditions early
- Sends alerts for timely human intervention
- Stores data for long-term analysis and reporting

The system is intended for **early warning and safety monitoring**, not certified industrial-grade measurement.

---

## 🔍 Parameters Monitored

- Carbon Dioxide (CO₂)
- Hydrogen Sulfide (H₂S)
- Carbon Monoxide (CO)
- Ammonia (NH₃)
- Nitrogen Dioxide (NO₂)
- Methane (CH₄)
- Formaldehyde (CH₂O)
- Volatile Organic Compounds (VOCs)
- Temperature
- Humidity

---

## 🧩 Hardware Components

| Component | Purpose |
|---------|--------|
| ESP32 | Main controller and IoT connectivity |
| MH-Z19B | CO₂ detection (NDIR sensor) |
| MQ-136 | Hydrogen sulfide (H₂S) detection |
| MiCS-6814 | CO, NO₂, NH₃ detection |
| ZE08-CH₂O | Formaldehyde detection |
| MQ-4 | Methane (CH₄) detection |
| SGP30 | VOC monitoring |
| DHT22 | Temperature & humidity |
| Power Supply | System power, 7.4V Battery |

---

## 🖥️ Software Overview

- Embedded firmware: Arduino framework (ESP32)
- Communication: Wi-Fi
- Data handling: Cloud server / web dashboard
- Alerts: Threshold-based notifications (web)

---

## 🏗️ System Architecture
Gas Sensors & DHT22 → ESP32 → Cloud Server → Web Dashboard / Alerts
---

## ⚠️ Limitations

- MQ-series and MiCS sensors are cross-sensitive and require calibration.
- Readings are influenced by temperature, humidity, and sensor aging.
- System is designed for **trend monitoring and early warning**, not laboratory or industrial certification.

---

## 🌍 Applications

- Sewerage systems
- Homes near drainage lines
- Sanitation worker safety
- Hotels and restaurants (gas leak detection)
- Industrial and agricultural environments

---

## 🔮 Future Improvements

- AI-based gas trend prediction
- Battery-powered deployment
- Mobile application integration
- Automatic ventilation and safety system control
- Community-level monitoring dashboards


