# Public Repository Safety

COREMI's workflow can be open while production operations remain private.

Do not commit:

- API keys, merchant secrets, certificates, private keys, cookies, or session tokens;
- production environment files or webhook payloads;
- customer emails, phone numbers, payment records, or account exports;
- unpublished interviews, licensed reports, or confidential source material;
- complete private research runs unless every source and right has been reviewed.

Before contributing, inspect the staged diff:

```bash
git diff --cached
```

If a secret was committed, rotating the secret is mandatory. Deleting the visible line alone is not sufficient because Git history may still contain it.
