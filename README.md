# FLIGHT400 Lab · Wabtec Bobathon

This repository contains the lab materials for the Wabtec IBM i Modernization Bobathon — a hands-on workshop where participants use IBM Bob IDE to explore, modernize, and extend a real IBM i application (FLIGHT400). Exercises cover code explanation, RPG modernization, system querying, React app generation, field expansion, SQL optimization, and automated testing.

---

## For Participants

**Everything you need to complete the lab is available on the hosted lab site.** Start with the environment setup, then work through the exercises at your own pace.

#### Participant Setup — Interactive setup guide with screenshots.
https://agz-16.github.io/wabtec_bobathon/setup.html

#### Lab Guide — Full exercise catalog with step-by-step instructions.
https://agz-16.github.io/wabtec_bobathon/


#### Offline copy of the lab guide

Use this if you want to read the whole guide (setup and all exercises, with screenshots) locally on your computer. 

1. Download the zip: https://github.com/agz-16/wabtec_bobathon/raw/main/offline.zip
2. Unzip it and open the `offline` folder.
3. Double-click **`index.html`**. It opens in your web browser. It is one self-contained file (about 21 MB) with all the screenshots built in.

---

## For Instructors

The instructor setup guide covers provisioning the IBM i environment, restoring the FLIGHT400 application, and preparing participant libraries before the event.

**Instructor Setup Guide** — [instructor-setup/README.md](instructor-setup/README.md)

**Updating the offline copy** — The `offline/` folder and `offline.zip` are generated from `docs/` by `build-offline.py`. After you change anything under `docs/`, run `python3 build-offline.py` from the repository root and commit the updated `offline/` folder and `offline.zip`.

**Updating the setup markdown** — `docs/tracks/setup.html` is the only place to edit the Environment Setup steps. `docs/setup.md` is generated from it: after editing the track file, run `python3 build-setup-md.py` from the repository root and commit the updated `docs/setup.md`. Do not edit `setup.md` by hand.

