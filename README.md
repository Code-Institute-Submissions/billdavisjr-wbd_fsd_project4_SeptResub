# Full Stack Development Course Milestone Project #4 of 4

## AUGUST-SEPTEMBER 2021 VERSION - FIRST RESUBMISSION

Student: Bill Davis

- <http://www.williambdavisjr.com>

- Email: [bill.davis@gmail.com](bill.davis@gmail.com)

PROJECT GIT REPOSITORY:

- [https://github.com/billdavisjr/wbd_fsd_project4](https://github.com/billdavisjr/wbd_fsd_project4)

DEPLOYED PROJECT SITE

- [https://wbd-fsd-project4.herokuapp.com/](https://wbd-fsd-project4.herokuapp.com/)

---

## CHANGES IN FIRST RESUBMISSION

Because I work full time and am taking this course as a continuing-education course in my spare time, I was not to complete the entire
projects in the time available. But I was able to come within 2% of the 50% passing score.  So I took advantage of the first of two
allowed resubmissions in the hopes that I could obtain a better grade.

### ADDED IN THIS RESUBMISSION

- Added links in My Account menu (when authenticated and superuser) to go to Django admin, Django admin quotes table editing and Django admin category table editing.
- Added new Manage menu for add/change/delete quotes and categories.
  - Added add-quotation functionality
  - Added edit-quotation functionality
  - Added delete-quotation functionality
  - Added category list functionality
  - Added add-category functionality
  - Added edit-category functionality
  - Added delete-category functionality
- Fixed error when passing a quote id that isn’t found
- Remove authors who are not in database yet from ‘Featured’ menu.
- Expanded "Featured" menu
- Added message header (was disabled) for displaying Django messages.
  - If no results found on search, display message telling user that.
  - Display count of search results and total # of quotes in database.
- Fixed lots of cosmetic problems on different size screens
- Added “deployment” documentation for GitPod and Heroku to the README.md file (finished or close to it, but untested

There is still a lot to do, but I only had a few days in which to work on the submission and I hope that this version will be more acceptable, even if it is still unfinished.

I tagged the prior submission in Git as "FirstSubmission" in case you wish to review the original submission.

---

## INTRODUCTION

This is the fourth milestone project for my Code Institute Full Stack Developer Course.

## IMPORTANT NOTE: DUE TO SOME UNFORSEEN CIRCUMSTANCES I WAS UNABLE TO COMPLETE THIS PROJECT BY THE DEADLINE

FOLLOWUP NOTE: THIS IS THE FIRST PROJECT RESUBMISSION ATTEMPT OF TWO ALLOWED; THE PROJECT IS STILL NOT COMPLETED BUT IS CLOSER TO IT.

An extension was requested due to some exigent circumstances (more below) but was not been approved because I already have paid for two extension since I am taking this course in my spare time and my job did not allow for much of that.

I recently lost my job, had to find and start a new one, and also experienced a family emergency, I lost a lot of time and was not able to finish this project in the time available. I am taking this course as a continuing education course after working hours and I just did not have enough time available to do the work. I had no problems with the material (I've got 40 years of software development experience and a bachelor's degree in Computer Science), I just had problems finding TIME to work on the coursework project on nights/weekends.

Therefore I am providing what I had time to do, rather than submitting nothing, but it's probably less than halfway done.

I'm not asking for sympathy, just expressiong my apologies for the state of this submission.

I have learned a lot from this course and I am disappointed that I was unable to do a better job. I'm sure I would have if I'd had more time available or was a full-time student. Hopefully my prior 3 projects demonstrate that, too.

---

## PROJECT CONCEPT

We've all seen quotations in books, hung on a wall, as an e-mail signature, or used in a presentation.

This site is a quotations database and search engine, with categorizations and ratings. It's useful to search for quotations
about a topic for many purposes, such as those described earlier. Searching the database is free, but with a user subscription
you can maintain a list of favorite and with a more expensive subscription, add your own quotes to the database.

This site is a recreation of the third milestone project (which was done with Python3 and Flask) using Python3 and Django
instead, and adding features such as:

- User accounts and authentication
- Annual Subscriptions you can purchase to let you store your favorites and to add your own quotes.
- Credit card support for subscription purchases using Stripe.

I have many additional plans and ideas for this site as well (detailed elsewhere) that will not be a part of this project, but will be implemented later. Eventually I hope to monetize this site even further, by selling merchandize or posters with the quotes & sayings printed on them, with photographic or other backgrounds, possibly using a site such as Cafe Press or RedBubble if I can find one that has an API that lets me submit artwork generated by the site, to be produced onto things like posters, mugs, t-shirts, masks, and so on.

### PREVIOUS VERSION OF THIS SITE FROM THIRD MILESTONE PROJECT

- [https://wbd-fsd-project3.herokuapp.com/](https://wbd-fsd-project3.herokuapp.com/)

### PREVIOUS VERSION GIT REPOSITORIES

- [https://github.com/billdavisjr/wbd_fsd_project3.git](https://github.com/billdavisjr/wbd_fsd_project3.git)

- [https://git.heroku.com/wbd-fsd-project3.git](https://git.heroku.com/wbd-fsd-project3.git)

---

### PREVIOUS PROJECTS

Project 1 - IowaPen web site 1.0 repo: <https://github.com/IowaPen/WBD_FSD_Project1>

Project 2 - IowaPen web site 2.0 repo: <https://github.com/IowaPen/WBD_FSD_Project2>

Production IowaPen Web Site is at <https://iowapen.club>

- repo: <https://github.com/IowaPen/iowapen.github.io>
- hosted on GitHub Pages at <https://iowapen.github.io/> and also at the production URL above.

---

## UX - USER EXPERIENCE

This section provides insight into the UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

### USER STORIES

User stores are statements of the form "As a _user type_, I want to perform an _action_, so I can achieve a _goal_.

Here are the user stories for this project.

- As a collector of quotes, I want to store my quotes in a database, so I can access them anywhere.

- As a fan of quotes, I want to be able to search for a quote using a few words, so I can find it and use it.

- As a write, I need to be able to search for quotes by category or keyword, so I can start a chapter or section with an appropriate quote.

- As someone who is putting together a presentation, I need to be able to search for a relevant quote, so that I can put it in my presentation.

- As a user of this site I need to be able to favorite quotes in the site's database so I can find them again (a simple form of having your own list of quotes)

- As a user of this site I need to be able to keep a database of my own quotes including favoriting them and rating them.

### FUTURE

- As someone wanting a gift for a friend, I want to find or add a quote relevant to my friend, then have it put on a poster, t-shirt or coffee mug.

---

## DESIGN

### DATABASE / DJANGO MODELS

    Category  - the type/subject of the quote
        - id (PK - unique)
        - name
        - display_name

    Public Quotes
        - id (private key) - unique
        - Owner (null) - not visible to users
        - UniqueID
        - Text
        - Person
        - Category id (foreign key)
        - Source
        - DateSaid
        - Favorite (boolean)
        - Star Rating (float 0.0-5.0 in .5 increments) - not settable by users except sys admin

To load the above database tables with data, fixtures are available. From the command line do the following, in this order;

_**It is important to do them in the right order:**_

> $ python3 manage.py loaddata categories
>
> $ python3 manage.py loaddata quotations

### MODELS NOT YET CREATED

    User Rating (of public quotes)
        - User id
        - Quote id (foreign key)
        - Favorite (boolean)
        - Star Rating (float - 0.0 to 5.0)

    Subscription
        - Date purchased
        - Term
            - Trial $0 (1 month)
            - Yearly $5 (100 quotes)
            - Lifetime $50 (1000 quotes)
            - Unlimited $100 (unlimited quotes)
        - Type
            - None (not an actual type)
                You can search for quotes in the public database and that's all
                    - you don't have a subscription or and account; ANYONE gets this much.
            - Basic
                - you can favorite quotes in the public database
            - Full
                - add your own quotes
                - star ratings (0.0-5.0) for your own quotes
                - favorite your own quotes
                - favorite public quotes

---

## WIREFRAMES

### MAIN PAGE - SEARCH ENGINE

Wireframes are available in the /wireframes directory in the repository. Several tools were used before I settled on Balsamiq since CodeInstitute provides a free version for students.

Just like other web search engines, you type in some text and click search. You'll be taken to a search results page.
This page also lets you click "Random Quote" to display a nicely formatted random quote in the text box below the Search
field. That box will also be filled with a random quote each time the page is loaded. The logo at the top will have a
moving starfield behind it such as what you'd see in a science fiction movie or TV show. I actually own the domain names
quotations.space and quotation.space (singular) for use with this site, along with quoogle.com (like google, but starting
with 'quo' instead of 'goo') but am not sure I want to risk using a domain name so similar, to avoid legal hassles.

![Main Page - Search Engine](./wireframes/png/main_page_search.png)

NOTE: Time did note permit me to add other wireframe images here.

- Search results - card viewable
- Search results - list viewable
- Search results - random button

- Categories
- Add Category (admin ONLY)
- Edit Category (admin ONLY)

- Add quote
- Edit quote
- Full screen quote display

- Account creation
- Account editing

- Subscription sign up
  - trial
  - basic
    - (favorite/rate quotes @ \$5/yr)
  - FUTURE
    - full
      - add/edit own quotes with their own favorite status and star rating (\$25/yr)
      - Lifetime (\$100 for life)
      - Unlimited?

---

## FEATURES

### Existing Features

- Allow user to do a freeform search for quotes, matching. the text or author name.

- Allow sorting of the search results by:
  - author
  - star rating
  - category

- Filter by star rating (1.0 - 5.0)

- View curated list of quotes by specific people.  This sites's focus is "space quotes", by that I mean scientists, science fiction and fantasy authors, but we'll also have quotes by well known folks like Mark Twain, Ambrose Bierce, Ben Franklin, Abe Lincoln etc.

### Features Left to Implement

- Allow user to do things based on their subscription level
  - Free level: search
  - Basic level: favorite and add star rating that overrides built-in rating
  - Full level: add their own quotes, add quotes from the main library to their "collection"

- Allow users to put quotes on graphical backgrounds from a library from free images or uploading their own.
  - Move the quote around the image
  - Change the font and style and size of the text
  - Save the image to a JPG or PNG file and download it.
  - Store the image settings (text location/box size, font/size/style, photo) in a database table

---

## Technologies Used

This section discusses all of the languages, frameworks, libraries, and any other tools used to construct this project, a link to its official site and a short sentence of why it was used.

- [Python3] - mandated by the course requirements

- [Django] - mandated by the course requirements

### Django frameworks

See the requirements.txt file for all frameworks used; some are called by other frameworks we use directly and are added to the requirements.txt file using the command `$pip3 freeze >requirements.txt` and they can be installed by `pip3 install -r requirements.txt` or individually by `pip3 install <name of framework>` e.g. `pip3 install db_database_url`

Used for PostgreSQL support (when deployed on Heroku where that is used instead of SQLite)

- sycopg2-binary
- dj_database_url

Authentication

- django-allauth - Allauth, used for user loging/authentication

Used for Amazon S3 support

- boto3 -
- django_storages -

Other

- gunicorn - our web server on Heroku

### JavaScript Frameworks

- [JQuery](https://jquery.com)

  - The project uses **JQuery** to simplify DOM manipulation.

- [Bootstrap](https://getbootstrap.com/)

  - The project uses **Bootstrap** for CSS formatting of our page GUIs.

- [FontAwesome](https://fontawesome.com/)

  - We use FontAwesome for the various icons on our site.

- [Google Fonts](https://fonts.google.com/)
  - We use the Google Fonts API for our site fonts (Lato, etc.)

### WIREFRAME TOOLS

- [Balsamiq](https://balsamiq.com/wireframes/)

  - Wireframes for the design of the various pages were created in the popular Balsamiq wireframe tool; Code Institute gives
    students a free license to use it for a year (at present, anyway).

- [Figma](https://www.figma.com)

  - Web-based wireframe tool with a free tier; used because Balsamiq had a free key through
    Code Institute that expired at the end of the year, when meant it was going to expire in the middle of the design process
    and when the Code Institute staff was out of the office over the holidays. Stopped using Figma when Code Institute sent us
    a key for Balsamiq for 2021.

- [Pencil](https://pencil.evolus.vn/)
  - Another wireframe tool that I investigated before going back to Balsamiq.

### OTHER TOOLS / SERVICES

- [GitHub](https://www.github.com/)

- [GitPod](https://www.gitpod.io)

- [Heroku](https://www.heroku.com)

- SqlLite3

  - used by Django for the development server database

- PostgreSQL

  - used in production on Heroku to replace the Sqlite 3 database Django normally uses.

- [AWS - Amazon Web Services](http://aws.amazon.com/)

  - we use Amazon Web Services to <<<<< FILL IN THE REASONS >>>>>

- Syntax checkers and Linters on GitPod are used to keep the code clean, correct and consistently styled for best practices.
  - markdownlint
  - cornflakes

### IMAGE MANIPULATION

I attempted to use tools such as [TinyJPG](https://tinyjpg.com/) to shrink the size of the background graphic (yellow with a book at
the bottom) but got too much banding of the yellow background and so did it myself using a graphics program and shrinking it myself.
I got it down to about 50% of the original size, at least, before JPEG compression artifacts started banding the yellow background.

## FAVICON FOR SITE

To add a favicon.ico to a Django app so it has a distinctive icon in the web browser window/tab, I found information at:

<https://simpleit.rocks/python/django/django-favicon-adding/>

## SCRIPTS

I created several shell scripts to make development easier, backup/restore the database etc. These can be found in the /scripts folder.

### DATABASE DUMP RESTORE

These were inspired by a note in the course on getting your data into PostgreSQL in Heroku if you didn't create fixtures (though I have).
These could also be useful in creating final fixtures, since I moved data over from an Excel spreadsheet of quotes and might make fixes or other changes to the quotes once they are in the database on my development machine.

- dumpdb.sh - dumps the database to a file named db.json in the root of the project, pretty printed through command line tool json_pp
- loaddb.sh - loads the database from db.json into db.sqlite3.

## DATA CLEANUP

- [Microsft Excel](https://www.microsoft.com/)
  - my "database" of quotations has been kept in a simple text file for years, because it's fast and easy to add quotes to the end. It's also each to move to different platforms, as I have done repeatedly over many years when learning a new programming language or p latform. Also, a text filke can be used with any system. It's been fast enough in practice, even with over 10,000 quotes, and reading them into an in-memory array makes it speedy. But for this project I wanted a database so I used Excel to clean up the text file into rows and columns of data. I also use Microsoft Visual Basic for Applications (VBA) to write some code to do some of the cleanup and export the quotatio data in JSON format for import into the SQL database.

---

## TESTING

<<< I DID NOT HAVE THE TIME TO FILL OUT THIS SECTION>>>

### RESPONSIVE TESTING

    DESKTOP
    * Desktop computer
        * 2560 x 1440 (Apple iMac)
        * Google Chrome Developer Tool screen size emulation

    MOBILE
    * iPhone 11 Pro Max
    * iPhone 4s
    * iPad Air
    * iPad mini

### BUGS

#### Unusual bugs

Ran into this problem after GitPod updated us to vscode from theia.  I was getting the message "Class 'Category' has no 'objects' memberpylint(no-member)" and a similar one for the other model, in views.py in the quotations app.  In Googling for the problem, it's a warning from the linter and there are several solutions but one is to add:

> objects = models.Manager()

in models.py for each model class.  There are other fixes as well that involved adding linter property settings but I preferred this fix.

See: <https://stackoverflow.com/questions/45135263/class-has-no-objects-member#comment77506387_45150811>

---

## DEPLOYMENT

This section describes the process to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

It provides all details of the differences between the deployed version and the development version, if any, including:

- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

> NOTE: followed the same process as the Boutique Ado deployment in the course.

Create accounts on the following services if you don’t have one; the free account on all of these is fine:

- [GitHub](https://github.com) - for access to our project source code / cloning it
- [GitPod](https://gitpod.io/) - for our development environment / IDE
- [Heroku](https://heroku.com) - for hosting our web application and database
- [Strip](https://stripe.com) - for e-commerce credit-card handling

If you're not using one or more of the above sites, but something similar,  hopefully the following will help you but it's not possible
to describe how to check out, install, and deploy on every available source code repository, IDE, hosting environment, etc.

### GITPOD DEPLOYMENT (development environment)

- Clone the GitHub source code into your own GitHub repository.
- Open the repository in Gitpod. (See GitPod.com for info on how to use GitPod with GitHub)
- Set environment variables (some of them, not all that are used in Heroku)
- Install Django packages (from requirements.txt; might need to update pkgs, regenerate requirements.txt)
  - <<< add the command to install packages from requirements.txt >>>
- Run migrations and populate database using fixtures ($ python3 manage.py migrate)
- Start server & find URL to use to view site. ($python3 manage.py rundserver)

### HEROKU DEPLOYMENT (production or test environment)

- Clone the source code into your own repository in GitHub.
  - << add how> >>
- Open the repository in Gitpod. (See GitPod.com for info on how)
  - << add how >>
- Make sure you have verified the email address you used creating your Heroku account and log in to your account.
- Install the Heroku CLI in your development environment if you are not using GitPod. (where it was installed for you)
  - << add how >>
- Log in to Heroku from the command line:

  >  \$ heroku login -i

  To get commands you can use for Heroku toolbelt / Command Line Interface (already installed in Gitpod) in terminal see:

  > \$ heroku
  >
  > \$ heroku apps

- Check and update heroku tool belt in terminal:

  > \$ heroku update

  If you don’t use GitPod, refer to Heroku.com for how to install the Heroku CLI in your IDE.

- Install the Django packages the project uses:

  > $pip install -r requirements.txt

  The -r means install the pacakges from the requirements.txt file. If you want to install updated packages (latest version) then
  use:

   > $pip install -r requirements.txt

  and then you might want to generate an updated requirements file with the new versions.  This is not required but might be
  helpful if things don't seem to be working.

  > pip3 freeze --local > requirements.txt

- Create a heroku app, in terminal:

  > \$ heroku create _uniqueAppName_ --region us

- Connect repository to Heroku

  > \$ git remote -v

  this will give a list of remote repositories for this project

<< add more detail here >>

- Set up Postgresql database

  > \$ heroku addons:create heroku-postgresql:hobby-dev

  Open and log in to the heroku.com web site and go to the app dashboard, click on settings > config vars to find the DATABASE_URL string

### SET UP DJANGO ENVIRONMENT VARIABLES IN HEROKU

  << how do you get there

Use this or some other Django secret key generator to create one for your deployment:

<https://miniwebtool.com/django-secret-key-generator/>

Environment variables used:

> SECRET_KEY = << get from secret key generator above >>
>
> HOSTNAME = _yourHerokuAppName_
>
> DEVELOPMENT = 1
>
> DATABASE_URL =_database url you set up earlier - from Heroku settings config variables_
>
> DEBUG = 1

Note: the USE*AWS and AWS*\* variables

- AWS was used in the FSD course to host static files and images, but is not this project because setting this up in AWS is just too dang complex to document in a README file, honestly! If you want to do that, feel free, but I don't feel it's necessary to do here.

### STRIPE variables

<< if I make it to implementing that, add it here>>

_Note_: You can look at your environment variables using ‘heroku config’ from the command line.

- Set SECRET_KEY and other environment variables in config vars on heroku dashboard

- **IMPORTANT** - Restart vscode before checking if this works. Enviroment variable are activated on restarting vscode.

In terminal:

> \$ heroku config

this will show that the DATABASE_URL has been stored

### CREATE PROCFILE IF NEEDED

in terminal:

> \$ python manage.py migrate
>
> \$ echo web: gunicorn django_todo.wsgi:application > Procfile
>
> \$ heroku config:set DISABLE_COLLECTSTATIC=1 -a yourAppName

Add heroku app name to ALLOWED_HOSTS in settings.py or use environment variable (HOSTNAME), be sure to also allow localhost.

### **IMPORTANT: Make sure to commit all changes before trying to push to heroku**

In terminal, push to GitHub

> \$ git push

And then deploy to Heroku.

> \$ git push heroku master

To link heroku to github

1. go to heroku dashboard, click on "deploy"
2. in "deployment method" section, click on GitHub
3. put in GitHub repo name then click > search > select
4. manually deploy from this place any time you want to update the live website.

<< add info on how to set up so you can just do \$ git push (or git push master or git push origin master??) >>

You can set the "Deploy" tab in Heroku to connect to GitHub. Search for your repo, click Connect and then enable automatic deploys.
Now when you push to GitHub the code will be deployed to Heroku as well.

Note: If you created the web app using web site instead of the CLI you may need to set up your Heroku git remote:

> \$ heroku git:remote -a yourAppName

And check it:

> \$ git remote -v

and make sure you see something that looks like:

> heroku  <https://git.heroku.com/yourAppName.git> (fetch)
>
> heroku  <https://git.heroku.com/yourAppName.git> (push)
>
> origin  <https://github.com/yourGitHubAccount/yourRepoName.git> (fetch)
>
> origin  <https://github.com/yourGitHubAccount/yourRepoName.git> (push)

If it doesn’t deploy correctly you can check the logs to figure out why:

> \$ heroku logs —tail

To test if it works locally

SETTING UP DATABASE (apply migrations, load data using fixtures)

Use SQLite3 in GitPod and Postgres on Heroku. If you want to use something else, update environment variables accordingly.

> \$ python3 manage.py migrate

Then (in this order, very important):

> \$ python3 manage.py loaddata categories
>
> \$ python3 manage.py loaddata quotes

#### CREATE A USER TO LOG IN

> \$ python3 manage.py create superuser

#### TESTING YOUR SETUP

In terminal:

> \$ python manage.py runserver

Then ctrl-click local link provided in terminal for the web app.

To test if it works on heroku

1. git push most recent code to github
2. log into heroku dashboard for app
3. click deploy
4. scroll down to "Manual deploy"
5. select correct branch of github code
6. click "deploy branch"
7. Once build is completed, click "view" button

Go to the URL + /admin and log in as your superuser account to see if you can.

#### CLEANUP

- Remember to remove the DISABLE_COLLECTSTATIC environment variable once you are deployed to Heroku

#### Attribution

The source for some of the Heroku deploy process (HIGHLY modified here):
<https://code-institute-room.slack.com/files/UF94247RB/FNZUV8MS8/Untitled.txt>

---

## CREDITS

### CONTENT

- The quotes in my quotes database (which is 10 times larger than the ~1000 quotes used in this project) have been gathered over a few decades by myself from a myriad of sources; quotes articles, quotes in books, the list is endless. Originally kept in a text file, they were imported into an Excel spreadsheet to make it easier to output in JSON format (custom Visual Basic for Applications code was written and is in the /vba directory of the repository) and to sort, number, de-duplicate and in many ways clean up and standardize the quotation collection. That larger collection of quotes is NOT included here.

### MEDIA

- The photos used in this site were obtained from the following source(s):

  - Page background image from Pexels.com by [Stas Knop](https://www.pexels.com/@stasknop) can be found [here](https://www.pexels.com/photo/white-book-in-white-table-near-yellow-wall-3760323/)

  - Favicon was created by me

  - The animated starfield behind the page header is from WikiMedia Commons:
    <https://commons.wikimedia.org/wiki/File:StarfieldSimulation.gif>
    <https://upload.wikimedia.org/wikipedia/commons/e/e4/StarfieldSimulation.gif>

### Acknowledgements

- The template for this README file came from a [template](https://github.com/Code-Institute-Solutions/readme-template) from Code Institute.
  The README file for that is at the end of this README file.

- Some code in the base.css file (the .icon class) came from [Bulma](https://bulma.io/), a CSS framework similar to Bootstrap

- Creating the scrollable CATEGORY dropdown menu used the CSS from this code example: [Bootstrap Scrollable Dropdown Menu](https://www.codeply.com/go/Uh8qadr3q2/bootstrap-scrollable-dropdown-menu)

---
---
---

### THE FOLLOWING IS THE README.MD FILE FROM THE [CODE INSTITUTE GITPOD REPOSITORY TEMPLATE](https://github.com/Code-Institute-Org/gitpod-full-template)

---

If you have difficulty checking out the code and having it compile for some reason, fork the above
template, create a new GitPod workspace from it by adding <https://gitpod.io/#>
to the front of your forked repository URL, then once the code in the repository that runs when you
open in it GitPod has set up the environment, copy over the source code for this project and replace
the GitPod template code. You might want to remove all the git related hidden directories/files first.

---

![Code Institute Logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Bill Davis,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started.
You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though!
It contains some important information about Gitpod and the extensions we use.

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the [README.md](https://github.com/Eventyret/vscode-bcdn) file at the official repo</a> for more options.

---

Happy coding!
