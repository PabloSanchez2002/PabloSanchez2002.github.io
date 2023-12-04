
# Web page built on Github Pages
Here you will learn how you can build your own web page just like this one, without any knowledge of backend technology or server programing.

### Step 1: Create a New Repository

First, you need to create a new repository on GitHub where you will host your website. You can name it anything you like, but it's best to keep it simple and descriptive. Make sure you check the box that says "Initialize this repository with a README" so that you can clone the repository to your local machine.

### Step 2: Clone the Repository

Next, you need to clone the repository to your local machine using Git. You can use the command line or a GUI tool like GitHub Desktop. To clone the repository using the command line, navigate to the directory where you want to save the repository and run the following command:

    ```console
    $ git clone https://github.com/your-username/your-repository-name.git
    ```

### Step 3: Choose a Jekyll Theme

There are many Jekyll themes available that you can use for your website. You can browse them on the official Jekyll website or on GitHub. Once you have chosen a theme, you can download or clone it to your local machine.

### Step 4: Copy the Theme Files to Your Repository

Once you have downloaded or cloned the Jekyll theme, you need to copy its files to your repository. Make sure you copy only the necessary files and not the entire repository. The files you need to copy will depend on the theme, but typically they will include an _includes directory, a _layouts directory, and a assets directory. You should also copy the index.html file and any other files that are required by the theme.

### Step 5: Configure Your Website

Now that you have copied the Jekyll theme files to your repository, you need to configure your website. You can do this by editing the _config.yml file in your repository. This file contains various settings for your website, such as the site title, description, and author information. You can also configure the theme settings in this file, such as the color scheme and font choices.

### Step 6: Add Your Content

With the Jekyll theme set up and configured, you can now add your own content to the website. You can create new pages by adding new Markdown files to the repository. These files should be saved in the root directory or in a subdirectory, depending on the theme's file structure. You can also add images and other media to your website by saving them in the assets directory.


### Step 7: Push Your Changes to GitHub

Once you have tested your website locally, you can push your changes to GitHub. To do this, navigate to your repository in the command line and run the following commands:

    ```console
    $ git add .
    $ git commit -m "First commit :)"
    $ git push origin master
    ```

### Step 8: Configure GitHub Pages

Now that you have pushed your changes to GitHub, you need to configure GitHub Pages to serve your website. To do this, navigate to your repository on GitHub and click on the "Settings" tab. Then, scroll down to the "GitHub Pages" section and click on the "Choose a theme" button. Select the theme you want to use and click on the "Select theme" button. Finally, click on the "Save" button to save your changes.

### Step 9: View Your Website

Once you have configured GitHub Pages, you can view your website by navigating to https://your-username.github.io/your-repository-name/ in your browser. You can also view your website by navigating to https://your-username.github.io/ in your browser and clicking on the link to your repository.

### Step 10: Add a Custom Domain

If you want to use a custom domain for your website, you can do so by adding a CNAME file to your repository. To do this, navigate to your repository on GitHub and click on the "Settings" tab. Then, scroll down to the "GitHub Pages" section and click on the "Add custom domain" button. Enter your custom domain in the "Custom domain" field and click on the "Save" button. Finally, add a CNAME file to your repository with the following contents:

    ```console
    your-custom-domain.com
    ```

## And thats pretty much it! You can now build your own web page just like this one, without any knowledge of backend technology or server programing!!! :O


[/back](./)