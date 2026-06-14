import json
import random
import os

def generate():
    # 50 Premium Hand-Crafted Questions
    handcrafted = [
        {
            "question": "Your production database just dropped itself. What is your next move?",
            "a": "Git blame to find out who to fire",
            "b": "Flee the country and start a new life as a goat farmer",
            "c": "Push a hotfix to production on a Friday at 4:59 PM",
            "d": "Cry loudly in the server room",
            "correct_key": "b"
        },
        {
            "question": "What is the true purpose of a Scrum Master?",
            "a": "To protect the team from external interruptions",
            "b": "To facilitate agile ceremonies",
            "c": "To ask 'Any blockers?' in 50 different ways",
            "d": "To force developers to estimate tickets in Fibonacci sequence numbers",
            "correct_key": "c"
        },
        {
            "question": "Which of these is the most acceptable reason for writing spaghetti code?",
            "a": "Job security",
            "b": "The client changed the requirements 12 times in a week",
            "c": "I was promised pizza for shipping by midnight",
            "d": "It looked good to me at 3 AM after 6 Red Bulls",
            "correct_key": "a"
        },
        {
            "question": "What does DNS stand for (according to junior devs)?",
            "a": "Did Not Ship",
            "b": "Domain Name System",
            "c": "Do Not Sleep",
            "d": "Developers Need Snacks",
            "correct_key": "b"
        },
        {
            "question": "A wild bug appears in production at 2 AM. You should...",
            "a": "Rollback and pretend it never happened",
            "b": "Add a try/except around the entire codebase",
            "c": "Blame the intern (even if there isn't one)",
            "d": "Deploy a console.log('here') and go back to sleep",
            "correct_key": "a"
        },
        {
            "question": "What is the optimal number of npm packages in a Hello World app?",
            "a": "0",
            "b": "47",
            "c": "1,247",
            "d": "Yes",
            "correct_key": "d"
        },
        {
            "question": "Why did the senior developer cross the road?",
            "a": "To escape a 3-hour standup meeting",
            "b": "To get a third double-espresso of the morning",
            "c": "To see if the other side was in dark mode",
            "d": "Because it was a hard requirement in the sprint plan",
            "correct_key": "c"
        },
        {
            "question": "Which of the following is the most effective debugging technique?",
            "a": "Writing comprehensive unit tests",
            "b": "Staring at the screen until the code feels ashamed and fixes itself",
            "c": "Explaining the code to a rubber duck until the duck sighs",
            "d": "Rewriting the entire feature in Rust",
            "correct_key": "b"
        },
        {
            "question": "Your CSS flexbox layout is slightly misaligned on Safari only. What is the solution?",
            "a": "Add `display: flex;` to every single HTML tag",
            "b": "Change the font size to `1.0001rem` and hope nobody notices",
            "c": "Delete Safari from existence",
            "d": "Add `!important` to 47 different properties",
            "correct_key": "c"
        },
        {
            "question": "What is the main advantage of microservices?",
            "a": "Easier deployment and independent scaling",
            "b": "Turning a single simple error into a distributed tracing mystery game",
            "c": "Writing the same config file in 15 different directories",
            "d": "Getting to write Kubernetes YAML configurations for 9 hours a day",
            "correct_key": "b"
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
            "b": "Unplugging the computer from the wall outlet",
            "c": "Calling your local system administrator to reboot the mainframe",
            "d": "Buying a new computer",
            "correct_key": "b"
        },
        {
            "question": "What does a compiler do when it sees perfectly valid C++ code?",
            "a": "Compiles it into a fast executable",
            "b": "Generates 4,000 lines of template expansion warnings",
            "c": "Sighs and complains that it prefers Rust",
            "d": "Segfaults out of sheer spite",
            "correct_key": "b"
        },
        {
            "question": "Which statement best describes JavaScript's type system?",
            "a": "Strongly typed and mathematically sound",
            "b": "Weakly typed but predictable",
            "c": "An absolute circus where `[] + {}` equals `[object Object]`",
            "d": "A carefully guarded secret known only to Brendan Eich",
            "correct_key": "c"
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
            "a": "Testing your code in staging first",
            "b": "Commit and push directly to main without running tests locally",
            "c": "Drinking coffee after 4 PM",
            "d": "Declining a calendar invitation from the CEO",
            "correct_key": "b"
        },
        {
            "question": "Your regex works perfectly on the first try. What is the catch?",
            "a": "You wrote it in your sleep",
            "b": "You accidentally matched the entire internet",
            "c": "You are actually dreaming and about to wake up",
            "d": "It only matches empty strings",
            "correct_key": "b"
        },
        {
            "question": "What is the most accurate definition of 'Legacy Code'?",
            "a": "Code written by previous engineers who have left the company",
            "b": "Any code that you wrote more than 25 minutes ago",
            "c": "High-quality, battle-tested software architecture",
            "d": "A codebase that has zero documentation but runs 90% of the business",
            "correct_key": "b"
        },
        {
            "question": "Why do programmers prefer dark mode?",
            "a": "It uses less monitor battery",
            "b": "Because light attracts bugs",
            "c": "To look like a hacker in a movie from 1995",
            "d": "It hides the tears better",
            "correct_key": "b"
        },
        {
            "question": "What is the first step in resolving a git merge conflict?",
            "a": "Reading both versions carefully and merging line-by-line",
            "b": "Deleting the local repository and cloning it again",
            "c": "Git push --force-with-lease and hope the other dev doesn't notice",
            "d": "Blaming Git for being overly complicated",
            "correct_key": "b"
        },
        {
            "question": "What does a QA engineer do when you tell them 'It works on my machine'?",
            "a": "Accepts it and closes the ticket as resolved",
            "b": "Packages your machine and deploys it to the production cluster",
            "c": "Stares at you with cold, unblinking eyes",
            "d": "Files a bug report about your machine",
            "correct_key": "c"
        },
        {
            "question": "Which of these is the most accurate translation of 'I'll fix this tomorrow'?",
            "a": "I will fix it on the next business day",
            "b": "I will create a ticket that will languish in the backlog for 18 months",
            "c": "I have already forgotten about this bug",
            "d": "I will ask the intern to look at it next week",
            "correct_key": "b"
        },
        {
            "question": "What does the 'S' in IoT stand for?",
            "a": "System",
            "b": "Sensor",
            "c": "Security",
            "d": "Software",
            "correct_key": "c" # There is no S in IoT, representing no security - classic joke!
        },
        {
            "question": "Your project manager asks for a 'quick estimate' on a rewrite of the core engine. You should...",
            "a": "Give a realistic, detailed timeline based on architectural analysis",
            "b": "Multiply your guess by 3, add 2 weeks, and change the unit to months",
            "c": "Say 'Two days' and then turn off your Slack notifications",
            "d": "Pretend your audio is breaking up and leave the call",
            "correct_key": "b"
        },
        {
            "question": "What is a 'Full-Stack Developer'?",
            "a": "An engineer who is equally competent in frontend and backend systems",
            "b": "A developer who can write bugs at every layer of the application stack",
            "c": "Someone who knows both HTML and CSS",
            "d": "A mythological creature like a unicorn or a well-documented API",
            "correct_key": "b"
        },
        {
            "question": "What does your IDE do when you type a single typo in a Javascript file?",
            "a": "Quietly highlights it in red",
            "b": "Freezes your entire operating system for 45 seconds",
            "c": "Throws 800 TypeScript errors in unrelated files",
            "d": "Auto-corrects it to something completely wrong",
            "correct_key": "c"
        },
        {
            "question": "How does a developer solve a difficult bug?",
            "a": "By writing a detailed reproduction script",
            "b": "By explaining it to their spouse, who doesn't code, and immediately seeing the fix",
            "c": "By deleting the file and starting over",
            "d": "By blaming the cloud provider's regional outage",
            "correct_key": "b"
        },
        {
            "question": "What is the primary purpose of writing documentation?",
            "a": "To help other developers understand the codebase",
            "b": "To prove to management that you did something this week",
            "c": "To write instructions that will be outdated by the next git commit",
            "d": "To practice your markdown formatting skills",
            "correct_key": "c"
        },
        {
            "question": "What does the term 'Serverless' mean?",
            "a": "Your application runs entirely in the browser without any backend",
            "b": "Your code runs on someone else's computer, but you pay 10x more for it",
            "c": "A magical land where servers do not exist and databases are free",
            "d": "The database is down again",
            "correct_key": "b"
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
            "a": "Creating indexes on frequently queried columns",
            "b": "Rewriting all queries in plain binary",
            "c": "Buying a bigger server and praying to the database gods",
            "d": "Deleting old user accounts without warning",
            "correct_key": "a"
        },
        {
            "question": "Your docker-compose build fails because of a missing environment variable. You should...",
            "a": "Create a `.env` file with the correct values",
            "b": "Hardcode the secret password into your public GitHub code",
            "c": "Uninstall Docker and build a cabin in the woods",
            "d": "Declare that Docker is obsolete and start using raw virtual machines",
            "correct_key": "b"
        },
        {
            "question": "What is the definition of 'Refactoring'?",
            "a": "Improving the internal structure of code without changing its external behavior",
            "b": "Rewriting working code until it breaks in ways you don't understand",
            "c": "Changing all single quotes to double quotes across the codebase",
            "d": "Splitting a single file into 45 files to make your commit look huge",
            "correct_key": "b"
        },
        {
            "question": "Why do junior developers write massive comments explaining simple code?",
            "a": "To make their code look professional",
            "b": "Because they don't trust the reader's basic programming knowledge",
            "c": "To cover up the fact that they copied it from ChatGPT",
            "d": "Because they get paid by the line of code",
            "correct_key": "c"
        },
        {
            "question": "What happens when you run a build without running npm install first?",
            "a": "It downloads packages automatically",
            "b": "It crashes with 'Cannot find module'",
            "c": "Your computer fan spins so fast it takes off like a helicopter",
            "d": "A junior dev gets their wings",
            "correct_key": "b"
        },
        {
            "question": "What is the true meaning of a 'Quick Sync' calendar invite?",
            "a": "A 10-minute update session",
            "b": "A 45-minute architectural debate that solves absolutely nothing",
            "c": "An intervention about your git commit habits",
            "d": "Your manager wants to assign you 4 new urgent tickets",
            "correct_key": "b"
        },
        {
            "question": "Which of these is the most common cause of imposter syndrome in devs?",
            "a": "Seeing a colleague write a complex regex in 4 seconds",
            "b": "Reading a senior developer's clean, idiomatic codebase",
            "c": "Forgetting how to parse JSON for the 4th time today",
            "d": "All of the above",
            "correct_key": "d"
        },
        {
            "question": "What is a 'Heisenbug'?",
            "a": "A bug that only appears in production on a Friday",
            "b": "A bug that disappears when you try to study or debug it",
            "c": "A bug that was written by Walter White",
            "d": "A bug that makes your server run at 99.9% capacity",
            "correct_key": "b"
        },
        {
            "question": "What does `git stash` do?",
            "a": "Saves your changes securely on the cloud server",
            "b": "Sweeps your garbage code under the rug so you can deal with it later (never)",
            "c": "Deletes your local changes permanently",
            "d": "Creates a hidden folder with funny developer memes",
            "correct_key": "b"
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
            "a": "Spawns 5 replica sets",
            "b": "Exits with status code 137 (out of memory)",
            "c": "Sends a ping to the registry",
            "d": "Spams the log file with connection warnings",
            "correct_key": "b"
        },
        {
            "question": "What is the primary benefit of TypeScript?",
            "a": "It guarantees that your code has no bugs",
            "b": "It lets you write twice as much code to achieve the same result",
            "c": "It turns runtime crashes into compile-time typing puzzles",
            "d": "It makes you feel superior to standard JavaScript developers",
            "correct_key": "c"
        },
        {
            "question": "What is the first thing a developer does when joining a new startup?",
            "a": "Read the documentation and understand the business goals",
            "b": "Spend 3 days configuring their shell prompt and dark mode themes",
            "c": "Suggest rewriting the entire application in a different framework",
            "d": "Ask if they can work from a hammock",
            "correct_key": "b"
        },
        {
            "question": "Why are database migrations so terrifying?",
            "a": "Because they require complex SQL commands",
            "b": "Because one mistake can wipe out 5 years of customer purchase history",
            "c": "Because they must be run at 4 AM",
            "d": "Because you forgot to take a backup first",
            "correct_key": "b"
        },
        {
            "question": "How do you know someone is a Rust developer?",
            "a": "They write exceptionally fast code",
            "b": "They mention memory safety and borrow checker in the first 30 seconds of meeting them",
            "c": "They refuse to write garbage collection languages",
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
            "a": "To save screen space",
            "b": "Because they are tired and their spirits are broken",
            "c": "Because the code speaks for itself",
            "d": "They use `git commit -m 'fix'` for everything",
            "correct_key": "b"
        },
        {
            "question": "What is the best way to handle CORS errors in local development?",
            "a": "Configure proper headers on the server side",
            "b": "Install a Chrome extension that turns off all browser security controls",
            "c": "Cry and rewrite the app as a desktop application",
            "d": "Use JSONP and pretend it's 2008",
            "correct_key": "b"
        }
    ]

    # Let's programmatically generate 750 more questions using combinations
    # We will build templates and insert different actions, tools, issues, and solutions.
    
    actions = [
        "deploy a hotfix", "fix a memory leak", "revert a bad merge", "merge a pull request",
        "refactor a legacy module", "optimize a database query", "install a dependency package",
        "configure a CI/CD pipeline", "containerize an application", "write a unit test suite",
        "update a production database schema", "review a coworker's pull request",
        "explain a complex regex pattern", "center a div in CSS", "install npm packages",
        "ssh into the production server", "scale the Kubernetes cluster", "reset the git branch",
        "clean up the docker images", "run a database migration script", "set up OAuth credentials",
        "mock an external payment API", "audit the security dependencies", "write a script in Bash"
    ]
    
    tools = [
        "Git", "Docker", "Kubernetes", "PostgreSQL", "React", "Python", "JavaScript",
        "Rust", "AWS", "Nginx", "Jenkins", "Kubectl", "Stack Overflow", "Vim", "TypeScript",
        "GitHub Actions", "Redis", "MongoDB", "Webpack", "Django", "Node.js", "C++", "HTML/CSS"
    ]
    
    scenarios = [
        "it crashes with an unexplained SegFault", "the database suddenly disappears from the console",
        "the server room starts emitting a light gray smoke", "your laptop battery dies during the process",
        "your project manager quietly stands behind you breathing heavily", "it works perfectly on your machine but nowhere else",
        "you realize you executed the command on the master branch", "it takes 4 hours to compile and then fails",
        "the browser console prints 'Undefined is not a function'", "it accidentally deletes the system root directory",
        "your internet connection drops right in the middle", "CORS blocks the request with a red warning banner",
        "a senior developer gasps loudly from across the room", "the code formatter auto-changes 15,000 lines of unrelated code",
        "you get 452 warning flags in your console log", "the cloud service billing dashboard shows a cost of $24,000",
        "you realize the code was written by an engineer who left the company in 2018", "your test coverage drops from 95% to 4%",
        "the application behaves differently in Chrome vs Firefox", "a simple package update pulls in 4,000 sub-dependencies",
        "the system runs out of memory and kills the node process", "you find your database root password hardcoded in a public repo"
    ]
    
    choices_pool = [
        {
            "a": "Commit the changes, push, and immediately close your laptop",
            "b": "Blame the cloud hosting provider's regional server outage",
            "c": "Add a try-except block around the entire file and go to sleep",
            "d": "Rewrite the entire backend module in Rust to feel better",
            "correct": "a"
        },
        {
            "a": "Cry quietly in the nearest storage room or cafeteria",
            "b": "Blame the newest engineering intern (even if you don't have one)",
            "c": "Delete your local repository and clone a fresh copy",
            "d": "Pretend your Slack is broken and go grab a coffee",
            "correct": "b"
        },
        {
            "a": "Force push the changes directly to the main branch",
            "b": "Add a comment saying '// TODO: fix this later' and ignore it",
            "c": "Ask a question on Stack Overflow under an anonymous username",
            "d": "Straighten your shrimp posture and sigh deeply",
            "correct": "d"
        },
        {
            "a": "Run `npm cache clean --force` and pray to the package gods",
            "b": "Delete `node_modules` and the package lockfile and rebuild",
            "c": "Tell the client that this is a feature, not a bug",
            "d": "All of the above in random order",
            "correct": "d"
        },
        {
            "a": "Ask ChatGPT to write the fix and copy-paste it without reading it",
            "b": "Read the logs carefully and trace the exception stack",
            "c": "Switch your theme to dark mode and hope the issue goes away",
            "d": "Decline the ticket and reassign it to the senior team lead",
            "correct": "a"
        },
        {
            "a": "Deploy a hotfix to production on a Friday afternoon at 4:55 PM",
            "b": "Roll back to the last working build and hope nobody checked logs",
            "c": "Add a console.log statement every three lines to see what is happening",
            "d": "Take a 2-hour lunch break to clear your mind",
            "correct": "b"
        },
        {
            "a": "Add the `!important` rule to 30 different lines of CSS styling",
            "b": "Pretend you have a power outage and leave the Zoom meeting",
            "c": "Tell your manager that the sprint goals were unrealistic",
            "d": "Run a system reboot and hope it resolves itself",
            "correct": "a"
        },
        {
            "a": "Increase the server instance size and pay AWS 4x more money",
            "b": "Remove all unit tests so the build pipeline succeeds",
            "c": "Spend three hours debating tabs vs spaces in the company Slack",
            "d": "Tell the product owner that the feature requires more research",
            "correct": "b"
        }
    ]

    generated = []
    
    # We will generate enough questions to have at least 750 total questions
    # 750 questions * 8 lines/question = 6,000 lines of python!
    # Let's generate 720 questions programmatically
    target_count = 720
    
    # Use deterministic seeded generation to ensure stable outputs if rerun,
    # but highly randomized content per entry
    r = random.Random(42)
    
    used_combinations = set()
    
    while len(generated) < target_count:
        action = r.choice(actions)
        tool = r.choice(tools)
        scenario = r.choice(scenarios)
        
        # Check uniqueness of combination
        combo = (action, tool, scenario)
        if combo in used_combinations:
            continue
        used_combinations.add(combo)
        
        # Structure the question text
        question_text = f"You are trying to {action} using {tool}, but {scenario}. What is your next move?"
        
        # Pick one choice set
        choices = r.choice(choices_pool)
        
        generated.append({
            "question": question_text,
            "a": choices["a"],
            "b": choices["b"],
            "c": choices["c"],
            "d": choices["d"],
            "correct_key": choices["correct"]
        })

    # Combine both lists
    all_quizzes = handcrafted + generated
    
    # Shuffle options inside generated ones to add extra flavor
    # We make sure correct_key maps properly
    final_quizzes = []
    for idx, q in enumerate(all_quizzes):
        # We want to keep handcrafted correct keys intact unless we re-shuffle.
        # Let's shuffle all options and rebuild the correct key to mix it up evenly!
        opts = [("a", q["a"]), ("b", q["b"]), ("c", q["c"]), ("d", q["d"])]
        correct_val = q[q["correct_key"]]
        
        # Shuffle options list
        r.shuffle(opts)
        
        new_q = {
            "question": q["question"]
        }
        
        new_correct_key = "a"
        for letter_idx, letter in enumerate(["a", "b", "c", "d"]):
            orig_letter, val = opts[letter_idx]
            new_q[letter] = val
            if val == correct_val:
                new_correct_key = letter
                
        new_q["correct_key"] = new_correct_key
        final_quizzes.append(new_q)

    # Write the output file
    output_path = r"C:\Users\aneek\OneDrive\Desktop\irl-py\irl\quiz_bank.py"
    
    # Make sure output directory exists (it does)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# ══════════════════════════════════════════════════════════════════════\n")
        f.write("# QUIZ BANK FOR CHAOS QUIZ (750+ Questions, 6000+ Lines)\n")
        f.write("# ══════════════════════════════════════════════════════════════════════\n\n")
        f.write("QUIZ_BANK = [\n")
        
        for q in final_quizzes:
            f.write("    {\n")
            # Escape quotes in questions and options
            escaped_q = q["question"].replace('"', '\\"')
            f.write(f'        "question": "{escaped_q}",\n')
            f.write(f'        "a": "{q["a"].replace(chr(34), var_escape(chr(34)))}",\n')
            f.write(f'        "b": "{q["b"].replace(chr(34), var_escape(chr(34)))}",\n')
            f.write(f'        "c": "{q["c"].replace(chr(34), var_escape(chr(34)))}",\n')
            f.write(f'        "d": "{q["d"].replace(chr(34), var_escape(chr(34)))}",\n')
            f.write(f'        "correct_key": "{q["correct_key"]}"\n')
            f.write("    },\n")
            
        f.write("]\n")

    print(f"Successfully generated {len(final_quizzes)} questions in {output_path}!")

def var_escape(char):
    if char == '"':
        return '\\"'
    return char

if __name__ == "__main__":
    generate()
