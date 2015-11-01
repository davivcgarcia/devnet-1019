Demonstration Script
===

This is the demonstration script done during **Cisco Live Cancun 2015** session **DEVNET-1019**. The demonstration deploys the **Python** web application, built using **Flask** framework, to a **Dokku** instance running at **Cisco Intercloud Services (CIS)** public cloud.

 1. CLONE GIT REPOSITORY WITH PYTHON APPLICATION EXAMPLE:

 *git clone git@github.com:davivcgarcia/devnet-1019.git*

 2. ACCESS THE LOCAL CLONED REPOSITORY:

 *cd devnet-1019*

 3. CREATE THE DOKKU REMOTE GIT ENDPOINT FOR THE APPLICATION:

 *git remote add dokku dokku@dokku.duckdns.org:devnet-1019*

 4. CREATE APPLICATION PROFILE AT DOKKU:

 *dokku apps:create devnet-1019*

 5. DEPLOY THE APPLICATION CODE TO DOKKU:

 *git push dokku master*

 6. VERIFY THE APPLICATION RUNNING:

 *dokku ps devnet-1019*

 7. SCALE THE APPLICATION TO 2 INSTANCES:

 *dokku ps:scale devnet-1019 web=2*

 8. VERIFY THE APPLICATION RUNNING AFTER SCALING:

 *dokku ps devnet-1019*

 9. CONNECT TO DOKKU INSTANCE RUNNING AT CISCO INTERCLOUD SERVICES (CIS):

 *ssh dokku.duckdns.org*

 10. VERIFY HOW DOKKU USES DOCKER CONTAINERS:

 *sudo docker ps*

 11. VERIFY HOW DOKKU USES NGINX:

 *sudo cat /home/dokku/devnet-1019/nginx.conf*

 12. DESTROY THE APPLICATION PROFILE AND SHUTDOWN FROM DOKKU:

 *dokku apps:destroy devnet-1019*
