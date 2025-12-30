# Shared Room Expense Manager

A **professional, console-based expense management system** designed for **shared rooms and bachelor accommodations**.  
This project focuses on **data consistency, persistence, and real-world financial workflows**, making it suitable for **college evaluation, internships, and portfolio showcasing**.

---

##  Key Highlights

- **Dynamic expense tracking** with unique Expense IDs
- **Member-wise spending analysis** (auto-updated on edit/delete)
- **Monthly budget lifecycle management**
- **Persistent configuration recovery** (budget & month survive restarts)
- **Accurate remaining-days calculation** using calendar-aware logic
- **Full CRUD operations** (Create, Read, Update, Delete)
- **Defensive programming** for stability and error prevention

---

## Problem Statement

In shared rooms, improper tracking of daily expenses often leads to budget exhaustion before month-end. Manual calculations lack transparency and consistency, especially when expenses are updated or corrected.

This project provides a **structured, reliable, and maintainable solution** to manage shared expenses effectively.

---

## Core Concepts & Fundamentals Used

- **Modular Programming**
- **File Handling & Persistence**
- **CRUD Operations**
- **Dynamic Data Structures**
- **Defensive Programming**
- **Calendar-based Date Logic**
- **Single Source of Truth Design**
- **Configuration Management**

---

##  Features

### 🔹 Expense Management
- Add new expenses with validation
- Prevent duplicate Expense IDs
- Update expense amount or payer name
- Delete incorrect expense entries

### 🔹 Budget & Time Management
- Monthly budget initialized once per cycle
- Budget re-initialized only on monthly reset
- Remaining balance calculation
- Remaining days calculation based on month length (28 / 30 / 31 days)

### 🔹 Member-wise Analysis
- Automatically computes how much each member spent
- Always consistent after updates or deletions
- No redundant or duplicated data storage

### 🔹 Persistence & Recovery
- Expenses stored in text files
- Budget and active month stored in a configuration file
- Application restores state after restart
- Monthly archive maintained for historical reference

---

##  Project Structure

Room_Expense_Manager/                                                    
│                                                                                  
├── main.py # Application controller (menu & flow)                                     
├── expense_manager.py # Expense CRUD operations                                      
├── member_manager.py # Member-wise spending calculation                                      
├── analytics.py # Budget, balance & date calculations                             
├── file_handler.py # Persistence & configuration handling                                   
│                                                                         
├── expenses_data.txt # Stored expense records                                           
├── config.txt # Persistent budget & month config                                        
├── archive/                                                             
│ └── month_backup.txt # Archived monthly records                                            

---

## How to Run the Project

1. Ensure **Python 3.x** is installed
2. Navigate to the project directory
3. Run the application:
   ```bash
   python main.py
4. Follow the on-screen menu options


##  Sample Workflow

- Enter the **monthly budget** and **active month** when the application starts  
- Add **daily expenses** with unique Expense IDs  
- Track **remaining balance** and **remaining days in the month**  
- View **member-wise spending summary**  
- **Update or delete** incorrect expense entries  
- **Reset the month** and archive old data at month end  

---

## Design Decisions (Why This Approach)

- **Expenses as single source of truth** → prevents data inconsistency  
- **Derived member contributions** → automatically updated on edits or deletions  
- **File-based persistence** → lightweight, offline-friendly, and simple  
- **Calendar-aware month handling** → accurate remaining-day calculation for all months  

---

## Future Enhancements

- Daily average spending suggestions  
- Category-wise monthly expense reports  
- Who-owes-whom settlement calculation  
- GUI or Web-based interface  
- Database-backed persistence  

---

## Academic & Internship Relevance

- Demonstrates **applied software engineering principles**  
- Strong alignment with **Data Structures and Python fundamentals**  
- Easy to explain in **viva examinations and technical interviews**  
- Focuses on **real-world problem solving** with clean architecture  

---

## Conclusion

This project goes beyond a basic academic exercise by implementing **realistic financial workflows**, **persistent state management**, and **robust update handling**. It stands as a **solid, professional-grade console application** suitable for **college submission, internships, and portfolio presentation**.
