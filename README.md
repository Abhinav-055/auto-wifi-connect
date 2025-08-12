# Auto Wi-Fi Connect (VIT Vellore)

This tool automatically connects you to the VIT Vellore Wi-Fi network and logs you in.

## How It Works
- The executable (`main.exe`) can be found inside releases under assets.
- When run for the first time, it will ask for:
  1. **Wi-Fi SSID (name)** — the network name (e.g., `VIT2.4G` or `VIT5G`)
  2. **Username** — your VIT credentials
  3. **Password** — your VIT credentials

Once set up, you can schedule it to run automatically whenever your system starts.

---

## Setup in Task Scheduler

1. **Open Task Scheduler**  
   Press `Win + S`, search for **Task Scheduler**, and open it.

2. **Create a New Task**  
   - Click **Create Task** (not "Basic Task" for more control).
   - Give it a name like **Auto Wi-Fi Connect**.
   - Enable **Run with highest privileges**.

3. **Add the EXE**  
   - Go to the **Actions** tab.
   - Click **New** → Choose **Start a program**.
   - Browse to `main.exe` in your project folder.

4. **Set Trigger**  
   - Go to the **Triggers** tab.
   - Click **New**.
   - Select **At log on** or **At startup**.

5. **Save and Test**  
   - Click **OK** to save the task.
   - Right-click your new task and choose **Run** to test.

---
