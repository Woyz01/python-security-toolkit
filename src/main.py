import argparse
from pathlib import Path

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



def build_parser():
    parser = argparse.ArgumentParser(
        description="Python güvenlik aracı"
    )
    subparsers = parser.add_subparsers(dest='command', required=True)
    hash_parser = subparsers.add_parser('hash', help = "Dosyanın hashini hesapla")
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
        "--excepted",
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
