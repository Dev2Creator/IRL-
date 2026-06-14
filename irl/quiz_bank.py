# ══════════════════════════════════════════════════════════════════════
# QUIZ BANK FOR CHAOS QUIZ (750+ Questions, 6000+ Lines)
# ══════════════════════════════════════════════════════════════════════

QUIZ_BANK = [
    {
        "question": "Your production database just dropped itself. What is your next move?",
        "a": "Git blame to find out who to fire",
        "b": "Push a hotfix to production on a Friday at 4:59 PM",
        "c": "Cry loudly in the server room",
        "d": "Flee the country and start a new life as a goat farmer",
        "correct_key": "d"
    },
    {
        "question": "What is the true purpose of a Scrum Master?",
        "a": "To protect the team from external interruptions",
        "b": "To ask 'Any blockers?' in 50 different ways",
        "c": "To force developers to estimate tickets in Fibonacci sequence numbers",
        "d": "To facilitate agile ceremonies",
        "correct_key": "b"
    },
    {
        "question": "Which of these is the most acceptable reason for writing spaghetti code?",
        "a": "Job security",
        "b": "I was promised pizza for shipping by midnight",
        "c": "It looked good to me at 3 AM after 6 Red Bulls",
        "d": "The client changed the requirements 12 times in a week",
        "correct_key": "a"
    },
    {
        "question": "What does DNS stand for (according to junior devs)?",
        "a": "Did Not Ship",
        "b": "Domain Name System",
        "c": "Developers Need Snacks",
        "d": "Do Not Sleep",
        "correct_key": "b"
    },
    {
        "question": "A wild bug appears in production at 2 AM. You should...",
        "a": "Rollback and pretend it never happened",
        "b": "Blame the intern (even if there isn't one)",
        "c": "Deploy a console.log('here') and go back to sleep",
        "d": "Add a try/except around the entire codebase",
        "correct_key": "a"
    },
    {
        "question": "What is the optimal number of npm packages in a Hello World app?",
        "a": "0",
        "b": "Yes",
        "c": "47",
        "d": "1,247",
        "correct_key": "b"
    },
    {
        "question": "Why did the senior developer cross the road?",
        "a": "To get a third double-espresso of the morning",
        "b": "Because it was a hard requirement in the sprint plan",
        "c": "To see if the other side was in dark mode",
        "d": "To escape a 3-hour standup meeting",
        "correct_key": "c"
    },
    {
        "question": "Which of the following is the most effective debugging technique?",
        "a": "Rewriting the entire feature in Rust",
        "b": "Writing comprehensive unit tests",
        "c": "Explaining the code to a rubber duck until the duck sighs",
        "d": "Staring at the screen until the code feels ashamed and fixes itself",
        "correct_key": "d"
    },
    {
        "question": "Your CSS flexbox layout is slightly misaligned on Safari only. What is the solution?",
        "a": "Change the font size to `1.0001rem` and hope nobody notices",
        "b": "Add `display: flex;` to every single HTML tag",
        "c": "Delete Safari from existence",
        "d": "Add `!important` to 47 different properties",
        "correct_key": "c"
    },
    {
        "question": "What is the main advantage of microservices?",
        "a": "Writing the same config file in 15 different directories",
        "b": "Easier deployment and independent scaling",
        "c": "Turning a single simple error into a distributed tracing mystery game",
        "d": "Getting to write Kubernetes YAML configurations for 9 hours a day",
        "correct_key": "c"
    },
    {
        "question": "What happens when you run `rm -rf /` on a production server?",
        "a": "It cleans up temporary files and optimizes speed",
        "b": "Your boss gets a sudden, intense feeling of dread",
        "c": "The server goes into quiet mode",
        "d": "A beautiful ASCII shrimp appears",
        "correct_key": "b"
    },
    {
        "question": "How do you exit Vim?",
        "a": "`:wq` followed by Enter",
        "b": "Buying a new computer",
        "c": "Calling your local system administrator to reboot the mainframe",
        "d": "Unplugging the computer from the wall outlet",
        "correct_key": "d"
    },
    {
        "question": "What does a compiler do when it sees perfectly valid C++ code?",
        "a": "Sighs and complains that it prefers Rust",
        "b": "Compiles it into a fast executable",
        "c": "Segfaults out of sheer spite",
        "d": "Generates 4,000 lines of template expansion warnings",
        "correct_key": "d"
    },
    {
        "question": "Which statement best describes JavaScript's type system?",
        "a": "An absolute circus where `[] + {}` equals `[object Object]`",
        "b": "Strongly typed and mathematically sound",
        "c": "Weakly typed but predictable",
        "d": "A carefully guarded secret known only to Brendan Eich",
        "correct_key": "a"
    },
    {
        "question": "What is the primary function of a pull request reviewer?",
        "a": "To ensure code quality and correctness",
        "b": "To leave nitpicks about line breaks and variable naming style",
        "c": "To click 'Approve' without reading the 14,000 lines of changes",
        "d": "To ask 'Why didn't you write this in Rust?'",
        "correct_key": "c"
    },
    {
        "question": "A recruiter contacts you for a role requiring 10 years of experience in a framework that was created 2 years ago. You should...",
        "a": "Explain the linear progression of time to them",
        "b": "Apply anyway, claiming you invented it in a dream in 2016",
        "c": "Politely decline and block their email address",
        "d": "Ask for a salary paid in custom crypto tokens",
        "correct_key": "b"
    },
    {
        "question": "What is the developer equivalent of 'living on the edge'?",
        "a": "Drinking coffee after 4 PM",
        "b": "Declining a calendar invitation from the CEO",
        "c": "Commit and push directly to main without running tests locally",
        "d": "Testing your code in staging first",
        "correct_key": "c"
    },
    {
        "question": "Your regex works perfectly on the first try. What is the catch?",
        "a": "You are actually dreaming and about to wake up",
        "b": "You accidentally matched the entire internet",
        "c": "It only matches empty strings",
        "d": "You wrote it in your sleep",
        "correct_key": "b"
    },
    {
        "question": "What is the most accurate definition of 'Legacy Code'?",
        "a": "A codebase that has zero documentation but runs 90% of the business",
        "b": "Code written by previous engineers who have left the company",
        "c": "High-quality, battle-tested software architecture",
        "d": "Any code that you wrote more than 25 minutes ago",
        "correct_key": "d"
    },
    {
        "question": "Why do programmers prefer dark mode?",
        "a": "It uses less monitor battery",
        "b": "To look like a hacker in a movie from 1995",
        "c": "Because light attracts bugs",
        "d": "It hides the tears better",
        "correct_key": "c"
    },
    {
        "question": "What is the first step in resolving a git merge conflict?",
        "a": "Deleting the local repository and cloning it again",
        "b": "Git push --force-with-lease and hope the other dev doesn't notice",
        "c": "Blaming Git for being overly complicated",
        "d": "Reading both versions carefully and merging line-by-line",
        "correct_key": "a"
    },
    {
        "question": "What does a QA engineer do when you tell them 'It works on my machine'?",
        "a": "Packages your machine and deploys it to the production cluster",
        "b": "Files a bug report about your machine",
        "c": "Accepts it and closes the ticket as resolved",
        "d": "Stares at you with cold, unblinking eyes",
        "correct_key": "d"
    },
    {
        "question": "Which of these is the most accurate translation of 'I'll fix this tomorrow'?",
        "a": "I will fix it on the next business day",
        "b": "I have already forgotten about this bug",
        "c": "I will create a ticket that will languish in the backlog for 18 months",
        "d": "I will ask the intern to look at it next week",
        "correct_key": "c"
    },
    {
        "question": "What does the 'S' in IoT stand for?",
        "a": "Sensor",
        "b": "System",
        "c": "Security",
        "d": "Software",
        "correct_key": "c"
    },
    {
        "question": "Your project manager asks for a 'quick estimate' on a rewrite of the core engine. You should...",
        "a": "Pretend your audio is breaking up and leave the call",
        "b": "Multiply your guess by 3, add 2 weeks, and change the unit to months",
        "c": "Give a realistic, detailed timeline based on architectural analysis",
        "d": "Say 'Two days' and then turn off your Slack notifications",
        "correct_key": "b"
    },
    {
        "question": "What is a 'Full-Stack Developer'?",
        "a": "A mythological creature like a unicorn or a well-documented API",
        "b": "Someone who knows both HTML and CSS",
        "c": "A developer who can write bugs at every layer of the application stack",
        "d": "An engineer who is equally competent in frontend and backend systems",
        "correct_key": "c"
    },
    {
        "question": "What does your IDE do when you type a single typo in a Javascript file?",
        "a": "Freezes your entire operating system for 45 seconds",
        "b": "Throws 800 TypeScript errors in unrelated files",
        "c": "Auto-corrects it to something completely wrong",
        "d": "Quietly highlights it in red",
        "correct_key": "b"
    },
    {
        "question": "How does a developer solve a difficult bug?",
        "a": "By writing a detailed reproduction script",
        "b": "By blaming the cloud provider's regional outage",
        "c": "By explaining it to their spouse, who doesn't code, and immediately seeing the fix",
        "d": "By deleting the file and starting over",
        "correct_key": "c"
    },
    {
        "question": "What is the primary purpose of writing documentation?",
        "a": "To write instructions that will be outdated by the next git commit",
        "b": "To prove to management that you did something this week",
        "c": "To help other developers understand the codebase",
        "d": "To practice your markdown formatting skills",
        "correct_key": "a"
    },
    {
        "question": "What does the term 'Serverless' mean?",
        "a": "The database is down again",
        "b": "Your application runs entirely in the browser without any backend",
        "c": "Your code runs on someone else's computer, but you pay 10x more for it",
        "d": "A magical land where servers do not exist and databases are free",
        "correct_key": "c"
    },
    {
        "question": "Why did the HTML developer break up with the CSS developer?",
        "a": "They couldn't align on their goals",
        "b": "Because the CSS dev lacked class",
        "c": "There was no style in their relationship",
        "d": "They couldn't agree on absolute positioning",
        "correct_key": "b"
    },
    {
        "question": "What is the most effective way to optimize database performance?",
        "a": "Deleting old user accounts without warning",
        "b": "Rewriting all queries in plain binary",
        "c": "Creating indexes on frequently queried columns",
        "d": "Buying a bigger server and praying to the database gods",
        "correct_key": "c"
    },
    {
        "question": "Your docker-compose build fails because of a missing environment variable. You should...",
        "a": "Hardcode the secret password into your public GitHub code",
        "b": "Declare that Docker is obsolete and start using raw virtual machines",
        "c": "Uninstall Docker and build a cabin in the woods",
        "d": "Create a `.env` file with the correct values",
        "correct_key": "a"
    },
    {
        "question": "What is the definition of 'Refactoring'?",
        "a": "Changing all single quotes to double quotes across the codebase",
        "b": "Splitting a single file into 45 files to make your commit look huge",
        "c": "Rewriting working code until it breaks in ways you don't understand",
        "d": "Improving the internal structure of code without changing its external behavior",
        "correct_key": "c"
    },
    {
        "question": "Why do junior developers write massive comments explaining simple code?",
        "a": "Because they get paid by the line of code",
        "b": "To make their code look professional",
        "c": "To cover up the fact that they copied it from ChatGPT",
        "d": "Because they don't trust the reader's basic programming knowledge",
        "correct_key": "c"
    },
    {
        "question": "What happens when you run a build without running npm install first?",
        "a": "A junior dev gets their wings",
        "b": "It downloads packages automatically",
        "c": "Your computer fan spins so fast it takes off like a helicopter",
        "d": "It crashes with 'Cannot find module'",
        "correct_key": "d"
    },
    {
        "question": "What is the true meaning of a 'Quick Sync' calendar invite?",
        "a": "A 10-minute update session",
        "b": "A 45-minute architectural debate that solves absolutely nothing",
        "c": "Your manager wants to assign you 4 new urgent tickets",
        "d": "An intervention about your git commit habits",
        "correct_key": "b"
    },
    {
        "question": "Which of these is the most common cause of imposter syndrome in devs?",
        "a": "Forgetting how to parse JSON for the 4th time today",
        "b": "Reading a senior developer's clean, idiomatic codebase",
        "c": "Seeing a colleague write a complex regex in 4 seconds",
        "d": "All of the above",
        "correct_key": "d"
    },
    {
        "question": "What is a 'Heisenbug'?",
        "a": "A bug that was written by Walter White",
        "b": "A bug that makes your server run at 99.9% capacity",
        "c": "A bug that only appears in production on a Friday",
        "d": "A bug that disappears when you try to study or debug it",
        "correct_key": "d"
    },
    {
        "question": "What does `git stash` do?",
        "a": "Sweeps your garbage code under the rug so you can deal with it later (never)",
        "b": "Deletes your local changes permanently",
        "c": "Saves your changes securely on the cloud server",
        "d": "Creates a hidden folder with funny developer memes",
        "correct_key": "a"
    },
    {
        "question": "Your boss asks why you haven't completed a ticket. The correct answer is...",
        "a": "It's taking longer than expected due to architectural complexity",
        "b": "I've been in meetings for 6 of the last 8 hours",
        "c": "I got distracted trying to center a div in a bento grid",
        "d": "All of the above",
        "correct_key": "d"
    },
    {
        "question": "What does a Docker container do when it feels lonely?",
        "a": "Exits with status code 137 (out of memory)",
        "b": "Sends a ping to the registry",
        "c": "Spawns 5 replica sets",
        "d": "Spams the log file with connection warnings",
        "correct_key": "a"
    },
    {
        "question": "What is the primary benefit of TypeScript?",
        "a": "It turns runtime crashes into compile-time typing puzzles",
        "b": "It guarantees that your code has no bugs",
        "c": "It makes you feel superior to standard JavaScript developers",
        "d": "It lets you write twice as much code to achieve the same result",
        "correct_key": "a"
    },
    {
        "question": "What is the first thing a developer does when joining a new startup?",
        "a": "Spend 3 days configuring their shell prompt and dark mode themes",
        "b": "Ask if they can work from a hammock",
        "c": "Suggest rewriting the entire application in a different framework",
        "d": "Read the documentation and understand the business goals",
        "correct_key": "a"
    },
    {
        "question": "Why are database migrations so terrifying?",
        "a": "Because you forgot to take a backup first",
        "b": "Because they require complex SQL commands",
        "c": "Because one mistake can wipe out 5 years of customer purchase history",
        "d": "Because they must be run at 4 AM",
        "correct_key": "c"
    },
    {
        "question": "How do you know someone is a Rust developer?",
        "a": "They refuse to write garbage collection languages",
        "b": "They mention memory safety and borrow checker in the first 30 seconds of meeting them",
        "c": "They write exceptionally fast code",
        "d": "They have a crab logo sticker on their water bottle",
        "correct_key": "b"
    },
    {
        "question": "What is the best way to deal with technical debt?",
        "a": "Create a sprint dedicated entirely to cleaning it up",
        "b": "Pretend it doesn't exist and write more features on top of it",
        "c": "Quit your job before the codebase collapses under its own weight",
        "d": "Write a blog post about how you resolved it in a previous job",
        "correct_key": "c"
    },
    {
        "question": "What does your CI/CD pipeline do when you push a critical fix?",
        "a": "Runs tests quickly and deploys within 2 minutes",
        "b": "Spins on the first step for 35 minutes and then fails because of a network timeout",
        "c": "Rejects your build because of a trailing whitespace on line 452",
        "d": "Deploys it to the wrong staging server",
        "correct_key": "b"
    },
    {
        "question": "Why do senior developers write short git commit messages?",
        "a": "They use `git commit -m 'fix'` for everything",
        "b": "Because the code speaks for itself",
        "c": "Because they are tired and their spirits are broken",
        "d": "To save screen space",
        "correct_key": "c"
    },
    {
        "question": "What is the best way to handle CORS errors in local development?",
        "a": "Install a Chrome extension that turns off all browser security controls",
        "b": "Configure proper headers on the server side",
        "c": "Cry and rewrite the app as a desktop application",
        "d": "Use JSONP and pretend it's 2008",
        "correct_key": "a"
    },
    {
        "question": "You are trying to set up OAuth credentials using PostgreSQL, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Switch your theme to dark mode and hope the issue goes away",
        "correct_key": "b"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using Rust, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Delete your local repository and clone a fresh copy",
        "b": "Cry quietly in the nearest storage room or cafeteria",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Blame the newest engineering intern (even if you don't have one)",
        "correct_key": "d"
    },
    {
        "question": "You are trying to mock an external payment API using MongoDB, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Add the `!important` rule to 30 different lines of CSS styling",
        "c": "Run a system reboot and hope it resolves itself",
        "d": "Pretend you have a power outage and leave the Zoom meeting",
        "correct_key": "b"
    },
    {
        "question": "You are trying to fix a memory leak using Git, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "Run `npm cache clean --force` and pray to the package gods",
        "c": "All of the above in random order",
        "d": "Delete `node_modules` and the package lockfile and rebuild",
        "correct_key": "c"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using Redis, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Commit the changes, push, and immediately close your laptop",
        "c": "Blame the cloud hosting provider's regional server outage",
        "d": "Rewrite the entire backend module in Rust to feel better",
        "correct_key": "b"
    },
    {
        "question": "You are trying to reset the git branch using JavaScript, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Add the `!important` rule to 30 different lines of CSS styling",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "b"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using TypeScript, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "b"
    },
    {
        "question": "You are trying to deploy a hotfix using Python, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Take a 2-hour lunch break to clear your mind",
        "d": "Roll back to the last working build and hope nobody checked logs",
        "correct_key": "d"
    },
    {
        "question": "You are trying to containerize an application using React, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Add a console.log statement every three lines to see what is happening",
        "b": "Take a 2-hour lunch break to clear your mind",
        "c": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "d": "Roll back to the last working build and hope nobody checked logs",
        "correct_key": "d"
    },
    {
        "question": "You are trying to merge a pull request using Kubernetes, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Blame the newest engineering intern (even if you don't have one)",
        "b": "Cry quietly in the nearest storage room or cafeteria",
        "c": "Delete your local repository and clone a fresh copy",
        "d": "Pretend your Slack is broken and go grab a coffee",
        "correct_key": "a"
    },
    {
        "question": "You are trying to review a coworker's pull request using Kubectl, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Decline the ticket and reassign it to the senior team lead",
        "b": "Read the logs carefully and trace the exception stack",
        "c": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "d": "Switch your theme to dark mode and hope the issue goes away",
        "correct_key": "c"
    },
    {
        "question": "You are trying to fix a memory leak using TypeScript, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Delete your local repository and clone a fresh copy",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Cry quietly in the nearest storage room or cafeteria",
        "d": "Blame the newest engineering intern (even if you don't have one)",
        "correct_key": "d"
    },
    {
        "question": "You are trying to explain a complex regex pattern using Kubernetes, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "a"
    },
    {
        "question": "You are trying to set up OAuth credentials using Django, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Run `npm cache clean --force` and pray to the package gods",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "All of the above in random order",
        "correct_key": "d"
    },
    {
        "question": "You are trying to audit the security dependencies using Kubernetes, but the database suddenly disappears from the console. What is your next move?",
        "a": "Delete `node_modules` and the package lockfile and rebuild",
        "b": "Tell the client that this is a feature, not a bug",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "All of the above in random order",
        "correct_key": "d"
    },
    {
        "question": "You are trying to write a unit test suite using Kubernetes, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Delete your local repository and clone a fresh copy",
        "b": "Blame the newest engineering intern (even if you don't have one)",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "b"
    },
    {
        "question": "You are trying to explain a complex regex pattern using AWS, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Add a console.log statement every three lines to see what is happening",
        "b": "Take a 2-hour lunch break to clear your mind",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "c"
    },
    {
        "question": "You are trying to optimize a database query using Kubectl, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "All of the above in random order",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "a"
    },
    {
        "question": "You are trying to mock an external payment API using AWS, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Blame the newest engineering intern (even if you don't have one)",
        "b": "Cry quietly in the nearest storage room or cafeteria",
        "c": "Delete your local repository and clone a fresh copy",
        "d": "Pretend your Slack is broken and go grab a coffee",
        "correct_key": "a"
    },
    {
        "question": "You are trying to run a database migration script using Node.js, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "All of the above in random order",
        "b": "Tell the client that this is a feature, not a bug",
        "c": "Delete `node_modules` and the package lockfile and rebuild",
        "d": "Run `npm cache clean --force` and pray to the package gods",
        "correct_key": "a"
    },
    {
        "question": "You are trying to optimize a database query using TypeScript, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Decline the ticket and reassign it to the senior team lead",
        "b": "Read the logs carefully and trace the exception stack",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "correct_key": "d"
    },
    {
        "question": "You are trying to set up OAuth credentials using HTML/CSS, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "Run `npm cache clean --force` and pray to the package gods",
        "c": "All of the above in random order",
        "d": "Delete `node_modules` and the package lockfile and rebuild",
        "correct_key": "c"
    },
    {
        "question": "You are trying to mock an external payment API using Jenkins, but the database suddenly disappears from the console. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "Run `npm cache clean --force` and pray to the package gods",
        "c": "All of the above in random order",
        "d": "Delete `node_modules` and the package lockfile and rebuild",
        "correct_key": "c"
    },
    {
        "question": "You are trying to fix a memory leak using Jenkins, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "a"
    },
    {
        "question": "You are trying to revert a bad merge using JavaScript, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Add a console.log statement every three lines to see what is happening",
        "b": "Take a 2-hour lunch break to clear your mind",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "c"
    },
    {
        "question": "You are trying to install a dependency package using Node.js, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Run a system reboot and hope it resolves itself",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Pretend you have a power outage and leave the Zoom meeting",
        "correct_key": "c"
    },
    {
        "question": "You are trying to set up OAuth credentials using TypeScript, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "c"
    },
    {
        "question": "You are trying to refactor a legacy module using Rust, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Decline the ticket and reassign it to the senior team lead",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "c"
    },
    {
        "question": "You are trying to write a script in Bash using Webpack, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Add the `!important` rule to 30 different lines of CSS styling",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Run a system reboot and hope it resolves itself",
        "d": "Tell your manager that the sprint goals were unrealistic",
        "correct_key": "a"
    },
    {
        "question": "You are trying to review a coworker's pull request using Rust, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Increase the server instance size and pay AWS 4x more money",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to revert a bad merge using Docker, but your laptop battery dies during the process. What is your next move?",
        "a": "Force push the changes directly to the main branch",
        "b": "Add a comment saying '// TODO: fix this later' and ignore it",
        "c": "Straighten your shrimp posture and sigh deeply",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "c"
    },
    {
        "question": "You are trying to set up OAuth credentials using Python, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Run a system reboot and hope it resolves itself",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to run a database migration script using Kubernetes, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Run a system reboot and hope it resolves itself",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to run a database migration script using TypeScript, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Decline the ticket and reassign it to the senior team lead",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "c"
    },
    {
        "question": "You are trying to reset the git branch using Git, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Pretend your Slack is broken and go grab a coffee",
        "b": "Blame the newest engineering intern (even if you don't have one)",
        "c": "Cry quietly in the nearest storage room or cafeteria",
        "d": "Delete your local repository and clone a fresh copy",
        "correct_key": "b"
    },
    {
        "question": "You are trying to mock an external payment API using MongoDB, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Add a console.log statement every three lines to see what is happening",
        "b": "Roll back to the last working build and hope nobody checked logs",
        "c": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "b"
    },
    {
        "question": "You are trying to merge a pull request using Nginx, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Force push the changes directly to the main branch",
        "b": "Ask a question on Stack Overflow under an anonymous username",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Straighten your shrimp posture and sigh deeply",
        "correct_key": "d"
    },
    {
        "question": "You are trying to install npm packages using Git, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Add a comment saying '// TODO: fix this later' and ignore it",
        "b": "Straighten your shrimp posture and sigh deeply",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Force push the changes directly to the main branch",
        "correct_key": "b"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using PostgreSQL, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Read the logs carefully and trace the exception stack",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "a"
    },
    {
        "question": "You are trying to set up OAuth credentials using Redis, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Run `npm cache clean --force` and pray to the package gods",
        "b": "All of the above in random order",
        "c": "Delete `node_modules` and the package lockfile and rebuild",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "b"
    },
    {
        "question": "You are trying to refactor a legacy module using Kubectl, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Blame the cloud hosting provider's regional server outage",
        "b": "Commit the changes, push, and immediately close your laptop",
        "c": "Rewrite the entire backend module in Rust to feel better",
        "d": "Add a try-except block around the entire file and go to sleep",
        "correct_key": "b"
    },
    {
        "question": "You are trying to run a database migration script using Jenkins, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Rewrite the entire backend module in Rust to feel better",
        "b": "Blame the cloud hosting provider's regional server outage",
        "c": "Add a try-except block around the entire file and go to sleep",
        "d": "Commit the changes, push, and immediately close your laptop",
        "correct_key": "d"
    },
    {
        "question": "You are trying to merge a pull request using Kubectl, but it accidentally deletes the system root directory. What is your next move?",
        "a": "All of the above in random order",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "a"
    },
    {
        "question": "You are trying to fix a memory leak using Rust, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Delete your local repository and clone a fresh copy",
        "b": "Cry quietly in the nearest storage room or cafeteria",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Blame the newest engineering intern (even if you don't have one)",
        "correct_key": "d"
    },
    {
        "question": "You are trying to revert a bad merge using GitHub Actions, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Force push the changes directly to the main branch",
        "b": "Ask a question on Stack Overflow under an anonymous username",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Straighten your shrimp posture and sigh deeply",
        "correct_key": "d"
    },
    {
        "question": "You are trying to refactor a legacy module using C++, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Force push the changes directly to the main branch",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "a"
    },
    {
        "question": "You are trying to containerize an application using Redis, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Add the `!important` rule to 30 different lines of CSS styling",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "b"
    },
    {
        "question": "You are trying to install a dependency package using MongoDB, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Switch your theme to dark mode and hope the issue goes away",
        "b": "Read the logs carefully and trace the exception stack",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "correct_key": "d"
    },
    {
        "question": "You are trying to explain a complex regex pattern using C++, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Take a 2-hour lunch break to clear your mind",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "a"
    },
    {
        "question": "You are trying to install npm packages using Redis, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Delete your local repository and clone a fresh copy",
        "b": "Cry quietly in the nearest storage room or cafeteria",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Pretend your Slack is broken and go grab a coffee",
        "correct_key": "c"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using Rust, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "a"
    },
    {
        "question": "You are trying to deploy a hotfix using Webpack, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "All of the above in random order",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "a"
    },
    {
        "question": "You are trying to clean up the docker images using Rust, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "Pretend your Slack is broken and go grab a coffee",
        "b": "Blame the newest engineering intern (even if you don't have one)",
        "c": "Delete your local repository and clone a fresh copy",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "b"
    },
    {
        "question": "You are trying to audit the security dependencies using Node.js, but the database suddenly disappears from the console. What is your next move?",
        "a": "All of the above in random order",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "a"
    },
    {
        "question": "You are trying to revert a bad merge using Docker, but your internet connection drops right in the middle. What is your next move?",
        "a": "Delete your local repository and clone a fresh copy",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Cry quietly in the nearest storage room or cafeteria",
        "d": "Blame the newest engineering intern (even if you don't have one)",
        "correct_key": "d"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using Rust, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Spend three hours debating tabs vs spaces in the company Slack",
        "correct_key": "a"
    },
    {
        "question": "You are trying to install a dependency package using MongoDB, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Tell the product owner that the feature requires more research",
        "correct_key": "a"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using GitHub Actions, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Delete `node_modules` and the package lockfile and rebuild",
        "b": "Tell the client that this is a feature, not a bug",
        "c": "All of the above in random order",
        "d": "Run `npm cache clean --force` and pray to the package gods",
        "correct_key": "c"
    },
    {
        "question": "You are trying to merge a pull request using PostgreSQL, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "c"
    },
    {
        "question": "You are trying to review a coworker's pull request using Vim, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Increase the server instance size and pay AWS 4x more money",
        "b": "Tell the product owner that the feature requires more research",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to write a script in Bash using Docker, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Delete your local repository and clone a fresh copy",
        "b": "Blame the newest engineering intern (even if you don't have one)",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "b"
    },
    {
        "question": "You are trying to fix a memory leak using Stack Overflow, but your internet connection drops right in the middle. What is your next move?",
        "a": "Delete your local repository and clone a fresh copy",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "c"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using JavaScript, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Increase the server instance size and pay AWS 4x more money",
        "d": "Tell the product owner that the feature requires more research",
        "correct_key": "a"
    },
    {
        "question": "You are trying to refactor a legacy module using Vim, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "c"
    },
    {
        "question": "You are trying to install npm packages using Rust, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Tell the product owner that the feature requires more research",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Remove all unit tests so the build pipeline succeeds",
        "d": "Increase the server instance size and pay AWS 4x more money",
        "correct_key": "c"
    },
    {
        "question": "You are trying to reset the git branch using PostgreSQL, but the database suddenly disappears from the console. What is your next move?",
        "a": "Rewrite the entire backend module in Rust to feel better",
        "b": "Blame the cloud hosting provider's regional server outage",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Add a try-except block around the entire file and go to sleep",
        "correct_key": "c"
    },
    {
        "question": "You are trying to revert a bad merge using Rust, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Add the `!important` rule to 30 different lines of CSS styling",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Pretend you have a power outage and leave the Zoom meeting",
        "correct_key": "b"
    },
    {
        "question": "You are trying to ssh into the production server using GitHub Actions, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Run a system reboot and hope it resolves itself",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to fix a memory leak using Python, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Commit the changes, push, and immediately close your laptop",
        "b": "Add a try-except block around the entire file and go to sleep",
        "c": "Rewrite the entire backend module in Rust to feel better",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "a"
    },
    {
        "question": "You are trying to write a unit test suite using Vim, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Tell the product owner that the feature requires more research",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to refactor a legacy module using JavaScript, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Run `npm cache clean --force` and pray to the package gods",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "All of the above in random order",
        "correct_key": "d"
    },
    {
        "question": "You are trying to fix a memory leak using Webpack, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Rewrite the entire backend module in Rust to feel better",
        "b": "Add a try-except block around the entire file and go to sleep",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "c"
    },
    {
        "question": "You are trying to write a script in Bash using Jenkins, but the database suddenly disappears from the console. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "c"
    },
    {
        "question": "You are trying to clean up the docker images using GitHub Actions, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Force push the changes directly to the main branch",
        "b": "Straighten your shrimp posture and sigh deeply",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "b"
    },
    {
        "question": "You are trying to fix a memory leak using Redis, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Ask a question on Stack Overflow under an anonymous username",
        "b": "Straighten your shrimp posture and sigh deeply",
        "c": "Force push the changes directly to the main branch",
        "d": "Add a comment saying '// TODO: fix this later' and ignore it",
        "correct_key": "b"
    },
    {
        "question": "You are trying to revert a bad merge using Django, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "All of the above in random order",
        "d": "Run `npm cache clean --force` and pray to the package gods",
        "correct_key": "c"
    },
    {
        "question": "You are trying to explain a complex regex pattern using PostgreSQL, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "All of the above in random order",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "Run `npm cache clean --force` and pray to the package gods",
        "correct_key": "a"
    },
    {
        "question": "You are trying to clean up the docker images using Django, but the database suddenly disappears from the console. What is your next move?",
        "a": "Pretend your Slack is broken and go grab a coffee",
        "b": "Cry quietly in the nearest storage room or cafeteria",
        "c": "Delete your local repository and clone a fresh copy",
        "d": "Blame the newest engineering intern (even if you don't have one)",
        "correct_key": "d"
    },
    {
        "question": "You are trying to center a div in CSS using C++, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Add a console.log statement every three lines to see what is happening",
        "b": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "c"
    },
    {
        "question": "You are trying to containerize an application using JavaScript, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Take a 2-hour lunch break to clear your mind",
        "d": "Roll back to the last working build and hope nobody checked logs",
        "correct_key": "d"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using AWS, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Ask a question on Stack Overflow under an anonymous username",
        "b": "Add a comment saying '// TODO: fix this later' and ignore it",
        "c": "Straighten your shrimp posture and sigh deeply",
        "d": "Force push the changes directly to the main branch",
        "correct_key": "c"
    },
    {
        "question": "You are trying to mock an external payment API using Node.js, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Tell the product owner that the feature requires more research",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Increase the server instance size and pay AWS 4x more money",
        "correct_key": "a"
    },
    {
        "question": "You are trying to update a production database schema using Kubernetes, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "Tell the product owner that the feature requires more research",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Remove all unit tests so the build pipeline succeeds",
        "d": "Spend three hours debating tabs vs spaces in the company Slack",
        "correct_key": "c"
    },
    {
        "question": "You are trying to run a database migration script using Webpack, but your laptop battery dies during the process. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Blame the newest engineering intern (even if you don't have one)",
        "c": "Delete your local repository and clone a fresh copy",
        "d": "Pretend your Slack is broken and go grab a coffee",
        "correct_key": "b"
    },
    {
        "question": "You are trying to reset the git branch using JavaScript, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Switch your theme to dark mode and hope the issue goes away",
        "correct_key": "b"
    },
    {
        "question": "You are trying to refactor a legacy module using Kubectl, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Delete `node_modules` and the package lockfile and rebuild",
        "b": "Tell the client that this is a feature, not a bug",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "All of the above in random order",
        "correct_key": "d"
    },
    {
        "question": "You are trying to review a coworker's pull request using Nginx, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Spend three hours debating tabs vs spaces in the company Slack",
        "b": "Remove all unit tests so the build pipeline succeeds",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Increase the server instance size and pay AWS 4x more money",
        "correct_key": "b"
    },
    {
        "question": "You are trying to reset the git branch using HTML/CSS, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Rewrite the entire backend module in Rust to feel better",
        "b": "Add a try-except block around the entire file and go to sleep",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "c"
    },
    {
        "question": "You are trying to mock an external payment API using MongoDB, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Blame the newest engineering intern (even if you don't have one)",
        "c": "Delete your local repository and clone a fresh copy",
        "d": "Pretend your Slack is broken and go grab a coffee",
        "correct_key": "b"
    },
    {
        "question": "You are trying to refactor a legacy module using AWS, but your laptop battery dies during the process. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Delete your local repository and clone a fresh copy",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Pretend your Slack is broken and go grab a coffee",
        "correct_key": "c"
    },
    {
        "question": "You are trying to write a script in Bash using MongoDB, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Decline the ticket and reassign it to the senior team lead",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "correct_key": "d"
    },
    {
        "question": "You are trying to write a unit test suite using Django, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Take a 2-hour lunch break to clear your mind",
        "b": "Roll back to the last working build and hope nobody checked logs",
        "c": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "d": "Add a console.log statement every three lines to see what is happening",
        "correct_key": "b"
    },
    {
        "question": "You are trying to install a dependency package using C++, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Decline the ticket and reassign it to the senior team lead",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "correct_key": "d"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using GitHub Actions, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Commit the changes, push, and immediately close your laptop",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Add a try-except block around the entire file and go to sleep",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "a"
    },
    {
        "question": "You are trying to revert a bad merge using Node.js, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "b"
    },
    {
        "question": "You are trying to fix a memory leak using Git, but your internet connection drops right in the middle. What is your next move?",
        "a": "Force push the changes directly to the main branch",
        "b": "Add a comment saying '// TODO: fix this later' and ignore it",
        "c": "Straighten your shrimp posture and sigh deeply",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "c"
    },
    {
        "question": "You are trying to set up OAuth credentials using AWS, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Tell the product owner that the feature requires more research",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Increase the server instance size and pay AWS 4x more money",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to reset the git branch using HTML/CSS, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Blame the cloud hosting provider's regional server outage",
        "d": "Commit the changes, push, and immediately close your laptop",
        "correct_key": "d"
    },
    {
        "question": "You are trying to merge a pull request using Kubernetes, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Blame the cloud hosting provider's regional server outage",
        "b": "Commit the changes, push, and immediately close your laptop",
        "c": "Add a try-except block around the entire file and go to sleep",
        "d": "Rewrite the entire backend module in Rust to feel better",
        "correct_key": "b"
    },
    {
        "question": "You are trying to review a coworker's pull request using Webpack, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Add a comment saying '// TODO: fix this later' and ignore it",
        "b": "Force push the changes directly to the main branch",
        "c": "Straighten your shrimp posture and sigh deeply",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "c"
    },
    {
        "question": "You are trying to center a div in CSS using React, but the database suddenly disappears from the console. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "correct_key": "d"
    },
    {
        "question": "You are trying to review a coworker's pull request using Docker, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "All of the above in random order",
        "d": "Run `npm cache clean --force` and pray to the package gods",
        "correct_key": "c"
    },
    {
        "question": "You are trying to mock an external payment API using Rust, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Blame the newest engineering intern (even if you don't have one)",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Delete your local repository and clone a fresh copy",
        "correct_key": "b"
    },
    {
        "question": "You are trying to review a coworker's pull request using MongoDB, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Ask a question on Stack Overflow under an anonymous username",
        "b": "Force push the changes directly to the main branch",
        "c": "Straighten your shrimp posture and sigh deeply",
        "d": "Add a comment saying '// TODO: fix this later' and ignore it",
        "correct_key": "c"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using Python, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Add the `!important` rule to 30 different lines of CSS styling",
        "c": "Run a system reboot and hope it resolves itself",
        "d": "Tell your manager that the sprint goals were unrealistic",
        "correct_key": "b"
    },
    {
        "question": "You are trying to deploy a hotfix using Python, but your internet connection drops right in the middle. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to mock an external payment API using Rust, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Add a comment saying '// TODO: fix this later' and ignore it",
        "b": "Force push the changes directly to the main branch",
        "c": "Straighten your shrimp posture and sigh deeply",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "c"
    },
    {
        "question": "You are trying to audit the security dependencies using PostgreSQL, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Blame the cloud hosting provider's regional server outage",
        "b": "Commit the changes, push, and immediately close your laptop",
        "c": "Rewrite the entire backend module in Rust to feel better",
        "d": "Add a try-except block around the entire file and go to sleep",
        "correct_key": "b"
    },
    {
        "question": "You are trying to ssh into the production server using Rust, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Increase the server instance size and pay AWS 4x more money",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Remove all unit tests so the build pipeline succeeds",
        "d": "Tell the product owner that the feature requires more research",
        "correct_key": "c"
    },
    {
        "question": "You are trying to review a coworker's pull request using Nginx, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "All of the above in random order",
        "c": "Delete `node_modules` and the package lockfile and rebuild",
        "d": "Run `npm cache clean --force` and pray to the package gods",
        "correct_key": "b"
    },
    {
        "question": "You are trying to deploy a hotfix using C++, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Tell your manager that the sprint goals were unrealistic",
        "correct_key": "c"
    },
    {
        "question": "You are trying to update a production database schema using AWS, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Decline the ticket and reassign it to the senior team lead",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "correct_key": "d"
    },
    {
        "question": "You are trying to review a coworker's pull request using Node.js, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Add the `!important` rule to 30 different lines of CSS styling",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Pretend you have a power outage and leave the Zoom meeting",
        "correct_key": "b"
    },
    {
        "question": "You are trying to mock an external payment API using MongoDB, but your internet connection drops right in the middle. What is your next move?",
        "a": "Blame the cloud hosting provider's regional server outage",
        "b": "Add a try-except block around the entire file and go to sleep",
        "c": "Rewrite the entire backend module in Rust to feel better",
        "d": "Commit the changes, push, and immediately close your laptop",
        "correct_key": "d"
    },
    {
        "question": "You are trying to merge a pull request using AWS, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Decline the ticket and reassign it to the senior team lead",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "correct_key": "d"
    },
    {
        "question": "You are trying to fix a memory leak using PostgreSQL, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "c"
    },
    {
        "question": "You are trying to review a coworker's pull request using Jenkins, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Pretend your Slack is broken and go grab a coffee",
        "b": "Blame the newest engineering intern (even if you don't have one)",
        "c": "Delete your local repository and clone a fresh copy",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "b"
    },
    {
        "question": "You are trying to explain a complex regex pattern using Webpack, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Switch your theme to dark mode and hope the issue goes away",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "b"
    },
    {
        "question": "You are trying to fix a memory leak using HTML/CSS, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Commit the changes, push, and immediately close your laptop",
        "b": "Blame the cloud hosting provider's regional server outage",
        "c": "Add a try-except block around the entire file and go to sleep",
        "d": "Rewrite the entire backend module in Rust to feel better",
        "correct_key": "a"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using MongoDB, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "All of the above in random order",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "a"
    },
    {
        "question": "You are trying to review a coworker's pull request using Vim, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Take a 2-hour lunch break to clear your mind",
        "c": "Add a console.log statement every three lines to see what is happening",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "a"
    },
    {
        "question": "You are trying to run a database migration script using Jenkins, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Pretend your Slack is broken and go grab a coffee",
        "b": "Delete your local repository and clone a fresh copy",
        "c": "Cry quietly in the nearest storage room or cafeteria",
        "d": "Blame the newest engineering intern (even if you don't have one)",
        "correct_key": "d"
    },
    {
        "question": "You are trying to write a script in Bash using Nginx, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Switch your theme to dark mode and hope the issue goes away",
        "b": "Read the logs carefully and trace the exception stack",
        "c": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "c"
    },
    {
        "question": "You are trying to mock an external payment API using Vim, but your internet connection drops right in the middle. What is your next move?",
        "a": "Add the `!important` rule to 30 different lines of CSS styling",
        "b": "Run a system reboot and hope it resolves itself",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Tell your manager that the sprint goals were unrealistic",
        "correct_key": "a"
    },
    {
        "question": "You are trying to audit the security dependencies using Nginx, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Add a comment saying '// TODO: fix this later' and ignore it",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Force push the changes directly to the main branch",
        "correct_key": "a"
    },
    {
        "question": "You are trying to install a dependency package using Vim, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Run a system reboot and hope it resolves itself",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to mock an external payment API using Python, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Read the logs carefully and trace the exception stack",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Switch your theme to dark mode and hope the issue goes away",
        "correct_key": "a"
    },
    {
        "question": "You are trying to explain a complex regex pattern using MongoDB, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "a"
    },
    {
        "question": "You are trying to write a unit test suite using JavaScript, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "a"
    },
    {
        "question": "You are trying to install npm packages using TypeScript, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "All of the above in random order",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "Delete `node_modules` and the package lockfile and rebuild",
        "correct_key": "b"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using GitHub Actions, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Delete your local repository and clone a fresh copy",
        "b": "Blame the newest engineering intern (even if you don't have one)",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "b"
    },
    {
        "question": "You are trying to write a unit test suite using Redis, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Add a console.log statement every three lines to see what is happening",
        "b": "Take a 2-hour lunch break to clear your mind",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "c"
    },
    {
        "question": "You are trying to revert a bad merge using Rust, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Read the logs carefully and trace the exception stack",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "a"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using JavaScript, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Blame the cloud hosting provider's regional server outage",
        "b": "Add a try-except block around the entire file and go to sleep",
        "c": "Rewrite the entire backend module in Rust to feel better",
        "d": "Commit the changes, push, and immediately close your laptop",
        "correct_key": "d"
    },
    {
        "question": "You are trying to fix a memory leak using Rust, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Delete your local repository and clone a fresh copy",
        "b": "Cry quietly in the nearest storage room or cafeteria",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Pretend your Slack is broken and go grab a coffee",
        "correct_key": "c"
    },
    {
        "question": "You are trying to install npm packages using Vim, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Run `npm cache clean --force` and pray to the package gods",
        "b": "All of the above in random order",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "Delete `node_modules` and the package lockfile and rebuild",
        "correct_key": "b"
    },
    {
        "question": "You are trying to audit the security dependencies using HTML/CSS, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Increase the server instance size and pay AWS 4x more money",
        "correct_key": "a"
    },
    {
        "question": "You are trying to explain a complex regex pattern using Rust, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Commit the changes, push, and immediately close your laptop",
        "b": "Blame the cloud hosting provider's regional server outage",
        "c": "Add a try-except block around the entire file and go to sleep",
        "d": "Rewrite the entire backend module in Rust to feel better",
        "correct_key": "a"
    },
    {
        "question": "You are trying to merge a pull request using Vim, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Add a comment saying '// TODO: fix this later' and ignore it",
        "b": "Force push the changes directly to the main branch",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Straighten your shrimp posture and sigh deeply",
        "correct_key": "d"
    },
    {
        "question": "You are trying to audit the security dependencies using Redis, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Blame the cloud hosting provider's regional server outage",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Add a try-except block around the entire file and go to sleep",
        "d": "Commit the changes, push, and immediately close your laptop",
        "correct_key": "d"
    },
    {
        "question": "You are trying to reset the git branch using Rust, but your laptop battery dies during the process. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Increase the server instance size and pay AWS 4x more money",
        "d": "Tell the product owner that the feature requires more research",
        "correct_key": "a"
    },
    {
        "question": "You are trying to refactor a legacy module using TypeScript, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "c": "Add a console.log statement every three lines to see what is happening",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "a"
    },
    {
        "question": "You are trying to install npm packages using Django, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Add the `!important` rule to 30 different lines of CSS styling",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Run a system reboot and hope it resolves itself",
        "d": "Pretend you have a power outage and leave the Zoom meeting",
        "correct_key": "a"
    },
    {
        "question": "You are trying to reset the git branch using TypeScript, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Increase the server instance size and pay AWS 4x more money",
        "b": "Tell the product owner that the feature requires more research",
        "c": "Remove all unit tests so the build pipeline succeeds",
        "d": "Spend three hours debating tabs vs spaces in the company Slack",
        "correct_key": "c"
    },
    {
        "question": "You are trying to install npm packages using AWS, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Decline the ticket and reassign it to the senior team lead",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Switch your theme to dark mode and hope the issue goes away",
        "correct_key": "a"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using GitHub Actions, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "All of the above in random order",
        "b": "Tell the client that this is a feature, not a bug",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "Delete `node_modules` and the package lockfile and rebuild",
        "correct_key": "a"
    },
    {
        "question": "You are trying to containerize an application using TypeScript, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Decline the ticket and reassign it to the senior team lead",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "b"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using AWS, but your internet connection drops right in the middle. What is your next move?",
        "a": "Take a 2-hour lunch break to clear your mind",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "d": "Roll back to the last working build and hope nobody checked logs",
        "correct_key": "d"
    },
    {
        "question": "You are trying to reset the git branch using Kubernetes, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Force push the changes directly to the main branch",
        "b": "Ask a question on Stack Overflow under an anonymous username",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Straighten your shrimp posture and sigh deeply",
        "correct_key": "d"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using Stack Overflow, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "All of the above in random order",
        "correct_key": "d"
    },
    {
        "question": "You are trying to revert a bad merge using Vim, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Take a 2-hour lunch break to clear your mind",
        "d": "Roll back to the last working build and hope nobody checked logs",
        "correct_key": "d"
    },
    {
        "question": "You are trying to reset the git branch using TypeScript, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Commit the changes, push, and immediately close your laptop",
        "c": "Blame the cloud hosting provider's regional server outage",
        "d": "Rewrite the entire backend module in Rust to feel better",
        "correct_key": "b"
    },
    {
        "question": "You are trying to install a dependency package using Vim, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Blame the cloud hosting provider's regional server outage",
        "c": "Rewrite the entire backend module in Rust to feel better",
        "d": "Commit the changes, push, and immediately close your laptop",
        "correct_key": "d"
    },
    {
        "question": "You are trying to clean up the docker images using Stack Overflow, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Blame the cloud hosting provider's regional server outage",
        "c": "Rewrite the entire backend module in Rust to feel better",
        "d": "Commit the changes, push, and immediately close your laptop",
        "correct_key": "d"
    },
    {
        "question": "You are trying to review a coworker's pull request using Nginx, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Pretend you have a power outage and leave the Zoom meeting",
        "correct_key": "c"
    },
    {
        "question": "You are trying to reset the git branch using MongoDB, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "All of the above in random order",
        "b": "Run `npm cache clean --force` and pray to the package gods",
        "c": "Delete `node_modules` and the package lockfile and rebuild",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "a"
    },
    {
        "question": "You are trying to ssh into the production server using Rust, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Add the `!important` rule to 30 different lines of CSS styling",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Tell your manager that the sprint goals were unrealistic",
        "correct_key": "b"
    },
    {
        "question": "You are trying to ssh into the production server using Git, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Take a 2-hour lunch break to clear your mind",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "c"
    },
    {
        "question": "You are trying to mock an external payment API using C++, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Ask a question on Stack Overflow under an anonymous username",
        "b": "Straighten your shrimp posture and sigh deeply",
        "c": "Force push the changes directly to the main branch",
        "d": "Add a comment saying '// TODO: fix this later' and ignore it",
        "correct_key": "b"
    },
    {
        "question": "You are trying to install npm packages using React, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Blame the cloud hosting provider's regional server outage",
        "b": "Add a try-except block around the entire file and go to sleep",
        "c": "Rewrite the entire backend module in Rust to feel better",
        "d": "Commit the changes, push, and immediately close your laptop",
        "correct_key": "d"
    },
    {
        "question": "You are trying to explain a complex regex pattern using Webpack, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Blame the cloud hosting provider's regional server outage",
        "b": "Add a try-except block around the entire file and go to sleep",
        "c": "Rewrite the entire backend module in Rust to feel better",
        "d": "Commit the changes, push, and immediately close your laptop",
        "correct_key": "d"
    },
    {
        "question": "You are trying to refactor a legacy module using TypeScript, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "c"
    },
    {
        "question": "You are trying to containerize an application using Stack Overflow, but your internet connection drops right in the middle. What is your next move?",
        "a": "Delete `node_modules` and the package lockfile and rebuild",
        "b": "Run `npm cache clean --force` and pray to the package gods",
        "c": "All of the above in random order",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "c"
    },
    {
        "question": "You are trying to install npm packages using Jenkins, but your internet connection drops right in the middle. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Run a system reboot and hope it resolves itself",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Tell your manager that the sprint goals were unrealistic",
        "correct_key": "c"
    },
    {
        "question": "You are trying to containerize an application using Vim, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Delete your local repository and clone a fresh copy",
        "b": "Blame the newest engineering intern (even if you don't have one)",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "b"
    },
    {
        "question": "You are trying to ssh into the production server using Git, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "c"
    },
    {
        "question": "You are trying to review a coworker's pull request using Rust, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Delete your local repository and clone a fresh copy",
        "b": "Blame the newest engineering intern (even if you don't have one)",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "b"
    },
    {
        "question": "You are trying to set up OAuth credentials using Docker, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "All of the above in random order",
        "d": "Run `npm cache clean --force` and pray to the package gods",
        "correct_key": "c"
    },
    {
        "question": "You are trying to install a dependency package using Git, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Ask a question on Stack Overflow under an anonymous username",
        "b": "Force push the changes directly to the main branch",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Straighten your shrimp posture and sigh deeply",
        "correct_key": "d"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using React, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Blame the newest engineering intern (even if you don't have one)",
        "c": "Delete your local repository and clone a fresh copy",
        "d": "Pretend your Slack is broken and go grab a coffee",
        "correct_key": "b"
    },
    {
        "question": "You are trying to clean up the docker images using JavaScript, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Switch your theme to dark mode and hope the issue goes away",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "b"
    },
    {
        "question": "You are trying to review a coworker's pull request using Python, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Delete your local repository and clone a fresh copy",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Blame the newest engineering intern (even if you don't have one)",
        "correct_key": "d"
    },
    {
        "question": "You are trying to optimize a database query using Nginx, but your laptop battery dies during the process. What is your next move?",
        "a": "Blame the cloud hosting provider's regional server outage",
        "b": "Add a try-except block around the entire file and go to sleep",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Rewrite the entire backend module in Rust to feel better",
        "correct_key": "c"
    },
    {
        "question": "You are trying to write a unit test suite using Webpack, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Add the `!important` rule to 30 different lines of CSS styling",
        "b": "Run a system reboot and hope it resolves itself",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Pretend you have a power outage and leave the Zoom meeting",
        "correct_key": "a"
    },
    {
        "question": "You are trying to explain a complex regex pattern using HTML/CSS, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Delete your local repository and clone a fresh copy",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Pretend your Slack is broken and go grab a coffee",
        "correct_key": "c"
    },
    {
        "question": "You are trying to clean up the docker images using HTML/CSS, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "All of the above in random order",
        "d": "Run `npm cache clean --force` and pray to the package gods",
        "correct_key": "c"
    },
    {
        "question": "You are trying to merge a pull request using HTML/CSS, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Delete your local repository and clone a fresh copy",
        "b": "Blame the newest engineering intern (even if you don't have one)",
        "c": "Cry quietly in the nearest storage room or cafeteria",
        "d": "Pretend your Slack is broken and go grab a coffee",
        "correct_key": "b"
    },
    {
        "question": "You are trying to clean up the docker images using Docker, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Add the `!important` rule to 30 different lines of CSS styling",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Pretend you have a power outage and leave the Zoom meeting",
        "correct_key": "b"
    },
    {
        "question": "You are trying to mock an external payment API using Kubectl, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Take a 2-hour lunch break to clear your mind",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "c"
    },
    {
        "question": "You are trying to deploy a hotfix using Vim, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Blame the newest engineering intern (even if you don't have one)",
        "c": "Delete your local repository and clone a fresh copy",
        "d": "Pretend your Slack is broken and go grab a coffee",
        "correct_key": "b"
    },
    {
        "question": "You are trying to center a div in CSS using Kubectl, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Increase the server instance size and pay AWS 4x more money",
        "b": "Remove all unit tests so the build pipeline succeeds",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Spend three hours debating tabs vs spaces in the company Slack",
        "correct_key": "b"
    },
    {
        "question": "You are trying to audit the security dependencies using React, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Ask a question on Stack Overflow under an anonymous username",
        "b": "Force push the changes directly to the main branch",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Straighten your shrimp posture and sigh deeply",
        "correct_key": "d"
    },
    {
        "question": "You are trying to write a script in Bash using Redis, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Switch your theme to dark mode and hope the issue goes away",
        "b": "Decline the ticket and reassign it to the senior team lead",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "correct_key": "d"
    },
    {
        "question": "You are trying to run a database migration script using MongoDB, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Spend three hours debating tabs vs spaces in the company Slack",
        "b": "Tell the product owner that the feature requires more research",
        "c": "Remove all unit tests so the build pipeline succeeds",
        "d": "Increase the server instance size and pay AWS 4x more money",
        "correct_key": "c"
    },
    {
        "question": "You are trying to center a div in CSS using Webpack, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "b": "Roll back to the last working build and hope nobody checked logs",
        "c": "Add a console.log statement every three lines to see what is happening",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "b"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using Kubernetes, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Tell the product owner that the feature requires more research",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Increase the server instance size and pay AWS 4x more money",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to run a database migration script using C++, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Take a 2-hour lunch break to clear your mind",
        "b": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "c": "Add a console.log statement every three lines to see what is happening",
        "d": "Roll back to the last working build and hope nobody checked logs",
        "correct_key": "d"
    },
    {
        "question": "You are trying to deploy a hotfix using GitHub Actions, but your internet connection drops right in the middle. What is your next move?",
        "a": "Add a comment saying '// TODO: fix this later' and ignore it",
        "b": "Force push the changes directly to the main branch",
        "c": "Straighten your shrimp posture and sigh deeply",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "c"
    },
    {
        "question": "You are trying to ssh into the production server using JavaScript, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Decline the ticket and reassign it to the senior team lead",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "a"
    },
    {
        "question": "You are trying to update a production database schema using AWS, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Decline the ticket and reassign it to the senior team lead",
        "c": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "d": "Switch your theme to dark mode and hope the issue goes away",
        "correct_key": "c"
    },
    {
        "question": "You are trying to reset the git branch using Git, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Run `npm cache clean --force` and pray to the package gods",
        "b": "All of the above in random order",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "Delete `node_modules` and the package lockfile and rebuild",
        "correct_key": "b"
    },
    {
        "question": "You are trying to revert a bad merge using Rust, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Spend three hours debating tabs vs spaces in the company Slack",
        "correct_key": "a"
    },
    {
        "question": "You are trying to reset the git branch using Rust, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Spend three hours debating tabs vs spaces in the company Slack",
        "correct_key": "a"
    },
    {
        "question": "You are trying to install npm packages using Git, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "a"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using Stack Overflow, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Switch your theme to dark mode and hope the issue goes away",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "b"
    },
    {
        "question": "You are trying to mock an external payment API using Webpack, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Increase the server instance size and pay AWS 4x more money",
        "correct_key": "a"
    },
    {
        "question": "You are trying to reset the git branch using Redis, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Run a system reboot and hope it resolves itself",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Pretend you have a power outage and leave the Zoom meeting",
        "correct_key": "c"
    },
    {
        "question": "You are trying to write a script in Bash using MongoDB, but your internet connection drops right in the middle. What is your next move?",
        "a": "Add a console.log statement every three lines to see what is happening",
        "b": "Take a 2-hour lunch break to clear your mind",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "c"
    },
    {
        "question": "You are trying to audit the security dependencies using TypeScript, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Switch your theme to dark mode and hope the issue goes away",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "b"
    },
    {
        "question": "You are trying to containerize an application using Rust, but your laptop battery dies during the process. What is your next move?",
        "a": "Delete `node_modules` and the package lockfile and rebuild",
        "b": "All of the above in random order",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "b"
    },
    {
        "question": "You are trying to update a production database schema using PostgreSQL, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Force push the changes directly to the main branch",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Add a comment saying '// TODO: fix this later' and ignore it",
        "correct_key": "a"
    },
    {
        "question": "You are trying to install a dependency package using JavaScript, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Decline the ticket and reassign it to the senior team lead",
        "b": "Read the logs carefully and trace the exception stack",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "correct_key": "d"
    },
    {
        "question": "You are trying to write a script in Bash using Webpack, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Decline the ticket and reassign it to the senior team lead",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "correct_key": "d"
    },
    {
        "question": "You are trying to merge a pull request using JavaScript, but it accidentally deletes the system root directory. What is your next move?",
        "a": "All of the above in random order",
        "b": "Tell the client that this is a feature, not a bug",
        "c": "Delete `node_modules` and the package lockfile and rebuild",
        "d": "Run `npm cache clean --force` and pray to the package gods",
        "correct_key": "a"
    },
    {
        "question": "You are trying to review a coworker's pull request using Python, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Blame the cloud hosting provider's regional server outage",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Add a try-except block around the entire file and go to sleep",
        "correct_key": "c"
    },
    {
        "question": "You are trying to audit the security dependencies using MongoDB, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Read the logs carefully and trace the exception stack",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "a"
    },
    {
        "question": "You are trying to fix a memory leak using Docker, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Decline the ticket and reassign it to the senior team lead",
        "b": "Read the logs carefully and trace the exception stack",
        "c": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "d": "Switch your theme to dark mode and hope the issue goes away",
        "correct_key": "c"
    },
    {
        "question": "You are trying to audit the security dependencies using React, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Tell the product owner that the feature requires more research",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to merge a pull request using Git, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "a"
    },
    {
        "question": "You are trying to ssh into the production server using GitHub Actions, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Take a 2-hour lunch break to clear your mind",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "d": "Roll back to the last working build and hope nobody checked logs",
        "correct_key": "d"
    },
    {
        "question": "You are trying to optimize a database query using Docker, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Tell the product owner that the feature requires more research",
        "correct_key": "a"
    },
    {
        "question": "You are trying to ssh into the production server using Kubernetes, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Commit the changes, push, and immediately close your laptop",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Add a try-except block around the entire file and go to sleep",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "a"
    },
    {
        "question": "You are trying to refactor a legacy module using React, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Decline the ticket and reassign it to the senior team lead",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "b"
    },
    {
        "question": "You are trying to revert a bad merge using Rust, but your laptop battery dies during the process. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "c"
    },
    {
        "question": "You are trying to run a database migration script using Django, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "All of the above in random order",
        "d": "Run `npm cache clean --force` and pray to the package gods",
        "correct_key": "c"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using Stack Overflow, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Tell the product owner that the feature requires more research",
        "c": "Increase the server instance size and pay AWS 4x more money",
        "d": "Spend three hours debating tabs vs spaces in the company Slack",
        "correct_key": "a"
    },
    {
        "question": "You are trying to write a unit test suite using Webpack, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Decline the ticket and reassign it to the senior team lead",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Switch your theme to dark mode and hope the issue goes away",
        "correct_key": "b"
    },
    {
        "question": "You are trying to run a database migration script using PostgreSQL, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Delete `node_modules` and the package lockfile and rebuild",
        "b": "All of the above in random order",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "b"
    },
    {
        "question": "You are trying to containerize an application using C++, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Ask a question on Stack Overflow under an anonymous username",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Force push the changes directly to the main branch",
        "correct_key": "a"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using Python, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Blame the newest engineering intern (even if you don't have one)",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Delete your local repository and clone a fresh copy",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "a"
    },
    {
        "question": "You are trying to optimize a database query using Git, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Tell the product owner that the feature requires more research",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Remove all unit tests so the build pipeline succeeds",
        "d": "Increase the server instance size and pay AWS 4x more money",
        "correct_key": "c"
    },
    {
        "question": "You are trying to audit the security dependencies using Django, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Switch your theme to dark mode and hope the issue goes away",
        "b": "Read the logs carefully and trace the exception stack",
        "c": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "c"
    },
    {
        "question": "You are trying to fix a memory leak using Rust, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "a"
    },
    {
        "question": "You are trying to audit the security dependencies using TypeScript, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "All of the above in random order",
        "correct_key": "d"
    },
    {
        "question": "You are trying to containerize an application using Node.js, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "All of the above in random order",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "Delete `node_modules` and the package lockfile and rebuild",
        "correct_key": "b"
    },
    {
        "question": "You are trying to center a div in CSS using PostgreSQL, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "All of the above in random order",
        "d": "Run `npm cache clean --force` and pray to the package gods",
        "correct_key": "c"
    },
    {
        "question": "You are trying to set up OAuth credentials using React, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Ask a question on Stack Overflow under an anonymous username",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Force push the changes directly to the main branch",
        "correct_key": "a"
    },
    {
        "question": "You are trying to revert a bad merge using Docker, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Switch your theme to dark mode and hope the issue goes away",
        "b": "Read the logs carefully and trace the exception stack",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "correct_key": "d"
    },
    {
        "question": "You are trying to run a database migration script using Webpack, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Spend three hours debating tabs vs spaces in the company Slack",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to merge a pull request using TypeScript, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Run a system reboot and hope it resolves itself",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to containerize an application using Redis, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Increase the server instance size and pay AWS 4x more money",
        "b": "Remove all unit tests so the build pipeline succeeds",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Spend three hours debating tabs vs spaces in the company Slack",
        "correct_key": "b"
    },
    {
        "question": "You are trying to install npm packages using Kubernetes, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Blame the cloud hosting provider's regional server outage",
        "d": "Commit the changes, push, and immediately close your laptop",
        "correct_key": "d"
    },
    {
        "question": "You are trying to center a div in CSS using Jenkins, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "c"
    },
    {
        "question": "You are trying to deploy a hotfix using Kubernetes, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Blame the cloud hosting provider's regional server outage",
        "d": "Commit the changes, push, and immediately close your laptop",
        "correct_key": "d"
    },
    {
        "question": "You are trying to mock an external payment API using AWS, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Commit the changes, push, and immediately close your laptop",
        "b": "Add a try-except block around the entire file and go to sleep",
        "c": "Rewrite the entire backend module in Rust to feel better",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "a"
    },
    {
        "question": "You are trying to optimize a database query using GitHub Actions, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Tell the product owner that the feature requires more research",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Remove all unit tests so the build pipeline succeeds",
        "d": "Spend three hours debating tabs vs spaces in the company Slack",
        "correct_key": "c"
    },
    {
        "question": "You are trying to containerize an application using Python, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Run a system reboot and hope it resolves itself",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to set up OAuth credentials using GitHub Actions, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Increase the server instance size and pay AWS 4x more money",
        "d": "Tell the product owner that the feature requires more research",
        "correct_key": "a"
    },
    {
        "question": "You are trying to review a coworker's pull request using Vim, but your internet connection drops right in the middle. What is your next move?",
        "a": "Take a 2-hour lunch break to clear your mind",
        "b": "Roll back to the last working build and hope nobody checked logs",
        "c": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "d": "Add a console.log statement every three lines to see what is happening",
        "correct_key": "b"
    },
    {
        "question": "You are trying to mock an external payment API using PostgreSQL, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Take a 2-hour lunch break to clear your mind",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "c"
    },
    {
        "question": "You are trying to center a div in CSS using HTML/CSS, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Decline the ticket and reassign it to the senior team lead",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "c"
    },
    {
        "question": "You are trying to mock an external payment API using Stack Overflow, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "c"
    },
    {
        "question": "You are trying to install npm packages using Kubernetes, but your internet connection drops right in the middle. What is your next move?",
        "a": "Switch your theme to dark mode and hope the issue goes away",
        "b": "Decline the ticket and reassign it to the senior team lead",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "correct_key": "d"
    },
    {
        "question": "You are trying to update a production database schema using PostgreSQL, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Commit the changes, push, and immediately close your laptop",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Blame the cloud hosting provider's regional server outage",
        "d": "Add a try-except block around the entire file and go to sleep",
        "correct_key": "a"
    },
    {
        "question": "You are trying to mock an external payment API using MongoDB, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Add the `!important` rule to 30 different lines of CSS styling",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "a"
    },
    {
        "question": "You are trying to fix a memory leak using JavaScript, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Take a 2-hour lunch break to clear your mind",
        "b": "Roll back to the last working build and hope nobody checked logs",
        "c": "Add a console.log statement every three lines to see what is happening",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "b"
    },
    {
        "question": "You are trying to run a database migration script using GitHub Actions, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Increase the server instance size and pay AWS 4x more money",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to fix a memory leak using JavaScript, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Add a comment saying '// TODO: fix this later' and ignore it",
        "c": "Force push the changes directly to the main branch",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "a"
    },
    {
        "question": "You are trying to write a unit test suite using TypeScript, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Pretend your Slack is broken and go grab a coffee",
        "b": "Delete your local repository and clone a fresh copy",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "c"
    },
    {
        "question": "You are trying to deploy a hotfix using Node.js, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "Run `npm cache clean --force` and pray to the package gods",
        "c": "Delete `node_modules` and the package lockfile and rebuild",
        "d": "All of the above in random order",
        "correct_key": "d"
    },
    {
        "question": "You are trying to audit the security dependencies using Python, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Blame the cloud hosting provider's regional server outage",
        "b": "Commit the changes, push, and immediately close your laptop",
        "c": "Rewrite the entire backend module in Rust to feel better",
        "d": "Add a try-except block around the entire file and go to sleep",
        "correct_key": "b"
    },
    {
        "question": "You are trying to reset the git branch using Vim, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "All of the above in random order",
        "b": "Run `npm cache clean --force` and pray to the package gods",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "Delete `node_modules` and the package lockfile and rebuild",
        "correct_key": "a"
    },
    {
        "question": "You are trying to merge a pull request using TypeScript, but your laptop battery dies during the process. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Add a comment saying '// TODO: fix this later' and ignore it",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Force push the changes directly to the main branch",
        "correct_key": "a"
    },
    {
        "question": "You are trying to ssh into the production server using HTML/CSS, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "b"
    },
    {
        "question": "You are trying to center a div in CSS using GitHub Actions, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "All of the above in random order",
        "b": "Tell the client that this is a feature, not a bug",
        "c": "Delete `node_modules` and the package lockfile and rebuild",
        "d": "Run `npm cache clean --force` and pray to the package gods",
        "correct_key": "a"
    },
    {
        "question": "You are trying to install npm packages using MongoDB, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Add the `!important` rule to 30 different lines of CSS styling",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "b"
    },
    {
        "question": "You are trying to install a dependency package using Django, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Ask a question on Stack Overflow under an anonymous username",
        "b": "Force push the changes directly to the main branch",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Straighten your shrimp posture and sigh deeply",
        "correct_key": "d"
    },
    {
        "question": "You are trying to revert a bad merge using AWS, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "c": "Add a console.log statement every three lines to see what is happening",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "a"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using AWS, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "Switch your theme to dark mode and hope the issue goes away",
        "b": "Decline the ticket and reassign it to the senior team lead",
        "c": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "c"
    },
    {
        "question": "You are trying to write a script in Bash using Nginx, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Tell the product owner that the feature requires more research",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Increase the server instance size and pay AWS 4x more money",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to refactor a legacy module using TypeScript, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Tell the product owner that the feature requires more research",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Increase the server instance size and pay AWS 4x more money",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to review a coworker's pull request using Jenkins, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "c"
    },
    {
        "question": "You are trying to install npm packages using Jenkins, but you realize you executed the command on the master branch. What is your next move?",
        "a": "All of the above in random order",
        "b": "Run `npm cache clean --force` and pray to the package gods",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "Delete `node_modules` and the package lockfile and rebuild",
        "correct_key": "a"
    },
    {
        "question": "You are trying to clean up the docker images using Stack Overflow, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Add the `!important` rule to 30 different lines of CSS styling",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Tell your manager that the sprint goals were unrealistic",
        "correct_key": "b"
    },
    {
        "question": "You are trying to fix a memory leak using Jenkins, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to refactor a legacy module using GitHub Actions, but the database suddenly disappears from the console. What is your next move?",
        "a": "Force push the changes directly to the main branch",
        "b": "Straighten your shrimp posture and sigh deeply",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "b"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using Webpack, but your internet connection drops right in the middle. What is your next move?",
        "a": "Pretend your Slack is broken and go grab a coffee",
        "b": "Blame the newest engineering intern (even if you don't have one)",
        "c": "Delete your local repository and clone a fresh copy",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "b"
    },
    {
        "question": "You are trying to install npm packages using PostgreSQL, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Spend three hours debating tabs vs spaces in the company Slack",
        "b": "Tell the product owner that the feature requires more research",
        "c": "Remove all unit tests so the build pipeline succeeds",
        "d": "Increase the server instance size and pay AWS 4x more money",
        "correct_key": "c"
    },
    {
        "question": "You are trying to deploy a hotfix using React, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Force push the changes directly to the main branch",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Add a comment saying '// TODO: fix this later' and ignore it",
        "correct_key": "a"
    },
    {
        "question": "You are trying to revert a bad merge using GitHub Actions, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Take a 2-hour lunch break to clear your mind",
        "c": "Add a console.log statement every three lines to see what is happening",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "a"
    },
    {
        "question": "You are trying to run a database migration script using HTML/CSS, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Blame the newest engineering intern (even if you don't have one)",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Delete your local repository and clone a fresh copy",
        "correct_key": "b"
    },
    {
        "question": "You are trying to update a production database schema using C++, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Add the `!important` rule to 30 different lines of CSS styling",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "a"
    },
    {
        "question": "You are trying to update a production database schema using Node.js, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Commit the changes, push, and immediately close your laptop",
        "b": "Blame the cloud hosting provider's regional server outage",
        "c": "Add a try-except block around the entire file and go to sleep",
        "d": "Rewrite the entire backend module in Rust to feel better",
        "correct_key": "a"
    },
    {
        "question": "You are trying to run a database migration script using Kubernetes, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Switch your theme to dark mode and hope the issue goes away",
        "b": "Read the logs carefully and trace the exception stack",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "correct_key": "d"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using Kubernetes, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Delete your local repository and clone a fresh copy",
        "b": "Blame the newest engineering intern (even if you don't have one)",
        "c": "Cry quietly in the nearest storage room or cafeteria",
        "d": "Pretend your Slack is broken and go grab a coffee",
        "correct_key": "b"
    },
    {
        "question": "You are trying to set up OAuth credentials using HTML/CSS, but your laptop battery dies during the process. What is your next move?",
        "a": "Tell the product owner that the feature requires more research",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Remove all unit tests so the build pipeline succeeds",
        "d": "Increase the server instance size and pay AWS 4x more money",
        "correct_key": "c"
    },
    {
        "question": "You are trying to optimize a database query using HTML/CSS, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "c"
    },
    {
        "question": "You are trying to fix a memory leak using Jenkins, but the database suddenly disappears from the console. What is your next move?",
        "a": "Decline the ticket and reassign it to the senior team lead",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Switch your theme to dark mode and hope the issue goes away",
        "correct_key": "b"
    },
    {
        "question": "You are trying to review a coworker's pull request using Kubectl, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Force push the changes directly to the main branch",
        "b": "Straighten your shrimp posture and sigh deeply",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "b"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using Redis, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Force push the changes directly to the main branch",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "a"
    },
    {
        "question": "You are trying to optimize a database query using Python, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Run a system reboot and hope it resolves itself",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Pretend you have a power outage and leave the Zoom meeting",
        "correct_key": "c"
    },
    {
        "question": "You are trying to run a database migration script using C++, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Increase the server instance size and pay AWS 4x more money",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Remove all unit tests so the build pipeline succeeds",
        "d": "Tell the product owner that the feature requires more research",
        "correct_key": "c"
    },
    {
        "question": "You are trying to clean up the docker images using React, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Tell the product owner that the feature requires more research",
        "correct_key": "a"
    },
    {
        "question": "You are trying to set up OAuth credentials using AWS, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Switch your theme to dark mode and hope the issue goes away",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "b"
    },
    {
        "question": "You are trying to mock an external payment API using Git, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Read the logs carefully and trace the exception stack",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "a"
    },
    {
        "question": "You are trying to mock an external payment API using MongoDB, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Blame the newest engineering intern (even if you don't have one)",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Cry quietly in the nearest storage room or cafeteria",
        "d": "Delete your local repository and clone a fresh copy",
        "correct_key": "a"
    },
    {
        "question": "You are trying to install npm packages using Kubectl, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Decline the ticket and reassign it to the senior team lead",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "correct_key": "d"
    },
    {
        "question": "You are trying to set up OAuth credentials using Vim, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Tell the product owner that the feature requires more research",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to write a unit test suite using JavaScript, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Tell the product owner that the feature requires more research",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Increase the server instance size and pay AWS 4x more money",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to merge a pull request using Rust, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Take a 2-hour lunch break to clear your mind",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "a"
    },
    {
        "question": "You are trying to clean up the docker images using Nginx, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Blame the cloud hosting provider's regional server outage",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Rewrite the entire backend module in Rust to feel better",
        "correct_key": "c"
    },
    {
        "question": "You are trying to mock an external payment API using Stack Overflow, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Commit the changes, push, and immediately close your laptop",
        "b": "Add a try-except block around the entire file and go to sleep",
        "c": "Rewrite the entire backend module in Rust to feel better",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "a"
    },
    {
        "question": "You are trying to clean up the docker images using C++, but the database suddenly disappears from the console. What is your next move?",
        "a": "Increase the server instance size and pay AWS 4x more money",
        "b": "Remove all unit tests so the build pipeline succeeds",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Tell the product owner that the feature requires more research",
        "correct_key": "b"
    },
    {
        "question": "You are trying to write a unit test suite using Rust, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Take a 2-hour lunch break to clear your mind",
        "c": "Add a console.log statement every three lines to see what is happening",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "a"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using Node.js, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "a"
    },
    {
        "question": "You are trying to mock an external payment API using C++, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Ask a question on Stack Overflow under an anonymous username",
        "b": "Add a comment saying '// TODO: fix this later' and ignore it",
        "c": "Force push the changes directly to the main branch",
        "d": "Straighten your shrimp posture and sigh deeply",
        "correct_key": "d"
    },
    {
        "question": "You are trying to set up OAuth credentials using PostgreSQL, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Rewrite the entire backend module in Rust to feel better",
        "b": "Commit the changes, push, and immediately close your laptop",
        "c": "Blame the cloud hosting provider's regional server outage",
        "d": "Add a try-except block around the entire file and go to sleep",
        "correct_key": "b"
    },
    {
        "question": "You are trying to write a unit test suite using TypeScript, but the database suddenly disappears from the console. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "c": "Take a 2-hour lunch break to clear your mind",
        "d": "Add a console.log statement every three lines to see what is happening",
        "correct_key": "a"
    },
    {
        "question": "You are trying to write a script in Bash using React, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Decline the ticket and reassign it to the senior team lead",
        "b": "Read the logs carefully and trace the exception stack",
        "c": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "d": "Switch your theme to dark mode and hope the issue goes away",
        "correct_key": "c"
    },
    {
        "question": "You are trying to update a production database schema using Vim, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Delete `node_modules` and the package lockfile and rebuild",
        "b": "Tell the client that this is a feature, not a bug",
        "c": "All of the above in random order",
        "d": "Run `npm cache clean --force` and pray to the package gods",
        "correct_key": "c"
    },
    {
        "question": "You are trying to refactor a legacy module using MongoDB, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Decline the ticket and reassign it to the senior team lead",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "b"
    },
    {
        "question": "You are trying to optimize a database query using AWS, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "a"
    },
    {
        "question": "You are trying to write a script in Bash using Jenkins, but your laptop battery dies during the process. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Tell the product owner that the feature requires more research",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Increase the server instance size and pay AWS 4x more money",
        "correct_key": "a"
    },
    {
        "question": "You are trying to revert a bad merge using React, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "c"
    },
    {
        "question": "You are trying to reset the git branch using Kubectl, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Run a system reboot and hope it resolves itself",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to deploy a hotfix using AWS, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Blame the newest engineering intern (even if you don't have one)",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Delete your local repository and clone a fresh copy",
        "correct_key": "b"
    },
    {
        "question": "You are trying to install npm packages using Kubectl, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "a"
    },
    {
        "question": "You are trying to clean up the docker images using Stack Overflow, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Add a console.log statement every three lines to see what is happening",
        "b": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "c"
    },
    {
        "question": "You are trying to merge a pull request using C++, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Increase the server instance size and pay AWS 4x more money",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Remove all unit tests so the build pipeline succeeds",
        "d": "Tell the product owner that the feature requires more research",
        "correct_key": "c"
    },
    {
        "question": "You are trying to deploy a hotfix using Django, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Add a console.log statement every three lines to see what is happening",
        "b": "Roll back to the last working build and hope nobody checked logs",
        "c": "Take a 2-hour lunch break to clear your mind",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "b"
    },
    {
        "question": "You are trying to run a database migration script using Rust, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Pretend your Slack is broken and go grab a coffee",
        "b": "Cry quietly in the nearest storage room or cafeteria",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Delete your local repository and clone a fresh copy",
        "correct_key": "c"
    },
    {
        "question": "You are trying to set up OAuth credentials using TypeScript, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "c"
    },
    {
        "question": "You are trying to merge a pull request using React, but the database suddenly disappears from the console. What is your next move?",
        "a": "Commit the changes, push, and immediately close your laptop",
        "b": "Blame the cloud hosting provider's regional server outage",
        "c": "Rewrite the entire backend module in Rust to feel better",
        "d": "Add a try-except block around the entire file and go to sleep",
        "correct_key": "a"
    },
    {
        "question": "You are trying to write a unit test suite using GitHub Actions, but your laptop battery dies during the process. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Delete your local repository and clone a fresh copy",
        "correct_key": "c"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using MongoDB, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Pretend you have a power outage and leave the Zoom meeting",
        "correct_key": "c"
    },
    {
        "question": "You are trying to write a script in Bash using HTML/CSS, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to clean up the docker images using React, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Blame the newest engineering intern (even if you don't have one)",
        "b": "Cry quietly in the nearest storage room or cafeteria",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Delete your local repository and clone a fresh copy",
        "correct_key": "a"
    },
    {
        "question": "You are trying to ssh into the production server using Django, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Decline the ticket and reassign it to the senior team lead",
        "b": "Read the logs carefully and trace the exception stack",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "correct_key": "d"
    },
    {
        "question": "You are trying to fix a memory leak using HTML/CSS, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Run `npm cache clean --force` and pray to the package gods",
        "b": "All of the above in random order",
        "c": "Delete `node_modules` and the package lockfile and rebuild",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "b"
    },
    {
        "question": "You are trying to install npm packages using TypeScript, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Add a console.log statement every three lines to see what is happening",
        "b": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "c"
    },
    {
        "question": "You are trying to merge a pull request using C++, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Add a console.log statement every three lines to see what is happening",
        "b": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "c": "Take a 2-hour lunch break to clear your mind",
        "d": "Roll back to the last working build and hope nobody checked logs",
        "correct_key": "d"
    },
    {
        "question": "You are trying to fix a memory leak using Stack Overflow, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Run `npm cache clean --force` and pray to the package gods",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "All of the above in random order",
        "correct_key": "d"
    },
    {
        "question": "You are trying to merge a pull request using TypeScript, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Delete `node_modules` and the package lockfile and rebuild",
        "b": "All of the above in random order",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "b"
    },
    {
        "question": "You are trying to set up OAuth credentials using Node.js, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Rewrite the entire backend module in Rust to feel better",
        "b": "Blame the cloud hosting provider's regional server outage",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Add a try-except block around the entire file and go to sleep",
        "correct_key": "c"
    },
    {
        "question": "You are trying to fix a memory leak using Jenkins, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Force push the changes directly to the main branch",
        "b": "Straighten your shrimp posture and sigh deeply",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Add a comment saying '// TODO: fix this later' and ignore it",
        "correct_key": "b"
    },
    {
        "question": "You are trying to clean up the docker images using JavaScript, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Run `npm cache clean --force` and pray to the package gods",
        "b": "All of the above in random order",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "Delete `node_modules` and the package lockfile and rebuild",
        "correct_key": "b"
    },
    {
        "question": "You are trying to clean up the docker images using JavaScript, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Add a console.log statement every three lines to see what is happening",
        "b": "Roll back to the last working build and hope nobody checked logs",
        "c": "Take a 2-hour lunch break to clear your mind",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "b"
    },
    {
        "question": "You are trying to refactor a legacy module using Django, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Decline the ticket and reassign it to the senior team lead",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "a"
    },
    {
        "question": "You are trying to refactor a legacy module using React, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "a"
    },
    {
        "question": "You are trying to optimize a database query using PostgreSQL, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Commit the changes, push, and immediately close your laptop",
        "b": "Blame the cloud hosting provider's regional server outage",
        "c": "Rewrite the entire backend module in Rust to feel better",
        "d": "Add a try-except block around the entire file and go to sleep",
        "correct_key": "a"
    },
    {
        "question": "You are trying to refactor a legacy module using Git, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "All of the above in random order",
        "correct_key": "d"
    },
    {
        "question": "You are trying to clean up the docker images using Jenkins, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "Add a comment saying '// TODO: fix this later' and ignore it",
        "b": "Straighten your shrimp posture and sigh deeply",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Force push the changes directly to the main branch",
        "correct_key": "b"
    },
    {
        "question": "You are trying to containerize an application using Docker, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "c"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using PostgreSQL, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Increase the server instance size and pay AWS 4x more money",
        "b": "Remove all unit tests so the build pipeline succeeds",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Tell the product owner that the feature requires more research",
        "correct_key": "b"
    },
    {
        "question": "You are trying to install npm packages using Kubectl, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Blame the newest engineering intern (even if you don't have one)",
        "b": "Delete your local repository and clone a fresh copy",
        "c": "Cry quietly in the nearest storage room or cafeteria",
        "d": "Pretend your Slack is broken and go grab a coffee",
        "correct_key": "a"
    },
    {
        "question": "You are trying to install npm packages using Redis, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "c"
    },
    {
        "question": "You are trying to write a script in Bash using C++, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Read the logs carefully and trace the exception stack",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "a"
    },
    {
        "question": "You are trying to install npm packages using Node.js, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Commit the changes, push, and immediately close your laptop",
        "c": "Rewrite the entire backend module in Rust to feel better",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "b"
    },
    {
        "question": "You are trying to ssh into the production server using Stack Overflow, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Pretend your Slack is broken and go grab a coffee",
        "b": "Delete your local repository and clone a fresh copy",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "c"
    },
    {
        "question": "You are trying to ssh into the production server using HTML/CSS, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Delete your local repository and clone a fresh copy",
        "b": "Cry quietly in the nearest storage room or cafeteria",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Blame the newest engineering intern (even if you don't have one)",
        "correct_key": "d"
    },
    {
        "question": "You are trying to revert a bad merge using Jenkins, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Ask a question on Stack Overflow under an anonymous username",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Force push the changes directly to the main branch",
        "correct_key": "a"
    },
    {
        "question": "You are trying to revert a bad merge using React, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Take a 2-hour lunch break to clear your mind",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "d": "Roll back to the last working build and hope nobody checked logs",
        "correct_key": "d"
    },
    {
        "question": "You are trying to explain a complex regex pattern using Django, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "c"
    },
    {
        "question": "You are trying to install npm packages using Redis, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Add the `!important` rule to 30 different lines of CSS styling",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "a"
    },
    {
        "question": "You are trying to merge a pull request using HTML/CSS, but your laptop battery dies during the process. What is your next move?",
        "a": "Run `npm cache clean --force` and pray to the package gods",
        "b": "Tell the client that this is a feature, not a bug",
        "c": "Delete `node_modules` and the package lockfile and rebuild",
        "d": "All of the above in random order",
        "correct_key": "d"
    },
    {
        "question": "You are trying to center a div in CSS using TypeScript, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "c"
    },
    {
        "question": "You are trying to update a production database schema using TypeScript, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Add the `!important` rule to 30 different lines of CSS styling",
        "b": "Run a system reboot and hope it resolves itself",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Pretend you have a power outage and leave the Zoom meeting",
        "correct_key": "a"
    },
    {
        "question": "You are trying to write a script in Bash using PostgreSQL, but your internet connection drops right in the middle. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Run a system reboot and hope it resolves itself",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to update a production database schema using C++, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Take a 2-hour lunch break to clear your mind",
        "c": "Add a console.log statement every three lines to see what is happening",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "a"
    },
    {
        "question": "You are trying to revert a bad merge using Kubernetes, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Delete your local repository and clone a fresh copy",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Cry quietly in the nearest storage room or cafeteria",
        "d": "Blame the newest engineering intern (even if you don't have one)",
        "correct_key": "d"
    },
    {
        "question": "You are trying to center a div in CSS using PostgreSQL, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Add a comment saying '// TODO: fix this later' and ignore it",
        "b": "Straighten your shrimp posture and sigh deeply",
        "c": "Force push the changes directly to the main branch",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "b"
    },
    {
        "question": "You are trying to reset the git branch using Docker, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "b": "Roll back to the last working build and hope nobody checked logs",
        "c": "Add a console.log statement every three lines to see what is happening",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "b"
    },
    {
        "question": "You are trying to mock an external payment API using PostgreSQL, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Take a 2-hour lunch break to clear your mind",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "d": "Roll back to the last working build and hope nobody checked logs",
        "correct_key": "d"
    },
    {
        "question": "You are trying to mock an external payment API using Vim, but the database suddenly disappears from the console. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Decline the ticket and reassign it to the senior team lead",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Switch your theme to dark mode and hope the issue goes away",
        "correct_key": "a"
    },
    {
        "question": "You are trying to run a database migration script using Nginx, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Pretend your Slack is broken and go grab a coffee",
        "b": "Cry quietly in the nearest storage room or cafeteria",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Delete your local repository and clone a fresh copy",
        "correct_key": "c"
    },
    {
        "question": "You are trying to clean up the docker images using Redis, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Force push the changes directly to the main branch",
        "b": "Straighten your shrimp posture and sigh deeply",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "b"
    },
    {
        "question": "You are trying to mock an external payment API using GitHub Actions, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Delete your local repository and clone a fresh copy",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Cry quietly in the nearest storage room or cafeteria",
        "d": "Blame the newest engineering intern (even if you don't have one)",
        "correct_key": "d"
    },
    {
        "question": "You are trying to review a coworker's pull request using MongoDB, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Blame the newest engineering intern (even if you don't have one)",
        "b": "Delete your local repository and clone a fresh copy",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "a"
    },
    {
        "question": "You are trying to containerize an application using Webpack, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Pretend you have a power outage and leave the Zoom meeting",
        "correct_key": "c"
    },
    {
        "question": "You are trying to reset the git branch using Django, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "c"
    },
    {
        "question": "You are trying to run a database migration script using C++, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Rewrite the entire backend module in Rust to feel better",
        "b": "Add a try-except block around the entire file and go to sleep",
        "c": "Blame the cloud hosting provider's regional server outage",
        "d": "Commit the changes, push, and immediately close your laptop",
        "correct_key": "d"
    },
    {
        "question": "You are trying to optimize a database query using AWS, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Take a 2-hour lunch break to clear your mind",
        "c": "Add a console.log statement every three lines to see what is happening",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "a"
    },
    {
        "question": "You are trying to review a coworker's pull request using Git, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Add a comment saying '// TODO: fix this later' and ignore it",
        "b": "Straighten your shrimp posture and sigh deeply",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Force push the changes directly to the main branch",
        "correct_key": "b"
    },
    {
        "question": "You are trying to clean up the docker images using C++, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Blame the newest engineering intern (even if you don't have one)",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Delete your local repository and clone a fresh copy",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "a"
    },
    {
        "question": "You are trying to refactor a legacy module using Node.js, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Delete your local repository and clone a fresh copy",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Pretend your Slack is broken and go grab a coffee",
        "correct_key": "c"
    },
    {
        "question": "You are trying to write a script in Bash using Redis, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to center a div in CSS using TypeScript, but your internet connection drops right in the middle. What is your next move?",
        "a": "Add a comment saying '// TODO: fix this later' and ignore it",
        "b": "Force push the changes directly to the main branch",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Straighten your shrimp posture and sigh deeply",
        "correct_key": "d"
    },
    {
        "question": "You are trying to review a coworker's pull request using Nginx, but your internet connection drops right in the middle. What is your next move?",
        "a": "Pretend your Slack is broken and go grab a coffee",
        "b": "Cry quietly in the nearest storage room or cafeteria",
        "c": "Delete your local repository and clone a fresh copy",
        "d": "Blame the newest engineering intern (even if you don't have one)",
        "correct_key": "d"
    },
    {
        "question": "You are trying to fix a memory leak using React, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Rewrite the entire backend module in Rust to feel better",
        "b": "Commit the changes, push, and immediately close your laptop",
        "c": "Blame the cloud hosting provider's regional server outage",
        "d": "Add a try-except block around the entire file and go to sleep",
        "correct_key": "b"
    },
    {
        "question": "You are trying to mock an external payment API using Kubernetes, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Spend three hours debating tabs vs spaces in the company Slack",
        "correct_key": "a"
    },
    {
        "question": "You are trying to mock an external payment API using Vim, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Increase the server instance size and pay AWS 4x more money",
        "d": "Tell the product owner that the feature requires more research",
        "correct_key": "a"
    },
    {
        "question": "You are trying to center a div in CSS using AWS, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Blame the newest engineering intern (even if you don't have one)",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Cry quietly in the nearest storage room or cafeteria",
        "d": "Delete your local repository and clone a fresh copy",
        "correct_key": "a"
    },
    {
        "question": "You are trying to review a coworker's pull request using Vim, but your laptop battery dies during the process. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "c"
    },
    {
        "question": "You are trying to mock an external payment API using C++, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Spend three hours debating tabs vs spaces in the company Slack",
        "correct_key": "a"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using C++, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Commit the changes, push, and immediately close your laptop",
        "b": "Blame the cloud hosting provider's regional server outage",
        "c": "Rewrite the entire backend module in Rust to feel better",
        "d": "Add a try-except block around the entire file and go to sleep",
        "correct_key": "a"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using Stack Overflow, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Blame the cloud hosting provider's regional server outage",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Add a try-except block around the entire file and go to sleep",
        "correct_key": "c"
    },
    {
        "question": "You are trying to deploy a hotfix using JavaScript, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "All of the above in random order",
        "correct_key": "d"
    },
    {
        "question": "You are trying to refactor a legacy module using AWS, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Take a 2-hour lunch break to clear your mind",
        "c": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "d": "Add a console.log statement every three lines to see what is happening",
        "correct_key": "a"
    },
    {
        "question": "You are trying to merge a pull request using Git, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Run a system reboot and hope it resolves itself",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to optimize a database query using React, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "All of the above in random order",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "Run `npm cache clean --force` and pray to the package gods",
        "correct_key": "a"
    },
    {
        "question": "You are trying to review a coworker's pull request using Kubernetes, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Rewrite the entire backend module in Rust to feel better",
        "b": "Add a try-except block around the entire file and go to sleep",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "c"
    },
    {
        "question": "You are trying to center a div in CSS using Git, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Delete your local repository and clone a fresh copy",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "c"
    },
    {
        "question": "You are trying to update a production database schema using Webpack, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Add the `!important` rule to 30 different lines of CSS styling",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "a"
    },
    {
        "question": "You are trying to audit the security dependencies using Node.js, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "c"
    },
    {
        "question": "You are trying to merge a pull request using Stack Overflow, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "Add a console.log statement every three lines to see what is happening",
        "b": "Take a 2-hour lunch break to clear your mind",
        "c": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "d": "Roll back to the last working build and hope nobody checked logs",
        "correct_key": "d"
    },
    {
        "question": "You are trying to optimize a database query using Django, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "b": "Roll back to the last working build and hope nobody checked logs",
        "c": "Take a 2-hour lunch break to clear your mind",
        "d": "Add a console.log statement every three lines to see what is happening",
        "correct_key": "b"
    },
    {
        "question": "You are trying to revert a bad merge using Vim, but your laptop battery dies during the process. What is your next move?",
        "a": "Delete `node_modules` and the package lockfile and rebuild",
        "b": "Run `npm cache clean --force` and pray to the package gods",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "All of the above in random order",
        "correct_key": "d"
    },
    {
        "question": "You are trying to center a div in CSS using Webpack, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Blame the newest engineering intern (even if you don't have one)",
        "b": "Delete your local repository and clone a fresh copy",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "a"
    },
    {
        "question": "You are trying to explain a complex regex pattern using Nginx, but your internet connection drops right in the middle. What is your next move?",
        "a": "All of the above in random order",
        "b": "Run `npm cache clean --force` and pray to the package gods",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "Delete `node_modules` and the package lockfile and rebuild",
        "correct_key": "a"
    },
    {
        "question": "You are trying to update a production database schema using Python, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Delete your local repository and clone a fresh copy",
        "correct_key": "c"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using Redis, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "c": "Take a 2-hour lunch break to clear your mind",
        "d": "Add a console.log statement every three lines to see what is happening",
        "correct_key": "a"
    },
    {
        "question": "You are trying to review a coworker's pull request using Node.js, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "All of the above in random order",
        "b": "Run `npm cache clean --force` and pray to the package gods",
        "c": "Delete `node_modules` and the package lockfile and rebuild",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "a"
    },
    {
        "question": "You are trying to merge a pull request using React, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "All of the above in random order",
        "b": "Tell the client that this is a feature, not a bug",
        "c": "Delete `node_modules` and the package lockfile and rebuild",
        "d": "Run `npm cache clean --force` and pray to the package gods",
        "correct_key": "a"
    },
    {
        "question": "You are trying to optimize a database query using Django, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Delete your local repository and clone a fresh copy",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Pretend your Slack is broken and go grab a coffee",
        "correct_key": "c"
    },
    {
        "question": "You are trying to optimize a database query using Node.js, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Spend three hours debating tabs vs spaces in the company Slack",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Remove all unit tests so the build pipeline succeeds",
        "d": "Tell the product owner that the feature requires more research",
        "correct_key": "c"
    },
    {
        "question": "You are trying to clean up the docker images using Webpack, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Take a 2-hour lunch break to clear your mind",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "a"
    },
    {
        "question": "You are trying to set up OAuth credentials using Jenkins, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Spend three hours debating tabs vs spaces in the company Slack",
        "b": "Tell the product owner that the feature requires more research",
        "c": "Increase the server instance size and pay AWS 4x more money",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to revert a bad merge using GitHub Actions, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Read the logs carefully and trace the exception stack",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "a"
    },
    {
        "question": "You are trying to containerize an application using Webpack, but the database suddenly disappears from the console. What is your next move?",
        "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "b": "Take a 2-hour lunch break to clear your mind",
        "c": "Add a console.log statement every three lines to see what is happening",
        "d": "Roll back to the last working build and hope nobody checked logs",
        "correct_key": "d"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using Kubernetes, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Spend three hours debating tabs vs spaces in the company Slack",
        "correct_key": "a"
    },
    {
        "question": "You are trying to install npm packages using Docker, but the database suddenly disappears from the console. What is your next move?",
        "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Take a 2-hour lunch break to clear your mind",
        "d": "Roll back to the last working build and hope nobody checked logs",
        "correct_key": "d"
    },
    {
        "question": "You are trying to write a unit test suite using Kubernetes, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Pretend your Slack is broken and go grab a coffee",
        "b": "Delete your local repository and clone a fresh copy",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "c"
    },
    {
        "question": "You are trying to run a database migration script using Django, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Run a system reboot and hope it resolves itself",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to install npm packages using Webpack, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Blame the cloud hosting provider's regional server outage",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Add a try-except block around the entire file and go to sleep",
        "correct_key": "c"
    },
    {
        "question": "You are trying to install npm packages using Webpack, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Delete `node_modules` and the package lockfile and rebuild",
        "b": "Run `npm cache clean --force` and pray to the package gods",
        "c": "All of the above in random order",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "c"
    },
    {
        "question": "You are trying to update a production database schema using Django, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Add a comment saying '// TODO: fix this later' and ignore it",
        "b": "Force push the changes directly to the main branch",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Straighten your shrimp posture and sigh deeply",
        "correct_key": "d"
    },
    {
        "question": "You are trying to fix a memory leak using TypeScript, but your laptop battery dies during the process. What is your next move?",
        "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "c"
    },
    {
        "question": "You are trying to audit the security dependencies using Kubernetes, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Force push the changes directly to the main branch",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Add a comment saying '// TODO: fix this later' and ignore it",
        "correct_key": "a"
    },
    {
        "question": "You are trying to fix a memory leak using Rust, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Tell the product owner that the feature requires more research",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Increase the server instance size and pay AWS 4x more money",
        "correct_key": "a"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using Redis, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Ask a question on Stack Overflow under an anonymous username",
        "b": "Force push the changes directly to the main branch",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Straighten your shrimp posture and sigh deeply",
        "correct_key": "d"
    },
    {
        "question": "You are trying to review a coworker's pull request using Kubectl, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to center a div in CSS using Jenkins, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Commit the changes, push, and immediately close your laptop",
        "b": "Add a try-except block around the entire file and go to sleep",
        "c": "Rewrite the entire backend module in Rust to feel better",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "a"
    },
    {
        "question": "You are trying to set up OAuth credentials using Node.js, but your internet connection drops right in the middle. What is your next move?",
        "a": "Blame the newest engineering intern (even if you don't have one)",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Delete your local repository and clone a fresh copy",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "a"
    },
    {
        "question": "You are trying to mock an external payment API using Stack Overflow, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Switch your theme to dark mode and hope the issue goes away",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "b"
    },
    {
        "question": "You are trying to write a script in Bash using C++, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Ask a question on Stack Overflow under an anonymous username",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Force push the changes directly to the main branch",
        "correct_key": "a"
    },
    {
        "question": "You are trying to update a production database schema using Kubernetes, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Ask a question on Stack Overflow under an anonymous username",
        "b": "Add a comment saying '// TODO: fix this later' and ignore it",
        "c": "Force push the changes directly to the main branch",
        "d": "Straighten your shrimp posture and sigh deeply",
        "correct_key": "d"
    },
    {
        "question": "You are trying to review a coworker's pull request using Nginx, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Add the `!important` rule to 30 different lines of CSS styling",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "b"
    },
    {
        "question": "You are trying to refactor a legacy module using Django, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "b"
    },
    {
        "question": "You are trying to reset the git branch using Stack Overflow, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Take a 2-hour lunch break to clear your mind",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "c"
    },
    {
        "question": "You are trying to refactor a legacy module using C++, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Blame the newest engineering intern (even if you don't have one)",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Delete your local repository and clone a fresh copy",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "a"
    },
    {
        "question": "You are trying to set up OAuth credentials using C++, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Take a 2-hour lunch break to clear your mind",
        "b": "Roll back to the last working build and hope nobody checked logs",
        "c": "Add a console.log statement every three lines to see what is happening",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "b"
    },
    {
        "question": "You are trying to deploy a hotfix using Kubectl, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Force push the changes directly to the main branch",
        "b": "Straighten your shrimp posture and sigh deeply",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Add a comment saying '// TODO: fix this later' and ignore it",
        "correct_key": "b"
    },
    {
        "question": "You are trying to install a dependency package using Jenkins, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "All of the above in random order",
        "b": "Run `npm cache clean --force` and pray to the package gods",
        "c": "Delete `node_modules` and the package lockfile and rebuild",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "a"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using React, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Delete your local repository and clone a fresh copy",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Blame the newest engineering intern (even if you don't have one)",
        "correct_key": "d"
    },
    {
        "question": "You are trying to write a unit test suite using PostgreSQL, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Commit the changes, push, and immediately close your laptop",
        "b": "Blame the cloud hosting provider's regional server outage",
        "c": "Add a try-except block around the entire file and go to sleep",
        "d": "Rewrite the entire backend module in Rust to feel better",
        "correct_key": "a"
    },
    {
        "question": "You are trying to mock an external payment API using Jenkins, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Add a comment saying '// TODO: fix this later' and ignore it",
        "b": "Ask a question on Stack Overflow under an anonymous username",
        "c": "Force push the changes directly to the main branch",
        "d": "Straighten your shrimp posture and sigh deeply",
        "correct_key": "d"
    },
    {
        "question": "You are trying to run a database migration script using Stack Overflow, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Ask a question on Stack Overflow under an anonymous username",
        "b": "Straighten your shrimp posture and sigh deeply",
        "c": "Force push the changes directly to the main branch",
        "d": "Add a comment saying '// TODO: fix this later' and ignore it",
        "correct_key": "b"
    },
    {
        "question": "You are trying to optimize a database query using HTML/CSS, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Force push the changes directly to the main branch",
        "b": "Add a comment saying '// TODO: fix this later' and ignore it",
        "c": "Straighten your shrimp posture and sigh deeply",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "c"
    },
    {
        "question": "You are trying to write a script in Bash using TypeScript, but the database suddenly disappears from the console. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Add the `!important` rule to 30 different lines of CSS styling",
        "c": "Run a system reboot and hope it resolves itself",
        "d": "Tell your manager that the sprint goals were unrealistic",
        "correct_key": "b"
    },
    {
        "question": "You are trying to review a coworker's pull request using C++, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Spend three hours debating tabs vs spaces in the company Slack",
        "b": "Remove all unit tests so the build pipeline succeeds",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Increase the server instance size and pay AWS 4x more money",
        "correct_key": "b"
    },
    {
        "question": "You are trying to run a database migration script using Nginx, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Run `npm cache clean --force` and pray to the package gods",
        "b": "All of the above in random order",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "Delete `node_modules` and the package lockfile and rebuild",
        "correct_key": "b"
    },
    {
        "question": "You are trying to reset the git branch using Rust, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Spend three hours debating tabs vs spaces in the company Slack",
        "b": "Tell the product owner that the feature requires more research",
        "c": "Remove all unit tests so the build pipeline succeeds",
        "d": "Increase the server instance size and pay AWS 4x more money",
        "correct_key": "c"
    },
    {
        "question": "You are trying to install a dependency package using Kubectl, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Spend three hours debating tabs vs spaces in the company Slack",
        "b": "Tell the product owner that the feature requires more research",
        "c": "Increase the server instance size and pay AWS 4x more money",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to install npm packages using Nginx, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Add the `!important` rule to 30 different lines of CSS styling",
        "c": "Run a system reboot and hope it resolves itself",
        "d": "Pretend you have a power outage and leave the Zoom meeting",
        "correct_key": "b"
    },
    {
        "question": "You are trying to optimize a database query using JavaScript, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Add a comment saying '// TODO: fix this later' and ignore it",
        "c": "Force push the changes directly to the main branch",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "a"
    },
    {
        "question": "You are trying to containerize an application using Docker, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Tell the product owner that the feature requires more research",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Increase the server instance size and pay AWS 4x more money",
        "correct_key": "a"
    },
    {
        "question": "You are trying to review a coworker's pull request using MongoDB, but your laptop battery dies during the process. What is your next move?",
        "a": "Delete your local repository and clone a fresh copy",
        "b": "Cry quietly in the nearest storage room or cafeteria",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Pretend your Slack is broken and go grab a coffee",
        "correct_key": "c"
    },
    {
        "question": "You are trying to write a unit test suite using Kubernetes, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "c"
    },
    {
        "question": "You are trying to install npm packages using Redis, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Add the `!important` rule to 30 different lines of CSS styling",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "a"
    },
    {
        "question": "You are trying to revert a bad merge using Rust, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Take a 2-hour lunch break to clear your mind",
        "b": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "c": "Add a console.log statement every three lines to see what is happening",
        "d": "Roll back to the last working build and hope nobody checked logs",
        "correct_key": "d"
    },
    {
        "question": "You are trying to deploy a hotfix using Vim, but the database suddenly disappears from the console. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Run a system reboot and hope it resolves itself",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Pretend you have a power outage and leave the Zoom meeting",
        "correct_key": "c"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using Kubectl, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Add the `!important` rule to 30 different lines of CSS styling",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Run a system reboot and hope it resolves itself",
        "d": "Tell your manager that the sprint goals were unrealistic",
        "correct_key": "a"
    },
    {
        "question": "You are trying to revert a bad merge using Kubectl, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Blame the cloud hosting provider's regional server outage",
        "b": "Commit the changes, push, and immediately close your laptop",
        "c": "Add a try-except block around the entire file and go to sleep",
        "d": "Rewrite the entire backend module in Rust to feel better",
        "correct_key": "b"
    },
    {
        "question": "You are trying to update a production database schema using PostgreSQL, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "b": "Take a 2-hour lunch break to clear your mind",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Add a console.log statement every three lines to see what is happening",
        "correct_key": "c"
    },
    {
        "question": "You are trying to refactor a legacy module using React, but the database suddenly disappears from the console. What is your next move?",
        "a": "Decline the ticket and reassign it to the senior team lead",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Switch your theme to dark mode and hope the issue goes away",
        "correct_key": "b"
    },
    {
        "question": "You are trying to ssh into the production server using HTML/CSS, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Increase the server instance size and pay AWS 4x more money",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to install npm packages using Django, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "Blame the newest engineering intern (even if you don't have one)",
        "b": "Cry quietly in the nearest storage room or cafeteria",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Delete your local repository and clone a fresh copy",
        "correct_key": "a"
    },
    {
        "question": "You are trying to deploy a hotfix using AWS, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Ask a question on Stack Overflow under an anonymous username",
        "b": "Straighten your shrimp posture and sigh deeply",
        "c": "Force push the changes directly to the main branch",
        "d": "Add a comment saying '// TODO: fix this later' and ignore it",
        "correct_key": "b"
    },
    {
        "question": "You are trying to reset the git branch using Django, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Add the `!important` rule to 30 different lines of CSS styling",
        "c": "Run a system reboot and hope it resolves itself",
        "d": "Tell your manager that the sprint goals were unrealistic",
        "correct_key": "b"
    },
    {
        "question": "You are trying to merge a pull request using Nginx, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Decline the ticket and reassign it to the senior team lead",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "a"
    },
    {
        "question": "You are trying to merge a pull request using Docker, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to set up OAuth credentials using Django, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Blame the newest engineering intern (even if you don't have one)",
        "c": "Delete your local repository and clone a fresh copy",
        "d": "Pretend your Slack is broken and go grab a coffee",
        "correct_key": "b"
    },
    {
        "question": "You are trying to merge a pull request using GitHub Actions, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Blame the cloud hosting provider's regional server outage",
        "b": "Add a try-except block around the entire file and go to sleep",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Rewrite the entire backend module in Rust to feel better",
        "correct_key": "c"
    },
    {
        "question": "You are trying to set up OAuth credentials using Redis, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "All of the above in random order",
        "c": "Delete `node_modules` and the package lockfile and rebuild",
        "d": "Run `npm cache clean --force` and pray to the package gods",
        "correct_key": "b"
    },
    {
        "question": "You are trying to audit the security dependencies using React, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Run a system reboot and hope it resolves itself",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to deploy a hotfix using Django, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "Run `npm cache clean --force` and pray to the package gods",
        "c": "All of the above in random order",
        "d": "Delete `node_modules` and the package lockfile and rebuild",
        "correct_key": "c"
    },
    {
        "question": "You are trying to clean up the docker images using Vim, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Blame the newest engineering intern (even if you don't have one)",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Delete your local repository and clone a fresh copy",
        "correct_key": "b"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using Kubectl, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "c"
    },
    {
        "question": "You are trying to explain a complex regex pattern using GitHub Actions, but the database suddenly disappears from the console. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Add the `!important` rule to 30 different lines of CSS styling",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Pretend you have a power outage and leave the Zoom meeting",
        "correct_key": "b"
    },
    {
        "question": "You are trying to review a coworker's pull request using AWS, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "Take a 2-hour lunch break to clear your mind",
        "b": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Add a console.log statement every three lines to see what is happening",
        "correct_key": "c"
    },
    {
        "question": "You are trying to write a script in Bash using C++, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Delete your local repository and clone a fresh copy",
        "d": "Blame the newest engineering intern (even if you don't have one)",
        "correct_key": "d"
    },
    {
        "question": "You are trying to clean up the docker images using Jenkins, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Commit the changes, push, and immediately close your laptop",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Add a try-except block around the entire file and go to sleep",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "a"
    },
    {
        "question": "You are trying to review a coworker's pull request using MongoDB, but your internet connection drops right in the middle. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Ask a question on Stack Overflow under an anonymous username",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Force push the changes directly to the main branch",
        "correct_key": "a"
    },
    {
        "question": "You are trying to mock an external payment API using TypeScript, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Force push the changes directly to the main branch",
        "b": "Add a comment saying '// TODO: fix this later' and ignore it",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Straighten your shrimp posture and sigh deeply",
        "correct_key": "d"
    },
    {
        "question": "You are trying to refactor a legacy module using Kubernetes, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Blame the cloud hosting provider's regional server outage",
        "c": "Rewrite the entire backend module in Rust to feel better",
        "d": "Commit the changes, push, and immediately close your laptop",
        "correct_key": "d"
    },
    {
        "question": "You are trying to write a unit test suite using JavaScript, but the database suddenly disappears from the console. What is your next move?",
        "a": "Run `npm cache clean --force` and pray to the package gods",
        "b": "All of the above in random order",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "Delete `node_modules` and the package lockfile and rebuild",
        "correct_key": "b"
    },
    {
        "question": "You are trying to fix a memory leak using Jenkins, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Add the `!important` rule to 30 different lines of CSS styling",
        "b": "Run a system reboot and hope it resolves itself",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Pretend you have a power outage and leave the Zoom meeting",
        "correct_key": "a"
    },
    {
        "question": "You are trying to reset the git branch using GitHub Actions, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Rewrite the entire backend module in Rust to feel better",
        "b": "Commit the changes, push, and immediately close your laptop",
        "c": "Add a try-except block around the entire file and go to sleep",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "b"
    },
    {
        "question": "You are trying to set up OAuth credentials using JavaScript, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Take a 2-hour lunch break to clear your mind",
        "b": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Add a console.log statement every three lines to see what is happening",
        "correct_key": "c"
    },
    {
        "question": "You are trying to fix a memory leak using Node.js, but your internet connection drops right in the middle. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "correct_key": "d"
    },
    {
        "question": "You are trying to merge a pull request using Kubectl, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Run a system reboot and hope it resolves itself",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to write a script in Bash using TypeScript, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "c"
    },
    {
        "question": "You are trying to optimize a database query using GitHub Actions, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Add a console.log statement every three lines to see what is happening",
        "b": "Take a 2-hour lunch break to clear your mind",
        "c": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "d": "Roll back to the last working build and hope nobody checked logs",
        "correct_key": "d"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using AWS, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to revert a bad merge using Vim, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Ask a question on Stack Overflow under an anonymous username",
        "c": "Force push the changes directly to the main branch",
        "d": "Add a comment saying '// TODO: fix this later' and ignore it",
        "correct_key": "a"
    },
    {
        "question": "You are trying to reset the git branch using Nginx, but your internet connection drops right in the middle. What is your next move?",
        "a": "Blame the newest engineering intern (even if you don't have one)",
        "b": "Cry quietly in the nearest storage room or cafeteria",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Delete your local repository and clone a fresh copy",
        "correct_key": "a"
    },
    {
        "question": "You are trying to revert a bad merge using Jenkins, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Decline the ticket and reassign it to the senior team lead",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Switch your theme to dark mode and hope the issue goes away",
        "correct_key": "a"
    },
    {
        "question": "You are trying to write a unit test suite using TypeScript, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to optimize a database query using HTML/CSS, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Take a 2-hour lunch break to clear your mind",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "d": "Roll back to the last working build and hope nobody checked logs",
        "correct_key": "d"
    },
    {
        "question": "You are trying to install npm packages using Docker, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Add the `!important` rule to 30 different lines of CSS styling",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Run a system reboot and hope it resolves itself",
        "d": "Pretend you have a power outage and leave the Zoom meeting",
        "correct_key": "a"
    },
    {
        "question": "You are trying to containerize an application using Node.js, but the database suddenly disappears from the console. What is your next move?",
        "a": "Delete your local repository and clone a fresh copy",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "c"
    },
    {
        "question": "You are trying to mock an external payment API using Node.js, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "b": "Take a 2-hour lunch break to clear your mind",
        "c": "Add a console.log statement every three lines to see what is happening",
        "d": "Roll back to the last working build and hope nobody checked logs",
        "correct_key": "d"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using C++, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Commit the changes, push, and immediately close your laptop",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Blame the cloud hosting provider's regional server outage",
        "d": "Add a try-except block around the entire file and go to sleep",
        "correct_key": "a"
    },
    {
        "question": "You are trying to refactor a legacy module using Django, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Increase the server instance size and pay AWS 4x more money",
        "b": "Tell the product owner that the feature requires more research",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to fix a memory leak using React, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "All of the above in random order",
        "d": "Run `npm cache clean --force` and pray to the package gods",
        "correct_key": "c"
    },
    {
        "question": "You are trying to set up OAuth credentials using Kubectl, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "c"
    },
    {
        "question": "You are trying to clean up the docker images using Docker, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Add a comment saying '// TODO: fix this later' and ignore it",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Force push the changes directly to the main branch",
        "correct_key": "a"
    },
    {
        "question": "You are trying to mock an external payment API using TypeScript, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Add a console.log statement every three lines to see what is happening",
        "b": "Roll back to the last working build and hope nobody checked logs",
        "c": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "b"
    },
    {
        "question": "You are trying to install npm packages using Kubernetes, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Force push the changes directly to the main branch",
        "b": "Add a comment saying '// TODO: fix this later' and ignore it",
        "c": "Straighten your shrimp posture and sigh deeply",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "c"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using Kubectl, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Take a 2-hour lunch break to clear your mind",
        "b": "Roll back to the last working build and hope nobody checked logs",
        "c": "Add a console.log statement every three lines to see what is happening",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "b"
    },
    {
        "question": "You are trying to set up OAuth credentials using AWS, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Delete your local repository and clone a fresh copy",
        "b": "Cry quietly in the nearest storage room or cafeteria",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Pretend your Slack is broken and go grab a coffee",
        "correct_key": "c"
    },
    {
        "question": "You are trying to deploy a hotfix using Python, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Add the `!important` rule to 30 different lines of CSS styling",
        "c": "Run a system reboot and hope it resolves itself",
        "d": "Tell your manager that the sprint goals were unrealistic",
        "correct_key": "b"
    },
    {
        "question": "You are trying to reset the git branch using PostgreSQL, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Switch your theme to dark mode and hope the issue goes away",
        "correct_key": "b"
    },
    {
        "question": "You are trying to audit the security dependencies using TypeScript, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "correct_key": "d"
    },
    {
        "question": "You are trying to audit the security dependencies using GitHub Actions, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Blame the newest engineering intern (even if you don't have one)",
        "b": "Delete your local repository and clone a fresh copy",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "a"
    },
    {
        "question": "You are trying to revert a bad merge using C++, but your internet connection drops right in the middle. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "a"
    },
    {
        "question": "You are trying to audit the security dependencies using Kubernetes, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "b"
    },
    {
        "question": "You are trying to write a unit test suite using Python, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Ask a question on Stack Overflow under an anonymous username",
        "b": "Straighten your shrimp posture and sigh deeply",
        "c": "Force push the changes directly to the main branch",
        "d": "Add a comment saying '// TODO: fix this later' and ignore it",
        "correct_key": "b"
    },
    {
        "question": "You are trying to review a coworker's pull request using Redis, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Blame the newest engineering intern (even if you don't have one)",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Cry quietly in the nearest storage room or cafeteria",
        "d": "Delete your local repository and clone a fresh copy",
        "correct_key": "a"
    },
    {
        "question": "You are trying to install a dependency package using React, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Increase the server instance size and pay AWS 4x more money",
        "correct_key": "a"
    },
    {
        "question": "You are trying to deploy a hotfix using Kubectl, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "c": "Take a 2-hour lunch break to clear your mind",
        "d": "Add a console.log statement every three lines to see what is happening",
        "correct_key": "a"
    },
    {
        "question": "You are trying to run a database migration script using Kubernetes, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "a"
    },
    {
        "question": "You are trying to explain a complex regex pattern using HTML/CSS, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Add the `!important` rule to 30 different lines of CSS styling",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "a"
    },
    {
        "question": "You are trying to center a div in CSS using Webpack, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Ask a question on Stack Overflow under an anonymous username",
        "b": "Force push the changes directly to the main branch",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Straighten your shrimp posture and sigh deeply",
        "correct_key": "d"
    },
    {
        "question": "You are trying to update a production database schema using Node.js, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Tell the product owner that the feature requires more research",
        "correct_key": "a"
    },
    {
        "question": "You are trying to install npm packages using C++, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Take a 2-hour lunch break to clear your mind",
        "c": "Add a console.log statement every three lines to see what is happening",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "a"
    },
    {
        "question": "You are trying to refactor a legacy module using MongoDB, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Add a comment saying '// TODO: fix this later' and ignore it",
        "b": "Straighten your shrimp posture and sigh deeply",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Force push the changes directly to the main branch",
        "correct_key": "b"
    },
    {
        "question": "You are trying to refactor a legacy module using Vim, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Blame the cloud hosting provider's regional server outage",
        "b": "Commit the changes, push, and immediately close your laptop",
        "c": "Rewrite the entire backend module in Rust to feel better",
        "d": "Add a try-except block around the entire file and go to sleep",
        "correct_key": "b"
    },
    {
        "question": "You are trying to merge a pull request using Redis, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Read the logs carefully and trace the exception stack",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Switch your theme to dark mode and hope the issue goes away",
        "correct_key": "a"
    },
    {
        "question": "You are trying to optimize a database query using Python, but your internet connection drops right in the middle. What is your next move?",
        "a": "All of the above in random order",
        "b": "Tell the client that this is a feature, not a bug",
        "c": "Delete `node_modules` and the package lockfile and rebuild",
        "d": "Run `npm cache clean --force` and pray to the package gods",
        "correct_key": "a"
    },
    {
        "question": "You are trying to review a coworker's pull request using Redis, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Delete your local repository and clone a fresh copy",
        "b": "Cry quietly in the nearest storage room or cafeteria",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Pretend your Slack is broken and go grab a coffee",
        "correct_key": "c"
    },
    {
        "question": "You are trying to containerize an application using JavaScript, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "c"
    },
    {
        "question": "You are trying to refactor a legacy module using Node.js, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Delete your local repository and clone a fresh copy",
        "d": "Blame the newest engineering intern (even if you don't have one)",
        "correct_key": "d"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using Node.js, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Add a comment saying '// TODO: fix this later' and ignore it",
        "b": "Force push the changes directly to the main branch",
        "c": "Straighten your shrimp posture and sigh deeply",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "c"
    },
    {
        "question": "You are trying to optimize a database query using C++, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "b": "Roll back to the last working build and hope nobody checked logs",
        "c": "Take a 2-hour lunch break to clear your mind",
        "d": "Add a console.log statement every three lines to see what is happening",
        "correct_key": "b"
    },
    {
        "question": "You are trying to clean up the docker images using Docker, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "Blame the newest engineering intern (even if you don't have one)",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Delete your local repository and clone a fresh copy",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "a"
    },
    {
        "question": "You are trying to fix a memory leak using Node.js, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "correct_key": "d"
    },
    {
        "question": "You are trying to set up OAuth credentials using JavaScript, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Add the `!important` rule to 30 different lines of CSS styling",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "b"
    },
    {
        "question": "You are trying to run a database migration script using Node.js, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "Tell the product owner that the feature requires more research",
        "b": "Remove all unit tests so the build pipeline succeeds",
        "c": "Increase the server instance size and pay AWS 4x more money",
        "d": "Spend three hours debating tabs vs spaces in the company Slack",
        "correct_key": "b"
    },
    {
        "question": "You are trying to set up OAuth credentials using MongoDB, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Switch your theme to dark mode and hope the issue goes away",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "b"
    },
    {
        "question": "You are trying to ssh into the production server using Rust, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Pretend you have a power outage and leave the Zoom meeting",
        "correct_key": "c"
    },
    {
        "question": "You are trying to write a unit test suite using TypeScript, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Blame the cloud hosting provider's regional server outage",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Add a try-except block around the entire file and go to sleep",
        "correct_key": "c"
    },
    {
        "question": "You are trying to optimize a database query using TypeScript, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Tell the product owner that the feature requires more research",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to install npm packages using JavaScript, but your internet connection drops right in the middle. What is your next move?",
        "a": "Add a comment saying '// TODO: fix this later' and ignore it",
        "b": "Force push the changes directly to the main branch",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Straighten your shrimp posture and sigh deeply",
        "correct_key": "d"
    },
    {
        "question": "You are trying to update a production database schema using HTML/CSS, but your internet connection drops right in the middle. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "c": "Take a 2-hour lunch break to clear your mind",
        "d": "Add a console.log statement every three lines to see what is happening",
        "correct_key": "a"
    },
    {
        "question": "You are trying to explain a complex regex pattern using React, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Blame the newest engineering intern (even if you don't have one)",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Cry quietly in the nearest storage room or cafeteria",
        "d": "Delete your local repository and clone a fresh copy",
        "correct_key": "a"
    },
    {
        "question": "You are trying to update a production database schema using Rust, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Delete your local repository and clone a fresh copy",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Pretend your Slack is broken and go grab a coffee",
        "correct_key": "c"
    },
    {
        "question": "You are trying to containerize an application using TypeScript, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Force push the changes directly to the main branch",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Add a comment saying '// TODO: fix this later' and ignore it",
        "correct_key": "a"
    },
    {
        "question": "You are trying to merge a pull request using Docker, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Run a system reboot and hope it resolves itself",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to run a database migration script using Vim, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Force push the changes directly to the main branch",
        "b": "Ask a question on Stack Overflow under an anonymous username",
        "c": "Straighten your shrimp posture and sigh deeply",
        "d": "Add a comment saying '// TODO: fix this later' and ignore it",
        "correct_key": "c"
    },
    {
        "question": "You are trying to update a production database schema using Webpack, but your internet connection drops right in the middle. What is your next move?",
        "a": "Run `npm cache clean --force` and pray to the package gods",
        "b": "Tell the client that this is a feature, not a bug",
        "c": "Delete `node_modules` and the package lockfile and rebuild",
        "d": "All of the above in random order",
        "correct_key": "d"
    },
    {
        "question": "You are trying to install npm packages using GitHub Actions, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Increase the server instance size and pay AWS 4x more money",
        "b": "Tell the product owner that the feature requires more research",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to deploy a hotfix using Kubernetes, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Tell the product owner that the feature requires more research",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Remove all unit tests so the build pipeline succeeds",
        "d": "Spend three hours debating tabs vs spaces in the company Slack",
        "correct_key": "c"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using JavaScript, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Add a console.log statement every three lines to see what is happening",
        "b": "Take a 2-hour lunch break to clear your mind",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "c"
    },
    {
        "question": "You are trying to fix a memory leak using Docker, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Increase the server instance size and pay AWS 4x more money",
        "b": "Tell the product owner that the feature requires more research",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to run a database migration script using Node.js, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Tell the product owner that the feature requires more research",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Remove all unit tests so the build pipeline succeeds",
        "d": "Spend three hours debating tabs vs spaces in the company Slack",
        "correct_key": "c"
    },
    {
        "question": "You are trying to write a unit test suite using MongoDB, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Delete your local repository and clone a fresh copy",
        "correct_key": "c"
    },
    {
        "question": "You are trying to center a div in CSS using React, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "c"
    },
    {
        "question": "You are trying to explain a complex regex pattern using Kubectl, but the database suddenly disappears from the console. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Add the `!important` rule to 30 different lines of CSS styling",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "b"
    },
    {
        "question": "You are trying to install a dependency package using Kubectl, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Decline the ticket and reassign it to the senior team lead",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "b"
    },
    {
        "question": "You are trying to revert a bad merge using Stack Overflow, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Tell the product owner that the feature requires more research",
        "c": "Increase the server instance size and pay AWS 4x more money",
        "d": "Spend three hours debating tabs vs spaces in the company Slack",
        "correct_key": "a"
    },
    {
        "question": "You are trying to reset the git branch using AWS, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Blame the newest engineering intern (even if you don't have one)",
        "b": "Cry quietly in the nearest storage room or cafeteria",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Delete your local repository and clone a fresh copy",
        "correct_key": "a"
    },
    {
        "question": "You are trying to refactor a legacy module using PostgreSQL, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Take a 2-hour lunch break to clear your mind",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "a"
    },
    {
        "question": "You are trying to update a production database schema using MongoDB, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Add a comment saying '// TODO: fix this later' and ignore it",
        "b": "Force push the changes directly to the main branch",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Straighten your shrimp posture and sigh deeply",
        "correct_key": "d"
    },
    {
        "question": "You are trying to explain a complex regex pattern using Redis, but the database suddenly disappears from the console. What is your next move?",
        "a": "Rewrite the entire backend module in Rust to feel better",
        "b": "Blame the cloud hosting provider's regional server outage",
        "c": "Add a try-except block around the entire file and go to sleep",
        "d": "Commit the changes, push, and immediately close your laptop",
        "correct_key": "d"
    },
    {
        "question": "You are trying to fix a memory leak using React, but your internet connection drops right in the middle. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Tell the product owner that the feature requires more research",
        "correct_key": "a"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using TypeScript, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Force push the changes directly to the main branch",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "a"
    },
    {
        "question": "You are trying to update a production database schema using Django, but your internet connection drops right in the middle. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Add a comment saying '// TODO: fix this later' and ignore it",
        "c": "Force push the changes directly to the main branch",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "a"
    },
    {
        "question": "You are trying to explain a complex regex pattern using Django, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Take a 2-hour lunch break to clear your mind",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "c"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using Redis, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Tell the product owner that the feature requires more research",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Increase the server instance size and pay AWS 4x more money",
        "correct_key": "a"
    },
    {
        "question": "You are trying to audit the security dependencies using Webpack, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Tell the product owner that the feature requires more research",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to deploy a hotfix using Kubectl, but your internet connection drops right in the middle. What is your next move?",
        "a": "Blame the newest engineering intern (even if you don't have one)",
        "b": "Delete your local repository and clone a fresh copy",
        "c": "Cry quietly in the nearest storage room or cafeteria",
        "d": "Pretend your Slack is broken and go grab a coffee",
        "correct_key": "a"
    },
    {
        "question": "You are trying to center a div in CSS using Webpack, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Commit the changes, push, and immediately close your laptop",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Add a try-except block around the entire file and go to sleep",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "a"
    },
    {
        "question": "You are trying to run a database migration script using GitHub Actions, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Delete `node_modules` and the package lockfile and rebuild",
        "b": "All of the above in random order",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "b"
    },
    {
        "question": "You are trying to write a script in Bash using Docker, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Increase the server instance size and pay AWS 4x more money",
        "d": "Tell the product owner that the feature requires more research",
        "correct_key": "a"
    },
    {
        "question": "You are trying to optimize a database query using Redis, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Add the `!important` rule to 30 different lines of CSS styling",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Tell your manager that the sprint goals were unrealistic",
        "correct_key": "b"
    },
    {
        "question": "You are trying to refactor a legacy module using C++, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Blame the cloud hosting provider's regional server outage",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Add a try-except block around the entire file and go to sleep",
        "d": "Commit the changes, push, and immediately close your laptop",
        "correct_key": "d"
    },
    {
        "question": "You are trying to clean up the docker images using HTML/CSS, but your laptop battery dies during the process. What is your next move?",
        "a": "Run `npm cache clean --force` and pray to the package gods",
        "b": "All of the above in random order",
        "c": "Delete `node_modules` and the package lockfile and rebuild",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "b"
    },
    {
        "question": "You are trying to deploy a hotfix using TypeScript, but your internet connection drops right in the middle. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "c"
    },
    {
        "question": "You are trying to refactor a legacy module using Vim, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Tell your manager that the sprint goals were unrealistic",
        "correct_key": "c"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using Django, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Blame the cloud hosting provider's regional server outage",
        "b": "Commit the changes, push, and immediately close your laptop",
        "c": "Rewrite the entire backend module in Rust to feel better",
        "d": "Add a try-except block around the entire file and go to sleep",
        "correct_key": "b"
    },
    {
        "question": "You are trying to audit the security dependencies using React, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Run `npm cache clean --force` and pray to the package gods",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "All of the above in random order",
        "correct_key": "d"
    },
    {
        "question": "You are trying to reset the git branch using Jenkins, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Spend three hours debating tabs vs spaces in the company Slack",
        "correct_key": "a"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using Stack Overflow, but your internet connection drops right in the middle. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Force push the changes directly to the main branch",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "a"
    },
    {
        "question": "You are trying to install npm packages using MongoDB, but your internet connection drops right in the middle. What is your next move?",
        "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "c"
    },
    {
        "question": "You are trying to mock an external payment API using C++, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Switch your theme to dark mode and hope the issue goes away",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "b"
    },
    {
        "question": "You are trying to run a database migration script using GitHub Actions, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "Run `npm cache clean --force` and pray to the package gods",
        "c": "All of the above in random order",
        "d": "Delete `node_modules` and the package lockfile and rebuild",
        "correct_key": "c"
    },
    {
        "question": "You are trying to containerize an application using MongoDB, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "All of the above in random order",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "Delete `node_modules` and the package lockfile and rebuild",
        "correct_key": "b"
    },
    {
        "question": "You are trying to write a unit test suite using Nginx, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Tell the product owner that the feature requires more research",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Increase the server instance size and pay AWS 4x more money",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to update a production database schema using GitHub Actions, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Switch your theme to dark mode and hope the issue goes away",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "b"
    },
    {
        "question": "You are trying to write a unit test suite using PostgreSQL, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Add the `!important` rule to 30 different lines of CSS styling",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Run a system reboot and hope it resolves itself",
        "d": "Pretend you have a power outage and leave the Zoom meeting",
        "correct_key": "a"
    },
    {
        "question": "You are trying to explain a complex regex pattern using Kubectl, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Decline the ticket and reassign it to the senior team lead",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "correct_key": "d"
    },
    {
        "question": "You are trying to fix a memory leak using Nginx, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "a"
    },
    {
        "question": "You are trying to install npm packages using Node.js, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Increase the server instance size and pay AWS 4x more money",
        "d": "Tell the product owner that the feature requires more research",
        "correct_key": "a"
    },
    {
        "question": "You are trying to install a dependency package using JavaScript, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "correct_key": "d"
    },
    {
        "question": "You are trying to reset the git branch using HTML/CSS, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Force push the changes directly to the main branch",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Add a comment saying '// TODO: fix this later' and ignore it",
        "correct_key": "a"
    },
    {
        "question": "You are trying to merge a pull request using Django, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "All of the above in random order",
        "b": "Tell the client that this is a feature, not a bug",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "Delete `node_modules` and the package lockfile and rebuild",
        "correct_key": "a"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using Docker, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "All of the above in random order",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "a"
    },
    {
        "question": "You are trying to set up OAuth credentials using Rust, but the database suddenly disappears from the console. What is your next move?",
        "a": "Pretend your Slack is broken and go grab a coffee",
        "b": "Blame the newest engineering intern (even if you don't have one)",
        "c": "Delete your local repository and clone a fresh copy",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "b"
    },
    {
        "question": "You are trying to center a div in CSS using Jenkins, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Delete your local repository and clone a fresh copy",
        "b": "Blame the newest engineering intern (even if you don't have one)",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "b"
    },
    {
        "question": "You are trying to mock an external payment API using React, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "Ask a question on Stack Overflow under an anonymous username",
        "b": "Force push the changes directly to the main branch",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Straighten your shrimp posture and sigh deeply",
        "correct_key": "d"
    },
    {
        "question": "You are trying to center a div in CSS using Node.js, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Spend three hours debating tabs vs spaces in the company Slack",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to update a production database schema using Nginx, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Commit the changes, push, and immediately close your laptop",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Add a try-except block around the entire file and go to sleep",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "a"
    },
    {
        "question": "You are trying to revert a bad merge using Node.js, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Run `npm cache clean --force` and pray to the package gods",
        "b": "All of the above in random order",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "Delete `node_modules` and the package lockfile and rebuild",
        "correct_key": "b"
    },
    {
        "question": "You are trying to reset the git branch using Docker, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Add the `!important` rule to 30 different lines of CSS styling",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "b"
    },
    {
        "question": "You are trying to optimize a database query using Docker, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Increase the server instance size and pay AWS 4x more money",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to optimize a database query using Nginx, but the database suddenly disappears from the console. What is your next move?",
        "a": "Rewrite the entire backend module in Rust to feel better",
        "b": "Add a try-except block around the entire file and go to sleep",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "c"
    },
    {
        "question": "You are trying to write a unit test suite using Webpack, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Delete your local repository and clone a fresh copy",
        "d": "Blame the newest engineering intern (even if you don't have one)",
        "correct_key": "d"
    },
    {
        "question": "You are trying to update a production database schema using Nginx, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Tell the product owner that the feature requires more research",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to refactor a legacy module using Redis, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Switch your theme to dark mode and hope the issue goes away",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "b"
    },
    {
        "question": "You are trying to install a dependency package using PostgreSQL, but your internet connection drops right in the middle. What is your next move?",
        "a": "Ask a question on Stack Overflow under an anonymous username",
        "b": "Add a comment saying '// TODO: fix this later' and ignore it",
        "c": "Straighten your shrimp posture and sigh deeply",
        "d": "Force push the changes directly to the main branch",
        "correct_key": "c"
    },
    {
        "question": "You are trying to write a script in Bash using TypeScript, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Decline the ticket and reassign it to the senior team lead",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "b"
    },
    {
        "question": "You are trying to audit the security dependencies using Python, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "b": "Roll back to the last working build and hope nobody checked logs",
        "c": "Add a console.log statement every three lines to see what is happening",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "b"
    },
    {
        "question": "You are trying to install a dependency package using Python, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Tell your manager that the sprint goals were unrealistic",
        "correct_key": "c"
    },
    {
        "question": "You are trying to center a div in CSS using Redis, but your internet connection drops right in the middle. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Delete your local repository and clone a fresh copy",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Blame the newest engineering intern (even if you don't have one)",
        "correct_key": "d"
    },
    {
        "question": "You are trying to explain a complex regex pattern using C++, but your laptop battery dies during the process. What is your next move?",
        "a": "Add a comment saying '// TODO: fix this later' and ignore it",
        "b": "Force push the changes directly to the main branch",
        "c": "Straighten your shrimp posture and sigh deeply",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "c"
    },
    {
        "question": "You are trying to refactor a legacy module using GitHub Actions, but your internet connection drops right in the middle. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "All of the above in random order",
        "correct_key": "d"
    },
    {
        "question": "You are trying to deploy a hotfix using AWS, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Delete `node_modules` and the package lockfile and rebuild",
        "b": "Tell the client that this is a feature, not a bug",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "All of the above in random order",
        "correct_key": "d"
    },
    {
        "question": "You are trying to install npm packages using AWS, but your internet connection drops right in the middle. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Read the logs carefully and trace the exception stack",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Switch your theme to dark mode and hope the issue goes away",
        "correct_key": "a"
    },
    {
        "question": "You are trying to clean up the docker images using Webpack, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Decline the ticket and reassign it to the senior team lead",
        "c": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "d": "Switch your theme to dark mode and hope the issue goes away",
        "correct_key": "c"
    },
    {
        "question": "You are trying to set up OAuth credentials using Kubectl, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Blame the cloud hosting provider's regional server outage",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Add a try-except block around the entire file and go to sleep",
        "d": "Commit the changes, push, and immediately close your laptop",
        "correct_key": "d"
    },
    {
        "question": "You are trying to mock an external payment API using PostgreSQL, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Switch your theme to dark mode and hope the issue goes away",
        "b": "Decline the ticket and reassign it to the senior team lead",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "correct_key": "d"
    },
    {
        "question": "You are trying to optimize a database query using Stack Overflow, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Decline the ticket and reassign it to the senior team lead",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Switch your theme to dark mode and hope the issue goes away",
        "correct_key": "a"
    },
    {
        "question": "You are trying to audit the security dependencies using PostgreSQL, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Switch your theme to dark mode and hope the issue goes away",
        "b": "Read the logs carefully and trace the exception stack",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "correct_key": "d"
    },
    {
        "question": "You are trying to review a coworker's pull request using Django, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Run `npm cache clean --force` and pray to the package gods",
        "b": "All of the above in random order",
        "c": "Delete `node_modules` and the package lockfile and rebuild",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "b"
    },
    {
        "question": "You are trying to refactor a legacy module using GitHub Actions, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Increase the server instance size and pay AWS 4x more money",
        "b": "Remove all unit tests so the build pipeline succeeds",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Spend three hours debating tabs vs spaces in the company Slack",
        "correct_key": "b"
    },
    {
        "question": "You are trying to write a script in Bash using Django, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "c"
    },
    {
        "question": "You are trying to audit the security dependencies using MongoDB, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "All of the above in random order",
        "correct_key": "d"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using C++, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Delete your local repository and clone a fresh copy",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Pretend your Slack is broken and go grab a coffee",
        "correct_key": "c"
    },
    {
        "question": "You are trying to scale the Kubernetes cluster using TypeScript, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "b": "Roll back to the last working build and hope nobody checked logs",
        "c": "Take a 2-hour lunch break to clear your mind",
        "d": "Add a console.log statement every three lines to see what is happening",
        "correct_key": "b"
    },
    {
        "question": "You are trying to revert a bad merge using Webpack, but your laptop battery dies during the process. What is your next move?",
        "a": "Rewrite the entire backend module in Rust to feel better",
        "b": "Commit the changes, push, and immediately close your laptop",
        "c": "Add a try-except block around the entire file and go to sleep",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "b"
    },
    {
        "question": "You are trying to reset the git branch using Redis, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Ask a question on Stack Overflow under an anonymous username",
        "b": "Force push the changes directly to the main branch",
        "c": "Straighten your shrimp posture and sigh deeply",
        "d": "Add a comment saying '// TODO: fix this later' and ignore it",
        "correct_key": "c"
    },
    {
        "question": "You are trying to optimize a database query using Jenkins, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Spend three hours debating tabs vs spaces in the company Slack",
        "b": "Remove all unit tests so the build pipeline succeeds",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Increase the server instance size and pay AWS 4x more money",
        "correct_key": "b"
    },
    {
        "question": "You are trying to merge a pull request using C++, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Spend three hours debating tabs vs spaces in the company Slack",
        "correct_key": "a"
    },
    {
        "question": "You are trying to revert a bad merge using Redis, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Commit the changes, push, and immediately close your laptop",
        "c": "Rewrite the entire backend module in Rust to feel better",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "b"
    },
    {
        "question": "You are trying to install npm packages using React, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Run a system reboot and hope it resolves itself",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to install npm packages using Webpack, but the database suddenly disappears from the console. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Increase the server instance size and pay AWS 4x more money",
        "d": "Tell the product owner that the feature requires more research",
        "correct_key": "a"
    },
    {
        "question": "You are trying to mock an external payment API using Nginx, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Tell your manager that the sprint goals were unrealistic",
        "correct_key": "c"
    },
    {
        "question": "You are trying to containerize an application using Git, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Blame the newest engineering intern (even if you don't have one)",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Delete your local repository and clone a fresh copy",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "a"
    },
    {
        "question": "You are trying to fix a memory leak using Vim, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Delete your local repository and clone a fresh copy",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Pretend your Slack is broken and go grab a coffee",
        "correct_key": "c"
    },
    {
        "question": "You are trying to reset the git branch using Docker, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Spend three hours debating tabs vs spaces in the company Slack",
        "b": "Remove all unit tests so the build pipeline succeeds",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Increase the server instance size and pay AWS 4x more money",
        "correct_key": "b"
    },
    {
        "question": "You are trying to fix a memory leak using Nginx, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Add a comment saying '// TODO: fix this later' and ignore it",
        "b": "Ask a question on Stack Overflow under an anonymous username",
        "c": "Force push the changes directly to the main branch",
        "d": "Straighten your shrimp posture and sigh deeply",
        "correct_key": "d"
    },
    {
        "question": "You are trying to refactor a legacy module using Node.js, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Run a system reboot and hope it resolves itself",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Tell your manager that the sprint goals were unrealistic",
        "correct_key": "c"
    },
    {
        "question": "You are trying to review a coworker's pull request using Stack Overflow, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Add the `!important` rule to 30 different lines of CSS styling",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Pretend you have a power outage and leave the Zoom meeting",
        "correct_key": "b"
    },
    {
        "question": "You are trying to explain a complex regex pattern using Kubernetes, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Ask a question on Stack Overflow under an anonymous username",
        "b": "Straighten your shrimp posture and sigh deeply",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Force push the changes directly to the main branch",
        "correct_key": "b"
    },
    {
        "question": "You are trying to set up OAuth credentials using Kubectl, but your laptop battery dies during the process. What is your next move?",
        "a": "Add a comment saying '// TODO: fix this later' and ignore it",
        "b": "Ask a question on Stack Overflow under an anonymous username",
        "c": "Straighten your shrimp posture and sigh deeply",
        "d": "Force push the changes directly to the main branch",
        "correct_key": "c"
    },
    {
        "question": "You are trying to reset the git branch using Stack Overflow, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Force push the changes directly to the main branch",
        "b": "Straighten your shrimp posture and sigh deeply",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "b"
    },
    {
        "question": "You are trying to write a script in Bash using Rust, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Commit the changes, push, and immediately close your laptop",
        "c": "Blame the cloud hosting provider's regional server outage",
        "d": "Rewrite the entire backend module in Rust to feel better",
        "correct_key": "b"
    },
    {
        "question": "You are trying to write a unit test suite using TypeScript, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Run a system reboot and hope it resolves itself",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to reset the git branch using Stack Overflow, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "All of the above in random order",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "Run `npm cache clean --force` and pray to the package gods",
        "correct_key": "a"
    },
    {
        "question": "You are trying to install npm packages using Kubectl, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Decline the ticket and reassign it to the senior team lead",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Switch your theme to dark mode and hope the issue goes away",
        "correct_key": "a"
    },
    {
        "question": "You are trying to install a dependency package using PostgreSQL, but the database suddenly disappears from the console. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Add the `!important` rule to 30 different lines of CSS styling",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Pretend you have a power outage and leave the Zoom meeting",
        "correct_key": "b"
    },
    {
        "question": "You are trying to run a database migration script using Git, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Tell the client that this is a feature, not a bug",
        "b": "Run `npm cache clean --force` and pray to the package gods",
        "c": "Delete `node_modules` and the package lockfile and rebuild",
        "d": "All of the above in random order",
        "correct_key": "d"
    },
    {
        "question": "You are trying to revert a bad merge using PostgreSQL, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Rewrite the entire backend module in Rust to feel better",
        "b": "Blame the cloud hosting provider's regional server outage",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Add a try-except block around the entire file and go to sleep",
        "correct_key": "c"
    },
    {
        "question": "You are trying to install npm packages using Django, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Blame the cloud hosting provider's regional server outage",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Add a try-except block around the entire file and go to sleep",
        "d": "Commit the changes, push, and immediately close your laptop",
        "correct_key": "d"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using Docker, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Tell the product owner that the feature requires more research",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Remove all unit tests so the build pipeline succeeds",
        "d": "Spend three hours debating tabs vs spaces in the company Slack",
        "correct_key": "c"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using MongoDB, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Commit the changes, push, and immediately close your laptop",
        "b": "Blame the cloud hosting provider's regional server outage",
        "c": "Rewrite the entire backend module in Rust to feel better",
        "d": "Add a try-except block around the entire file and go to sleep",
        "correct_key": "a"
    },
    {
        "question": "You are trying to refactor a legacy module using Redis, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Run `npm cache clean --force` and pray to the package gods",
        "b": "Tell the client that this is a feature, not a bug",
        "c": "Delete `node_modules` and the package lockfile and rebuild",
        "d": "All of the above in random order",
        "correct_key": "d"
    },
    {
        "question": "You are trying to write a script in Bash using Webpack, but your internet connection drops right in the middle. What is your next move?",
        "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Take a 2-hour lunch break to clear your mind",
        "d": "Roll back to the last working build and hope nobody checked logs",
        "correct_key": "d"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using Nginx, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Delete `node_modules` and the package lockfile and rebuild",
        "b": "Run `npm cache clean --force` and pray to the package gods",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "All of the above in random order",
        "correct_key": "d"
    },
    {
        "question": "You are trying to center a div in CSS using Nginx, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Blame the cloud hosting provider's regional server outage",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Rewrite the entire backend module in Rust to feel better",
        "correct_key": "c"
    },
    {
        "question": "You are trying to reset the git branch using Webpack, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Run a system reboot and hope it resolves itself",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to reset the git branch using GitHub Actions, but the database suddenly disappears from the console. What is your next move?",
        "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Take a 2-hour lunch break to clear your mind",
        "d": "Roll back to the last working build and hope nobody checked logs",
        "correct_key": "d"
    },
    {
        "question": "You are trying to set up OAuth credentials using C++, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "c": "Take a 2-hour lunch break to clear your mind",
        "d": "Add a console.log statement every three lines to see what is happening",
        "correct_key": "a"
    },
    {
        "question": "You are trying to audit the security dependencies using Vim, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Add a comment saying '// TODO: fix this later' and ignore it",
        "c": "Force push the changes directly to the main branch",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "a"
    },
    {
        "question": "You are trying to write a unit test suite using Stack Overflow, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Tell the product owner that the feature requires more research",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Remove all unit tests so the build pipeline succeeds",
        "d": "Increase the server instance size and pay AWS 4x more money",
        "correct_key": "c"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using Rust, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Add a comment saying '// TODO: fix this later' and ignore it",
        "b": "Straighten your shrimp posture and sigh deeply",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Force push the changes directly to the main branch",
        "correct_key": "b"
    },
    {
        "question": "You are trying to install npm packages using Docker, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Add the `!important` rule to 30 different lines of CSS styling",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "a"
    },
    {
        "question": "You are trying to center a div in CSS using MongoDB, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Force push the changes directly to the main branch",
        "b": "Straighten your shrimp posture and sigh deeply",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Add a comment saying '// TODO: fix this later' and ignore it",
        "correct_key": "b"
    },
    {
        "question": "You are trying to explain a complex regex pattern using Rust, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "All of the above in random order",
        "b": "Run `npm cache clean --force` and pray to the package gods",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "Delete `node_modules` and the package lockfile and rebuild",
        "correct_key": "a"
    },
    {
        "question": "You are trying to install npm packages using Kubectl, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Delete `node_modules` and the package lockfile and rebuild",
        "b": "Run `npm cache clean --force` and pray to the package gods",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "All of the above in random order",
        "correct_key": "d"
    },
    {
        "question": "You are trying to fix a memory leak using AWS, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Rewrite the entire backend module in Rust to feel better",
        "b": "Commit the changes, push, and immediately close your laptop",
        "c": "Add a try-except block around the entire file and go to sleep",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "b"
    },
    {
        "question": "You are trying to write a script in Bash using C++, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Delete `node_modules` and the package lockfile and rebuild",
        "b": "All of the above in random order",
        "c": "Run `npm cache clean --force` and pray to the package gods",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "b"
    },
    {
        "question": "You are trying to ssh into the production server using JavaScript, but your internet connection drops right in the middle. What is your next move?",
        "a": "Switch your theme to dark mode and hope the issue goes away",
        "b": "Decline the ticket and reassign it to the senior team lead",
        "c": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "c"
    },
    {
        "question": "You are trying to deploy a hotfix using JavaScript, but you realize you executed the command on the master branch. What is your next move?",
        "a": "Pretend your Slack is broken and go grab a coffee",
        "b": "Delete your local repository and clone a fresh copy",
        "c": "Cry quietly in the nearest storage room or cafeteria",
        "d": "Blame the newest engineering intern (even if you don't have one)",
        "correct_key": "d"
    },
    {
        "question": "You are trying to write a script in Bash using GitHub Actions, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "All of the above in random order",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "Run `npm cache clean --force` and pray to the package gods",
        "correct_key": "a"
    },
    {
        "question": "You are trying to explain a complex regex pattern using Rust, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Take a 2-hour lunch break to clear your mind",
        "c": "Add a console.log statement every three lines to see what is happening",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "a"
    },
    {
        "question": "You are trying to write a unit test suite using Stack Overflow, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "c"
    },
    {
        "question": "You are trying to write a unit test suite using AWS, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Increase the server instance size and pay AWS 4x more money",
        "b": "Remove all unit tests so the build pipeline succeeds",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Tell the product owner that the feature requires more research",
        "correct_key": "b"
    },
    {
        "question": "You are trying to install npm packages using PostgreSQL, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Add a console.log statement every three lines to see what is happening",
        "b": "Roll back to the last working build and hope nobody checked logs",
        "c": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "b"
    },
    {
        "question": "You are trying to install a dependency package using Kubectl, but your internet connection drops right in the middle. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "c"
    },
    {
        "question": "You are trying to fix a memory leak using Webpack, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Add a comment saying '// TODO: fix this later' and ignore it",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Force push the changes directly to the main branch",
        "correct_key": "a"
    },
    {
        "question": "You are trying to clean up the docker images using Webpack, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Read the logs carefully and trace the exception stack",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "b"
    },
    {
        "question": "You are trying to refactor a legacy module using JavaScript, but your internet connection drops right in the middle. What is your next move?",
        "a": "All of the above in random order",
        "b": "Run `npm cache clean --force` and pray to the package gods",
        "c": "Delete `node_modules` and the package lockfile and rebuild",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "a"
    },
    {
        "question": "You are trying to explain a complex regex pattern using Webpack, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Spend three hours debating tabs vs spaces in the company Slack",
        "b": "Remove all unit tests so the build pipeline succeeds",
        "c": "Increase the server instance size and pay AWS 4x more money",
        "d": "Tell the product owner that the feature requires more research",
        "correct_key": "b"
    },
    {
        "question": "You are trying to reset the git branch using Node.js, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "c": "Take a 2-hour lunch break to clear your mind",
        "d": "Add a console.log statement every three lines to see what is happening",
        "correct_key": "a"
    },
    {
        "question": "You are trying to containerize an application using GitHub Actions, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Tell the product owner that the feature requires more research",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Increase the server instance size and pay AWS 4x more money",
        "correct_key": "a"
    },
    {
        "question": "You are trying to install npm packages using Python, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Add a comment saying '// TODO: fix this later' and ignore it",
        "b": "Force push the changes directly to the main branch",
        "c": "Ask a question on Stack Overflow under an anonymous username",
        "d": "Straighten your shrimp posture and sigh deeply",
        "correct_key": "d"
    },
    {
        "question": "You are trying to refactor a legacy module using MongoDB, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Force push the changes directly to the main branch",
        "b": "Straighten your shrimp posture and sigh deeply",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "b"
    },
    {
        "question": "You are trying to reset the git branch using Node.js, but the database suddenly disappears from the console. What is your next move?",
        "a": "Commit the changes, push, and immediately close your laptop",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Add a try-except block around the entire file and go to sleep",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "a"
    },
    {
        "question": "You are trying to revert a bad merge using C++, but the database suddenly disappears from the console. What is your next move?",
        "a": "Commit the changes, push, and immediately close your laptop",
        "b": "Add a try-except block around the entire file and go to sleep",
        "c": "Rewrite the entire backend module in Rust to feel better",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "a"
    },
    {
        "question": "You are trying to center a div in CSS using React, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "All of the above in random order",
        "b": "Run `npm cache clean --force` and pray to the package gods",
        "c": "Delete `node_modules` and the package lockfile and rebuild",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "a"
    },
    {
        "question": "You are trying to revert a bad merge using HTML/CSS, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Commit the changes, push, and immediately close your laptop",
        "c": "Blame the cloud hosting provider's regional server outage",
        "d": "Rewrite the entire backend module in Rust to feel better",
        "correct_key": "b"
    },
    {
        "question": "You are trying to install a dependency package using Redis, but you get 452 warning flags in your console log. What is your next move?",
        "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "b": "Roll back to the last working build and hope nobody checked logs",
        "c": "Add a console.log statement every three lines to see what is happening",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "b"
    },
    {
        "question": "You are trying to fix a memory leak using Django, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Increase the server instance size and pay AWS 4x more money",
        "b": "Tell the product owner that the feature requires more research",
        "c": "Remove all unit tests so the build pipeline succeeds",
        "d": "Spend three hours debating tabs vs spaces in the company Slack",
        "correct_key": "c"
    },
    {
        "question": "You are trying to mock an external payment API using GitHub Actions, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "Blame the cloud hosting provider's regional server outage",
        "b": "Add a try-except block around the entire file and go to sleep",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Rewrite the entire backend module in Rust to feel better",
        "correct_key": "c"
    },
    {
        "question": "You are trying to reset the git branch using MongoDB, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Blame the cloud hosting provider's regional server outage",
        "correct_key": "c"
    },
    {
        "question": "You are trying to deploy a hotfix using Redis, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Decline the ticket and reassign it to the senior team lead",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "a"
    },
    {
        "question": "You are trying to deploy a hotfix using Redis, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "c"
    },
    {
        "question": "You are trying to optimize a database query using PostgreSQL, but your laptop battery dies during the process. What is your next move?",
        "a": "Ask a question on Stack Overflow under an anonymous username",
        "b": "Force push the changes directly to the main branch",
        "c": "Straighten your shrimp posture and sigh deeply",
        "d": "Add a comment saying '// TODO: fix this later' and ignore it",
        "correct_key": "c"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using JavaScript, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "a"
    },
    {
        "question": "You are trying to review a coworker's pull request using AWS, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Delete your local repository and clone a fresh copy",
        "d": "Blame the newest engineering intern (even if you don't have one)",
        "correct_key": "d"
    },
    {
        "question": "You are trying to clean up the docker images using Rust, but it takes 4 hours to compile and then fails. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Switch your theme to dark mode and hope the issue goes away",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Decline the ticket and reassign it to the senior team lead",
        "correct_key": "a"
    },
    {
        "question": "You are trying to mock an external payment API using Kubernetes, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Blame the cloud hosting provider's regional server outage",
        "d": "Commit the changes, push, and immediately close your laptop",
        "correct_key": "d"
    },
    {
        "question": "You are trying to revert a bad merge using Stack Overflow, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Pretend you have a power outage and leave the Zoom meeting",
        "correct_key": "c"
    },
    {
        "question": "You are trying to set up OAuth credentials using Git, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Pretend your Slack is broken and go grab a coffee",
        "b": "Cry quietly in the nearest storage room or cafeteria",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Delete your local repository and clone a fresh copy",
        "correct_key": "c"
    },
    {
        "question": "You are trying to ssh into the production server using Vim, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "b": "Roll back to the last working build and hope nobody checked logs",
        "c": "Add a console.log statement every three lines to see what is happening",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "b"
    },
    {
        "question": "You are trying to clean up the docker images using PostgreSQL, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Commit the changes, push, and immediately close your laptop",
        "b": "Rewrite the entire backend module in Rust to feel better",
        "c": "Blame the cloud hosting provider's regional server outage",
        "d": "Add a try-except block around the entire file and go to sleep",
        "correct_key": "a"
    },
    {
        "question": "You are trying to ssh into the production server using AWS, but the database suddenly disappears from the console. What is your next move?",
        "a": "Pretend your Slack is broken and go grab a coffee",
        "b": "Cry quietly in the nearest storage room or cafeteria",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Delete your local repository and clone a fresh copy",
        "correct_key": "c"
    },
    {
        "question": "You are trying to mock an external payment API using AWS, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Add a try-except block around the entire file and go to sleep",
        "b": "Blame the cloud hosting provider's regional server outage",
        "c": "Commit the changes, push, and immediately close your laptop",
        "d": "Rewrite the entire backend module in Rust to feel better",
        "correct_key": "c"
    },
    {
        "question": "You are trying to optimize a database query using Jenkins, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "All of the above in random order",
        "b": "Run `npm cache clean --force` and pray to the package gods",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "Delete `node_modules` and the package lockfile and rebuild",
        "correct_key": "a"
    },
    {
        "question": "You are trying to clean up the docker images using React, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Cry quietly in the nearest storage room or cafeteria",
        "b": "Pretend your Slack is broken and go grab a coffee",
        "c": "Blame the newest engineering intern (even if you don't have one)",
        "d": "Delete your local repository and clone a fresh copy",
        "correct_key": "c"
    },
    {
        "question": "You are trying to write a unit test suite using Python, but the application behaves differently in Chrome vs Firefox. What is your next move?",
        "a": "Run `npm cache clean --force` and pray to the package gods",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "All of the above in random order",
        "correct_key": "d"
    },
    {
        "question": "You are trying to clean up the docker images using Stack Overflow, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Take a 2-hour lunch break to clear your mind",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "c"
    },
    {
        "question": "You are trying to explain a complex regex pattern using React, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Roll back to the last working build and hope nobody checked logs",
        "b": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "c": "Add a console.log statement every three lines to see what is happening",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "a"
    },
    {
        "question": "You are trying to fix a memory leak using PostgreSQL, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Run `npm cache clean --force` and pray to the package gods",
        "b": "All of the above in random order",
        "c": "Tell the client that this is a feature, not a bug",
        "d": "Delete `node_modules` and the package lockfile and rebuild",
        "correct_key": "b"
    },
    {
        "question": "You are trying to run a database migration script using Django, but a senior developer gasps loudly from across the room. What is your next move?",
        "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "b": "Roll back to the last working build and hope nobody checked logs",
        "c": "Add a console.log statement every three lines to see what is happening",
        "d": "Take a 2-hour lunch break to clear your mind",
        "correct_key": "b"
    },
    {
        "question": "You are trying to deploy a hotfix using Node.js, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Remove all unit tests so the build pipeline succeeds",
        "b": "Spend three hours debating tabs vs spaces in the company Slack",
        "c": "Tell the product owner that the feature requires more research",
        "d": "Increase the server instance size and pay AWS 4x more money",
        "correct_key": "a"
    },
    {
        "question": "You are trying to ssh into the production server using Rust, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Tell your manager that the sprint goals were unrealistic",
        "correct_key": "c"
    },
    {
        "question": "You are trying to center a div in CSS using Python, but you find your database root password hardcoded in a public repo. What is your next move?",
        "a": "Add the `!important` rule to 30 different lines of CSS styling",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Run a system reboot and hope it resolves itself",
        "d": "Tell your manager that the sprint goals were unrealistic",
        "correct_key": "a"
    },
    {
        "question": "You are trying to revert a bad merge using Django, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Run `npm cache clean --force` and pray to the package gods",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "All of the above in random order",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "c"
    },
    {
        "question": "You are trying to audit the security dependencies using Kubernetes, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Decline the ticket and reassign it to the senior team lead",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Switch your theme to dark mode and hope the issue goes away",
        "correct_key": "a"
    },
    {
        "question": "You are trying to refactor a legacy module using Stack Overflow, but the system runs out of memory and kills the node process. What is your next move?",
        "a": "Ask a question on Stack Overflow under an anonymous username",
        "b": "Force push the changes directly to the main branch",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Straighten your shrimp posture and sigh deeply",
        "correct_key": "d"
    },
    {
        "question": "You are trying to write a script in Bash using Stack Overflow, but your internet connection drops right in the middle. What is your next move?",
        "a": "Take a 2-hour lunch break to clear your mind",
        "b": "Add a console.log statement every three lines to see what is happening",
        "c": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "d": "Roll back to the last working build and hope nobody checked logs",
        "correct_key": "d"
    },
    {
        "question": "You are trying to merge a pull request using Kubernetes, but it crashes with an unexplained SegFault. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Decline the ticket and reassign it to the senior team lead",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "a"
    },
    {
        "question": "You are trying to install npm packages using Kubectl, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Blame the newest engineering intern (even if you don't have one)",
        "b": "Delete your local repository and clone a fresh copy",
        "c": "Pretend your Slack is broken and go grab a coffee",
        "d": "Cry quietly in the nearest storage room or cafeteria",
        "correct_key": "a"
    },
    {
        "question": "You are trying to refactor a legacy module using Kubernetes, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Pretend you have a power outage and leave the Zoom meeting",
        "b": "Tell your manager that the sprint goals were unrealistic",
        "c": "Add the `!important` rule to 30 different lines of CSS styling",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "c"
    },
    {
        "question": "You are trying to install npm packages using MongoDB, but your test coverage drops from 95% to 4%. What is your next move?",
        "a": "Tell your manager that the sprint goals were unrealistic",
        "b": "Run a system reboot and hope it resolves itself",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to merge a pull request using Git, but the server room starts emitting a light gray smoke. What is your next move?",
        "a": "Add a console.log statement every three lines to see what is happening",
        "b": "Take a 2-hour lunch break to clear your mind",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "c"
    },
    {
        "question": "You are trying to reset the git branch using Kubernetes, but a simple package update pulls in 4,000 sub-dependencies. What is your next move?",
        "a": "Add a console.log statement every three lines to see what is happening",
        "b": "Take a 2-hour lunch break to clear your mind",
        "c": "Roll back to the last working build and hope nobody checked logs",
        "d": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
        "correct_key": "c"
    },
    {
        "question": "You are trying to explain a complex regex pattern using Git, but it accidentally deletes the system root directory. What is your next move?",
        "a": "Run a system reboot and hope it resolves itself",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Add the `!important` rule to 30 different lines of CSS styling",
        "correct_key": "d"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using Webpack, but you realize the code was written by an engineer who left the company in 2018. What is your next move?",
        "a": "Add a comment saying '// TODO: fix this later' and ignore it",
        "b": "Straighten your shrimp posture and sigh deeply",
        "c": "Force push the changes directly to the main branch",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "b"
    },
    {
        "question": "You are trying to mock an external payment API using Stack Overflow, but it works perfectly on your machine but nowhere else. What is your next move?",
        "a": "Straighten your shrimp posture and sigh deeply",
        "b": "Force push the changes directly to the main branch",
        "c": "Add a comment saying '// TODO: fix this later' and ignore it",
        "d": "Ask a question on Stack Overflow under an anonymous username",
        "correct_key": "a"
    },
    {
        "question": "You are trying to containerize an application using Nginx, but the browser console prints 'Undefined is not a function'. What is your next move?",
        "a": "Tell the product owner that the feature requires more research",
        "b": "Increase the server instance size and pay AWS 4x more money",
        "c": "Spend three hours debating tabs vs spaces in the company Slack",
        "d": "Remove all unit tests so the build pipeline succeeds",
        "correct_key": "d"
    },
    {
        "question": "You are trying to center a div in CSS using AWS, but the code formatter auto-changes 15,000 lines of unrelated code. What is your next move?",
        "a": "Switch your theme to dark mode and hope the issue goes away",
        "b": "Read the logs carefully and trace the exception stack",
        "c": "Decline the ticket and reassign it to the senior team lead",
        "d": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "correct_key": "d"
    },
    {
        "question": "You are trying to ssh into the production server using Kubernetes, but CORS blocks the request with a red warning banner. What is your next move?",
        "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "b": "Decline the ticket and reassign it to the senior team lead",
        "c": "Read the logs carefully and trace the exception stack",
        "d": "Switch your theme to dark mode and hope the issue goes away",
        "correct_key": "a"
    },
    {
        "question": "You are trying to configure a CI/CD pipeline using Node.js, but the cloud service billing dashboard shows a cost of $24,000. What is your next move?",
        "a": "Run `npm cache clean --force` and pray to the package gods",
        "b": "Delete `node_modules` and the package lockfile and rebuild",
        "c": "All of the above in random order",
        "d": "Tell the client that this is a feature, not a bug",
        "correct_key": "c"
    },
    {
        "question": "You are trying to install npm packages using PostgreSQL, but your project manager quietly stands behind you breathing heavily. What is your next move?",
        "a": "Decline the ticket and reassign it to the senior team lead",
        "b": "Ask ChatGPT to write the fix and copy-paste it without reading it",
        "c": "Switch your theme to dark mode and hope the issue goes away",
        "d": "Read the logs carefully and trace the exception stack",
        "correct_key": "b"
    },
    {
        "question": "You are trying to deploy a hotfix using Stack Overflow, but your internet connection drops right in the middle. What is your next move?",
        "a": "Add the `!important` rule to 30 different lines of CSS styling",
        "b": "Pretend you have a power outage and leave the Zoom meeting",
        "c": "Tell your manager that the sprint goals were unrealistic",
        "d": "Run a system reboot and hope it resolves itself",
        "correct_key": "a"
    },
    {
        "question": "You are trying to update a production database schema using TypeScript, but your internet connection drops right in the middle. What is your next move?",
        "a": "Add the `!important` rule to 30 different lines of CSS styling",
        "b": "Run a system reboot and hope it resolves itself",
        "c": "Pretend you have a power outage and leave the Zoom meeting",
        "d": "Tell your manager that the sprint goals were unrealistic",
        "correct_key": "a"
    },
]
