'''
import requests
from bs4 import BeautifulSoup
#Task1-->web scriper
def scrape_titles():
    url = "https://quotes.toscrape.com"
    response = requests.get(url)
    if response.status_code == 200:2
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("span", class_="text")1
        for i, quote in enumerate(quotes, start=1):
            print(f"{i}. {quote.text}")
    else:
        print("Failed to fetch the page")
scrape_titles()
'''
#Task2--> Data visualization
import pandas as pd
import plotly.express as px

# Step 1: Load Dataset
def load_dataset():
    # file_path = input("Enter the path to your CSV file: ")
    file_path = "Tasks/textfile.txt"
    try:
        df = pd.read_csv(file_path)
        print("\nData loaded successfully!\n")
        print(df.head())
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

# Step 2: Interactive Visualization Tool
def create_visualization(df):
    print("\nAvailable Columns:", list(df.columns))
    print("\nChoose a chart type:\n1. Scatter Plot\n2. Bar Chart\n3. Line Chart\n4. Pie Chart")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        x = input("Enter X-axis column: ")
        y = input("Enter Y-axis column: ")
        fig = px.scatter(df, x=x, y=y, title=f"Scatter Plot of {y} vs {x}")
    elif choice == "2":
        x = input("Enter X-axis column: ")
        y = input("Enter Y-axis column: ")
        fig = px.bar(df, x=x, y=y, title=f"Bar Chart of {y} vs {x}")
    elif choice == "3":
        x = input("Enter X-axis column: ")
        y = input("Enter Y-axis column: ")
        fig = px.line(df, x=x, y=y, title=f"Line Chart of {y} vs {x}")
    elif choice == "4":
        labels = input("Enter column name for labels (categorical): ")
        values = input("Enter column name for values (numerical): ")
        fig = px.pie(df, names=labels, values=values, title="Pie Chart")
    else:
        print("Invalid choice.")
        return

    fig.show()

# Step 3: Run the Tool
def main():
    df = load_dataset()
    if df is not None:
        create_visualization(df)

if __name__ == "__main__":
    main()



#Task3--> Automation Task
# import os
# import time
# import shutil
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler

# # Configuration
# DOWNLOADS = r"C:\Users\MAMANDURU JAGAN\Downloads"
# TARGET = r"D:\Automation_Downloads"

# # File type mapping
# TYPES = {
#     "Images": ['.jpg', '.jpeg', '.png', '.gif'],
#     "Documents": ['.pdf', '.docx', '.txt', '.csv'],
#     "Videos": ['.mp4', '.mkv', '.avi'],
#     "Scripts": ['.py', '.js', '.html', '.css'],
#     "Music": ['.mp3', '.wav', '.aac']
# }

# def organize_file(file_path):
#     """Move file to appropriate folder based on extension"""
#     filename = os.path.basename(file_path)
    
#     # Skip incomplete downloads
#     if filename.endswith(('.tmp', '.crdownload', '.part')):
#         return
    
#     time.sleep(1.5)  # Wait for download completion
#     ext = os.path.splitext(file_path)[1].lower()
    
#     # Find matching folder or use "Others"
#     folder = next((f for f, exts in TYPES.items() if ext in exts), "Others")
    
#     # Create folder and move file
#     folder_path = os.path.join(TARGET, folder)
#     os.makedirs(folder_path, exist_ok=True)
#     shutil.move(file_path, os.path.join(folder_path, filename))
#     print(f"✅ Moved to {folder}: {filename}")

# class FileHandler(FileSystemEventHandler):
#     """Handle file creation and movement events"""
#     def on_created(self, event):
#         if not event.is_directory:
#             organize_file(event.src_path)
    
#     def on_moved(self, event):
#         if not event.is_directory:
#             organize_file(event.dest_path)

# # Main execution
# if __name__ == "__main__":
#     os.makedirs(DOWNLOADS, exist_ok=True)
#     os.makedirs(TARGET, exist_ok=True)
    
#     observer = Observer()
#     observer.schedule(FileHandler(), path=DOWNLOADS, recursive=False)
#     observer.start()
    
#     try:
#         print(f"📁 Watching: {DOWNLOADS}")
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()
