**Loyiha nomi: Blog tizimi API**

**Maqsad**

FastAPI yordamida oddiy blog tizimi yarating. Tizimda foydalanuvchilar ro‘yxatdan o‘tishi, tizimga kirishi, maqolalar yozishi va boshqa foydalanuvchilarning maqolalariga izoh qoldirishi mumkin bo‘lsin.

---

**Texnologiyalar**

* FastAPI  
* SQLAlchemy  
* Pydantic  
* JWT Authentication  
* SQLite yoki PostgreSQL

---

**Ma'lumotlar bazasi modellari**

**User**

* id  
* first\_name  
* last\_name  
* email  
* hashed\_password  
* created\_at

**Post**

* id  
* title  
* content  
* created\_at  
* updated\_at  
* author\_id

**Comment**

* id  
* content  
* created\_at  
* author\_id  
* post\_id

---

**Talablar**

**1\. Foydalanuvchini ro‘yxatdan o‘tkazish**

API foydalanuvchini ro‘yxatdan o‘tkazishi kerak.

Ma'lumotlar:

* Ism  
* Familiya  
* Email  
* Parol

Qoidalar:

* Email yagona bo‘lishi kerak.  
* Parol hash ko‘rinishida saqlanishi kerak.

---

**2\. Tizimga kirish**

Foydalanuvchi email va parol orqali tizimga kiradi.

Natijada:

* JWT access token qaytariladi.

---

**3\. Profil ma'lumotlarini olish**

Tizimga kirgan foydalanuvchi:

* o‘z ma'lumotlarini ko‘ra olishi kerak.

---

**4\. Maqola yaratish**

Faqat autentifikatsiyadan o‘tgan foydalanuvchi maqola yarata oladi.

Ma'lumotlar:

* Sarlavha  
* Matn

---

**5\. Barcha maqolalarni olish**

API barcha maqolalarni qaytarishi kerak.

Har bir maqola bilan:

* maqola muallifi  
* izohlar soni

ham qaytarilsin.

---

**6\. Bitta maqolani olish**

ID bo‘yicha bitta maqolani olish.

Natijada:

* maqola ma'lumotlari  
* muallif ma'lumotlari  
* barcha izohlar

qaytarilsin.

---

**7\. Maqolani tahrirlash**

Faqat maqola muallifi o‘z maqolasini tahrirlay oladi.

Boshqa foydalanuvchi urinsa:

* 403 Forbidden qaytarilsin.

---

**8\. Maqolani o‘chirish**

Faqat maqola muallifi o‘z maqolasini o‘chira oladi.

Boshqa foydalanuvchi urinsa:

* 403 Forbidden qaytarilsin.

---

**9\. Izoh qo‘shish**

Autentifikatsiyadan o‘tgan foydalanuvchi istalgan maqolaga izoh yozishi mumkin.

Ma'lumot:

* Izoh matni

---

**10\. Izohni o‘chirish**

Faqat izoh muallifi o‘z izohini o‘chira oladi.

---

**11\. Qidiruv**

Foydalanuvchi maqolalarni sarlavha bo‘yicha qidira olishi kerak.

Misol:

* python  
* fastapi  
* database

so‘zlari bo‘yicha qidirish.

