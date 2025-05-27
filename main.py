import tkinter as tk
import random
from math import cos, sin, pi

class HeartPostcard:
    def __init__(self, root):
        self.root = root
        self.root.title("Valentine's Postcard")
        self.root.geometry("500x500")
        self.root.configure(bg="#ffe6f0")  # Softer pink background

        # Create canvas
        self.canvas = tk.Canvas(root, width=500, height=500, bg="#ffe6f0", highlightthickness=0)
        self.canvas.pack(expand=True, fill="both")

        # Animation settings
        self.hearts = []
        self.max_hearts = 30
        self.animation_speed = 50  # ms between updates

        # Draw initial hearts
        self.draw_hearts()

        # Add text with shadow effect
        self.create_text_with_shadow()

        # Bind mouse click to add new heart
        self.canvas.bind("<Button-1>", self.add_heart_on_click)

        # Start animation
        self.animate_hearts()

    def create_heart_points(self, x, y, size):
        """Generate smoother heart shape using parametric equations"""
        points = []
        for t in range(0, 360, 10):  # More points for smoother curve
            t_rad = t * pi / 180
            px = x + size * 16 * (sin(t_rad) ** 3)
            py = y - size * (13 * cos(t_rad) - 5 * cos(2 * t_rad) - 2 * cos(3 * t_rad) - cos(4 * t_rad))
            points.extend([px, py])
        return points

    def draw_heart(self, x, y, size, color):
        """Draw a single heart and return its canvas ID"""
        points = self.create_heart_points(x, y, size)
        return self.canvas.create_polygon(points, fill=color, outline="#333333", smooth=True)

    def draw_hearts(self):
        """Draw initial set of hearts"""
        colors = ["#ff4d4d", "#ff80bf", "#cc0066", "#ff99cc"]  # More vibrant colors
        for _ in range(self.max_hearts):
            x = random.randint(50, 450)
            y = random.randint(50, 450)
            size = random.uniform(0.5, 1.5)  # Smoother size variation
            color = random.choice(colors)
            heart_id = self.draw_heart(x, y, size, color)
            self.hearts.append({"id": heart_id, "x": x, "y": y, "size": size, "dx": random.uniform(-0.5, 0.5), "dy": random.uniform(-0.5, 0.5)})

    def create_text_with_shadow(self):
        """Add text with a shadow effect"""
        shadow_offset = 3
        self.canvas.create_text(252, 252, text="Ich liebe dich", font=("Arial", 28, "bold"), fill="#4d0000")
        self.canvas.create_text(250, 250, text="Ich liebe dich", font=("Arial", 28, "bold"), fill="#ffffff")

    def add_heart_on_click(self, event):
        """Add a new heart at mouse click position"""
        colors = ["#ff4d4d", "#ff80bf", "#cc0066", "#ff99cc"]
        size = random.uniform(0.5, 1.5)
        heart_id = self.draw_heart(event.x, event.y, size, random.choice(colors))
        self.hearts.append({"id": heart_id, "x": event.x, "y": event.y, "size": size, "dx": random.uniform(-0.5, 0.5), "dy": random.uniform(-0.5, 0.5)})

    def animate_hearts(self):
        """Animate hearts with slight movement"""
        for heart in self.hearts:
            heart["x"] += heart["dx"]
            heart["y"] += heart["dy"]
            # Bounce off canvas edges
            if heart["x"] < 50 or heart["x"] > 450:
                heart["dx"] *= -1
            if heart["y"] < 50 or heart["y"] > 450:
                heart["dy"] *= -1
            # Update heart position
            self.canvas.delete(heart["id"])
            heart["id"] = self.draw_heart(heart["x"], heart["y"], heart["size"], "#ff4d4d")
        self.canvas.after(self.animation_speed, self.animate_hearts)

if __name__ == "__main__":
    root = tk.Tk()
    app = HeartPostcard(root)
    root.mainloop()
