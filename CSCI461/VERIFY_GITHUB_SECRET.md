# How to Verify Your GitHub Secret `EC2_SSH_KEY`

## ⚠️ The Secret MUST Contain the PRIVATE Key

Your GitHub secret `EC2_SSH_KEY` must contain the **private key**, not the public key.

## ✅ Correct Format (PRIVATE Key):

```
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZWQyNTUxOQAAACA30Fa2kSByxb7JSeq0myuawSv2LC4QO8Y08Whan+9YtQAAAIi0Rxh1tEcYdQAAAAtzc2gtZWQyNTUxOQAAACA30Fa2kSByxb7JSeq0myuawSv2LC4QO8Y08Whan+9YtQAAAEAwUQIBATAFBgMrZXAEIgQg1dCHVM7NKfaHqdRDNnJVYjfQVraRIHLFvslJ6rSbK5rBK/YsLhA7xjTxaFqf71i1AAAAAAECAwQF
-----END OPENSSH PRIVATE KEY-----
```

**Key points:**
- ✅ Starts with `-----BEGIN OPENSSH PRIVATE KEY-----`
- ✅ Contains base64 encoded content in the middle
- ✅ Ends with `-----END OPENSSH PRIVATE KEY-----`
- ✅ NO blank lines between BEGIN and END

## ❌ Wrong Format (PUBLIC Key - This won't work!):

```
ssh-ed25519 N9BWtpEgcsW+yUnqtJsrmsEr9iwuEDvGNPFoWp/vWLU=
```

This is the PUBLIC key - it should NOT be in the GitHub secret!

## Steps to Fix:

1. **Go to GitHub:**
   - Repository → Settings → Secrets and variables → Actions

2. **Edit `EC2_SSH_KEY` secret**

3. **Delete everything in the secret value field**

4. **Copy the PRIVATE key from your `my-ci-key` file:**
   - Open `my-ci-key` in your project folder
   - Copy ALL of it (including BEGIN and END lines)
   - Make sure there are NO blank lines between BEGIN and END

5. **Paste it into the GitHub secret field**

6. **Save**

7. **Verify:**
   - After saving, the workflow's "Prepare SSH key" step should show:
     - ✅ "SSH private key format verified"
     - ✅ "Public key extracted successfully"
     - It should extract: `ssh-ed25519 N9BWtpEgcsW+yUnqtJsrmsEr9iwuEDvGNPFoWp/vWLU=`

## Quick Test:

After updating the secret, trigger the workflow and check the "Prepare SSH key" step logs. It will tell you if:
- ✅ The secret contains a private key (good!)
- ❌ The secret contains a public key (will show error message)

## Current Status:

✅ EC2 instance has the public key in `~/.ssh/authorized_keys`
✅ EC2_HOST should be set to: `3.14.4.22`
❌ EC2_SSH_KEY needs to contain the PRIVATE key (not public!)

Fix the secret and the authentication should work!

