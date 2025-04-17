# 📋 Todo API

Ushbu loyiha Todo API uchun to‘liq va interaktiv hujjat yaratish bo‘yicha ishlab chiqilgan. Loyihaning asosiy maqsadi – API’ni qanday ishlatishni yoritib beruvchi tushunarli hujjat yaratishdir, bu esa boshqa dasturchilar uchun undan samarali foydalanishni osonlashtiradi.

## 📌 Loyihaning vazifalari

Todo API quyidagi asosiy funksiyalarni o‘z ichiga oladi:

- 👤 Foydalanuvchilarni autentifikatsiya qilish (ro‘yxatdan o‘tish, kirish)
- ✅ Vazifalarni yaratish, ko‘rish, yangilash va o‘chirish
- 🗂 Vazifalarni kategoriyalarga ajratish
- ⏳ Vazifalarga ustuvorlik va muddati belgilash
- 🔀 Kichik vazifalar (subtasks) yaratish
- 💬 Vazifalar bo‘yicha izohlar qo‘shish
- 👥 Vazifalarni foydalanuvchilarga tayinlash
- 📊 Vazifalar bo‘yicha statistikalar va hisobotlar

## 🧩 Muammo

API ishlayotgan bo‘lsa-da, unga tegishli hujjatlarning yo‘qligi yangi dasturchilarning tushunishini va foydalanishini qiyinlashtiradi. Har bir so‘rovga qanday javob qaytishi, qanday parametrlar berilishi kerakligi noaniq bo‘ladi. Shuningdek, yangi versiyalar chiqarilganda o‘zgarishlar haqida foydalanuvchilarga xabar berish ham muammo tug‘diradi.

## ✅ Yechim

Loyihada **Django REST Framework** va **drf-yasg (Swagger/OpenAPI)** yordamida API uchun interaktiv hujjat yaratildi. Ushbu hujjat quyidagilarni o‘z ichiga oladi:

- API endpointlari
- So‘rov parametrlari
- Javob formatlari
- Xatolik kodlari
- Ishlash misollari va qo‘llanmalar

## 🧱 API Tuzilishi

API bir nechta modullarga bo‘lingan va har bir modul o‘ziga tegishli endpointlar orqali ishlaydi. Quyidagilar asosiy bo‘limlardir:

### 🔐 Autentifikatsiya
| Endpoint | Usul | Tavsif |
|----------|------|--------|
| `/auth/register/` | POST | Ro‘yxatdan o‘tish |
| `/auth/login/` | POST | Tizimga kirish |
| `/auth/logout/` | POST | Tizimdan chiqish |

### 🗂 Kategoriyalar
| Endpoint | Usul | Tavsif |
|----------|------|--------|
| `/categories/` | GET, POST | Kategoriyalar ro‘yxati va yaratish |
| `/categories/{id}/` | GET, PUT, DELETE | Bitta kategoriya bilan ishlash |

### ✅ Vazifalar
| Endpoint | Usul | Tavsif |
|----------|------|--------|
| `/tasks/` | GET, POST | Vazifalar ro‘yxati va yaratish |
| `/tasks/{id}/` | GET, PUT, DELETE | Bitta vazifa bilan ishlash |

### 📋 Kichik vazifalar (subtasks)
| Endpoint | Usul | Tavsif |
|----------|------|--------|
| `/subtasks/` | GET, POST | Subtasklar ro‘yxati va yaratish |
| `/subtasks/{id}/` | GET, PUT, DELETE | Bitta subtask bilan ishlash |

### 💬 Izohlar
| Endpoint | Usul | Tavsif |
|----------|------|--------|
| `/comments/` | GET, POST | Izohlar ro‘yxati va yaratish |
| `/comments/{id}/` | GET, PUT, DELETE | Izohlarni boshqarish |

### 📈 Statistikalar
| Endpoint | Usul | Tavsif |
|----------|------|--------|
| `/tasks/statistics/` | GET | Vazifalar bo‘yicha statistik ma'lumotlar |

## ⚙️ Texnologiyalar

- Python
- Django
- Django REST Framework (DRF)
- drf-yasg (Swagger uchun)
- PostgreSQL yoki SQLite

## 🚀 Ishga tushirish

```bash
# Virtual muhit yaratish va faollashtirish
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Kerakli kutubxonalarni o‘rnatish
pip install -r requirements.txt

# Migratsiyalarni bajarish
python manage.py migrate

# Serverni ishga tushirish
python manage.py runserver
```
## 🧑‍💻 Muallif
### Mamadaliyev Bunyodjon
Loyiha ta’lim maqsadida Astrum IT Academy doirasida ishlab chiqilgan.