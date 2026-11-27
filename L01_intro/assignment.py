"""
ENPM605 L01 — Python Variables: References, Identity, Mutability, Bytecode

Objective:
    Show, with my own experiments, how Python variables really work:
    1. Variables are references (name tags), not boxes. Two names can
       point to the same object (aliasing).
    2. The difference between == (same value) and `is` (same object).
    3. Mutable objects (list) change in place; immutable objects (int)
       create a new object when "changed", checked using id().
    4. Python compiles source code to bytecode before running it,
       inspected using the dis module.

Why it matters for robotics:
    Shared references can silently corrupt sensor data or robot state
    when two parts of the code modify the same list.

Author: Rohit Hindurao
Date:   27 Nov 2026
"""
import dis

# Task 1
wheel_speeds = [25, 30, 28]
backup = wheel_speeds
backup.append(20)
print("Wheel_speeds = ", wheel_speeds)
print("BACKUP = ", backup)
print("wheel speeds is backup: ", wheel_speeds is backup)
# Both names point to the SAME list object in memory.
# b = a copies the reference, not the list.

safe_backup = wheel_speeds.copy()
safe_backup.append(66)
print("wheel speeds : ", wheel_speeds)
print("Safe backup : ", safe_backup)
print("Safe backup is wheel speed ", safe_backup is wheel_speeds)

# Part A: backup = wheel_speeds copied the REFERENCE, so both names
#         pointed to the same list object -> changes showed in both, `is` was True.
# Part B: .copy() created a NEW list object with the same contents,
#         so changing safe_backup did not affect wheel_speeds -> `is` is False.

# Task 2
# == compares VALUES (are the contents equal?)
# is compares IDENTITY (is it the exact same object?)
# Rule: use == for values; use `is` only to check None (PEP 8).
left_lidar = [1.2, 0.8, 0.5]
right_lidar = [1.2, 0.8, 0.5]
print("left lidar == to right lidar: ", left_lidar == right_lidar)
print("left lidar is right lidar: ", left_lidar is right_lidar)
target = None
print("target is none: ", target is None)

# task 3
# Part A
battery = 80
print(id(battery))
id_before = id(battery)
battery += 5
print(id(battery))
id_after = id(battery)

print("before id and after id are same: ", id_before == id_after)

# Part B
waypoints = [1, 2]
print(id(waypoints))
waypoint_old_id = id(waypoints)
waypoints += [3]
print(id(waypoints))
waypoint_new_id = id(waypoints)
print("waypoint old id is new id : ", waypoint_old_id == waypoint_new_id)

# Task 4
dis.dis("x = 2 + 3")
dis.dis("x = a + b") 
