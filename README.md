# Daily Email Scheduler

This project automatically sends a daily email with attachments using Python and macOS's launchd service.

## Project Overview

### Purpose
- Sends automated daily emails
- Includes vision board image and PDF attachments
- Scheduled for 7:30 AM daily delivery
- Uses Gmail SMTP for email delivery

### File Structure
/Users/looremeta/My_Projects/email_scheduler/
├── send_email.py              # Main Python script
├── config.py                  # Configuration file (not in git)
├── 2025 jubilee-pilgrims of hope VISION Board.png
├── Pilgrims of Hope.pdf
├── email.log                  # Success/general logs
├── email.error.log           # Error logs
└── README.md                 # This documentation

## Setup Process

1. Create Python Script (`send_email.py`)
   - Contains email sending logic
   - Handles attachments
   - Uses Gmail SMTP

2. Create Configuration (`config.py`)
   ```python
   # Email configuration
   GMAIL_USERNAME = "your-email@gmail.com"
   GMAIL_PASSWORD = "your-app-password"
   SENDER_EMAIL = "Your Name <your-email@gmail.com>"
   RECEIVER_EMAIL = "recipient@email.com"
   ```

3. Create LaunchAgent
   - Create directory: `mkdir -p ~/Library/LaunchAgents`
   - Create plist: `~/Library/LaunchAgents/com.email.daily.plist`
   - Set permissions: `chmod 644 ~/Library/LaunchAgents/com.email.daily.plist`

4. Load Service
   ```bash
   launchctl load ~/Library/LaunchAgents/com.email.daily.plist
   ```

## Making Changes

### Modify Email Content
1. Open `send_email.py`
2. Edit message body
3. Save file (no restart needed)

### Change Schedule Time
1. Edit `~/Library/LaunchAgents/com.email.daily.plist`
2. Modify Hour/Minute values
3. Reload service:
   ```bash
   launchctl unload ~/Library/LaunchAgents/com.email.daily.plist
   launchctl load ~/Library/LaunchAgents/com.email.daily.plist
   ```

### Update Attachments
1. Replace files in project directory:
   - Vision Board: `2025 jubilee-pilgrims of hope VISION Board.png`
   - PDF: `Pilgrims of Hope.pdf`
2. Keep same filenames or update paths in `send_email.py`

## Service Management

### Common Commands
```bash
# Check service status
launchctl list | grep com.email.daily

# Test run immediately
launchctl start com.email.daily

# View logs
cat email.log
cat email.error.log
```

## Troubleshooting

### Common Issues
1. Emails Not Sending
   - Verify Gmail app password in config.py
   - Check internet connection
   - Review error logs
   - Confirm attachments exist

2. Schedule Not Running
   - Ensure computer is awake at scheduled time
   - Check launchd service status
   - Verify file permissions

### Permission Fixes
```bash
chmod 644 ~/Library/LaunchAgents/com.email.daily.plist
chmod +x /Users/looremeta/My_Projects/email_scheduler/send_email.py
```

## Security Notes
- Keep config.py secure and never commit to git
- Use app-specific password for Gmail
- Regularly update Gmail app password if needed

## Maintenance
1. Monitor log files for errors
2. Verify email delivery daily
3. Check attachment files exist
4. Update message content as needed
