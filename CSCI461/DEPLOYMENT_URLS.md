# Deployment URLs for Phase 2 Autograder

## Backend Service URL
**URL:** `http://3.14.4.22`

**Endpoints:**
- Frontend (root): `http://3.14.4.22/`
- Health Check: `http://3.14.4.22/health`
- Models List: `http://3.14.4.22/models`
- Register: `http://3.14.4.22/register`

**Verification:**
Visit `http://3.14.4.22/health` - you should see:
```json
{
  "status": "ok",
  "message": "registry is running"
}
```

## Frontend Service URL
**URL:** `http://3.14.4.22/`

**Note:** The frontend is served from the same FastAPI application at the root endpoint. This is acceptable per the requirement: "it is okay even if you have a blank html page".

You can access:
- Frontend page: `http://3.14.4.22/` (displays HTML interface)
- API endpoints: `http://3.14.4.22/health`, `http://3.14.4.22/models`, etc.

## Where to Register These URLs

1. **Check your course management system** (Canvas, Blackboard, etc.)
   - Look for "Phase 2 Autograder" or "Milestone 8" assignment
   - There should be a form or input fields to submit deployment URLs

2. **Check the autograder portal** (if separate)
   - Your instructor should have provided a link to register deployment URLs
   - Common locations: course website, GitHub Classroom, or dedicated autograder platform

3. **Screenshot Requirements:**
   - Screenshot of the autograder form showing:
     - Backend URL: `http://3.14.4.22`
     - Frontend URL: `http://3.14.4.22/`
   - The URLs should be registered/submitted in the autograder system

## Testing Your Deployment

### Test Backend:
```bash
curl http://3.14.4.22/health
```

Expected response:
```json
{"status":"ok","message":"registry is running"}
```

### Test Frontend:
Open in browser: `http://3.14.4.22/`

You should see the Trustworthy Model Registry frontend page.

## Troubleshooting

If the services are not accessible:
1. Check EC2 Security Group - port 80 must be open (HTTP traffic)
2. Verify the container is running: SSH into EC2 and run `docker ps`
3. Check EC2 instance status in AWS Console
4. Verify the deployment workflow completed successfully

