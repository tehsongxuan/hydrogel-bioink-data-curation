"""Download the Zenodo source files used by this project and verify them.

Source: Zenodo record 19602891 (DOI 10.5281/zenodo.19602891).
Destination: data/raw/zenodo_19602891/ (created if missing).

Usage, from the repository root:
    python scripts/download_data.py            # rheology archive + image index (Phases 00-05)
    python scripts/download_data.py --images   # also images.zip, about 460 MiB (Phase 06)

Each file is checked against the MD5 checksum that Zenodo publishes for it.
The two primary files are also checked against the checksums recorded when
this project's Phase 1 audit was run, so a changed source release is caught.
A file already present with the correct checksum is not downloaded again.
Only the Python standard library is used.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.request
from pathlib import Path

RECORD_ID = "19602891"
RECORD_API = f"https://zenodo.org/api/records/{RECORD_ID}"
REPO_ROOT = Path(__file__).resolve().parent.parent
DEST = REPO_ROOT / "data" / "raw" / f"zenodo_{RECORD_ID}"

PRIMARY_FILES = ["ALG-Ph_HA-Ph_rheology_data.zip", "image_index.csv"]
IMAGE_FILES = ["images.zip"]

# MD5 checksums of the exact files used in this project's Phase 1 audit.
PROJECT_MD5 = {
    "ALG-Ph_HA-Ph_rheology_data.zip": "4eaac901afc46212108bfdad8b39b5c2",
    "image_index.csv": "e0fc1a61b6f5d5b2ea87a69a97d4aa58",
}


def md5_of(path: Path) -> str:
    digest = hashlib.md5()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def fetch_record(api_url: str) -> dict[str, dict]:
    """Return {filename: {"url": ..., "md5": ..., "size": ...}} from the Zenodo API."""
    with urllib.request.urlopen(api_url, timeout=60) as response:
        record = json.load(response)
    files = {}
    for entry in record.get("files", []):
        name = entry["key"]
        checksum = entry.get("checksum", "")
        files[name] = {
            "url": entry["links"].get("content") or entry["links"]["self"],
            "md5": checksum.split(":", 1)[1] if checksum.startswith("md5:") else None,
            "size": entry.get("size"),
        }
    return files


def download(url: str, target: Path, size: int | None) -> None:
    partial = target.with_suffix(target.suffix + ".part")
    with urllib.request.urlopen(url, timeout=60) as response, partial.open("wb") as out:
        done = 0
        while block := response.read(1024 * 1024):
            out.write(block)
            done += len(block)
            if size:
                print(f"\r  {done / size:6.1%} of {size / 1024**2:,.1f} MiB", end="", flush=True)
    print()
    partial.replace(target)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--images", action="store_true", help="also download images.zip (about 460 MiB)")
    parser.add_argument("--record-api", default=RECORD_API, help=argparse.SUPPRESS)
    parser.add_argument("--dest", type=Path, default=DEST, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    wanted = PRIMARY_FILES + (IMAGE_FILES if args.images else [])
    args.dest.mkdir(parents=True, exist_ok=True)
    print(f"Destination: {args.dest}")

    try:
        available = fetch_record(args.record_api)
    except OSError as error:
        print(f"FAILED: could not reach the Zenodo record ({error}).")
        print(f"Download the files manually from https://zenodo.org/records/{RECORD_ID} into {args.dest}")
        return 1

    failures = 0
    for name in wanted:
        print(f"\n{name}")
        info = available.get(name)
        if info is None:
            print(f"  FAILED: not listed in Zenodo record {RECORD_ID}.")
            failures += 1
            continue

        expected = PROJECT_MD5.get(name) or info["md5"]
        target = args.dest / name

        if target.is_file() and md5_of(target) == expected:
            print("  Already present, checksum matches. Skipped.")
            continue

        try:
            download(info["url"], target, info["size"])
        except OSError as error:
            print(f"  FAILED: download error ({error}).")
            failures += 1
            continue

        actual = md5_of(target)
        if info["md5"] and actual != info["md5"]:
            print(f"  FAILED: checksum {actual} does not match Zenodo's {info['md5']}. File may be incomplete.")
            failures += 1
        elif name in PROJECT_MD5 and actual != PROJECT_MD5[name]:
            print(f"  FAILED: checksum {actual} differs from the version this project used ({PROJECT_MD5[name]}).")
            print("  The Zenodo record may have been updated; results may not match the published reports.")
            failures += 1
        else:
            print(f"  OK: downloaded and verified (md5 {actual}).")

    print(f"\nResult: {len(wanted) - failures} of {len(wanted)} files ready.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
