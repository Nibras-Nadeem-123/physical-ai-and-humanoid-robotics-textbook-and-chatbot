**I have updated the `.github/workflows/deploy.yml` file to use the latest versions of the GitHub Actions, which should resolve the deprecation warning you encountered.**

To make these changes take effect and to potentially resolve the GitHub Pages 404 error, please:

1.  **Commit and push the changes** I just made to `.github/workflows/deploy.yml` to your `main` branch.
    *   You can do this manually:
        ```bash
        git add .github/workflows/deploy.yml
        git commit -m "chore(github): update deploy workflow actions"
        git push origin main
        ```

2.  **Manually trigger the 'Deploy to GitHub Pages' workflow on the 'main' branch** again, as described in the previous instructions:
    *   Go to your repository on GitHub: `https://github.com/Nibras-Nadeem-123/Physical-AI-and-humanoid-Robotics`
    *   Navigate to the 'Actions' tab.
    *   In the left sidebar, click on 'Deploy to GitHub Pages'.
    *   On the workflow's page, click the 'Run workflow' dropdown button.
    *   Select 'main' and click 'Run workflow'.

**Please confirm once you have completed these steps and checked the GitHub Pages URL.**
