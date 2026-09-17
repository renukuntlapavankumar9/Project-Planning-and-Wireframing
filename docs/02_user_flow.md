# User Flow & Screen Map: FitPulse

## Primary Navigation Architecture
FitPulse uses a 5-tab Bottom Navigation Bar present across all primary screens.

[ Dashboard ] <---> [ Workout Track ] <---> [ Habit Log ] <---> [ Analytics ] <---> [ Profile ]


## Screen Specifications & Wireframe Mapping

### Screen 1: Dashboard (Home)
* **Header:** Avatar, Current Streak Badge (🔥), Notifications.
* **Primary Metric:** Circular ring progress indicator (Calories, Active Time, Steps).
* **CTA:** Full-width "Start Today's Workout" primary button.
* **Secondary View:** Horizontal card slider showing today's pending habits.

### Screen 2: Active Workout Tracking
* **Header:** Exercise Title, Active Workout Timer.
* **Interactive Area:** Exercise demonstration placeholder + Set/Rep input fields.
* **Control:** Large bottom-anchored "Complete Set" button designed for thumb reachability.

### Screen 3: Habit Logging
* **Header:** Weekly calendar view with visual completion badges.
* **List View:** Vertical habit list itemizing target frequency, current streak, and checkbox controls.
* **Action:** Floating Action Button (`+`) to register a new habit.

### Screen 4: Analytics & Progress
* **Segment Control:** Timeframe selector (Week / Month / Year).
* **Visuals:** Bar charts for workout volume and a grid-based consistency heatmap.
* **Metrics:** Summary statistics (Total Sets Completed, Total Active Hours).

### Screen 5: User Profile & Settings
* **Header:** User Avatar, Display Name, Current Fitness Goal Badge.
* **List:** Account Details, Goal Customization, App Preferences, Export Data CTA.