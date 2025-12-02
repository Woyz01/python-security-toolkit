# Python Security Toolkit

Python Security Toolkit, dosya bütünlüğü kontrolü, hash hesaplama ve hash doğrulama işlemleri için geliştirilmiş açık kaynak bir güvenlik aracıdır.

Bu araç sayesinde:
- Bir dosyanın **MD5 / SHA256 / SHA512** gibi algoritmalarla hash değerini hesaplayabilir,
- Daha önce bilinen bir hash ile karşılaştırarak **dosyanın değiştirilip değiştirilmediğini** doğrulayabilirsiniz.

---

Özellikler

# Dosya Hash Hesaplama
Desteklenen algoritmalar:
- `md5`
- `sha1`
- `sha224`
- `sha256` (varsayılan)
- `sha384`
- `sha512`

# Hash Doğrulama
- Kullanıcının verdiği hash değeri ile dosyanın gerçek hash değeri karşılaştırılır.
- Dosya bütünlüğünün bozulup bozulmadığı tespit edilir.

# Komut Satırı Arayüzü (CLI)
Basit ve anlaşılır bir komut satırı yapısı sunar:
- `hash` komutu → hash üretir
- `verify` komutu → hash doğrular

---

# Kurulum

Projeyi klonlayın:

```bash
git clone https://github.com/Woyz01/python-security-toolkit.git
cd python-security-toolkit


# Python sanal ortamı oluştur(opsiyonel):
- python -m venv .venv
- source .venv/bin/activate  
- .venv\Scripts\activate


# Dosya hash hesaplama

- python src/main.py hash -f test.txt --algo sha256

Örnek çıktı şu şekildedir :

- SHA256 (test.txt): a3f2b1c9e7...


# Hash Doğrulama

- python src/main.py verify -f test.txt --algo sha256 --excepted a3f2b1c9e7...

Eğer komut başarılı ise  çıktı ;

- ✅ Hash doğrulandı. Dosya bütünlüğü sağlam.

Hatalı ise;

- ❌ Hash uyuşmuyor! Dosya değiştirilmiş olabilir.


Proje Yapısı da şu şekildedir ;

python-security-toolkit/
│
├── src/
│   ├── main.py           # CLI arabirimi
│   ├── hash_utils.py      # Hash hesaplama & doğrulama fonksiyonları
│
├── README.md
├── .gitignore
└── requirements.txt (opsiyonel)


Güvenlik Notu

Bu araç basit güvenlik analizleri ve eğitim amaçlı geliştirilmiştir.
Gerçek kurumsal ortamlarda daha kapsamlı güvenlik çözümleri kullanılmalıdır.


Katkı

Katkılarınızı memnuniyetle karşılıyoruz!
Pull request gönderebilir veya issue açabilirsiniz.


Destek Ol

Projeyi beğendiysen GitHub’da yıldız vermeyi unutma! ✨



Geliştirici

Cihan ŞAHİN
GitHub: https://github.com/Woyz01




