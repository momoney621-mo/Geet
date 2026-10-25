# Geet

Waitlist site for **Geet**, an iPhone app where squads of 2–4 friends compete to stay locked in: phone-locked study blocks, random lock checks, and a 75-day season title scored on effort.

Early access opens **November 5, 2026**. Ages 13+.

## Files

- `index.html` — the waitlist page
- `privacy.html` — privacy policy
- `src/index.body.html` + `build.py` — source for `index.html` (run `python3 build.py` after editing)

## Before launch

In `src/index.body.html`, fill in:

- `FORM_ENDPOINT` — where signups are sent (for example, a Formspree form URL). Until this is set, the form can't save signups on GitHub Pages.
- `SHARE_URL` — the public link to this site, used in the squad invite.
- Instagram and YouTube links (`yourhandle`).

In `privacy.html`, replace `privacy@YOURDOMAIN.com` with a real contact email.

## Hosting

Turn on GitHub Pages (Settings → Pages → Deploy from branch → `main`, root) to put the site online.
