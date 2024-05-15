[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/JnIGdh-D)


## Team Name - Kinetic

| Team Member| SJSU ID |
| --- | --- |
| Shreekar Kolanu | 017406493 |
| Pawan Aditya Man| 017506450 |
| Naga Varun Bathina| 017434261 |
|  Divyam Savsaviya | 017536714 |

# **Our Github Repo**
https://github.com/gopinathsjsu/teamprojectsection-01-cmpe202-tuesday-kinetic_spring


# **Team Contributions**


| Team Member| TASKS |
| --- | --- |
| Varshith Pabbisetty | worked on Backend schemas and routes for users, artists, movies, theatres, and screens. |
| Pawan Aditya Man | worked on creating UML diagrams and worked on backed for creating endpoints for faculty, course. Created the collections on postman with all the listed APIs and also worked for Integrating frontend and backend.
| Naga Varun Bathina | worked on front end architecture, sign-up, login ui. Integration, with backend. The home page,Grading Assignments, creating Assignments, create Subject, Teacher and assisted in Cloud deployment and read-me file|
| Shreekar Kolanu | Worked on the Frontend, schemas and routes for creating Announcements,Quiz and deployment of the project with auto-scaling & load-balancer in EC2.|




# **Starting the Backend**
```
cd backend
npm start
```

# **Starting the Frontend**
```
cd frontend
npm start
```

# **Tech Stack**
**Frontend:** React JS

**Backend:** Node JS

**Database:** MongoDB Atlas

**Deployment :** EC2 with Load balancing(ALB) and ALG

# **Design Choices**
**Backend Development:**

1. **Backend Schemas and Routes:**
   - Implemented robust backend schemas and routes for essential entities such as students, faculty, admin, assignments, announcements, quizzes, grades. This ensures a well-structured and organized data flow within the application.

2. **Scalability through Deployment:**
   - Opted for EC2 with Load Balancing during deployment, ensuring scalability and reliability. This choice enables the application to efficiently handle varying loads, distributing traffic across multiple instances for improved performance.

3. **Database Choice:**
   - Utilized MongoDB Atlas as the database solution. MongoDB's NoSQL architecture provides flexibility in handling diverse data types, facilitating efficient storage and retrieval of complex data structures relevant to the project.

**Frontend Architecture and User Interface Design:**

1. **Comprehensive Frontend Architecture:**
   - Designed a comprehensive frontend architecture that encompasses key user interfaces, including the home page,creating subjects, posting quizzes, grading student, viewing grades. This design choice ensures a cohesive and seamless user experience.

2. **User-Focused UI Design:**
   - Prioritized user experience by focusing on user interfaces such as sign-up, login, and intuitive navigation across key pages. This design approach enhances user engagement and satisfaction.

3. **Documentation and Diagrams:**
   - Included detailed diagrams and a README file as part of the frontend architecture. This documentation provides clarity to developers and stakeholders, aiding in understanding the project's structure and facilitating smoother collaboration.

4. **Integrated Frontend with Backend:**
   - Integrated frontend components seamlessly with the backend, ensuring a cohesive and responsive application. This design choice enhances data flow and interaction between different layers of the application.

# **Journals**
Aditya's Journal

[Rohit Project Journal.md](https://github.com/gopinathsjsu/team-project-wizard/files/13575328/RohitProject.Journal.md)

Shreekar's Journal

[Shreekar project Journal Journal.md](https://github.com/gopinathsjsu/teamprojectsection-01-cmpe202-tuesday-kinetic_spring/tree/cd0ca66950a5d47f40319bef0a1103d68724f1f6/Project%20Journel)

Varun's Journal

[Sameer.proj.Journal (1).md](https://github.com/gopinathsjsu/team-project-wizard/files/13578211/Sameer.proj.Journal.1.md)

Divyam's Journal

[Varshith Project Journal.md](https://github.com/gopinathsjsu/team-project-wizard/files/13575522/Varshith.Project.Journal.md)


# **XP Values**

1. **Communication:**
   - Implemented a diverse set of communication channels, including weekly Zoom and WhatsApp status calls, supplemented by a dedicated collaboration platform (e.g., Slack or Microsoft Teams). This multi-channel approach facilitated real-time communication, quick updates, and dynamic discussions, fostering a more connected and agile development environment.

2. **Feedback:**
   - Instituted iterative review sessions at key development milestones, beyond regular status updates. Utilizing collaborative tools like Zoom and shared documents, these sessions allowed for real-time feedback from team members and stakeholders. This iterative feedback approach ensured swift adjustments, promoting a responsive and user-focused development cycle.

# **UI WIRE FRAMES**
[UI Wire FRAMES (1).pdf](https://github.com/gopinathsjsu/team-project-wizard/files/13577687/UI.Wire.FRAMES.1.pdf)


# **Taskboard**

<img width="254" alt="Screenshot 2023-12-05 at 10 53 43 PM" src="https://github.com/gopinathsjsu/team-project-wizard/assets/60455498/4fec1df9-1ea2-4764-8719-3a3b1e935dde">

# **Features Set**

1. **Membership Options:**
   - Introduces both Regular and Premium membership choices. While Regular membership comes at no cost, opting for Premium membership entails an annual fee of $15.

2. **Analytics Dashboard:**
   - Equips theater staff with a visual depiction of theater occupancy trends over the preceding 30/60/90 days. Presents a concise overview of data categorized by both location and movies.

3. **Location Selection:**
   - Empowers users to select their preferred viewing location, aligning with a membership model designed for multiple locations.

4. **Book Multiple Seats:**
   - Permits enrolled members to reserve multiple seats (up to 8) for a movie screening, utilizing either rewards points or a predetermined payment method.

5. **Registration/Signup Page:**
   - Facilitates user enrollment in the Movie Theater Club by capturing essential information and initiating account creation.

6. **Rewards Points System:**
   - Gathers rewards points for all members, accruing at a rate of 1 point for every dollar spent. Premium members benefit from the added advantage of having the online service fee waived.

7. **Home/Landing Page:**
   - Offers a comprehensive snapshot of theaters, locations, current movie schedules, and forthcoming releases. Functions as the primary entry point for users.

8. **Book Tickets:**
   - Empowers users to secure movie tickets, with a nominal online service fee of $1.50 per ticket.

9. **Theater Employee Section:**
   - An Angular application tailored for theater employees (admins), providing functionalities to add, update, or remove movies, manage showtimes, allocate theaters, configure seating arrangements, and access analytics.

10. **Cancel Tickets and Request Refund:**
    - Allows users to annul booked tickets before the showtime and request a refund if needed.

11. **View Movie Schedules:**
    - Presents the schedules for current movie showtimes, assisting users in planning their visits to the theater.

12. **Discount Price Configuration:**
    - Empowers theater employees to set discounted prices for shows occurring before 6 pm and for Tuesday showings, offering pricing flexibility.

13. **Membership Page (For Enrolled Members):**
    - Exhibits details for enrolled members, including purchased movie tickets, accumulated rewards points, and a record of movies watched within the past 30 days.

# **Architecture Diagram**

![architectureD](https://github.com/gopinathsjsu/team-project-wizard/assets/60455498/0a0d50de-5dac-45e9-a9b0-170874e20776)

# **USE CASE Diagram**

![USE CASE](https://github.com/gopinathsjsu/team-project-wizard/assets/60455498/2e0a9fc8-1834-41c2-b2fb-17324695d402)

# **AGILE WIZARDS SPRINT SHEET**

[Wizards agile sprint sheet.xlsx](https://github.com/gopinathsjsu/team-project-wizard/files/13577257/Wizards.agile.sprint.sheet.xlsx)


# **DEPLOYMENT DIAGRAM**
![Untitled](https://github.com/gopinathsjsu/team-project-wizard/assets/60455498/182034df-1156-4494-bf5a-8b093157cc10)


# **COMPONENT DIAGRAM**

![component D diagram (1)](https://github.com/gopinathsjsu/team-project-wizard/assets/60455498/5f8d6f60-0ee1-4476-8ae6-ae7111d5870a)

# **BURNDOWN CHART**

![WhatsApp Image 2023-12-04 at 12 12 43 (1)](https://github.com/gopinathsjsu/team-project-wizard/assets/60455498/4b20b4de-2cf1-4860-bac9-d5192229afca)


