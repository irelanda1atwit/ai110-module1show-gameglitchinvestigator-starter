# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

--- The hints were reversed and you needed to refresh the page to start a new game.


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

--- The AI correctly fixed the issue with the inverted hints and I verified it by testing it myself. The AI incorrectly added a test I made to a new file and I fixed it by moving it to the logic section.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

--- I used both pytest and manually testing the game to solve the issues. I had the ai add documentation and exlpain the changes it made. One pytest I added was to reject invalid inputs.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

--- It was looking for a literal rather than a number. It works by functioning as a webpage and if you want to see any changes you made you need to refesh the page. I had it check for number match instead.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.


Id like to use pytest going forward since I've never used it before. I think going forward it helps me find issues with my code that I think will be there but arent exactly sure how or what it will do. It changed how I used ai to help by showing me how agents can do large logic changes or small tweaks depending on the intstuctions you give them.