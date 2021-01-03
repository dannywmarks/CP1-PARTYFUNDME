PartyFun'd  

[https://partyfund.herokuapp.com/]()  

04.28.2020  
Danny Marks   


![moneyshot-logo](https://app.genmymodel.com/personal/projects/_8Y5hsHhtEeqeQcxm9hmzHw)

##**Oveview**: 

Create a Kickstarter / Go Fundme clone for the Bar and Nightlife industry. The web app would be a promotional tool to promote and pre-sell events and provide value to customers. (_During the covid19 pandemic bars and bartenders have turned to gofundme to raise money to cover losses because they have not been able to open their doors. PartyFundME would be catered specifically for bars/nightclubs to raise money but provide a platform for the bar or person throwing event to offer some value return i.e. open bars, private partys, band, dj, etc._ ) 

>I had a startup a few years ago called MoneyShot. The concept was to send drinks back and forth to friends on their birthdays. (If it was my buddy Emmet's birthday and he is in NYC and I knew his favorite bar, I wanted to send him a drink or pay for his bar tab for his birthday. The app had a hard time gaining traction due to lack of participating bars.  
>[Shark Tank audition video](https://www.youtube.com/watch?v=gf_a_UmJkUQ&feature=youtu.be) 
> 
 
MoneyShot never gained traction, but I did have  success  “crowdfunding” parties. I would throw parties for friends' birthdays at popular bars in SF.   
>1. I would create a flyer for the party.   
2. Post on social media circle, inviting everyone to the party but if they coudn't make it could buy a round.
3. Used money that was "chipped in" / donated to create a tab at the bar
Moneyshot would average 1000$ raised a party. The bar owners and staff were happy, party goers were happy, and most of all the person we threw the parties for were happy. 

##**Goals**: 
 
Build a platform that would allow bar owners and eventually users to create and crowdfund events at Bar/Nightclub establishments. 

##**User Flow**

The Platform allows for a user view flyers to upcoming events. A user can purchase a ticket to an upcoming event, if they are registered. A user after registering, must confirm by email, once confirmed the user can log in. If the user chooses too they can purchase a ticket to a party. They will be directed to squares server where they can enter credit card information and purchase a ticket. Once payment is confirmed an email of the ticket for the event is sent to the user.
 
 Users can also see what events other users have purchased and are attending. A user can also see how much money has been raised for the party. For future updates the crowd funding portion can be built out in more detail. For now it is very basic.
 
 Users also have basic profile crud functionality
 
 There are some basic search functions, ability to search bars and events.
 
 There is an admin portal for an admin to confirm and add a venue to list of venues that users can throw parties at.

##**Specifications**
* Sign up and create user function.   
* User Profile
* Create and Manage Events (Admin Portal)
* View Events  
* Fund an Event  
* Receive receipt/ticket email of funding  
* Database Schema outline in Static Folder on GITHUB


##**API ROUTES**
/  
/admin_blueprint  
/api/bars  
/api/bar/<int:bar_id>  
/api/events  
/api/events/<int:event_id>


**Mail**  
/send_mail  
/ticket

**Bars**  
/bars/signup  
/bars  
/bars/<int:bar_id>

**Events**  
/events  
/events/<int:event_id>  
/events/new_event  
/events/<int:event_id>/update  
/events/<int:event_id>/delete

**Users**

/signup  
/confirm/token  
/login  
/logout  
/account  
/profile/<int:user_id>/delete

**Stripe**

/stripe  
/stripe_webhook


##**Technologies**  
Flask Blueprings
Flask Admin
Flask Dance/Oauth for future updates
Flask Login
Flask Bcrypt
Flask Mail
Sql Alchemy
PGSQL
Wtforms
Square Api

**Flask Blueprints:** Used to organize the design of application with intentions of future updates. 
 
**Flask Admin:** Flask admin library is used to manage parties and users from the front end.  

**Flask Dance/Oauth: **Flask Dance was configured, but is not full integrated. It's real use will be when a messaging system between bartenders and users is added to the application in future updates.  

**Flask Login:** Flask Login was used to securely handle authentication and authorization of users.  

**Flask Mail:** Flask Mail was used to confirm users when registered. Add users to mailing list and allow for mass emails, and also was used to email confirmation ticket when users bought tickets to event.  

**Sql Alchemy and PSQL:** These technqologies were used to manage the data flow to and from the database. SQL alchemy was used to cleanly manage and organize database queries.  

**Wtforms:** Used to gracefully manage form submissions and error checking
Square Api : Square API is used to manage payments for the event.  

**Postman** Used to test and manage back end routes.

##**Future Updates**#####

Adding bartenders/employees that will be working the event the ability to comment, and be listed on the event.  

User comments on past/future events.  

Past event section. 

Blog section about event. 

Allow events to be posted on twitter

