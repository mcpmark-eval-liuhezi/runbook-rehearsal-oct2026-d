#!/usr/bin/env python3
"""Lightweight service stub used by the legacy-config retirement drill."""


LEGACY_MARKER = "# DEPRECATED-RUNBOOK-MARKER-7QF3"


def load(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def main():
    print("runbook-rehearsal-drill is up")


if __name__ == "__main__":
    main()
