# kwtSMS Power Automate Connector: Testing Guide

## Step 1: Get a Free Power Platform Account

1. Go to https://powerapps.microsoft.com/en-us/developerplan/
2. Click "Start free"
3. Sign in with a Microsoft account (Outlook, Hotmail, or create one)
4. Follow the prompts to create a developer environment
5. Once set up, go to https://make.powerautomate.com

## Step 2: Import the Custom Connector

1. In Power Automate, click the left sidebar menu
2. Go to **More** > **Discover all**
3. Under **Data**, click **Custom connectors**
4. Click **+ New custom connector** (top right)
5. Select **Import an OpenAPI file**
6. Name it `kwtSMS`
7. Click **Import** and select your `apiDefinition.swagger.json` file
8. Click **Continue**

## Step 3: Configure the Connector

You should see tabs: General, Security, Definition, Code, Test.

### General tab
1. Upload `icon.png` as the connector icon
2. Set icon background color to `#FFA200`
3. Description should already be filled from the swagger
4. Host should show `www.kwtsms.com`
5. Base URL should show `/API`

### Security tab
1. This should show the connection parameters: Username, Password, Sender ID
2. If it doesn't show them, you may need to manually set Authentication type to "No authentication" since our connector uses policy template body injection (the policyTemplateInstances handle auth)

### Definition tab
1. Verify all 5 actions are listed:
   - CheckBalance
   - ListSenderIDs
   - CheckCoverage
   - ValidateNumbers
   - SendSMS
2. Click each action to verify the parameters look correct

### Code tab
1. Leave empty (no script.csx needed)

### Click "Create connector" (top right)

## Step 4: Create a Connection

1. After creating the connector, go to the **Test** tab
2. Click **+ New connection**
3. Enter your kwtSMS credentials:
   - Username: your kwtSMS API username
   - Password: your kwtSMS API password
   - Sender ID: `KWT-SMS` (for testing)
4. Click **Create**

## Step 5: Test Each Action

### Test 1: Check Balance
1. In the Test tab, select **CheckBalance**
2. Click **Test operation** (no inputs needed)
3. Expected response:
   ```json
   {
     "result": "OK",
     "available": (your balance),
     "purchased": (total purchased)
   }
   ```

### Test 2: List Sender IDs
1. Select **ListSenderIDs**
2. Click **Test operation**
3. Expected response:
   ```json
   {
     "result": "OK",
     "senderid": ["KWT-SMS"]
   }
   ```

### Test 3: Check Coverage
1. Select **CheckCoverage**
2. Click **Test operation**
3. Expected response:
   ```json
   {
     "result": "OK",
     "prefixes": ["965"]
   }
   ```

### Test 4: Validate Numbers
1. Select **ValidateNumbers**
2. Enter mobile: `96598765432`
3. Click **Test operation**
4. Expected response:
   ```json
   {
     "result": "OK",
     "mobile": {
       "OK": ["96598765432"]
     }
   }
   ```

### Test 5: Send SMS (test mode)
1. Select **SendSMS**
2. Enter:
   - mobile: `96598765432`
   - message: `Test from Power Automate`
   - test: `1`
3. Click **Test operation**
4. Expected response:
   ```json
   {
     "result": "OK",
     "msg-id": "(some hash)",
     "numbers": 1,
     "points-charged": 1,
     "balance-after": (your balance minus 1)
   }
   ```
5. Go to kwtsms.com dashboard > Sending Queue, find the test message, and delete it to recover the credit

## Step 6: Test in a Real Flow (optional)

1. Go to **My flows** in the left sidebar
2. Click **+ New flow** > **Instant cloud flow**
3. Name it "kwtSMS Test Flow"
4. Choose trigger: **Manually trigger a flow**
5. Click **+ New step**
6. Search for "kwtSMS" in the connector search
7. Select **Check Balance**
8. Save and run the flow
9. Check the run history to see the response

## Troubleshooting

### "No authentication" warning
The connector uses policy templates to inject credentials into the request body. If Power Automate shows a security warning, this is expected for body-based auth.

### Connection parameters not showing
If the connection dialog doesn't show Username/Password/Sender ID fields, check that `apiProperties.json` was correctly configured before import. Re-import if needed.

### Actions return errors
- **ERR003**: Wrong username or password. Verify credentials.
- **ERR010**: Zero balance. Top up your kwtSMS account.
- **HTTP 403**: Same as ERR003, authentication failed.

### Policy templates not injecting auth
If you get authentication errors even with correct credentials, the `setproperty` policy templates may not be working. In that case:
1. Edit the connector
2. Go to the Definition tab
3. For each action, manually add `username` and `password` as body parameters
4. Mark them as "internal" in the visibility settings
5. Update the connector and test again

## Notes

- Always use `test: 1` during development. Set to `0` for production.
- Delete test messages from kwtsms.com queue to recover credits.
- The Sender ID `KWT-SMS` is for testing only. Register a private sender ID for production.
- Phone numbers must be digits only, international format (e.g., `96598765432`).
