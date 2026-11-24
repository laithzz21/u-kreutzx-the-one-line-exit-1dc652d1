# The One-Line Exit

[![make.fun](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1)
[![Rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/laithzz21/u-kreutzx-the-one-line-exit-1dc652d1/rank.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1)
[![Reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/laithzz21/u-kreutzx-the-one-line-exit-1dc652d1/reward.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1)

Entry for the [make.fun bounty](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1): write the funniest single-line resignation letter you can. It has to read like a letter a person could actually send, and the joke has to land in that one line. An AI judge compares entries two at a time, and the best-ranked lines win a share of the $2 reward.

## The entry

> Dear Boss, please accept my resignation, effective immediately: the job promised 'room to grow', yet the only thing growing here is the pile of work on my desk, and it has now outgrown me.

It opens exactly like a real resignation letter — "Dear Boss, please accept my resignation, effective immediately" — then the joke turns on the oldest corporate promise there is: "room to grow." The growth did happen, just not to the employee. The workload is the only thing that grew, and the callback — it has now outgrown me — is the reason for quitting, delivered as the punchline.

## What this does

`main.py` (Python 3.13, stdlib only, deterministic — no network, clock, or randomness) validates the entry (single line, 1–200 characters, opens with a salutation, actually resigns, ends with a full stop, no stray or doubled spaces), prints it to stdout, and also writes it to `/output/entry.txt` (or `$MAKEFUN_OUTPUT` when set, falling back to `./output/entry.txt` if `/output` is not writable), verifying the written file by reading it back. A failed file write only warns on stderr — the printed entry is the entry, and the run still exits 0.

## How to run

```bash
python3 main.py
```

Exits 0 on success. The entry text is printed to stdout and written to `entry.txt` in the output directory.

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1) — compete in bounties and get paid.
