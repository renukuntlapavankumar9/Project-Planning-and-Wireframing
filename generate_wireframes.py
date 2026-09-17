import os
from PIL import Image, ImageDraw, ImageFont

# Ensure assets/wireframes directory exists
output_dir = os.path.join("assets", "wireframes")
os.makedirs(output_dir, exist_ok=True)

# Common dimensions & theme
WIDTH, HEIGHT = 375, 812  # Standard mobile viewport ratio
BG_COLOR = "#F8F9FA"
CARD_BG = "#FFFFFF"
TEXT_COLOR = "#111827"
ACCENT_COLOR = "#3B82F6"
BORDER_COLOR = "#E5E7EB"

def draw_device_frame(draw):
    # Device outer border & status bar placeholder
    draw.rectangle([0, 0, WIDTH-1, HEIGHT-1], outline="#D1D5DB", width=2)
    # Notch/Dynamic Island
    draw.rounded_rectangle([130, 10, 245, 30], radius=10, fill="#000000")
    # Bottom Navigation Bar
    draw.rectangle([0, HEIGHT-60, WIDTH, HEIGHT], fill=CARD_BG, outline=BORDER_COLOR)
    
    # Bottom Nav Icons
    nav_labels = ["Home", "Track", "Habits", "Stats", "Profile"]
    for i, label in enumerate(nav_labels):
        x = i * (WIDTH / 5) + 20
        draw.text((x, HEIGHT-40), label, fill="#6B7280")

def create_wireframe_1():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_device_frame(draw)
    
    # Header
    draw.text((20, 50), "Dashboard", fill=TEXT_COLOR)
    draw.ellipse([WIDTH-50, 45, WIDTH-20, 75], fill="#D1D5DB") # Avatar
    
    # Main Progress Ring Placeholder
    draw.ellipse([87, 120, 287, 320], outline=ACCENT_COLOR, width=12)
    draw.text((140, 200), "75% Completed", fill=TEXT_COLOR)
    
    # Quick Start Button
    draw.rounded_rectangle([20, 350, WIDTH-20, 400], radius=8, fill=ACCENT_COLOR)
    draw.text((115, 368), "START WORKOUT", fill="#FFFFFF")
    
    # Today's Habits Header
    draw.text((20, 430), "Today's Habits", fill=TEXT_COLOR)
    
    # Habit Cards
    for i in range(3):
        y = 460 + (i * 65)
        draw.rounded_rectangle([20, y, WIDTH-20, y+55], radius=8, fill=CARD_BG, outline=BORDER_COLOR)
        draw.rectangle([35, y+15, 60, y+40], outline=ACCENT_COLOR, width=2)
        draw.text((75, y+20), f"Habit Task #{i+1}", fill=TEXT_COLOR)

    img.save(os.path.join(output_dir, "01_dashboard.png"))

def create_wireframe_2():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_device_frame(draw)
    
    draw.text((20, 50), "< Workout Mode", fill=TEXT_COLOR)
    draw.text((WIDTH-80, 50), "00:24:15", fill=ACCENT_COLOR)
    
    # Visual Placeholder / Video Guide Frame
    draw.rounded_rectangle([20, 90, WIDTH-20, 240], radius=10, fill="#E5E7EB")
    draw.text((130, 155), "[ Exercise Guide ]", fill="#6B7280")
    
    # Exercise Set Inputs
    draw.text((20, 260), "Barbell Bench Press", fill=TEXT_COLOR)
    for i in range(3):
        y = 300 + (i * 55)
        draw.rounded_rectangle([20, y, WIDTH-20, y+45], radius=6, fill=CARD_BG, outline=BORDER_COLOR)
        draw.text((35, y+15), f"Set {i+1}", fill=TEXT_COLOR)
        draw.text((150, y+15), "10 Reps", fill="#6B7280")
        draw.text((260, y+15), "60 kg", fill="#6B7280")

    # Complete Set CTA
    draw.rounded_rectangle([20, HEIGHT-130, WIDTH-20, HEIGHT-80], radius=8, fill=ACCENT_COLOR)
    draw.text((130, HEIGHT-110), "LOG SET", fill="#FFFFFF")

    img.save(os.path.join(output_dir, "02_workout_tracker.png"))

def create_wireframe_3():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_device_frame(draw)
    
    draw.text((20, 50), "Habit Log", fill=TEXT_COLOR)
    
    # Calendar Strip
    for i in range(7):
        x = 20 + (i * 48)
        draw.rounded_rectangle([x, 90, x+40, 140], radius=6, fill=CARD_BG if i != 3 else ACCENT_COLOR, outline=BORDER_COLOR)
        draw.text((x+10, 105), f"D{i+1}", fill=TEXT_COLOR if i != 3 else "#FFFFFF")

    # Habit Checklist
    for i in range(5):
        y = 170 + (i * 65)
        draw.rounded_rectangle([20, y, WIDTH-20, y+50], radius=8, fill=CARD_BG, outline=BORDER_COLOR)
        draw.rectangle([35, y+15, 55, y+35], fill=ACCENT_COLOR if i < 2 else None, outline=ACCENT_COLOR, width=2)
        draw.text((70, y+18), f"Daily Habit Target #{i+1}", fill=TEXT_COLOR)

    # FAB (+)
    draw.ellipse([WIDTH-70, HEIGHT-130, WIDTH-20, HEIGHT-80], fill=ACCENT_COLOR)
    draw.text((WIDTH-50, HEIGHT-112), "+", fill="#FFFFFF")

    img.save(os.path.join(output_dir, "03_habit_log.png"))

def create_wireframe_4():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_device_frame(draw)
    
    draw.text((20, 50), "Analytics & Progress", fill=TEXT_COLOR)
    
    # Toggle Segment
    draw.rounded_rectangle([20, 90, WIDTH-20, 130], radius=8, fill="#E5E7EB")
    draw.text((50, 105), "Week", fill=ACCENT_COLOR)
    draw.text((160, 105), "Month", fill="#6B7280")
    draw.text((270, 105), "Year", fill="#6B7280")
    
    # Bar Chart Area
    draw.rounded_rectangle([20, 150, WIDTH-20, 350], radius=8, fill=CARD_BG, outline=BORDER_COLOR)
    for i in range(7):
        x = 40 + (i * 45)
        h = 50 + (i * 20) % 120
        draw.rectangle([x, 330-h, x+25, 330], fill=ACCENT_COLOR)

    # Metrics Summary
    draw.rounded_rectangle([20, 370, 175, 460], radius=8, fill=CARD_BG, outline=BORDER_COLOR)
    draw.text((30, 385), "Total Volume", fill="#6B7280")
    draw.text((30, 415), "12,450 kg", fill=TEXT_COLOR)
    
    draw.rounded_rectangle([195, 370, WIDTH-20, 460], radius=8, fill=CARD_BG, outline=BORDER_COLOR)
    draw.text((205, 385), "Active Hours", fill="#6B7280")
    draw.text((205, 415), "14.2 Hours", fill=TEXT_COLOR)

    img.save(os.path.join(output_dir, "04_analytics.png"))

def create_wireframe_5():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_device_frame(draw)
    
    draw.text((20, 50), "User Profile", fill=TEXT_COLOR)
    
    # Avatar & Details
    draw.ellipse([WIDTH//2 - 40, 90, WIDTH//2 + 40, 170], fill="#D1D5DB")
    draw.text((WIDTH//2 - 45, 185), "Alex Johnson", fill=TEXT_COLOR)
    draw.text((WIDTH//2 - 50, 205), "Goal: Muscle Gain", fill=ACCENT_COLOR)
    
    # Preference Options
    options = ["Account Details", "Target & Goals", "App Preferences", "Export Fitness Data", "Logout"]
    for i, option in enumerate(options):
        y = 250 + (i * 55)
        draw.rounded_rectangle([20, y, WIDTH-20, y+45], radius=6, fill=CARD_BG, outline=BORDER_COLOR)
        draw.text((35, y+15), option, fill=TEXT_COLOR)

    img.save(os.path.join(output_dir, "05_profile.png"))

if __name__ == "__main__":
    create_wireframe_1()
    create_wireframe_2()
    create_wireframe_3()
    create_wireframe_4()
    create_wireframe_5()
    print("Successfully generated 5 wireframe PNGs in assets/wireframes/")