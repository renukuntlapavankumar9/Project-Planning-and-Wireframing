# FitPulse — Mobile App Planning & Wireframing

[![Task Status](https.img.shields.io/badge/Week_1-Completed-success)]()
[![Deliverable](https://img.shields.io/badge/Format-PDF_Report-blue)]()

FitPulse is a modern, lightweight health, fitness, and daily habit tracking mobile application concept. This repository contains the complete Week 1 submission for the App Development Internship, encompassing project scoping, user interaction architecture, digital UI wireframes, and human-computer interaction (HCI) rationale.

---

## 📌 Deliverable Overview

The primary objective of this project is to model the preliminary planning phase of the mobile application development lifecycle (MADLC). 

* **App Concept:** FitPulse (AI-Powered Fitness & Habit Tracker)
* **Core Deliverable:** `output/Week1_Project_Planning_and_Wireframing.pdf`
* **UX Rationale Length:** 500+ Words
* **Screen Wireframes:** 5 Digital Screen Layouts

---

## 🚀 Key Features & Navigation Flow

FitPulse utilizes a persistent 5-tab bottom navigation hierarchy to reduce interaction friction and keep core utilities within single-tap reach:

1. **Dashboard (Home):** Real-time daily progress ring (calories/steps), active habit card sliders, and quick-start workout triggers.
2. **Active Workout Logger:** High-contrast exercise execution workspace with live timers and rep/set inputs.
3. **Habit Logging:** Weekly calendar view with interactive streak counters and completion checkboxes.
4. **Analytics & Progress:** Interactive timeframe toggles, volume bar charts, and consistency heatmaps.
5. **User Profile & Settings:** Centralized configuration for targets, physical metrics, and data exports.

---

## 🎨 UX Design Principles Applied

* **Fitts's Law & Touch Ergonomics:** High-frequency call-to-action (CTA) controls are anchored in the lower third of the viewport ("The Thumb Zone") to minimize reach strain.
* **Progressive Disclosure:** Advanced analytics are separated from daily logging interfaces to prevent cognitive overload for first-time users.
* **Jakob's Law:** Standardized bottom navigation icons leverage familiar mental models from established mobile applications.
* **Direct Feedback Loops:** Immediate visual state updates (progress fills and streak increments) reinforce positive behavioral habits.

---

## 📁 Repository Structure

```text
fitpulse/
├── assets/
│   └── wireframes/          # Generated digital UI wireframe PNGs
│       ├── 01_dashboard.png
│       ├── 02_workout_tracker.png
│       ├── 03_habit_log.png
│       ├── 04_analytics.png
│       └── 05_profile.png
├── docs/                    # Modular source documentation
│   ├── 01_project_plan.md
│   ├── 02_user_flow.md
│   └── 03_ux_rationale.md
├── output/                  # Final compiled PDF submission file
│   └── Week1_Project_Planning_and_Wireframing.pdf
├── generate_wireframes.py   # Python script to render wireframe layouts
├── generate_pdf.py          # ReportLab script compiling final PDF report
├── .gitignore
└── README.md