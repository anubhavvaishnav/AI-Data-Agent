import sqlite3
import os

# Just a quick script to set up a local sqlite db for testing
def init_db():
    db_name = "plant_sensors.db"
    
    # Delete old db if it exists so we don't get duplicate data errors
    if os.path.exists(db_name):
        os.remove(db_name)
        
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    # Create tables
    cur.execute('''CREATE TABLE machines (
        id INTEGER PRIMARY KEY,
        name TEXT,
        plant_location TEXT
    )''')

    cur.execute('''CREATE TABLE sensor_logs (
        log_id INTEGER PRIMARY KEY,
        machine_id INTEGER,
        temp_c REAL,
        vibration_hz REAL,
        status TEXT,
        timestamp TEXT
    )''')

    # Insert some mock data
    machines = [
        (1, 'CNC_Mill_01', 'Plant_A'),
        (2, 'Hydraulic_Press_02', 'Plant_A'),
        (3, 'Metal_3D_Printer_01', 'Plant_B')
    ]
    cur.executemany('INSERT INTO machines VALUES (?,?,?)', machines)

    logs = [
        (1, 1, 75.5, 45.2, 'Normal', '2023-10-01 08:00'),
        (2, 1, 92.1, 55.8, 'Overheating', '2023-10-01 10:00'),
        (3, 2, 40.0, 30.1, 'Normal', '2023-10-01 08:00'),
        (4, 3, 85.0, 60.0, 'Maintenance Required', '2023-10-01 10:00'),
        (5, 1, 78.0, 46.0, 'Normal', '2023-10-01 12:00')
    ]
    cur.executemany('INSERT INTO sensor_logs VALUES (?,?,?,?,?,?)', logs)

    conn.commit()
    conn.close()
    print(f"Database '{db_name}' initialized with mock data.")

if __name__ == "__main__":
    init_db()
