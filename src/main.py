import argparse
import time
from pathlib import Path
from port_utils import scan_ports
from hash_utils import compute_file_hash, verify_file_hash



def handle_hash(args):
    file_path = args.file
    algo = args.algo
    try:
        digest = compute_file_hash(file_path, algo)
        print(f"{algo.upper()} ({args.file.name}): {digest}")
    except FileNotFoundError:
        print(f"Dosya bulunamadı: {file_path}")
    except ValueError as e:
        print("Hata:", e)


def handle_verify(args):
    file_path = args.file
    algo = args.algo
    expected = args.excepted

    try:
        is_valid = verify_file_hash(file_path, expected, algo)
    except FileNotFoundError:
        print(f"Dosya bulunamadı: {file_path}")
        return
    except ValueError as e:
        print("Hata:", e)
        return

    if is_valid:
        print("✅ Hash doğrulandı. Dosya bütünlüğü sağlam.")
    else:
        print("❌ Hash uyuşmuyor! Dosya değiştirilmiş olabilir.")


def handle_scan_ports(args):
    host = args.host
    ports = args.ports
    results = scan_ports(host=host, ports=ports)
    print(f"Host: {host}")
    for port, is_open in results.items():
        if is_open:
            print(f"Port {port}: AÇIK")
        else:
            print(f"Port {port}:KAPALI")


def handle_watch_file(args):
    file_path = args.file
    algo = args.algo
    interval = args.interval
    compute_file_hash(file_path, algo)
    print(f"{file_path} dosyası {interval} saniye aralıklarla izleniyor... ")
    print( f"Ctrl+C ile çıkış")
    try:
        while True:
            time.sleep(interval)
            new_hash = compute_file_hash(file_path, algo)
            if new_hash != new_hash:
                print("⚠ Dosya değişti!")
                print(f"Eski hash: {last_hash}")
                print(f"Yeni hash: {new_hash}")
                last_hash = new_hash
    except KeyboardInterrupt:
        print("\nİzleme kullanıcı tarafından durduruldu.")




def build_parser():
    parser = argparse.ArgumentParser(          #argparse komut satırından parametre almaya yarar.
        description="Python güvenlik aracı"
    )
    subparsers = parser.add_subparsers(dest='command', required=True)
    hash_parser = subparsers.add_parser('hash', help = "Dosyanın hashini hesapla")
    scan_parser = subparsers.add_parser("scan_ports", help= "Belirli portları tara")
    watch_parser = subparsers.add_parser("watch-file", help= "Bir dosyayı hash değişiklerine karşı izle")
    watch_parser.add_argument(
        "-f", "--file",
        type=Path,
        required=True,
        help= "İzlenecek dosya yolu"
    )

    watch_parser.add_argument(
        "--algo",
        choices=["sha256", "md5"],
        default="sha256",
        help="Kullanılacak algoritma (varsayılan: sha256)",
    )

    watch_parser.add_argument(
        "--interval",
        type= int,
        default=5,
        help= "Kontrol aralığı (saniye, varsayılan: 5)",
    )
    watch_parser.set_defaults(func=handle_watch_file)

    scan_parser.add_argument(
        "--host",
        required=True,
        help= "Hedef IP veya domain (ör: 127.0.0.1 veya google.com)"
    )
    scan_parser.add_argument(
        "--ports",
        required=True,
        nargs="+",    #nargs bir argümanın kaç tane değer alacağını belirler."+" da bir veya daha fazla değer.
        type = int,   #"*" ise sıfır veya daha fazla değer.
        help= "Taranacak port numaraları (ör: 22 80 443)",

    )
    scan_parser.set_defaults(func=handle_scan_ports)

    hash_parser.add_argument(
        "-f", "--file",
        type=Path,
        required=True,
        help="Hash'i hesaplanacak dosya yolu"
    )
    hash_parser.add_argument(
        "--algo",
        choices=['md5', 'sha256'],
        default='sha256',
        help="Kullanılacak algoritma (varsayılan: sha256)"
    )
    hash_parser.set_defaults(func=handle_hash)

    verify_parser = subparsers.add_parser('verify', help="Dosya hash doğrulama")
    verify_parser.add_argument(
        "-f", "--file",
        type=Path,
        required=True,
        help="Doğrulanacak dosya yolu"
    )
    verify_parser.add_argument(
        "--algo",
        choices=['md5', 'sha256'],
        default='sha256',
        help="Kullanılacak algoritma (varsayılan: sha256)",
    )
    verify_parser.add_argument(
        "--expected",
        required=True,
        help="Beklenen hash değeri",
    )

    verify_parser.set_defaults(func=handle_verify)

    return parser



def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)



if __name__ == "__main__":
    main()
