# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
- I think the three main core actions a user is a weekly calender that involves daily actions, depending on the user's schedule, including walking time for the dog, feeding schedule and select pet name; this only applies if the user has more than one dog. Lastly, a check-off list that states if day's tasks have been accomplished
- The classes will user, with attributes like pet name and schedule and user availability. For the pet, it will include pet name(s), daily tasks like walking, eating, rest time

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
- Based on my initial design concept, I had two classes, user and pet, with each having attributes such as name, task(s), checkoff list. However, using Claude, it suggested that I have more classes, so as to have each attribute have its class. Thereby making it easier to have more defined attributes. 

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
- The consideration was given to priority, depending on task, since certain task(s) can have competing priorities. I decided rather than demote one priority, I will flag it, as a way of keeping track that it needs to be completed. In this way, I'll ensure that high priority tasks like walking the dog as top priority whilst giving the dog its daily vitamins can still be completed at a later time. 

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
- As I stated above, I flagged priority tasks rather than lower it. This forces the pet owner to weigh each task(s) and determine which, even though important, can be completed at a later time without having any adverse effect to the overall well-being of the pet.However, once I ran pawpal_system.py file, it flagged each tasks due to conflict. Therefore, I had to create a separate section that generates a schedule per pet that generates a schedule for each pet, based on owner availability,  rather than a general schedule for each pet.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?
- I used AI for all aspects of the projects. I started by stating the problem. Then based on my initial thinking asked for improvements. For example, during debugging, I was suppose to get 5 test, but I only had 4/4 test pass. On closer inspection, I realized that in the test file, test_pawpal, it was importing 'Cat' function but it did not use it as part of the test. When I pointed out the error, it was able to correct and have all 5/5 test pass. In conclusion, I didn't rely on AI to make decisions for me, I was able to control the results obtained by stating what was already accomplished, and asking for improvement on logic that I didn't understand especially with error messages like this 'python -m pip install -r requirements.txt
Python was not found; run without arguments to install from the Microsoft Store, or disable this short'. I learned that I had to use 'py' rather than 'python', even though it suggested 'python' while I was debugging, but changed to 'py' once I stated that it wasn't working.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
- I was in control of the interaction. For example, in test_pawpal file, it deleted the test for conflict detection, when I asked why, it acknowledge its error and restated the test condition. Since I reviewed  the answers provided, I was able to detect possible errors, thereby making debugging and designing the project a much easier process.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?
- The behaviors tested mainly involved conflicts. My original design was to start with a user with two pets, dog and cat and account for slight differences between the two. For instance, dog/cat need to be fed, however, only dogs require constant activities such as walking. Therefore, I had to account for both pet having a similar schedule, but with varying needs. In addition, I tied each pets' activity to the owner/user. This allowed for combined schedules that may have overlapping tasks. 

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?
- Based on testing done, so far I'll 4/5. Reason being I'll like to include a tracking feature that compares allocated time verses the actual time spent on each assigned task.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
- Overall execution of all sections of the project, and my ability to use AI in a project

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
- I'll like to include a tracking feature that tracks allocated vs actual time spent on each task for each pet. Generate a graph and use it as a guide to adjust time allotment for each task and pet.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
- AI is a useful tool that can be used as a companion during large projects, but it still makes mistakes and answers generated should be verified before using as part of a control measure. Using this approach it'll make the project easier to debug and wrong answers removed and/or modified before the project is finished.
