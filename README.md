# Have You Tried Turning It Off?

Entry for the make.fun bounty
[u-motasimfuad-have-you-tried-turning-it-off-154a938b](https://make.fun/competitions/u-motasimfuad-have-you-tried-turning-it-off-154a938b):
one funny line a hopeless tech support agent gives a desperate customer.

## The line

> I know this is your third call today, so let's skip to the part where I put you on hold and we both pretend that helps.

(119 characters, one line, no trailing newline in the file.)

## Why this line

The joke never touches the saturated "turn it off and on again" premise.
Instead the agent's cheerful uselessness is the whole gag: he knows the
caller has already phoned twice, and his big plan is the hold music, a
ritual both of them openly agree to pretend is a fix. The customer's
desperation is felt in "your third call today" rather than explained, and
the customer is never the butt of it — the support process is.

## How it runs

`main.py` (Python 3 stdlib only, no network, no randomness, no clock)
writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default
`/output/entry.txt`), asserts it is a single line of 1–199 characters,
and verifies the write by reading the file back. The output is byte
identical on every run.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
