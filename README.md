# 🗓️ E-Booking - ระบบจองห้องประชุมด้วย Django

![Banner](https://media.discordapp.net/attachments/1278174487929688085/1366846432778256475/19febf71b1176d3c.png?ex=68126e70&is=68111cf0&hm=5d644309bde09446aac8910c74ba69a32b582031a6027787b9ea2da7729151ab&=&format=webp&quality=lossless&width=1536&height=864)

ระบบสำหรับจองห้องประชุมในรูปแบบต่างๆ พร้อมระบบปฏิทิน, รายการจอง, อุปกรณ์เสริม และรองรับสิทธิ์ผู้ใช้ (Login ก่อนใช้งาน)

---

## ✨ ฟีเจอร์หลัก

✅ ลงชื่อเข้าใช้งานก่อนใช้งานระบบ  
✅ จองห้องผ่านฟอร์ม (เลือกวัน/เวลา/อุปกรณ์)  
✅ ปฏิทิน FullCalendar แสดงห้องที่ถูกจอง  
✅ ดูรายการจองทั้งหมด พร้อมรายละเอียด  
✅ ลบ/แก้ไขการจอง (ถ้าต้องการเพิ่ม)  
✅ ระบบแยกหน้า Admin (ใช้ Django Admin)

---

## ⚙️ ระบบที่ได้ที่ใช้

- 🐍 Django 5.1 (Python)
- 🖼 Bootstrap 5 (Frontend)
- 📅 FullCalendar.js (ระบบปฏิทิน)
- 👥 ระบบ Login + Logout ด้วย Django Auth
- ✅ ฟอร์มแบบ Responsive รองรับอุปกรณ์มือถือ

---

## 🖼️ ตัวอย่างหน้าจอระบบ

### 🔐 หน้า Login
> ระบบเข้าสู่ระบบก่อนจอง

![Login Screenshot](https://media.discordapp.net/attachments/1366351684577656924/1366971173434294312/image.png?ex=6812e29c&is=6811911c&hm=ab8135cf666520c461848ebf592c90753eadf92841e3eb78778953e01a7e09f3&=&format=webp&quality=lossless&width=1422&height=718)

---

### 🧾 แบบฟอร์มจองห้อง
> เลือกชื่อห้อง, จำนวนคน, วันเวลา, อุปกรณ์ ฯลฯ

![Form Screenshot](https://media.discordapp.net/attachments/1366351684577656924/1366807988446433361/image.png?ex=68124aa2&is=6810f922&hm=6680fbe3421c11a5243e50a08535c1789cb9fe78d85d30381301568a9d945fb3&=&format=webp&quality=lossless&width=1390&height=855)

---

### 📆 ปฏิทินแสดงการจอง
> ใช้ FullCalendar แสดงข้อมูลแบบทันสมัย

![Calendar Screenshot](https://media.discordapp.net/attachments/1366351684577656924/1366807987934724156/image.png?ex=68124aa2&is=6810f922&hm=747fede1dd70e92cf9d2fb495f51b5e333391de550755da0c4806be2d8805f6f&=&format=webp&quality=lossless&width=1430&height=804)

---

### 📋 รายการจองทั้งหมด
> แสดงข้อมูลที่จองไว้ พร้อมระบบค้นหา

![Booking List Screenshot](https://media.discordapp.net/attachments/1366351684577656924/1366971744359022603/image.png?ex=6812e324&is=681191a4&hm=0db962f1c07d48a65335525f7e0b955476cc29be4a02cae5d748884eb1b9d2e6&=&format=webp&quality=lossless&width=1452&height=665)

---

## 🛠️ โครงสร้างโปรเจกต์ (บางส่วน)
```
e_booking_project/ 
├── booking/
│  ├── models.py
│  ├── views.py
│  ├── urls.py
│  ├── static/
│  │   ├── images/
│  ├── templates/
│     ├── login.html
│     ├── index.html
│     ├── form.html
│     └── booking_list.html 
├── e_booking_project/
│    ├── settings.py
│    ├── urls.py
└── manage.py
```

### วิธีเริ่มโปรเจกต์ (รันแบบผู้พัฒนาใน localhost)

### 1. สร้าง virtual environment
```bash
python -m venv venv
```

### 2. Activate environment
```bash
venv\\Scripts\\activate
```

### 3. ติดตั้ง Django
```bash
pip install django
```

### 4. สร้างฐานข้อมูล + superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5. เริ่มรันเซิร์ฟเวอร์
```bash
python manage.py runserver
```

---

## 📩 ช่องทางการติดต่อ

<div align="center">

<table>
  <tr>
    <td align="center"><strong>🪪 Name</strong></td>
    <td align="center"><strong>🦹‍♂️ Nickname</strong></td>
    <td align="center"><strong>📧 Email</strong></td>
    <td align="center"><strong>💬 Line</strong></td>
  </tr>
  <tr>
    <td>Sittisak</td>
    <td>Kan</td>
    <td>kanzaza.5419@gmail.com</td>
    <td>kanzza007</td>
  </tr>
  <tr>
    <td>Saharat</td>
    <td>TT</td>
    <td>saharat.saradee97@gmail.com</td>
    <td>titeeneverdie</td>
  </tr>
  <tr>
    <td>Kerkkiat</td>
    <td>Tangmo</td>
    <td>maneeins2546@gmail.com</td>
    <td>0969296462</td>
  </tr>

</table>

</div>
<br>

<h1 align="center">🔨 Created by NoEpicDevs 😎</h1>

---
