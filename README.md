# Automated-Online-Proctor
An multi modal automated proctor for online exams 

![image](https://drive.google.com/uc?export=view&amp;id=1BYY_W6FPk5lUpe3D3uezw8iX4HwUR8qd){ width=80% }

# [EduVision](https://drive.google.com/file/d/1Y_jfNiyZLEzi1eiCqkztw63TbTPjA7bl/view?usp=sharing) - AI support for e-learning

## **1. Introduction**

+ COVID-19 has caused the already surging online education market to boom further. The  growing  popularity  of  MOOC courses   and   the   changing education   landscape   could   mean more  and  more  people  switching  to  online  education.
+ While useful without a doubt, online education has one major drawback : lack of control. Teachers cannot clearly monitor the activity of their students. This results in two major problems: 
> 1. The lack of supervision during lectures leads to a lower retentivity and poorer learning experience as **students are easily distracted.**
> 2. The second major area affected is the **evaluation process**, where students resort to **unfair means** during quizzes and tests. This leads to marks and possibly degree obtained being questionable			
+ EduVision proposes AI-Enabled solutions to tackle this lack of supervision. The proposed solution will require just a laptop with a functioning webcam and microphone. Computer Vision is incorporated to detect student emotions, expressions, head and eye movements and other activity to gauge their attentivity and prevent malpractices.

## **2. Features of EduVision**
EduVision aims to automate supervision in online education, be it during lectures or online examinations. We aim to achieve these two objectives with the help of Machine learning and Computer Vision techniques to fully automate this process. 
Not only does this method prove to be cost efficient, but it also reduces the burden for teachers who have to expend their energy and time in monitoring their students.
The module-wise features of EduVision are listed below:

* **MODULE 1 - Attention detection:** The largest seback of online learning is its one-way stream. When teachers proceed with their lectures, active engagement from the students is also necessary lest the students lose interest. While there are no ways to ensure active engangement, we can certainly detect a student's attentiveness and allow the teacher to leverage this knowledge to modify their lesson plans. Since webcams allow focused view of each student, we can make use of this data to identify various patterns and signs. This module is primarily focuses on detecting these signs in an online lecture environment. :

> 1.   Students’ posture and body language
2.   Students’ emotions detected from facial expressions
3.   Sleepiness or drowsiness signs inthe student.

![image](https://drive.google.com/uc?export=view&amp;id=1JeTGFfJLmpROZtjDqpu-8_WvVuywCGJS)

* **MODULE 2 - Detecting malpractices in online examinations:** Due to the limited field of view in webcams, examinations tend to be the most challenging part of virtual learning. Furthermore, constant video streams from hundreds of students lead to heavy bandwidth consumption, causing packet loss and consequently frame loss, for the invigilator online. Thus, the stream-based proctoring tends to perform poorly and does not serve its purpose. We require a scalable solution that can handle the traits of a test environment efficaciously. To do so, we introduce a proctoring method that tracks students' activities on their local machines and sends the consoliated report to the examiner. The proctor makes use of the following *five* crucial components to deduce the information:

> 1.   Face Authentication
2.   Head-pose Estimation
3.   Eye Tracking
4.   Speech Detection
5.   Detection of proscribed objects


![image](https://drive.google.com/uc?export=view&amp;id=1H6KfiXMaHXeEsKt4esN4A1UXxwvEG7bx)

(click here in case the images showing feature overview didn't load) [Overview diagram](https://drive.google.com/drive/folders/1elvubnvj_2EMJTL8FOml3LjYbZFlliCS?usp=sharing)

## **3. Proposed implementation**

### **3.1. Attention detection during online lectures**

We propose to monitor students’ attentivity in online lectures by considering certain metrics. Taking  into  account posture analysis ,  emotion  inference from  facial  expressions and sleepiness experienced by the students, we propose to detect the attention span during online lectures.

Prerequisite library : [OpenPose](https://arxiv.org/abs/1812.08008), a software that generates skeletal representations of a person’s posture.

#### **3.1.1. Posture analysis** 

1. The  human  body  can  be  used  to  detect  an  individual’s presence  of  mind  through  their  posture. When attentive, the person’s posture is firm whereas a distracted student tends  to  not  look  at  the  screen,  lean  back  and so on.
2. We propose a posture based classifier which can tell if a student is attentive or not.
3. The candidate’s image is fed through OpenPose to generate posture based representations. (See [diagram](https://drive.google.com/file/d/1qki1GlLZRbQaW485CSCpi6OWNuR0KK-s/view?usp=sharing))
4. We propose a convolutional neural network trained on these OpenPose representations of various postures in an online environment.
5. The classifier will identify 5 prominent postures : Attentive, Head rested on their hand, Leaning back, Writing. Not looking at the screen.
6. To minimize spurious alerts, a window of recent frames can be sampled to determine the prominent posture in that duration.

	
![img](https://drive.google.com/uc?export=view&amp;id=13aS1YTyL4-WM-9B4ubkarkspjwQpRoxf){width=80%}
	

#### **3.1.2. Emotion inference from facial expressions**

1. A  person’s emotions are conspicuous through  their  facial  expressions. We identified the most common emotions expressed by students as anxiety,  anger,  pride,  happiness,  boredom. 
2. The system proposed will determine  the emotion and also the   frequency   of   the   emotion variation. 
3. We plan to build an image classfier using transfer learning to detect emotions from the facial representations. 
4. Capturing the frequency of the predicted emotion  can be done using OpenCV.

| Emotion |Probable Cause|
|--------------|-----------------------|
|Laughter,Sadness |Social media, surroundings|
|Disgust, Anger | personal reasons,People around |
| Fear | Subject, faculty, peers |
|Anxiety and restlessness | Personal reasons, performance  pressure, peers |
| Boredom | Lack of interest in subject, Illness or Tirednes|


#### **3.1.3. Drowsiness**

1. Irregular sleep patterns and sleep loss can negatively impact a student’s cognitive performance and emotional stability.
2. We can measure the sleepiness by calculating the ratio of vertical to horizontal width of the eye of the student during regular intervals of the lecture.
3. The extent of opening of eyes is a significant indicator to detect how drowsy a person is.
4. By comparing the ratios regularly, we can identify specific instances of discrepancies in a student's attentiveness.


The drowsiness measure, observed emotions, and posture will be combined using a method of weighted averaging to compute a final score called the attentivity index, The weights will be determined experimentally. The preceding frames will be averaged to give the score over a certain time period. If the attentivity score dips below a certain threshold, the teacher can be alerted. Observing the attentivity trends of different students over extended time periods can also allow the teachers to identify those with special needs and accordingly provide assistance to those students.



### **3.2. Detecting malpractices during online examinations**

![image](https://drive.google.com/uc?export=view&amp;id=1sBPZ5SCxuP8qwSdUFjZg-JzXIjuFnPD-){width=50%}

In case the image does not load, click [here](https://drive.google.com/file/d/1sBPZ5SCxuP8qwSdUFjZg-JzXIjuFnPD-/view?usp=sharing) for implementation diagram
**Five fold approach** consisting of **facial recognition**, followed by **tracking head, eye and mouth movements,**  along with **detection of cheating material.**


We propose the use of three image processing Python Libraries : **[DLIB](https://pypi.org/project/dlib/), [OpenCV](https://opencv.org/) and [OpenFace](https://www.semanticscholar.org/paper/OpenFace%3A-A-general-purpose-face-recognition-with-Amos-Ludwiczuk/82e66c4832386cafcec16b92ac88088ffd1a1bc9).**

DLIB uses histogram based machine learning to generate a mask of a person’s face, See the figure below for reference.
OpenFace generates a 128 dimensional vector given an image of a person’s face, and the closer two vectors are means the more similar the two people look.
The video of the candidate will be fed frame by frame to DLIB and OpenFace to generate the mask and vector, respectively.
The detection modules are as follows :

1. Authentication: The generated feature vector will be compared to the student’s photo ID for similarity, to detect if someone else is giving the test.
2. Head  pose  estimation : Using the facial image, and the PnP equation, we can solve for the angle of tilt of the head, to determine if the person is looking into or outside of the screen. If the angle of tilt is found to be beyond a threshold, say 25 degrees, the action is marked as suspicious. 
3. Eye  tracking: If the person’s face is centred, the eyes are tracked to see if the candidate is staring out of the screen. Using the facial landmarks from DLIB library, the eyes will be extracted. Then they are converted to  grayscale and processed to extract the pupil using image processing with OpenCV. This tells us if the eyes are focused on the screen or away from it, perhaps at some book or cheating device.
4. Speech  detection : The  mouth  is monitored  for  lip  movements. The degree to which the mouth is open is computed using DLIB’s facial landmarks to determine if the candidate is talking or not.
5. We propose YOLO object detection  for identifying cheating materials such as books, phones etc. YOLO is fast and has very good accuracy.


The final “Suspicious flags” detected for the entire duration of the test are fed to a fuzzy  logic classifier to give a verdict of cheating or not.
The fuzzy logic classifier will have a rule base set for the specific flags and their duration and frequency. The verdict will be returned in terms of probability of there being malpractice.

Face Mask using DLIB            | Head Movement | Eye processing to locate pupil
:-------------------------:|:-------------------------:|:-------------------------:
![mg1](https://drive.google.com/uc?export=view&amp;id=1UZwUYH21PT_eNSsz_uxZzu5GhlG-zitS){width=30%} | ![img2](https://drive.google.com/uc?export=view&amp;id=1u9QDhdAGee0BEoZqdYVoyZ3ZDF11TIAl){width=35%} |   ![img3](https://drive.google.com/uc?export=view&amp;id=13v8MQi2FNNEYVG7_qtP1uZCxOQng_QoN){width=35%}

## **4. Technology Stack**
* Frontend - HTML, CSS, JavaScript, ReactJs
* Server side - Flask / Django
* Machine learning libraries - Tensorflow, Keras, OpenCV, Pandas, Sklearn, DLIB, OpenPose, OpenFace

## **5. Limitations**
* The user must have a working webcam and good internet connectivity.
* Limited field of view of the laptop webcam.
* The user must have proper lighting in the room.

### Results :
<img src="./media/embeddings.png" width="60%">.
<img src="./media/download (1).png" width="60%">.



### References :

#### Blogs, websites, tutorials, github repositories :
1) https://www.pyimagesearch.com/2017/05/08/drowsiness-detection-opencv/
2) https://github.com/yinguobing/head-pose-estimation
3) https://github.com/antoinelame/GazeTracking
4) https://www.learnopencv.com/head-pose-estimation-using-opencv-and-dlib/
5) https://github.com/jerryhouuu/Face-Yaw-Roll-Pitch-from-Pose-Estimation-using-OpenCV
6) https://github.com/krsatyam1996/Face-recognition-and-identification
7) https://github.com/cmusatyalab/openface
8) FaceNet: A Unified Embedding for Face Recognition and Clustering

#### Publications :
1. D. L. King and C. J. Case., “E-cheating: Incidence and trends among-college students.” in Issues in Information Systems, vol. 15, 2014.
2. D.  Varble,  “Reducing  cheating  opportunities  in  online  test,”AtlanticMarketing Journal, 09 2014.
3. E.  Flior  and  K.  Kowalski,  “Continuous  biometric  user  authenticationin  online  examinations,”  in2010  Seventh  International  Conference  onInformation Technology: New Generations, 2010, pp. 488–492.
4. M. McGinity, “Let your fingers do the talking,”Commun. ACM, vol. 48,pp. 21–23, 01 2005.  
5. A. Javed and Z. Aslam, “An intelligent alarm based visual eye trackingalgorithm for cheating free examination system,”International Journal of Intelligent Systems and Applications, vol. 5, pp. 86–92, 09 2013. 
6. S. S. Chua, J. B. Bondad, Z. R. Lumapas, and J. D. L. Garcia, “Onlineexamination system with cheating prevention using question bank ran-domization  and  tab  locking,”  in 2019  4th  International  Conference  onInformation Technology (InCIT), 2019, pp. 126–131.
7. R.  Bawarith,  D.  Abdullah,  D.  Anas,  and  P.  Dr,  “E-exam  cheatingdetection system,”International Journal of Advanced Computer Scienceand Applications, vol. 8, 04 2017.
8. A. A. Sukmandhani and I. Sutedja, “Face recognition method for onlineexams,” in 2019 International Conference on Information Managementand Technology (ICIMTech), vol. 1, 2019, pp. 175–179.
9. S.  Sawhney,  K.  Kacker,  S.  Jain,  S.  N.  Singh,  and  R.  Garg,  “Real-time  smart  attendance  system  using  face  recognition  techniques,”  in 2019 9th International Conference on Cloud Computing, Data ScienceEngineering (Confluence), 2019, pp. 522–525.[10]  
10. Y. Atoum, L. Chen, A. X. Liu, S. D. H. Hsu, and X. Liu, “Automated online  exam  proctoring,”IEEE  Transactions  on  Multimedia,  vol.  19,no. 7, pp. 1609–1624, 2017.
11. Liu Siyao and Gong Qianrang, “The research on anti-cheating strategyof online examination system,” in2011 2nd International Conference onArtificial  Intelligence,  Management  Science  and  Electronic  Commerce(AIMSEC), 2011, pp. 1738–1741.
12. S. Prathish, A. N. S., and K. Bijlani, “An intelligent system for onlineexam  monitoring,”  in2016  International  Conference  on  InformationScience (ICIS), 2016, pp. 138–143.
13. G.  Kasliwal,  “Cheating  detection  in  online  examinations,”Master’sProject, 2015.
14. A.  Arinaldi  and  M.  I.  Fanany,  “Cheating  video  description  basedon  sequences  of  gestures,”  in2017  5th  International  Conference  onInformation and Communication Technology (ICoIC7), 2017, pp. 1–6.
15. H. Xia and C. Li, “Face recognition and application of film and televisionactors  based  on  dlib,”  in2019  12th  International  Congress  on  Imageand Signal Processing, BioMedical Engineering and Informatics (CISP-BMEI), 2019, pp. 1–6.
16. X.  Li,  K.-m.  Chang,  Y.  Yuan,  and  A.  Hauptmann,  “Massive  openonline  proctor:  Protecting  the  credibility  of  moocs  certificates,”  inProceedings  of  the  18th  ACM  Conference  on  Computer  SupportedCooperative  Work  &  Social  Computing,  ser.  CSCW  ’15.New  York,NY, USA: Association for Computing Machinery, 2015, p. 1129–1137.[Online]. Available: https://doi.org/10.1145/2675133.2675245
17. S. H ̈offner, “Gaze tracking using common webcams,” Ph.D. dissertation,02 2018.
18. A. Kar and P. Corcoran, “A review and analysis of eye-gaze estimationsystems,  algorithms  and  performance  evaluation  methods  in  consumerplatforms,”IEEE Access, vol. 5, pp. 16 495–16 519, 2017.
19. C.  Meng  and  X.  Zhao,  “Webcam-based  eye  movement  analysis  usingcnn,”IEEE Access, vol. 5, pp. 19 581–19 587, 2017.
20. A.  Papoutsaki,  P.  Sangkloy,  J.  Laskey,  N.  Daskalova,  J.  Huang,  andJ. Hays, “Webgazer: Scalable webcam eye tracking using user interac-tions,” inIJCAI, 2016.
21. T. Imabuchi, O. D. A. Prima, and H. Ito, “Visible spectrum eye trackingfor  safety  driving  assistance,”  inTrends  in  Applied  Knowledge-BasedSystems and Data Science, H. Fujita, M. Ali, A. Selamat, J. Sasaki, andM.  Kurematsu,  Eds.Cham:  Springer  International  Publishing,  2016,pp. 428–434.
22. B. Amos, B. Ludwiczuk, and M. Satyanarayanan, “Openface: A general-purpose face recognition library with mobile applications,” CMU-CS-16-118, CMU School of Computer Science, Tech. Rep., 2016.
23. The OpenCV Reference Manual, 2nd ed., Itseez, April 2014.
24. F.  Rocca,  M.  Mancas,  and  B.  Gosselin,  “Head  pose  estimation  byperspective-n-point  solution  based  on  2d  markerless  face  tracking,”inIntelligent  Technologies  for  Interactive  Entertainment,  D.  Reidsma,I. Choi, and R. Bargar, Eds.    Cham: Springer International Publishing,2014, pp. 67–76.
25. J. Daugman, “New methods in iris recognition,”IEEE Transactions onSystems, Man, and Cybernetics, Part B (Cybernetics), vol. 37, no. 5, pp.1167–1175, 2007.
26. B. K. Savas ̧ and Y. Becerikli, “Real time driver fatigue detection basedon  svm  algorithm,”  in2018  6th  International  Conference  on  ControlEngineering Information Technology (CEIT), 2018, pp. 1–4.
27. M. Ariz, J. Bengoechea, A. Villanueva, and R. Cabeza, “A novel 2d/3ddatabase  with  automatic  face  annotation  for  head  tracking  and  poseestimation,”Computer  Vision  and  Image  Understanding,  vol.  148,  pp.201–210, 07 2016.
28. A.  Villanueva,  V.  Ponz,  L.  Sesma-Sanchez,  M.  Ariz,  S.  Porta,  andR.  Cabeza,  “Hybrid  method  based  on  topography  for  robust  detectionof   iris   center   and   eye   corners,”ACM   Trans.   Multimedia   Comput.Commun.   Appl.,   vol.   9,   no.   4,   Aug.   2013.   [Online].   Available:https://doi.org/10.1145/2501643.2501647

