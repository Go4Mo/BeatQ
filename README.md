# BeatQ
Welcome to BeatQ, an application that allows you and your friends to easily share music.


**Contributors:** Mohamed Bah, Vijay Bharadwaj, Sanjeev Lingam, Bradley Bottomlee


## Running Locally 
1. pip3 install virtualenv
2. virtualenv BeatQ or virtualenv -p python3 BeatQ
3. source BeatQ/Scripts/activate  or source BeatQ/bin/activate
4. pip3 install -r requirements.txt
5. set FLASK_APP=flaskr
6. set FLASK_ENV=dev
7. flask run

## Inspiration
We’ve all been in that situation at a party where that one person with the AUX has the worst music taste. It can be tough to tell them that their music sucks without creating an awkward situation. What if we gave more power to the people? That’s exactly how we came up with BeatQ, a web application that allows users to queue up songs to the DJ by making a simple request on their phones.

## What it does
BeatQ is the first ever web application that elevates a party to the next level by allowing users to collaborate simultaneously on developing a music queue and making sure everyone gets to jam out to their favorite song. A host must first create a BeatQ session, which is automatically connected to a Spotify playlist. The host has the ability to search for songs and add them to the playlist. On the dashboard is also an invited code. The host can send this code to others, who can use the join functionality to queue songs on their dashboard. The host has special permissions to end a session that he has created, or dequeue certain songs that were added. 

## How we built it
By utilizing the spotify API we created a host-client format in which the client connects to the host after entering a unique-id code generated from the host server. After the client joins the server, they are assigned a default level of premissions which both restricts and allows them to contribute to the queue. Ultimatly, the control of both the queue and the clients premissions lie with the host who can choose to opt out and pass the role of the host to a client. From their, users would have a dashboard view of members inside the queue, their premissions, and songs currently queued up. They can also search and ammend songs onto the queue if their premission allows it. 

## Challenges we ran into
* Setting up Flask and running a virtualenv
* Working with cookies
* Merge Conflicts
* Learning how to use Flask
* Connecting with spotify API
* Creating the search feature 

## Accomplishments that we are proud of
Solving each of the challenges. LEGGO

## What we learned
* Sleep is key
* Spotify API, Python, Flask, HTML/CSS, Git/Github
* Team communication, planning, and time management
* How to refresh API tokens 

## What's next for BeatQ

* Get some sleep

* Allows users to upvote and downvote a song as well as the person that added the song

* Silent DJ Mode: Silent DJ parties are a new form of party that are becoming increasningly more popular. Its when multiple people listen to the same song simultaniously. The problem is timing it so that it start simultaniously for everyone. The current solution for this is using specialized headphones that you can rent for $7 a day. Silent dj mode allows users to simultaniously listen to the same songs v.i.a. their own device just like a pocket radio. 

* Create a mobile version of this app

* Integrate it with the spotify app as an add-on or a plug-in

* Show it off to our friends

* <S>Sell</s> Share it with the world
