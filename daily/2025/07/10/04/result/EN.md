The correct way to solve the problem is to use the official WP Engine tool: https://github.com/wpengine/github-action-wpe-site-deploy
1) Instead of manually copying the environment,  commit the changes to Git and push them to a repository (e.g., GitHub).
2) The push will automatically trigger the deployment process to the production environment using GitHub Actions.
3) `github-action-wpe-site-deploy` provides the `SCRIPT` parameter, which allows specifying the path to a bash script.
This script will execute immediately and automatically on the target WP Engine environment after file deployment is complete.
Inside the script, use WP-CLI to trigger your PHP code.
4) This approach aligns with modern DevOps practices:
4.1) It ensures a complete audit trail through the Git commit history. 
4.2) It becomes repeatable and automated, reducing the risk of human error. 
4.3) It utilizes officially supported and documented features of the WP Engine platform.
---
I have completed 536 projects here on Upwork.
My GitHub profile: https://github.com/dmitrii-fediuk
My websites: https://df.tips?order=views, https://mage2.pro?order=views, https://dmitry.ai?order=views 