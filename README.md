# Python Security Toolkit

**Python Security Toolkit**, dosya bütünlüğü ve temel ağ güvenliği kontrolleri için geliştirilmiş, komut satırı tabanlı bir mini güvenlik aracıdır.

Bu araç sayesinde:

- Dosyaların hash değerlerini hesaplayabilir,
- Hash doğrulama ile dosya bütünlüğünü kontrol edebilir,
- Belirli portların açık/kapalı durumunu test edebilir,
- Kritik dosyaları hash değişikliklerine karşı izleyebilirsiniz.

---

# Özellikler

### Dosya Hash Hesaplama (`hash`)

Bir dosyanın hash değerini hesaplar.

Desteklenen algoritmalar:

- `md5`
- `sha1`
- `sha224`
- `sha256` (varsayılan)
- `sha384`
- `sha512`

**Kullanım:**

```bash
python src/main.py hash -f test.txt --algo sha256


Örnek Çıktı;

- SHA256 (test.txt): a3f2b1c9e7...

# Hash Doğrulama

Dosyanın gerçek hash’i ile beklenen hash değerini karşılaştırır ve dosyanın değiştirilip değiştirilmediğini tespit eder.

Kullanımı

- python src/main.py verify -f test.txt --algo sha256 --expected a3f2b1c9e7...

Beklenen Çıktı ise;

- ✅ Hash doğrulandı. Dosya bütünlüğü sağlam. /  ❌ Hash uyuşmuyor! Dosya değiştirilmiş olabilir.

# Port Tarama(scan_ports)

Belirli bir host (IP veya domain) üzerindeki portların açık mı kapalı mı olduğunu kontrol eder.

Kullanımı ise;

- python src/main.py scan_ports --host 127.0.0.1 --ports 80 443   // "--host" -> hedef IP veya domain(ör: 127.0.0.1, google.com ) gibi
                                                                  //""--ports" -> Bir veya daha fazla port (boşlukla ayrılır), örneğin: 80 443 8080
Örnek çıktı şu şekildedir.

Host: 127.0.0.1
Port 80: KAPALI
Port 443: KAPALI

# Dosya Bütünlüğü İzleme(watch-file)

Bir dosyanın hash değerini belirli aralıklarla kontrol eder. Eğer hash değişirse (dosya içerik olarak değişmişse) uyarı verir.

Kullanımı ise;

python src/main.py watch-file -f watchme.txt --algo sha256 --interval 3

beklenen çıktı ise;

watchme.txt dosyası 3 saniye aralıklarla izleniyor...
Ctrl+C ile çıkış

⚠ Dosya değişti!
Eski hash: a3f2b1c9e7...
Yeni hash: 91b42a0c5d...


Parametreler:

-f, --file → İzlenecek dosya

--algo → Hash algoritması (varsayılan: sha256)

--interval → Kontrol aralığı (saniye cinsinden, varsayılan: 5)


# Proje Yapısı


python-security-toolkit/
│
├── src/
│   ├── main.py        # CLI komutlarının tanımlandığı ana dosya
│   ├── hash_utils.py  # Hash hesaplama ve doğrulama fonksiyonları
│   ├── port_utils.py  # Port tarama yardımcı fonksiyonları
│
├── README.md
├── .gitignore
└── requirements.txt   # (opsiyonel)


# Kurulum

git clone https://github.com/Woyz01/python-security-toolkit.git
cd python-security-toolkit


Sanal ortam oluşturun:

python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate


Hash hesaplama;

python src/main.py hash -f test.txt --algo sha256

Hash doğrulama;

python src/main.py verify -f test.txt --algo sha256 --excepted a3f2b1c9e7...

Port tarama:

python src/main.py scan_ports --host 127.0.0.1 --ports 80 443

Dosya izleme;

python src/main.py watch-file -f watchme.txt --algo sha256 --interval 


Gerekirse bağımlılıkları kurun:

pip install -r requirements.txt


# Güvenlik Notu

Bu proje:

- Eğitim amaçlıdır,

- Temel güvenlik kontrolleri sağlar,

- Kurumsal üretim ortamları için tek başına yeterli bir çözüm değildir.

Gerçek sistemlerde daha gelişmiş çözümler ve birden fazla katmanlı güvenlik yaklaşımı kullanılmalıdır.




# Katkı

Katkı yapmak isterseniz:

- Depoyu fork’layın

- Yeni bir dal açın: feature/yeni-ozellik

- Değişikliklerinizi commit edin

- Pull request açın


# Destek

Projeyi faydalı bulduysanız, GitHub’da star vermeniz projeyi görünür kılmak için çok yardımcı olur.


# Yazan

- github.com/Woyz01






