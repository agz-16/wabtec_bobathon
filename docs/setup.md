<!-- Generated from docs/tracks/setup.html by build-setup-md.py. Do not edit by hand. -->

# Environment Setup

Complete all steps below before starting any exercise. Start by installing and logging in to Bob, then verify your extensions, find your library number, and finally connect to IBM i.

---

## 0.1 — Prerequisite Bob Setup

Check your inbox for the **"You've been invited to join your team"** email, then follow these steps to install Bob and sign in for the first time.

1. **Create your IBM ID** — Open the invitation email and click the link to create your IBM ID. This gives you an account to access IBM Bob.

2. **Download & open Bob** — Download Bob using the correct installer for your computer, then open it. If Bob asks whether to import settings from another editor, select your regular IDE or click **Skip for now**. If it asks about chat migration, click **Skip migration**.

3. **Log in to Bob** — In the Bob chat window, click **Log in to Bob**. When asked to allow Bob to sign in, click **Allow**. Bob will then ask if you want to open a link — click **Open**. This opens your browser to complete the sign-in.

4. **Verify your account is active** — Click the **gear icon** above the Bob chat window. If the chat window isn't open, click the Bob icon to the right of the center search bar to open it first.

   ![Bob settings panel showing the gear icon and General settings](img/settings-pt1.png)

   *Open Bob settings with the gear icon above the chat window*

   Under the **General** tab, confirm that coins are listed in your budget at **100% remaining** — this means your account is active and ready. You're all set even if you don't see a team name matching the screenshot below.

   > 💡 **Team dropdown:** If you have used Bob before and belong to multiple teams, a team dropdown will appear — make sure it shows a team with **Bobathon** in the name. If you only belong to one team, the dropdown may not be visible at all, which is expected.

   ![Bob team selector showing Bobathon account option](img/change-team.png)

   *If a team dropdown appears, select the Bobathon team*

---

## 0.2 — Verify and Install Required Extensions

Two extensions are required. The **IBM Bob Premium Package for i** is often pre-installed for your team — verify it below. The **IBM i Development Pack** must be installed manually.

1. **Open the Extensions view** — Click the Extensions icon in the Activity Bar — the vertical strip of icons on the far left side of Bob — or press `Cmd+Shift+X` (macOS) or `Ctrl+Shift+X` (Windows/Linux) to open the Extensions panel.

   ![Extensions icon in the Bob Activity Bar](img/open-market.png)

   *Click the Extensions icon in the Activity Bar to open the Extensions panel*

2. **Verify IBM Bob Premium Package for i** — Search for **"IBM Bob Premium"**. If **IBM Bob Premium Package for i** (publisher: IBM) appears with an **Install** button on the right, click **Install** now. If there is no **Install** button, you're all set — skip to step 3. This package includes Code for IBM i (source editing, object browser, IFS browser, Db2 for i, and more).

   ![Searching for IBM Bob Premium in the Extensions panel](img/searching-ibm-i.png)

   *Search for "IBM Bob Premium" — an Install button on the right means it still needs to be installed*

3. **Install IBM i Development Pack** — Just like the previous step, search for **"IBM i Development Pack"** in the Extensions panel. This extension is **not** pre-installed — click **Install** if it does not appear under *Installed*. Reload Bob if prompted.

4. **Open Bob Settings** — Click the **Bob Settings** button in the bottom-right corner of the Bob IDE to open the Settings panel.

   ![Bob Settings button in the bottom-right corner of the Bob IDE](img/bob_settings.png)

   *Click Bob Settings in the bottom-right corner of the Bob IDE*

5. **Install Premium Package for i** — Further down the panel, next to the **Add ons** setting, you should see IBM Bob Premium Package for i. Click **Install**. Bob may ask you to restart the IDE — if so, accept and restart.

   ![IBM Bob Premium Package for i shown next to the Add ons setting with an Install button](img/activatedd.png)

   *Click Install next to IBM Bob Premium Package for i under Add ons*

6. **Confirm it is activated in Bob** — Now click the icon in the very top-right corner (shown in the first screenshot below) to return to your Bob chat. From there, click either **Agent** or the **+** sign, and you should see the **IBM i Developer** and **IBM i Database** modes listed as options. If they don't appear, your IBM Bob account likely hasn't been linked to your Premium Package for i entitlements yet.

   ![Icon in the top-right corner of Bob to return to the chat](img/sidebar-button.png)

   *Click the icon in the top-right corner to return to the Bob chat*

   ![IBM i Developer and IBM i Database modes in the mode selector](img/new-modes.png)

   *IBM i Developer and IBM i Database appear in the mode list*

---

## 0.3 — Choose Your Server, IP Address and Library Number

Your instructor will assign you a library number. Each participant has their own copy of the FLIGHT400 application in a library named **FLGHT4nn** (e.g. FLGHT401, FLGHT402). Use only your assigned number throughout the exercises so everyone can work independently.

> **Action required (2 things):** (1) **paste the IP address** your instructor gave you into the box, and (2) in the table below, **click the row with your assigned library number**. You only do this once. The IP address, library name, dev port, and prompts throughout this guide update to match.

Your instructor will give you the IP address of your server. Wherever this guide shows `<myIPaddress>`, use that address.

> 💡 **Spelling note:** The library name is `FLGHT4nn` — note there is **no "I"** in FLGHT. Your instructor may say "Flight 4-nn" verbally, but when typing always use `FLGHT4nn` (F‑L‑G‑H‑T).

| Student # | Library | Dev Port | React App URL |
|:---:|---|:---:|---|
| 1 | `FLGHT401` | 3001 | `http://localhost:3001` |
| 2 | `FLGHT402` | 3002 | `http://localhost:3002` |
| 3 | `FLGHT403` | 3003 | `http://localhost:3003` |
| 4 | `FLGHT404` | 3004 | `http://localhost:3004` |
| 5 | `FLGHT405` | 3005 | `http://localhost:3005` |
| 6 | `FLGHT406` | 3006 | `http://localhost:3006` |
| 7 | `FLGHT407` | 3007 | `http://localhost:3007` |
| 8 | `FLGHT408` | 3008 | `http://localhost:3008` |
| 9 | `FLGHT409` | 3009 | `http://localhost:3009` |
| 10 | `FLGHT410` | 3010 | `http://localhost:3010` |
| 11 | `FLGHT411` | 3011 | `http://localhost:3011` |
| 12 | `FLGHT412` | 3012 | `http://localhost:3012` |
| 13 | `FLGHT413` | 3013 | `http://localhost:3013` |
| 14 | `FLGHT414` | 3014 | `http://localhost:3014` |
| 15 | `FLGHT415` | 3015 | `http://localhost:3015` |
| 16 | `FLGHT416` | 3016 | `http://localhost:3016` |
| 17 | `FLGHT417` | 3017 | `http://localhost:3017` |
| 18 | `FLGHT418` | 3018 | `http://localhost:3018` |
| 19 | `FLGHT419` | 3019 | `http://localhost:3019` |
| 20 | `FLGHT420` | 3020 | `http://localhost:3020` |

> 💡 The **Dev Port** is only needed for **Exercise 4**. When Bob asks you to pin your Vite dev server to a port, use your Dev Port. Your React app will be reachable at the React App URL shown — provided your SSH tunnel (Exercise 4, step 4.1.1) is active.

---

## 0.4 — Connect Bob IDE to IBM i

1. **Add a new connection** — Click the IBM i icon in the Activity Bar (indicated by the red arrow in the screenshot below), then click **New Connection**. Enter the host IP `<myIPaddress>`, the user profile `ITZUSER`, and the `ae_primary_key.pem` private key file your instructor shared with you. When prompted for the private key, browse to the saved `ae_primary_key.pem` file on your computer. **Do not use the password here — use only the `ae_primary_key.pem` private key file.**

   ![IBM i icon in the Bob Activity Bar](img/ibmi_icon.png)

   *Click the IBM i icon in the Activity Bar*

   ![IBM i connection dialog in Bob IDE](img/i-connection.png)

   *IBM i connection panel*

   > 💡 If you get a private key error when connecting, see **0.5** for instructions on setting the correct file permissions on `ae_primary_key.pem`.

2. **Add your assigned library to the User Library List** — In the Code for IBM i extension (arrow in the picture below), navigate to the **User Library List** section and click the **+** icon. An input field will pop up at the top of the screen — type `FLGHT4nn` and press **Enter**. You'll then see your library added to the list. Remember: **no "I"** — it's `FLGHT`, not `FLIGHT`.

   ![User Library List section in the Code for IBM i extension](img/add-library.png)

   *Navigate to User Library List and click the + icon*

   ![Input field prompting for library name](img/add-library-name.png)

   *Type FLGHT4nn and press Enter to add your library*

   > ✅ If you have a 5250 terminal, you can also add the library with: `ADDLIBLE FLGHT4nn` and launch the app with: `GO FLGHT4nn/FRSMAIN`

3. **Add your assigned library to the Object Browser** — While still in the Code for IBM i extension, go to the **Object Browser** section and click the funnel icon or the **Create new filter** button.

   ![Object Browser section showing the funnel/Create new filter button](img/add-object-filter.png)

   *Object Browser — click the funnel icon or Create new filter*

   Name your filter (e.g. your assigned number). In **Libraries**, enter your assigned library `FLGHT4nn`. For **Object types**, change it to **\*ALL** to see all object types: `*PGM` (RPG and CL programs), `*FILE` (display and database files), `*MENU` (application menus).

   > ⚠️ **Use `*ALL`, not `*`** — the wildcard `*` does not work for filtering object types in the Object Browser. You must type `*ALL` exactly.

   ![Object Browser filter fields with Object types set to *ALL](img/objectfilter.jpeg)

   *Enter FLGHT4nn as the library and choose your object types*

   Scroll down and click **Save Settings**. Your named filter will now appear in the Object Browser, and you can navigate and expand the members inside your library.

4. **Set the workspace to Library List** — Throughout the labs you'll see references to setting the scope or workspace to **QSYS** or your **Library List**. This is because Bob can work on local files on your laptop *and* on the IBM i you just connected to — all the labs focus on the IBM i.

   Click the **+** icon above the Bob chat window. When the options appear in the center of the screen, make sure your library is listed under **New Task in Library List** and select that option.

   ![Bob scope picker showing New Task in Library List option](img/set-workspace.png)

   *Select "New Task in Library List" — confirm your FLGHT4nn library is listed*

   ![Library List scope selected in the Bob chat](img/librarylist.png)

   *Verify the chat scope shows Library List*

---

## 0.5 — Set Private Key Permissions

Save the private key file your instructor shared with you and set its permissions so OpenSSH will accept it. You need this to connect Bob to IBM i in 0.4 and to open the SSH tunnel in Exercise 4.

1. **Save your private key and set its permissions** — Save the private key file your instructor shared with you to a folder on your computer, then set its permissions so OpenSSH will accept it.

   **macOS / Linux** — run in **Terminal**:

   ```
   chmod 600 ae_primary_key.pem
   ```

   **Windows** — run in **PowerShell** (run as Administrator if the command fails):

   ```
   icacls ae_primary_key.pem /inheritance:r /grant:r "$($env:USERNAME):R"
   ```

   This removes inherited permissions and grants only your user read access — required by OpenSSH on Windows.
