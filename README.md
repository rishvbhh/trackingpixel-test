
### Repository Overview
- `pixel.png`: Your 1x1 transparent tracking pixel image.
- `serv.py`: Python HTTP server that logs pixel requests into `pixel_requests.txt`.
- `test_email.html`: Sample HTML email template embedding the tracking pixel.
- `pixel_requests.txt`: Log file for recorded pixel requests.

### Step 1: Set up and Run the Tracking Pixel Server

1. Clone or download the repository:
   ```bash
   git clone https://github.com/rishvbhh/trackingpixel-test.git
   cd trackingpixel-test
   ```

2. Run the server:
   ```bash
   python serv.py
   ```
   This starts a server on port 8000, serving `pixel.png` and logging every access.

3. (Optional) Run ngrok in a separate terminal to expose your local server publicly:
   ```bash
   ngrok http 8000
   ```
   This gives you a public URL like `https://xxxxx.ngrok-free.app`.

### Step 2: Prepare the Tracking Pixel URL

- Use the public ngrok URL with `/pixel.png` appended as the pixel source, e.g.:  
  `https://xxxxx.ngrok-free.app/pixel.png`
- Replace the pixel URL inside `test_email.html` accordingly.

### Step 3: Send HTML Email with Tracking Pixel Using Thunderbird

1. **Install Thunderbird**  
   Download and install from https://www.thunderbird.net/ if not already installed.

2. **Set up your email account in Thunderbird** (e.g., Gmail or other SMTP-enabled email).

3. **Compose a new email:**

   - Click **Write** to open a new message window.
   - In the message window, click on **Insert** in the menu bar at the top.
   - Select **HTML...** from the dropdown.
   - Paste the full HTML content from `test_email.html` (which includes the tracking pixel `` tag with your ngrok URL).
   - This inserts the pixel and other HTML content properly into your email body.

4. **Fill in the recipient, subject, and send the email**.

### Step 4: Verify Logging

- When recipients open the email, their email client loads the tracking pixel.
- Your server logs these requests in `pixel_requests.txt`, with timestamp, IP, user-agent, and headers.
- Note that some email services like Gmail proxy and cache images, so logging may only show the initial fetch.

### Summary

| Step | Action                                         |
|-------|------------------------------------------------|
| 1     | Run your Python server (`serv.py`) on port 8000 |
| 2     | Start ngrok tunnel (`ngrok http 8000`) to get public URL |
| 3     | In Thunderbird, compose new mail, Insert → HTML, paste email template with pixel URL |
| 4     | Send email to test and check `pixel_requests.txt` for logs |
