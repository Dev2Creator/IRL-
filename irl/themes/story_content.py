# IRL™ 🌱 - Software for Humans

STORY_NODES = {
    "default": {
        "start": {
            "text": "You are a junior developer on your first day. The legacy monolith stares back at you. Your tech lead, an empty coffee cup in human form, says: 'Just fix the one bug in the auth service. Should be easy.'",
            "choices": [
                ("Run `npm install` and hope for the best", "npm_install"),
                ("Ask for documentation", "ask_docs"),
                ("Quit immediately", "quit")
            ]
        },
        "npm_install": {
            "text": "You run `npm install`. The terminal turns red. Warnings pour down like bloody rain. 8,432 vulnerabilities found. The fan on your laptop sounds like a jet engine.",
            "choices": [
                ("Run `npm audit fix --force`", "audit_fix"),
                ("Ignore the warnings and run `npm start`", "npm_start")
            ]
        },
        "ask_docs": {
            "text": "You ask for documentation. The entire open-plan office goes silent. Someone in the back laughs nervously. The tech lead stares at you. 'The code is the documentation,' they whisper.",
            "choices": [
                ("Read the code", "read_code"),
                ("Cry in the bathroom", "bathroom")
            ]
        },
        "quit": {
            "text": "You stand up, put your jacket back on, and walk out. You become a goat farmer in the Alps. You are truly happy. END.",
            "choices": []
        },
        "audit_fix": {
            "text": "`npm audit fix --force`. The ultimate gamble. Dependencies are updated. React is now v19, Webpack is broken, and nothing compiles. You just took down the entire staging environment.",
            "choices": [
                ("Blame DevOps", "blame_devops"),
                ("Git reset hard", "git_reset")
            ]
        },
        "npm_start": {
            "text": "You run `npm start`. The server starts on port 3000. Wait, port 3000 is already in use? You kill the process. You start again. The app loads... it's a blank white screen.",
            "choices": [
                ("Check the console", "console"),
                ("Clear cache and hard reload", "cache")
            ]
        },
        "read_code": {
            "text": "You open the main file. It is 14,000 lines long. There are variables named `data2`, `temp_final_v3`, and `DO_NOT_TOUCH`. You feel your sanity slipping away.",
            "choices": [
                ("Try to refactor it", "refactor"),
                ("Just add a console.log", "console_log")
            ]
        },
        "bathroom": {
            "text": "You cry in the bathroom. The WiFi is surprisingly good in here. You apply for a new job. END.",
            "choices": []
        },
        "blame_devops": {
            "text": "You successfully blame DevOps. They spend 3 weeks migrating to Kubernetes to 'fix the underlying issue'. You still haven't fixed the bug, but nobody remembers it anymore. YOU WIN.",
            "choices": []
        },
        "git_reset": {
            "text": "You `git reset --hard`. You lost all your work, but at least the errors are gone. You tell your manager you're 'still onboarding'. YOU SURVIVED. END.",
            "choices": []
        },
        "console": {
            "text": "Console: `Uncaught TypeError: undefined is not a function at Object.x [as render]`. It traces back to a minified file from a library last updated 7 years ago.",
            "choices": []
        },
        "cache": {
            "text": "You clear the cache. Now it's a 404 error. Progress? No, just pain. END.",
            "choices": []
        },
        "refactor": {
            "text": "You try to refactor the 14k line file. You break the billing system. The company loses $50,000 in an hour. You are escorted out by security. END.",
            "choices": []
        },
        "console_log": {
            "text": "You add `console.log('here')`. It prints 42,000 times in half a second. The browser crashes. END.",
            "choices": []
        }
    },
    "cyberpunk": {
        "start": {
            "text": "NIGHT CITY, 2077. You are a street-kid netrunner. A fixer named 'Glitch' hands you a data-shard. 'Get into the Arasaka mainframe and delete their node_modules directory. It's the only way to cripple them.'",
            "choices": [
                ("Jack into the terminal", "jack_in"),
                ("Check your cyberware first", "check_gear")
            ]
        },
        "jack_in": {
            "text": "You jack in. Neon ICE walls surround you. The Arasaka Daemons are tracking your IP.",
            "choices": [
                ("Deploy the SQL Injection worm", "sql_worm"),
                ("Attempt a brute force DDoS", "ddos")
            ]
        },
        "check_gear": {
            "text": "You check your gear. You have an outdated neural-deck and 3 RAM slots. This is suicide.",
            "choices": [
                ("Buy better RAM on the black market", "buy_ram"),
                ("Jack in anyway", "jack_in")
            ]
        },
        "sql_worm": {
            "text": "The SQL worm chews through the first firewall. You're in the central database. You see the `node_modules` directory. It is 4.2 Petabytes of corporate bloatware.",
            "choices": [
                ("Execute `rm -rf`", "rm_rf"),
                ("Upload a malicious package", "upload_package")
            ]
        },
        "ddos": {
            "text": "You attempt a DDoS. Arasaka's counter-intrusion software fries your neural deck. You flatline. END.",
            "choices": []
        },
        "buy_ram": {
            "text": "You try to buy RAM, but the ripperdoc scams you and installs a crypto-miner in your visual cortex. You now see Dogecoin charts everywhere you look. END.",
            "choices": []
        },
        "rm_rf": {
            "text": "You execute `rm -rf node_modules`. The corporate servers scream as dependencies vanish. Arasaka stock plummets. You unplug and fade into the neon shadows. A legend is born. YOU WIN.",
            "choices": []
        },
        "upload_package": {
            "text": "You upload a malicious npm package disguised as a React component. It's subtle, but it will slowly drain their credits over 10 years. A true professional. YOU WIN.",
            "choices": []
        }
    },
    "dracula": {
        "start": {
            "text": "The crypt is cold. You, Count Vladislav, a 400-year-old vampire and Full Stack Developer, have a PR due. The sun will rise in 2 hours. If you don't push to master, the stakeholders will literally stake you.",
            "choices": [
                ("Review the pull request", "review_pr"),
                ("Drink the blood of the QA tester", "drink_qa")
            ]
        },
        "review_pr": {
            "text": "You review the PR. There are merge conflicts in `package-lock.json`. A truly cursed file.",
            "choices": [
                ("Resolve conflicts manually", "resolve_manual"),
                ("Delete the file and run npm install", "nuke_lock")
            ]
        },
        "drink_qa": {
            "text": "You feed on the QA tester. You gain their power of nitpicking, but their blood is tainted with caffeine and anxiety. You are paralyzed by indecision. The sun rises. You turn to ash. END.",
            "choices": []
        },
        "resolve_manual": {
            "text": "You try to manually resolve 12,000 lines of JSON conflicts. Your immortal eyes bleed. You run out of time. The sun rises. END.",
            "choices": []
        },
        "nuke_lock": {
            "text": "You delete the lockfile. You run install. The dependencies resolve to completely different sub-versions, but the tests pass! You hit merge. The sky turns pink as the sun rises. You retreat to your coffin, victorious. YOU WIN.",
            "choices": []
        }
    },
    "toxic": {
        "start": {
            "text": "You are in a Discord call with 4 other devs. They are all trash. The server is crashing and nobody knows why. The tech lead says 'I bet it's because somebody didn't use TypeScript.'",
            "choices": [
                ("Flame the tech lead", "flame_lead"),
                ("Check the AWS logs", "check_aws")
            ]
        },
        "flame_lead": {
            "text": "You say: 'Ratio + L + TypeScript wouldn't have saved your garbage architecture + you have zero commits this week.'",
            "choices": [
                ("Mute your mic and laugh", "mute_laugh"),
                ("Leave the call", "leave_call")
            ]
        },
        "check_aws": {
            "text": "You check AWS CloudWatch. You see an infinite loop of lambda functions triggering each other. The bill is currently at $45,000 and climbing.",
            "choices": [
                ("Stop the lambdas", "stop_lambda"),
                ("Take a screenshot for Twitter and do nothing", "screenshot")
            ]
        },
        "mute_laugh": {
            "text": "The tech lead fires you on the spot. But you got the clip. You post it on TikTok and it goes viral. Worth it. YOU WIN.",
            "choices": []
        },
        "leave_call": {
            "text": "You leave the call. You are marked as 'not a team player' and put on a PIP. END.",
            "choices": []
        },
        "stop_lambda": {
            "text": "You try to stop the lambdas, but you don't have IAM permissions. You tag the DevOps guy, but he's playing Valorant. The company goes bankrupt. END.",
            "choices": []
        },
        "screenshot": {
            "text": "You tweet the screenshot. It gets 10k retweets. The CEO sees it. You are sued for NDA violation, but you gained 5,000 followers. A pyrrhic victory. END.",
            "choices": []
        }
    }
}
