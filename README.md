# Good Tomorrow GitBook Documentation

This repository contains production-ready multilingual GitBook documentation for the Good Tomorrow whitepaper.

English is configured as the default GitBook space through `.gitbook.yaml`. The localized spaces are available under `docs/zh`, `docs/ko`, and `docs/ja`, with matching navigation and page hierarchy.

## Documentation QA

```bash
python3 tools/validate_docs.py
```

## GitBook Setup

For the default English space, connect GitBook Git Sync to the repository root. For language variants, create separate GitBook spaces and set their project directories to `docs/zh`, `docs/ko`, and `docs/ja` respectively, then link those spaces as site variants in GitBook.
