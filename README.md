# 🔍 Python Port Scanner v2.0

A modular TCP Port Scanner built using Python's **socket** module.

This project scans a target host for open TCP ports, identifies common services running on those ports, and generates a detailed scan report. It was developed as part of my Python and Cybersecurity learning journey.

---

## 🚀 Features

- TCP Port Scanning
- Service Detection (SSH, HTTP, HTTPS, FTP, DNS, etc.)
- Hostname Validation
- Input Validation
- Configurable Port Range
- Socket Timeout for Faster Scanning
- Automatic Report Generation
- Modular Project Structure
- Scan Again Option

---

## 📂 Project Structure

```
python-port-scanner-v2/
│
├── main.py
│
├── scanner/
│   ├── service.py
│   └── validator.py
│
├── reports/
│   └── w_report.py
│
├── utils/
│   └── banner.py
│
└── output/
    └── report.txt
```

---

## ⚙️ Technologies Used

- Python 3
- Socket Module
- TCP Networking

---

## 🖥️ How It Works

1. Enter a target hostname or IP address.
2. Enter the starting and ending port.
3. The scanner validates all user input.
4. Each TCP port is checked using `socket.connect_ex()`.
5. Open ports are displayed.
6. Common services are identified.
7. A detailed report is saved automatically.

---

## 📸 Sample Output

```
Enter Target Address: scanme.nmap.org

Start Port: 20
End Port: 1000

Scanning...

22/tcp   OPEN   SSH
80/tcp   OPEN   HTTP

Total Checked Ports : 981
Total Open Ports    : 2

Report Saved Successfully.
```

---

## 📄 Sample Report

```
Checked Port Report

Target Address : scanme.nmap.org
Total Ports Checked : 981
Total Open Ports : 2

Open Port List

22/tcp   OPEN   SSH
80/tcp   OPEN   HTTP
```

---

## 🧠 Concepts Practiced

- Python Functions
- Python Modules
- Dictionaries
- Exception Handling
- File Handling
- Input Validation
- Socket Programming
- TCP Networking
- Port Scanning
- Service Detection

---

## ⚡ Performance

The scanner uses:

```python
socket.settimeout(0.3)
```

to reduce waiting time for closed or filtered ports, making scans significantly faster.

---

## 📈 Future Improvements

- Banner Grabbing
- DNS Resolution Display
- Multi-threaded Scanning
- Command Line Arguments
- CSV Export
- JSON Export
- Progress Indicator
- Improved Report Formatting

---

## ⚠️ Disclaimer

This project is intended for educational purposes only.

Only scan systems that you own or have explicit permission to test.

---

## 👨‍💻 Author

**Ashish Pangavhane**

- B.Tech Computer Engineering Student
- Aspiring Cybersecurity Professional
- Learning Python, Networking, and Ethical Hacking

---

⭐ If you found this project interesting, feel free to fork it or leave a star.
