#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import tempfile
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("verify_repository.py")
spec = importlib.util.spec_from_file_location("verify_repository", MODULE_PATH)
assert spec is not None and spec.loader is not None
verify_repository = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify_repository)

with tempfile.TemporaryDirectory() as tmp:
    root = Path(tmp)
    docs = root / "docs"
    docs.mkdir()
    (docs / "index.md").write_text("canonical\n", encoding="utf-8")

    assert verify_repository.exact_path_exists(root, "docs/index.md") is True
    assert verify_repository.exact_path_exists(root, "docs/INDEX.md") is False

print("verify_repository exact-path tests PASSED")
