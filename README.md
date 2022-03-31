# Depression-detection
#This data was collected with an on-line version of the Depression Anxiety Stress Scales (DASS), see http://www2.psy.unsw.edu.au/dass/
The columns containing some survey questions and personal information regarding age,race,religion,education.

Picked up the features related to depression,
Columns - 'Q3A','Q5A','Q10A','Q13A','Q16A','Q17A','Q21A','Q24A','Q26A','Q31A','Q34A','Q37A','Q38A','Q42A',
         'TIPI1','TIPI2','TIPI3','TIPI4','TIPI5','TIPI6','TIPI7','TIPI8','TIPI9','TIPI10',
         'education','urban','gender','engnat','age','hand','religion','orientation','race','voted','married','familysize'
  
(TPI1-TPI10) are Ten item personality Inventory, added the personality score and created single column for the ten items.

Q3	I couldn't seem to experience any positive feeling at all.

Q5	I just couldn&#39;t seem to get going.

Q10	I felt that I had nothing to look forward to.

Q13	I felt sad and depressed.

Q16	I felt that I had lost interest in just about everything.

Q17	I felt I wasn&#39;t worth much as a person.

Q21	I felt that life wasn&#39;t worthwhile.

Q24	I couldn&#39;t seem to get any enjoyment out of the things I did.

Q26	I felt down-hearted and blue.

Q31	I was unable to become enthusiastic about anything.

Q34	I felt I was pretty worthless.

Q37	I could see nothing in the future to be hopeful about.

Q38	I felt that life was meaningless.

Q42	I found it difficult to work up the initiative to do things.

After clening the data, data frame looks like,

![image](https://user-images.githubusercontent.com/91527488/161144503-043d8480-3986-4217-9004-0a7f7b666326.png)



**DATA VISUALIZATION :**

Visulaizing data in tableau after data cleaning process.

![image](https://user-images.githubusercontent.com/91527488/161142414-0ae151c4-9bc8-476f-848d-1870c4f3dd62.png)

![image](https://user-images.githubusercontent.com/91527488/161142862-230c2564-4923-43d1-b729-ea879674b6ae.png)

After Feature engineering and column transforms, the pipeline looks like:
![image](https://user-images.githubusercontent.com/91527488/161143671-79556578-db8c-4847-afd4-16d0c4346734.png)


Accuracy score :

![image](https://user-images.githubusercontent.com/91527488/161143790-35853e00-ee8c-406f-86c1-af815900ce96.png)

* Exporting the model object and deploying on streamlit

## importing the pipeline and data frame(used pycharm)

![image](https://user-images.githubusercontent.com/91527488/161144987-7df34f4c-e5b3-4867-9c74-ef9cc22a99fa.png)

After giving all the columns the data on streamlit looks like:
![Captureh](https://user-images.githubusercontent.com/91527488/161145405-5f4a0765-b8ac-40c5-bbb6-3ad5a00a247d.PNG)
![Capture2](https://user-images.githubusercontent.com/91527488/161146201-4506d95f-c1ce-4542-b41d-6d9d177fc5df.PNG)


The target variable is a classification value where the model returns 'yes' if there is depression and 'no' if there no depression.
![Captures 2](https://user-images.githubusercontent.com/91527488/161146037-67be7160-01b7-4364-8744-747306f7ae10.PNG)
![Captureres](https://user-images.githubusercontent.com/91527488/161146253-ef6af772-f322-4262-a6fc-32d0591ff642.PNG)



