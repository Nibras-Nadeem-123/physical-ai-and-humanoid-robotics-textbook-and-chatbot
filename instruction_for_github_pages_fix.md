🔴 DECISION NEEDED: GitHub Pages 404 Error

**Situation**: We are investigating the GitHub Pages 404 error.

**Problem**: The GitHub Actions workflow for deploying to GitHub Pages (`.github/workflows/deploy.yml`) is configured to run only on pushes to the `main` or `master` branches. Although your latest commits containing Docusaurus configuration changes are now on the `main` branch, the workflow might not have been triggered, or there might be a delay.

**To resolve the 404 error, you need to perform the following steps manually:**

1.  **Manually trigger the 'Deploy to GitHub Pages' workflow on the 'main' branch:**
    *   Go to your repository on GitHub: `https://github.com/Nibras-Nadeem-123/Physical-AI-and-humanoid-Robotics`
    *   Navigate to the 'Actions' tab.
    *   In the left sidebar, click on 'Deploy to GitHub Pages'.
    *   On the workflow's page, click the 'Run workflow' dropdown button (usually on the right side above the workflow runs list).
    *   Select 'main' from the 'Use workflow from' dropdown and click 'Run workflow'.

2.  **Monitor the workflow run** to ensure it completes successfully.

3.  **Verify GitHub Pages settings** after the workflow finishes:
    *   Go to your repository settings on GitHub -> 'Pages' section.
    *   Ensure 'Source' is set to 'Deploy from a branch' and the 'Branch' is set to `gh-pages` with the `/root` folder.

Once these steps are completed, please check your GitHub Pages URL again.

**Please confirm when you have triggered the workflow and checked the pages URL.**
