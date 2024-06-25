# Lego_case
The Lego case assignment



- What engineering practices do you think are important to build this platform? 
  * I will try to fail fast. Try some things out and quickly get a feel for whether of not the result has value. If not I will quickly move on.
  * Test. It may seem silly since this is a quick test, but it is an essential concept in clean code

- How will you, as a senior engineer, assist in setting the team for success? What will your 
focus be, and how do you intend to contribute to the team’s success?
    * There are many moving parts in a system like this. The secret to success is to make these work as a whole and to do this communication is the key. The machine builders will be kept informed and you will need to work closely with the plc team.     
    * Many of the parts will also change during the process and for the sw tests is one of the things that can keep track of changes in a fluent environment.
- What challenges or issues do you anticipate during the development process and what 
would your strategies be to address them? 
  * Mechanical issues where pieces cannot be sorted as expected. Small shovels of hats getting stuck in the machine. 
    * Like the fail quickly. I would need to test critical parts of the system before the final machine arrives so other solutions could be implemented in due time.
  * False classifications: 
    * Every image should be saved for the operator to look through and the machine can learn from it in the future. 
    * Also every final set should be photographed and validated.
  * Pieces that are not split into individual pieces. 
    * This could take a long time as well. A separate ML algorithm could look for this.
  * Issues from the operators - no overtime, less hours. Concern for their jobs. 
    * Should be handled with more communication. This will not take their jobs, and every person I have every meet wants to do their best deep down.
- When using image recognition or machine learning, which attributes do you believe should 
be prioritized to ensure accurate sorting? Additionally, describe how the system should 
handle anomalies, if any.
    * Since the system need to handle hundreds of different pieces I am incline to think it would be better to split the ML model into a series of models: big/small and by color. From the color and the size I would add CNN to determine which shape. 
    * This allows you to focus on single difficult distinctions.
    * In addition to the CNN one could add a 3d laser line scan as well as a weight cell to improve accuracy.
    * Anomalies (I am assuming you mean pieces which cannot be classified) should imo be sorted in its own "bucket" and handled manually.  
- How would you design a database to track and manage the necessary information for this 
platform? What attributes are important to store in the database and what aspects are 
important to consider here?
    * The most important part of the database is the production and updating the running sets. In the production we should save an image of the brick (or a link to it), as well as the id and which set it ended up in. The open sets should be linked to the set design with the list of brick ids in that set. I think a complete set should also contain a validation photo in the end.
    * A set af tables will be answered visually in another place.
- How would you ensure seamless integration and interaction between the different 
components of the platform?
    * I would leave the control to a PLC and have the PC/cloud be the slave. This might not be the case for this demo, but the PLC can keep track of the different sets in real time.
    * The vision systems can tell if this in a specific piece and if the set is indeed complete, but the PLC should keep track of the sets and what they should contain.
    * The communication between the PCs and the PLC could be done with Snap7, but there are other possibilities
- What stakeholders and resources would you engage to help achieve a successful solution
    * The most important stakeholder is imo the user in a case like this. They will be using the machine, and they will have to live with some of the choices for years. It is most important to listen to their concerns and desires and to get them on board with any solution.
    * The machine builders will also need to be kept close and it is important to have a common understanding with them that the machine is not done before all the parts work as a whole.
    * The other internal stakeholders are in my opinion not as important. The databases will need to be up to date and maintained but once the department has been informed and are on board I don't see it as a continues effort in the same way.
  