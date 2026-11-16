# FLIGHT400 Lab · American Eagle Bobathon

This repository contains the lab materials for the American Eagle IBM i Modernization Bobathon — a hands-on workshop where participants use IBM Bob IDE to explore, modernize, and extend a real IBM i application (FLIGHT400). Exercises cover code explanation, RPG modernization, system querying, React app generation, field expansion, SQL optimization, and automated testing.

---

## For Participants

Everything you need to complete the lab is available on the hosted lab site. Start with the environment setup, then work through the exercises at your own pace.

**Participant Setup** — Interactive setup guide with screenshots.
https://liv-fing.github.io/american_eagle_bobathon/setup.html

### Offline copy of the guide

Use this if you want to read the whole guide (setup and all exercises, with screenshots) without an internet connection.

1. Download the zip: https://github.com/liv-fing/american_eagle_bobathon/raw/main/offline.zip
2. Unzip it. You get a folder named `offline`.
3. Open the `offline` folder and double-click **`index.html`**. It opens in your web browser. It is one self-contained file (about 21 MB) with all the screenshots built in.
4. Do the same steps as the online guide. In step 0.3, paste your server IP address and click your library row.

Notes:
- Get your private key file and server IP address from your instructor **before** you go offline. External links still need internet.
- Fonts look slightly different offline. Nothing else changes.
- Do not open `offline/index.html` on GitHub itself. GitHub shows the page's source code instead of the guide, so use the zip.
- There is also an [offline Environment Setup in markdown](docs/setup.md), which covers setup only.

**Lab Guide** — Full exercise catalog with step-by-step instructions.
https://liv-fing.github.io/american_eagle_bobathon/

---

## For Instructors

The instructor setup guide covers provisioning the IBM i environment, restoring the FLIGHT400 application, and preparing participant libraries before the event.

**Instructor Setup Guide** — [instructor-setup/README.md](instructor-setup/README.md)

**Updating the offline copy** — The `offline/` folder and `offline.zip` are generated from `docs/` by `build-offline.py`. After you change anything under `docs/`, run `python3 build-offline.py` from the repository root and commit the updated `offline/` folder and `offline.zip`.

**Updating the setup markdown** — `docs/tracks/setup.html` is the only place to edit the Environment Setup steps. `docs/setup.md` is generated from it: after editing the track file, run `python3 build-setup-md.py` from the repository root and commit the updated `docs/setup.md`. Do not edit `setup.md` by hand.

